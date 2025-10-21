"""
Interface de gerenciamento de produtos
"""

import tkinter as tk
from tkinter import ttk, messagebox


class ProdutosFrame:
    """Frame para gerenciar produtos"""
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._criar_interface()
        self._atualizar_lista()
        
    def _criar_interface(self):
        """Cria a interface de produtos"""
        # Título
        title = tk.Label(
            self.frame,
            text="Gerenciamento de Produtos",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        title.pack(pady=20)
        
        # Frame para formulário
        form_frame = tk.Frame(self.frame, bg="white")
        form_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # Nome do Produto
        tk.Label(
            form_frame,
            text="Nome do Produto:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=5, padx=5)
        
        self.entry_nome = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.entry_nome.grid(row=0, column=1, pady=5, padx=5)
        
        # Categoria
        tk.Label(
            form_frame,
            text="Categoria:*",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=2, sticky="w", pady=5, padx=5)
        
        self.combo_categoria = ttk.Combobox(
            form_frame,
            font=("Arial", 11),
            width=20,
            state="readonly"
        )
        self.combo_categoria.grid(row=0, column=3, pady=5, padx=5)
        self._atualizar_combo_categorias()
        
        # Valor Unitário
        tk.Label(
            form_frame,
            text="Valor Unitário (R$):",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=5, padx=5)
        
        self.entry_valor = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.entry_valor.grid(row=1, column=1, pady=5, padx=5)
        
        # Quantidade Inicial
        tk.Label(
            form_frame,
            text="Quantidade Inicial:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=2, sticky="w", pady=5, padx=5)
        
        self.entry_quantidade = tk.Entry(form_frame, font=("Arial", 11), width=20)
        self.entry_quantidade.grid(row=1, column=3, pady=5, padx=5)
        
        # Botões de ação
        btn_frame = tk.Frame(self.frame, bg="white")
        btn_frame.pack(pady=15)
        
        self.btn_adicionar = tk.Button(
            btn_frame,
            text="➕ Adicionar Produto",
            command=self._adicionar_produto,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        self.btn_editar = tk.Button(
            btn_frame,
            text="✏️ Salvar Edição",
            command=self._editar_produto,
            font=("Arial", 11, "bold"),
            bg="#f39c12",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8,
            state=tk.DISABLED
        )
        self.btn_editar.pack(side=tk.LEFT, padx=5)
        
        self.btn_cancelar = tk.Button(
            btn_frame,
            text="❌ Cancelar",
            command=self._cancelar,
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8,
            state=tk.DISABLED
        )
        self.btn_cancelar.pack(side=tk.LEFT, padx=5)
        
        self.btn_excluir = tk.Button(
            btn_frame,
            text="🗑️ Excluir Produto",
            command=self._excluir_produto,
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_excluir.pack(side=tk.LEFT, padx=5)
        
        # Frame para tabela
        table_frame = tk.Frame(self.frame, bg="white")
        table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nome", "Categoria", "Valor", "Estoque"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome do Produto")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Valor", text="Valor Unitário")
        self.tree.heading("Estoque", text="Estoque")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=250, anchor="w")
        self.tree.column("Categoria", width=150, anchor="w")
        self.tree.column("Valor", width=120, anchor="e")
        self.tree.column("Estoque", width=100, anchor="center")
        
        # Bind para seleção
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        
        self.produto_selecionado = None
        
    def _atualizar_combo_categorias(self):
        """Atualiza o combo de categorias"""
        categorias = self.data_manager.listar_categorias()
        if categorias:
            valores = [f"{cat['id']} - {cat['nome']}" for cat in categorias]
            self.combo_categoria['values'] = valores
        else:
            self.combo_categoria['values'] = []
            messagebox.showwarning(
                "Atenção",
                "Nenhuma categoria cadastrada! Cadastre uma categoria antes de adicionar produtos."
            )
    
    def _atualizar_lista(self):
        """Atualiza a lista de produtos"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar produtos
        produtos = self.data_manager.listar_produtos()
        for prod in produtos:
            self.tree.insert("", tk.END, values=(
                prod['id'],
                prod['nome'],
                prod['categoria_nome'],
                f"R$ {prod['valor_unitario']:.2f}",
                prod['quantidade_estoque']
            ))
    
    def _on_select(self, event):
        """Callback quando um produto é selecionado"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            self.produto_selecionado = values[0]
            
            # Buscar dados completos do produto
            produto = self.data_manager.buscar_produto(self.produto_selecionado)
            if produto:
                # Preencher formulário
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, produto['nome'])
                
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, f"{produto['valor_unitario']:.2f}")
                
                # Selecionar categoria no combo
                for i, val in enumerate(self.combo_categoria['values']):
                    if val.startswith(str(produto['categoria_id'])):
                        self.combo_categoria.current(i)
                        break
                
                # Desabilitar campo de quantidade na edição
                self.entry_quantidade.delete(0, tk.END)
                self.entry_quantidade.config(state=tk.DISABLED)
                
                # Ativar botões de edição
                self.btn_editar.config(state=tk.NORMAL)
                self.btn_cancelar.config(state=tk.NORMAL)
                self.btn_adicionar.config(state=tk.DISABLED)
    
    def _adicionar_produto(self):
        """Adiciona um novo produto"""
        nome = self.entry_nome.get().strip()
        valor_str = self.entry_valor.get().strip()
        quantidade_str = self.entry_quantidade.get().strip()
        categoria_sel = self.combo_categoria.get()
        
        # Validações
        if not nome:
            messagebox.showerror("Erro", "O nome do produto é obrigatório!")
            return
        
        if not categoria_sel:
            messagebox.showerror("Erro", "Selecione uma categoria!")
            return
        
        try:
            valor = float(valor_str.replace(',', '.'))
            if valor <= 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Valor unitário inválido!")
            return
        
        try:
            quantidade = int(quantidade_str)
            if quantidade < 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Quantidade inválida!")
            return
        
        # Extrair ID da categoria
        categoria_id = int(categoria_sel.split(' - ')[0])
        
        # Adicionar produto
        produto_id = self.data_manager.criar_produto(nome, categoria_id, valor, quantidade)
        
        if produto_id:
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            self._limpar_formulario()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao adicionar produto!")
    
    def _editar_produto(self):
        """Edita o produto selecionado"""
        if not self.produto_selecionado:
            messagebox.showerror("Erro", "Nenhum produto selecionado!")
            return
        
        nome = self.entry_nome.get().strip()
        valor_str = self.entry_valor.get().strip()
        categoria_sel = self.combo_categoria.get()
        
        # Validações
        if not nome:
            messagebox.showerror("Erro", "O nome do produto é obrigatório!")
            return
        
        if not categoria_sel:
            messagebox.showerror("Erro", "Selecione uma categoria!")
            return
        
        try:
            valor = float(valor_str.replace(',', '.'))
            if valor <= 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Valor unitário inválido!")
            return
        
        # Extrair ID da categoria
        categoria_id = int(categoria_sel.split(' - ')[0])
        
        # Editar produto
        sucesso = self.data_manager.editar_produto(
            self.produto_selecionado, nome, categoria_id, valor
        )
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao editar produto!")
    
    def _excluir_produto(self):
        """Exclui o produto selecionado"""
        if not self.produto_selecionado:
            messagebox.showerror("Erro", "Selecione um produto para excluir!")
            return
        
        # Confirmar exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Deseja realmente excluir este produto?"
        )
        
        if not resposta:
            return
        
        # Excluir produto
        sucesso = self.data_manager.excluir_produto(self.produto_selecionado)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao excluir produto!")
    
    def _cancelar(self):
        """Cancela a edição"""
        self.produto_selecionado = None
        self._limpar_formulario()
        self.btn_editar.config(state=tk.DISABLED)
        self.btn_cancelar.config(state=tk.DISABLED)
        self.btn_adicionar.config(state=tk.NORMAL)
        self.entry_quantidade.config(state=tk.NORMAL)
        self.tree.selection_remove(self.tree.selection())
    
    def _limpar_formulario(self):
        """Limpa o formulário"""
        self.entry_nome.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.combo_categoria.set('')
