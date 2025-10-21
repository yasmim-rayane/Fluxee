"""
Interface de gerenciamento de vendas
"""

import tkinter as tk
from tkinter import ttk, messagebox


class VendasFrame:
    """Frame para gerenciar vendas"""
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Lista de produtos adicionados à venda
        self.produtos_venda = []
        
        self._criar_interface()
        self._atualizar_lista_vendas()
        
    def _criar_interface(self):
        """Cria a interface de vendas"""
        # Título
        title = tk.Label(
            self.frame,
            text="Gerenciamento de Vendas",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        title.pack(pady=20)
        
        # Frame superior com formulário e carrinho
        top_frame = tk.Frame(self.frame, bg="white")
        top_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Frame esquerdo - Formulário
        left_frame = tk.Frame(top_frame, bg="white", relief=tk.GROOVE, bd=2)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Título do formulário
        tk.Label(
            left_frame,
            text="Nova Venda",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=10)
        
        form_frame = tk.Frame(left_frame, bg="white")
        form_frame.pack(pady=10, padx=15, fill=tk.X)
        
        # Cliente
        tk.Label(
            form_frame,
            text="Cliente:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self.combo_cliente = ttk.Combobox(
            form_frame,
            font=("Arial", 10),
            width=35,
            state="readonly"
        )
        self.combo_cliente.grid(row=0, column=1, pady=5, padx=5, columnspan=2)
        self._atualizar_combo_clientes()
        
        # Forma de Pagamento
        tk.Label(
            form_frame,
            text="Forma Pagamento:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self.combo_pagamento = ttk.Combobox(
            form_frame,
            font=("Arial", 10),
            width=35,
            state="readonly",
            values=["Dinheiro", "Cartão Débito", "Cartão Crédito", "PIX", "Boleto"]
        )
        self.combo_pagamento.grid(row=1, column=1, pady=5, padx=5, columnspan=2)
        
        # Separador
        ttk.Separator(form_frame, orient="horizontal").grid(
            row=2, column=0, columnspan=3, sticky="ew", pady=10
        )
        
        # Adicionar produtos
        tk.Label(
            form_frame,
            text="Adicionar Produto:",
            font=("Arial", 11, "bold"),
            bg="white"
        ).grid(row=3, column=0, columnspan=3, sticky="w", pady=(10, 5))
        
        tk.Label(
            form_frame,
            text="Produto:",
            font=("Arial", 10),
            bg="white"
        ).grid(row=4, column=0, sticky="w", pady=5)
        
        self.combo_produto = ttk.Combobox(
            form_frame,
            font=("Arial", 10),
            width=25,
            state="readonly"
        )
        self.combo_produto.grid(row=4, column=1, pady=5, padx=5)
        self.combo_produto.bind("<<ComboboxSelected>>", self._on_produto_selected)
        self._atualizar_combo_produtos()
        
        tk.Label(
            form_frame,
            text="Qtd:",
            font=("Arial", 10),
            bg="white"
        ).grid(row=5, column=0, sticky="w", pady=5)
        
        self.entry_quantidade = tk.Entry(form_frame, font=("Arial", 10), width=10)
        self.entry_quantidade.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
        tk.Label(
            form_frame,
            text="Estoque:",
            font=("Arial", 10),
            bg="white"
        ).grid(row=5, column=2, sticky="w", pady=5)
        
        self.lbl_estoque = tk.Label(
            form_frame,
            text="0",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#e74c3c"
        )
        self.lbl_estoque.grid(row=5, column=2, pady=5, sticky="e")
        
        btn_add_produto = tk.Button(
            form_frame,
            text="➕ Adicionar ao Carrinho",
            command=self._adicionar_produto_carrinho,
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            cursor="hand2",
            pady=5
        )
        btn_add_produto.grid(row=6, column=0, columnspan=3, pady=10, sticky="ew")
        
        # Frame direito - Carrinho
        right_frame = tk.Frame(top_frame, bg="white", relief=tk.GROOVE, bd=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Título do carrinho
        tk.Label(
            right_frame,
            text="Carrinho de Compras",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=10)
        
        # Tabela do carrinho
        carrinho_table_frame = tk.Frame(right_frame, bg="white")
        carrinho_table_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(carrinho_table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree_carrinho = ttk.Treeview(
            carrinho_table_frame,
            columns=("Produto", "Qtd", "Valor Unit", "Subtotal"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=8
        )
        self.tree_carrinho.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree_carrinho.yview)
        
        self.tree_carrinho.heading("Produto", text="Produto")
        self.tree_carrinho.heading("Qtd", text="Qtd")
        self.tree_carrinho.heading("Valor Unit", text="Valor Unit.")
        self.tree_carrinho.heading("Subtotal", text="Subtotal")
        
        self.tree_carrinho.column("Produto", width=150)
        self.tree_carrinho.column("Qtd", width=50, anchor="center")
        self.tree_carrinho.column("Valor Unit", width=80, anchor="e")
        self.tree_carrinho.column("Subtotal", width=80, anchor="e")
        
        # Botão remover do carrinho
        btn_remover = tk.Button(
            right_frame,
            text="➖ Remover Selecionado",
            command=self._remover_produto_carrinho,
            font=("Arial", 9),
            bg="#e74c3c",
            fg="white",
            cursor="hand2",
            pady=3
        )
        btn_remover.pack(pady=5)
        
        # Total
        total_frame = tk.Frame(right_frame, bg="white")
        total_frame.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(
            total_frame,
            text="TOTAL:",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(side=tk.LEFT)
        
        self.lbl_total = tk.Label(
            total_frame,
            text="R$ 0,00",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#27ae60"
        )
        self.lbl_total.pack(side=tk.RIGHT)
        
        # Botões principais
        btn_frame = tk.Frame(right_frame, bg="white")
        btn_frame.pack(pady=10)
        
        self.btn_finalizar = tk.Button(
            btn_frame,
            text="✅ Finalizar Venda",
            command=self._finalizar_venda,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_finalizar.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = tk.Button(
            btn_frame,
            text="🗑️ Limpar Carrinho",
            command=self._limpar_carrinho,
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8
        )
        btn_limpar.pack(side=tk.LEFT, padx=5)
        
        # Frame inferior - Lista de vendas
        bottom_frame = tk.Frame(self.frame, bg="white")
        bottom_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            bottom_frame,
            text="Histórico de Vendas",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=10)
        
        # Tabela de vendas
        vendas_table_frame = tk.Frame(bottom_frame, bg="white")
        vendas_table_frame.pack(pady=5, fill=tk.BOTH, expand=True)
        
        scrollbar2 = ttk.Scrollbar(vendas_table_frame)
        scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree_vendas = ttk.Treeview(
            vendas_table_frame,
            columns=("Codigo", "Data", "Cliente", "Total", "Pagamento"),
            show="headings",
            yscrollcommand=scrollbar2.set,
            height=6
        )
        self.tree_vendas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar2.config(command=self.tree_vendas.yview)
        
        self.tree_vendas.heading("Codigo", text="Código")
        self.tree_vendas.heading("Data", text="Data/Hora")
        self.tree_vendas.heading("Cliente", text="Cliente")
        self.tree_vendas.heading("Total", text="Valor Total")
        self.tree_vendas.heading("Pagamento", text="Forma Pagamento")
        
        self.tree_vendas.column("Codigo", width=100, anchor="center")
        self.tree_vendas.column("Data", width=150, anchor="center")
        self.tree_vendas.column("Cliente", width=200)
        self.tree_vendas.column("Total", width=120, anchor="e")
        self.tree_vendas.column("Pagamento", width=150, anchor="center")
        
        # Botão excluir venda
        btn_excluir = tk.Button(
            bottom_frame,
            text="🗑️ Excluir Venda Selecionada",
            command=self._excluir_venda,
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_excluir.pack(pady=10)
    
    def _atualizar_combo_clientes(self):
        """Atualiza o combo de clientes"""
        clientes = self.data_manager.listar_clientes()
        if clientes:
            valores = [f"{c['id']} - {c['nome']}" for c in clientes]
            self.combo_cliente['values'] = valores
        else:
            self.combo_cliente['values'] = []
    
    def _atualizar_combo_produtos(self):
        """Atualiza o combo de produtos"""
        produtos = self.data_manager.listar_produtos()
        if produtos:
            valores = [f"{p['id']} - {p['nome']}" for p in produtos]
            self.combo_produto['values'] = valores
        else:
            self.combo_produto['values'] = []
    
    def _on_produto_selected(self, event):
        """Atualiza informações quando produto é selecionado"""
        produto_sel = self.combo_produto.get()
        if produto_sel:
            produto_id = int(produto_sel.split(' - ')[0])
            produto = self.data_manager.buscar_produto(produto_id)
            if produto:
                self.lbl_estoque.config(text=str(produto['quantidade_estoque']))
    
    def _adicionar_produto_carrinho(self):
        """Adiciona produto ao carrinho"""
        produto_sel = self.combo_produto.get()
        quantidade_str = self.entry_quantidade.get().strip()
        
        if not produto_sel:
            messagebox.showerror("Erro", "Selecione um produto!")
            return
        
        try:
            quantidade = int(quantidade_str)
            if quantidade <= 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Quantidade inválida!")
            return
        
        # Obter dados do produto
        produto_id = int(produto_sel.split(' - ')[0])
        produto = self.data_manager.buscar_produto(produto_id)
        
        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        
        # Verificar estoque
        if quantidade > produto['quantidade_estoque']:
            messagebox.showerror(
                "Erro",
                f"Estoque insuficiente! Disponível: {produto['quantidade_estoque']}"
            )
            return
        
        # Adicionar ao carrinho
        self.produtos_venda.append({
            'produto_id': produto_id,
            'nome': produto['nome'],
            'quantidade': quantidade,
            'valor_unitario': produto['valor_unitario']
        })
        
        # Atualizar interface
        self._atualizar_carrinho()
        self.combo_produto.set('')
        self.entry_quantidade.delete(0, tk.END)
        self.lbl_estoque.config(text="0")
    
    def _atualizar_carrinho(self):
        """Atualiza a visualização do carrinho"""
        # Limpar tabela
        for item in self.tree_carrinho.get_children():
            self.tree_carrinho.delete(item)
        
        # Adicionar produtos
        total = 0
        for prod in self.produtos_venda:
            subtotal = prod['quantidade'] * prod['valor_unitario']
            total += subtotal
            
            self.tree_carrinho.insert("", tk.END, values=(
                prod['nome'],
                prod['quantidade'],
                f"R$ {prod['valor_unitario']:.2f}",
                f"R$ {subtotal:.2f}"
            ))
        
        # Atualizar total
        self.lbl_total.config(text=f"R$ {total:,.2f}")
    
    def _remover_produto_carrinho(self):
        """Remove produto selecionado do carrinho"""
        selection = self.tree_carrinho.selection()
        if not selection:
            messagebox.showerror("Erro", "Selecione um produto para remover!")
            return
        
        item = self.tree_carrinho.item(selection[0])
        index = self.tree_carrinho.index(selection[0])
        
        # Remover da lista
        self.produtos_venda.pop(index)
        
        # Atualizar interface
        self._atualizar_carrinho()
    
    def _limpar_carrinho(self):
        """Limpa o carrinho"""
        self.produtos_venda = []
        self._atualizar_carrinho()
    
    def _finalizar_venda(self):
        """Finaliza a venda"""
        cliente_sel = self.combo_cliente.get()
        pagamento = self.combo_pagamento.get()
        
        # Validações
        if not cliente_sel:
            messagebox.showerror("Erro", "Selecione um cliente!")
            return
        
        if not pagamento:
            messagebox.showerror("Erro", "Selecione a forma de pagamento!")
            return
        
        if not self.produtos_venda:
            messagebox.showerror("Erro", "Adicione produtos ao carrinho!")
            return
        
        # Extrair ID do cliente
        cliente_id = int(cliente_sel.split(' - ')[0])
        
        # Criar venda
        venda_id = self.data_manager.criar_venda(
            cliente_id,
            self.produtos_venda,
            pagamento
        )
        
        if venda_id:
            messagebox.showinfo("Sucesso", f"Venda finalizada!\nCódigo: VND{venda_id:05d}")
            self._limpar_formulario()
            self._atualizar_lista_vendas()
            self._atualizar_combo_produtos()  # Atualizar estoques
        else:
            messagebox.showerror("Erro", "Erro ao finalizar venda!")
    
    def _limpar_formulario(self):
        """Limpa o formulário"""
        self.combo_cliente.set('')
        self.combo_pagamento.set('')
        self.combo_produto.set('')
        self.entry_quantidade.delete(0, tk.END)
        self.lbl_estoque.config(text="0")
        self._limpar_carrinho()
    
    def _atualizar_lista_vendas(self):
        """Atualiza a lista de vendas"""
        # Limpar tabela
        for item in self.tree_vendas.get_children():
            self.tree_vendas.delete(item)
        
        # Adicionar vendas
        vendas = self.data_manager.listar_vendas()
        for venda in vendas:
            self.tree_vendas.insert("", tk.END, values=(
                venda['codigo'],
                venda['data_hora'],
                venda['cliente_nome'],
                f"R$ {venda['valor_total']:.2f}",
                venda['forma_pagamento']
            ))
    
    def _excluir_venda(self):
        """Exclui a venda selecionada"""
        selection = self.tree_vendas.selection()
        if not selection:
            messagebox.showerror("Erro", "Selecione uma venda para excluir!")
            return
        
        item = self.tree_vendas.item(selection[0])
        codigo = item['values'][0]
        
        # Extrair ID do código
        venda_id = int(codigo.replace("VND", ""))
        
        # Confirmar exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Deseja realmente excluir esta venda?\n\n"
            "Os produtos serão devolvidos ao estoque."
        )
        
        if not resposta:
            return
        
        # Excluir venda
        sucesso = self.data_manager.excluir_venda(venda_id)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Venda excluída com sucesso!")
            self._atualizar_lista_vendas()
            self._atualizar_combo_produtos()
        else:
            messagebox.showerror("Erro", "Erro ao excluir venda!")
