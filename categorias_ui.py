"""
Interface de gerenciamento de categorias
"""

import tkinter as tk
from tkinter import ttk, messagebox


class CategoriasFrame:
    """Frame para gerenciar categorias"""
    
    def __init__(self, parent, data_manager, colors):
        self.parent = parent
        self.data_manager = data_manager
        self.colors = colors
        self.frame = tk.Frame(parent, bg=colors['white'])
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._criar_interface()
        self._atualizar_lista()
        
    def _criar_interface(self):
        """Cria a interface de categorias"""
        # Título
        title = tk.Label(
            self.frame,
            text="📂 Categorias",
            font=("Segoe UI", 24, "bold"),
            bg=self.colors['white'],
            fg=self.colors['text_dark']
        )
        title.pack(pady=(0, 25), anchor="w", padx=20)
        
        # Frame para formulário
        form_frame = tk.Frame(self.frame, bg=self.colors['white'])
        form_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # Campo Nome
        tk.Label(
            form_frame,
            text="Nome da Categoria:",
            font=("Segoe UI", 11),
            bg=self.colors['white'],
            fg=self.colors['text_dark']
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self.entry_nome = tk.Entry(form_frame, font=("Segoe UI", 11), width=40, bd=1, relief=tk.SOLID)
        self.entry_nome.grid(row=0, column=1, pady=5, padx=10)
        
        # Botões de ação
        btn_frame = tk.Frame(form_frame, bg=self.colors['white'])
        btn_frame.grid(row=0, column=2, padx=10)
        
        self.btn_adicionar = tk.Button(
            btn_frame,
            text="➕ Adicionar",
            command=self._adicionar_categoria,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['success'],
            fg=self.colors['white'],
            cursor="hand2",
            padx=20,
            pady=8,
            bd=0,
            relief=tk.FLAT
        )
        self.btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        self.btn_editar = tk.Button(
            btn_frame,
            text="✏️ Editar",
            command=self._editar_categoria,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['warning'],
            fg=self.colors['white'],
            cursor="hand2",
            padx=20,
            pady=8,
            bd=0,
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.btn_editar.pack(side=tk.LEFT, padx=5)
        
        self.btn_cancelar = tk.Button(
            btn_frame,
            text="❌ Cancelar",
            command=self._cancelar,
            font=("Segoe UI", 10, "bold"),
            bg="#6B7280",
            fg=self.colors['white'],
            cursor="hand2",
            padx=20,
            pady=8,
            bd=0,
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.btn_cancelar.pack(side=tk.LEFT, padx=5)
        
        # Frame para tabela
        table_frame = tk.Frame(self.frame, bg=self.colors['white'])
        table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nome"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome da Categoria")
        
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Nome", width=400, anchor="w")
        
        # Bind para seleção
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        
        # Botão excluir
        btn_excluir = tk.Button(
            self.frame,
            text="🗑️ Excluir Categoria",
            command=self._excluir_categoria,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['danger'],
            fg=self.colors['white'],
            cursor="hand2",
            padx=25,
            pady=10,
            bd=0,
            relief=tk.FLAT
        )
        btn_excluir.pack(pady=20)
        
        self.categoria_selecionada = None
        
    def _atualizar_lista(self):
        """Atualiza a lista de categorias"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar categorias
        categorias = self.data_manager.listar_categorias()
        for cat in categorias:
            self.tree.insert("", tk.END, values=(cat['id'], cat['nome']))
    
    def _on_select(self, event):
        """Callback quando uma categoria é selecionada"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            self.categoria_selecionada = values[0]
            
            # Preencher formulário
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, values[1])
            
            # Ativar botão editar
            self.btn_editar.config(state=tk.NORMAL)
            self.btn_cancelar.config(state=tk.NORMAL)
            self.btn_adicionar.config(state=tk.DISABLED)
    
    def _adicionar_categoria(self):
        """Adiciona uma nova categoria"""
        nome = self.entry_nome.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "O nome da categoria é obrigatório!")
            return
        
        # Adicionar categoria
        self.data_manager.criar_categoria(nome)
        
        # Limpar formulário
        self.entry_nome.delete(0, tk.END)
        
        # Atualizar lista
        self._atualizar_lista()
        
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
    
    def _editar_categoria(self):
        """Edita a categoria selecionada"""
        if not self.categoria_selecionada:
            messagebox.showerror("Erro", "Nenhuma categoria selecionada!")
            return
        
        nome = self.entry_nome.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "O nome da categoria é obrigatório!")
            return
        
        # Editar categoria
        sucesso = self.data_manager.editar_categoria(self.categoria_selecionada, nome)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Categoria editada com sucesso!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao editar categoria!")
    
    def _excluir_categoria(self):
        """Exclui a categoria selecionada"""
        if not self.categoria_selecionada:
            messagebox.showerror("Erro", "Selecione uma categoria para excluir!")
            return
        
        # Confirmar exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Ao excluir esta categoria, todos os produtos relacionados também serão excluídos.\n\n"
            "Deseja continuar?"
        )
        
        if not resposta:
            return
        
        # Excluir categoria
        sucesso = self.data_manager.excluir_categoria(self.categoria_selecionada)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Categoria e produtos relacionados excluídos!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao excluir categoria!")
    
    def _cancelar(self):
        """Cancela a edição"""
        self.categoria_selecionada = None
        self.entry_nome.delete(0, tk.END)
        self.btn_editar.config(state=tk.DISABLED)
        self.btn_cancelar.config(state=tk.DISABLED)
        self.btn_adicionar.config(state=tk.NORMAL)
        self.tree.selection_remove(self.tree.selection())
