"""
Interface de gerenciamento de entrada de estoque
"""

import tkinter as tk
from tkinter import ttk, messagebox


class EntradaEstoqueFrame:
    """Frame para gerenciar entrada de estoque"""
    
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._criar_interface()
        self._atualizar_lista()
        
    def _criar_interface(self):
        """Cria a interface de entrada de estoque"""
        # Título
        title = tk.Label(
            self.frame,
            text="Entrada de Estoque",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        title.pack(pady=20)
        
        # Frame superior - Formulário
        form_container = tk.Frame(self.frame, bg="white", relief=tk.GROOVE, bd=2)
        form_container.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(
            form_container,
            text="Registrar Nova Entrada",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=10)
        
        form_frame = tk.Frame(form_container, bg="white")
        form_frame.pack(pady=10, padx=20)
        
        # Produto
        tk.Label(
            form_frame,
            text="Produto:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=10, padx=5)
        
        self.combo_produto = ttk.Combobox(
            form_frame,
            font=("Arial", 11),
            width=40,
            state="readonly"
        )
        self.combo_produto.grid(row=0, column=1, pady=10, padx=10)
        self.combo_produto.bind("<<ComboboxSelected>>", self._on_produto_selected)
        self._atualizar_combo_produtos()
        
        # Estoque atual
        tk.Label(
            form_frame,
            text="Estoque Atual:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=2, sticky="w", pady=10, padx=10)
        
        self.lbl_estoque_atual = tk.Label(
            form_frame,
            text="0",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#e74c3c"
        )
        self.lbl_estoque_atual.grid(row=0, column=3, pady=10, padx=5)
        
        # Quantidade a adicionar
        tk.Label(
            form_frame,
            text="Quantidade a Adicionar:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=10, padx=5)
        
        self.entry_quantidade = tk.Entry(form_frame, font=("Arial", 11), width=20)
        self.entry_quantidade.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        
        # Novo estoque (calculado)
        tk.Label(
            form_frame,
            text="Novo Estoque:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=2, sticky="w", pady=10, padx=10)
        
        self.lbl_novo_estoque = tk.Label(
            form_frame,
            text="0",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#27ae60"
        )
        self.lbl_novo_estoque.grid(row=1, column=3, pady=10, padx=5)
        
        # Bind para calcular novo estoque
        self.entry_quantidade.bind("<KeyRelease>", self._calcular_novo_estoque)
        
        # Botões
        btn_frame = tk.Frame(form_container, bg="white")
        btn_frame.pack(pady=15)
        
        btn_registrar = tk.Button(
            btn_frame,
            text="✅ Registrar Entrada",
            command=self._registrar_entrada,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            cursor="hand2",
            padx=30,
            pady=10
        )
        btn_registrar.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = tk.Button(
            btn_frame,
            text="🔄 Limpar",
            command=self._limpar_formulario,
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            cursor="hand2",
            padx=30,
            pady=10
        )
        btn_limpar.pack(side=tk.LEFT, padx=5)
        
        # Frame inferior - Histórico
        history_frame = tk.Frame(self.frame, bg="white")
        history_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            history_frame,
            text="Histórico de Entradas",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=10)
        
        # Tabela
        table_frame = tk.Frame(history_frame, bg="white")
        table_frame.pack(pady=5, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Produto", "Quantidade", "DataHora"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade Adicionada")
        self.tree.heading("DataHora", text="Data e Hora")
        
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Produto", width=300, anchor="w")
        self.tree.column("Quantidade", width=180, anchor="center")
        self.tree.column("DataHora", width=200, anchor="center")
        
    def _atualizar_combo_produtos(self):
        """Atualiza o combo de produtos"""
        produtos = self.data_manager.listar_produtos()
        if produtos:
            valores = [f"{p['id']} - {p['nome']}" for p in produtos]
            self.combo_produto['values'] = valores
        else:
            self.combo_produto['values'] = []
            messagebox.showwarning(
                "Atenção",
                "Nenhum produto cadastrado! Cadastre produtos antes de registrar entradas."
            )
    
    def _on_produto_selected(self, event):
        """Atualiza estoque atual quando produto é selecionado"""
        produto_sel = self.combo_produto.get()
        if produto_sel:
            produto_id = int(produto_sel.split(' - ')[0])
            produto = self.data_manager.buscar_produto(produto_id)
            if produto:
                self.lbl_estoque_atual.config(text=str(produto['quantidade_estoque']))
                self._calcular_novo_estoque()
    
    def _calcular_novo_estoque(self, event=None):
        """Calcula e exibe o novo estoque"""
        try:
            estoque_atual = int(self.lbl_estoque_atual.cget("text"))
            quantidade_adicionar = int(self.entry_quantidade.get())
            novo_estoque = estoque_atual + quantidade_adicionar
            self.lbl_novo_estoque.config(text=str(novo_estoque))
        except:
            self.lbl_novo_estoque.config(text="0")
    
    def _registrar_entrada(self):
        """Registra uma nova entrada de estoque"""
        produto_sel = self.combo_produto.get()
        quantidade_str = self.entry_quantidade.get().strip()
        
        # Validações
        if not produto_sel:
            messagebox.showerror("Erro", "Selecione um produto!")
            return
        
        try:
            quantidade = int(quantidade_str)
            if quantidade <= 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Quantidade inválida! Digite um número positivo.")
            return
        
        # Extrair ID do produto
        produto_id = int(produto_sel.split(' - ')[0])
        
        # Registrar entrada
        entrada_id = self.data_manager.criar_entrada_estoque(produto_id, quantidade)
        
        if entrada_id:
            messagebox.showinfo(
                "Sucesso",
                f"Entrada registrada com sucesso!\n\n"
                f"Quantidade adicionada: {quantidade}\n"
                f"Novo estoque: {self.lbl_novo_estoque.cget('text')}"
            )
            self._limpar_formulario()
            self._atualizar_lista()
            self._atualizar_combo_produtos()
        else:
            messagebox.showerror("Erro", "Erro ao registrar entrada!")
    
    def _limpar_formulario(self):
        """Limpa o formulário"""
        self.combo_produto.set('')
        self.entry_quantidade.delete(0, tk.END)
        self.lbl_estoque_atual.config(text="0")
        self.lbl_novo_estoque.config(text="0")
    
    def _atualizar_lista(self):
        """Atualiza a lista de entradas"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar entradas
        entradas = self.data_manager.listar_entradas_estoque()
        
        # Ordenar por ID decrescente (mais recentes primeiro)
        entradas_ordenadas = sorted(entradas, key=lambda x: x['id'], reverse=True)
        
        for entrada in entradas_ordenadas:
            self.tree.insert("", tk.END, values=(
                entrada['id'],
                entrada['produto_nome'],
                f"+{entrada['quantidade']}",
                entrada['data_hora']
            ))
