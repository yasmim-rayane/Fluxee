"""
Interface de gerenciamento de clientes
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ClientesFrame:
    """Frame para gerenciar clientes"""
    
    def __init__(self, parent, data_manager, colors):
        self.parent = parent
        self.data_manager = data_manager
        self.colors = colors
        self.frame = tk.Frame(parent, bg=colors['white'])
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._criar_interface()
        self._atualizar_lista()
        
    def _criar_interface(self):
        """Cria a interface de clientes"""
        # Título
        title = tk.Label(
            self.frame,
            text="👥 Clientes",
            font=("Segoe UI", 24, "bold"),
            bg=self.colors['white'],
            fg=self.colors['text_dark']
        )
        title.pack(pady=(0, 25), anchor="w", padx=20)
        
    def _criar_interface(self):
        """Cria a interface de clientes"""
        # Título
        title = tk.Label(
            self.frame,
            text="Gerenciamento de Clientes",
            font=("Segoe UI", 18, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text_dark"]
        )
        title.pack(pady=20)
        
        # Frame para formulário
        form_frame = tk.Frame(self.frame, bg=self.colors["white"])
        form_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # Nome Completo
        tk.Label(
            form_frame,
            text="Nome Completo:",
            font=("Segoe UI", 11),
            bg=self.colors["white"]
        ).grid(row=0, column=0, sticky="w", pady=5, padx=5)
        
        self.entry_nome = tk.Entry(form_frame, font=("Segoe UI", 11), width=40)
        self.entry_nome.grid(row=0, column=1, pady=5, padx=5, columnspan=2)
        
        # CPF
        tk.Label(
            form_frame,
            text="CPF:",
            font=("Segoe UI", 11),
            bg=self.colors["white"]
        ).grid(row=0, column=3, sticky="w", pady=5, padx=5)
        
        self.entry_cpf = tk.Entry(form_frame, font=("Segoe UI", 11), width=20)
        self.entry_cpf.grid(row=0, column=4, pady=5, padx=5)
        
        # Data de Nascimento
        tk.Label(
            form_frame,
            text="Data Nascimento:",
            font=("Segoe UI", 11),
            bg=self.colors["white"]
        ).grid(row=1, column=0, sticky="w", pady=5, padx=5)
        
        self.entry_data_nasc = tk.Entry(form_frame, font=("Segoe UI", 11), width=20)
        self.entry_data_nasc.grid(row=1, column=1, pady=5, padx=5)
        self.entry_data_nasc.insert(0, "DD/MM/AAAA")
        self.entry_data_nasc.bind("<FocusIn>", self._on_entry_click)
        self.entry_data_nasc.config(fg="gray")
        
        # Gênero
        tk.Label(
            form_frame,
            text="Gênero:",
            font=("Segoe UI", 11),
            bg=self.colors["white"]
        ).grid(row=1, column=2, sticky="w", pady=5, padx=5)
        
        self.combo_genero = ttk.Combobox(
            form_frame,
            font=("Segoe UI", 11),
            width=18,
            state="readonly",
            values=["Masculino", "Feminino", "Outro", "Prefiro não informar"]
        )
        self.combo_genero.grid(row=1, column=3, pady=5, padx=5)
        
        # Botões de ação
        btn_frame = tk.Frame(self.frame, bg=self.colors["white"])
        btn_frame.pack(pady=15)
        
        self.btn_adicionar = tk.Button(
            btn_frame,
            text="➕ Adicionar Cliente",
            command=self._adicionar_cliente,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["success"],
            fg=self.colors["white"],
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        self.btn_editar = tk.Button(
            btn_frame,
            text="✏️ Salvar Edição",
            command=self._editar_cliente,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["warning"],
            fg=self.colors["white"],
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
            font=("Segoe UI", 11, "bold"),
            bg="#6B7280",
            fg=self.colors["white"],
            cursor="hand2",
            padx=20,
            pady=8,
            state=tk.DISABLED
        )
        self.btn_cancelar.pack(side=tk.LEFT, padx=5)
        
        self.btn_excluir = tk.Button(
            btn_frame,
            text="🗑️ Excluir Cliente",
            command=self._excluir_cliente,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["danger"],
            fg=self.colors["white"],
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_excluir.pack(side=tk.LEFT, padx=5)
        
        # Frame para tabela
        table_frame = tk.Frame(self.frame, bg=self.colors["white"])
        table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nome", "CPF", "DataNasc", "Genero"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome Completo")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("DataNasc", text="Data Nascimento")
        self.tree.heading("Genero", text="Gênero")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=250, anchor="w")
        self.tree.column("CPF", width=150, anchor="center")
        self.tree.column("DataNasc", width=120, anchor="center")
        self.tree.column("Genero", width=150, anchor="w")
        
        # Bind para seleção
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        
        self.cliente_selecionado = None
    
    def _on_entry_click(self, event):
        """Remove placeholder ao clicar no campo"""
        if self.entry_data_nasc.get() == "DD/MM/AAAA":
            self.entry_data_nasc.delete(0, tk.END)
            self.entry_data_nasc.config(fg="black")
    
    def _atualizar_lista(self):
        """Atualiza a lista de clientes"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar clientes
        clientes = self.data_manager.listar_clientes()
        for cliente in clientes:
            self.tree.insert("", tk.END, values=(
                cliente['id'],
                cliente['nome'],
                cliente['cpf'],
                cliente['data_nascimento'],
                cliente['genero']
            ))
    
    def _on_select(self, event):
        """Callback quando um cliente é selecionado"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            self.cliente_selecionado = values[0]
            
            # Buscar dados completos do cliente
            cliente = self.data_manager.buscar_cliente(self.cliente_selecionado)
            if cliente:
                # Preencher formulário
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, cliente['nome'])
                
                self.entry_cpf.delete(0, tk.END)
                self.entry_cpf.insert(0, cliente['cpf'])
                
                self.entry_data_nasc.delete(0, tk.END)
                self.entry_data_nasc.insert(0, cliente['data_nascimento'])
                self.entry_data_nasc.config(fg="black")
                
                self.combo_genero.set(cliente['genero'])
                
                # Ativar botões de edição
                self.btn_editar.config(state=tk.NORMAL)
                self.btn_cancelar.config(state=tk.NORMAL)
                self.btn_adicionar.config(state=tk.DISABLED)
    
    def _validar_cpf(self, cpf):
        """Validação completa de CPF (formato e dígitos verificadores)"""
        # Remove caracteres não numéricos
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos
        if len(cpf_numeros) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais (CPF inválido)
        if cpf_numeros == cpf_numeros[0] * 11:
            return False
        
        # Validação do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf_numeros[i]) * (10 - i)
        
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        if int(cpf_numeros[9]) != digito1:
            return False
        
        # Validação do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf_numeros[i]) * (11 - i)
        
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        if int(cpf_numeros[10]) != digito2:
            return False
        
        return True
    
    def _validar_data(self, data_str):
        """Valida formato de data DD/MM/AAAA"""
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except:
            return False
    
    def _adicionar_cliente(self):
        """Adiciona um novo cliente"""
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()
        genero = self.combo_genero.get()
        
        # Validações
        if not nome:
            messagebox.showerror("Erro", "O nome é obrigatório!")
            return
        
        if not cpf or not self._validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido! Verifique se o CPF está correto.")
            return
        
        if not data_nasc or data_nasc == "DD/MM/AAAA" or not self._validar_data(data_nasc):
            messagebox.showerror("Erro", "Data de nascimento inválida! Use DD/MM/AAAA")
            return
        
        if not genero:
            messagebox.showerror("Erro", "Selecione o gênero!")
            return
        
        # Adicionar cliente
        cliente_id = self.data_manager.criar_cliente(nome, data_nasc, cpf, genero)
        
        if cliente_id:
            messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
            self._limpar_formulario()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao adicionar cliente!")
    
    def _editar_cliente(self):
        """Edita o cliente selecionado"""
        if not self.cliente_selecionado:
            messagebox.showerror("Erro", "Nenhum cliente selecionado!")
            return
        
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()
        genero = self.combo_genero.get()
        
        # Validações
        if not nome:
            messagebox.showerror("Erro", "O nome é obrigatório!")
            return
        
        if not cpf or not self._validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido! Verifique se o CPF está correto.")
            return
        
        if not data_nasc or not self._validar_data(data_nasc):
            messagebox.showerror("Erro", "Data de nascimento inválida!")
            return
        
        if not genero:
            messagebox.showerror("Erro", "Selecione o gênero!")
            return
        
        # Editar cliente
        sucesso = self.data_manager.editar_cliente(
            self.cliente_selecionado, nome, data_nasc, cpf, genero
        )
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Cliente editado com sucesso!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao editar cliente!")
    
    def _excluir_cliente(self):
        """Exclui o cliente selecionado"""
        if not self.cliente_selecionado:
            messagebox.showerror("Erro", "Selecione um cliente para excluir!")
            return
        
        # Confirmar exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Deseja realmente excluir este cliente?\n\n"
            "Observação: As vendas relacionadas a este cliente não serão excluídas."
        )
        
        if not resposta:
            return
        
        # Excluir cliente
        sucesso = self.data_manager.excluir_cliente(self.cliente_selecionado)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            self._cancelar()
            self._atualizar_lista()
        else:
            messagebox.showerror("Erro", "Erro ao excluir cliente!")
    
    def _cancelar(self):
        """Cancela a edição"""
        self.cliente_selecionado = None
        self._limpar_formulario()
        self.btn_editar.config(state=tk.DISABLED)
        self.btn_cancelar.config(state=tk.DISABLED)
        self.btn_adicionar.config(state=tk.NORMAL)
        self.tree.selection_remove(self.tree.selection())
    
    def _limpar_formulario(self):
        """Limpa o formulário"""
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_data_nasc.insert(0, "DD/MM/AAAA")
        self.entry_data_nasc.config(fg="gray")
        self.combo_genero.set('')
