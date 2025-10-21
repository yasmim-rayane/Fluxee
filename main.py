"""
Sistema de Gerenciamento de Estoque e Vendas - WA
Interface principal com Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import DataManager
from categorias_ui import CategoriasFrame
from produtos_ui import ProdutosFrame
from clientes_ui import ClientesFrame
from vendas_ui import VendasFrame
from entrada_estoque_ui import EntradaEstoqueFrame


class SistemaWA:
    """Classe principal do sistema"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema WA - Gestão de Estoque e Vendas")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")
        
        # Instanciar gerenciador de dados
        self.data_manager = DataManager()
        
        # Configurar interface
        self._criar_interface()
        
    def _criar_interface(self):
        """Cria a interface principal"""
        # Frame superior com logo e título
        top_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        top_frame.pack(fill=tk.X, side=tk.TOP)
        
        title_label = tk.Label(
            top_frame, 
            text="SISTEMA WA", 
            font=("Arial", 24, "bold"),
            bg="#2c3e50", 
            fg="white"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            top_frame, 
            text="Gestão de Estoque e Vendas", 
            font=("Arial", 12),
            bg="#2c3e50", 
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Frame principal com menu lateral e conteúdo
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Menu lateral
        menu_frame = tk.Frame(main_frame, bg="#34495e", width=200)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        menu_frame.pack_propagate(False)
        
        # Botões do menu
        menu_buttons = [
            ("🏠 Dashboard", self.mostrar_dashboard),
            ("📂 Categorias", self.mostrar_categorias),
            ("📦 Produtos", self.mostrar_produtos),
            ("📥 Entrada Estoque", self.mostrar_entrada_estoque),
            ("👥 Clientes", self.mostrar_clientes),
            ("💰 Vendas", self.mostrar_vendas),
            ("🚪 Sair", self.root.quit)
        ]
        
        for text, command in menu_buttons:
            btn = tk.Button(
                menu_frame,
                text=text,
                command=command,
                font=("Arial", 11),
                bg="#34495e",
                fg="white",
                activebackground="#2c3e50",
                activeforeground="white",
                bd=0,
                pady=15,
                cursor="hand2",
                anchor="w",
                padx=20
            )
            btn.pack(fill=tk.X, pady=2)
            
            # Efeito hover
            def on_enter(e, button=btn):
                button.config(bg="#2c3e50")
            
            def on_leave(e, button=btn):
                button.config(bg="#34495e")
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
        
        # Frame de conteúdo
        self.content_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, bd=1)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Mostrar dashboard inicial
        self.mostrar_dashboard()
        
    def limpar_conteudo(self):
        """Limpa o frame de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_dashboard(self):
        """Mostra o dashboard com estatísticas"""
        self.limpar_conteudo()
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="Dashboard",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        title.pack(pady=20)
        
        # Frame para cards de estatísticas
        stats_frame = tk.Frame(self.content_frame, bg="white")
        stats_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Calcular estatísticas
        total_produtos = len(self.data_manager.listar_produtos())
        total_categorias = len(self.data_manager.listar_categorias())
        total_clientes = len(self.data_manager.listar_clientes())
        total_vendas = len(self.data_manager.listar_vendas())
        valor_total_vendas = sum(v['valor_total'] for v in self.data_manager.listar_vendas())
        
        # Cards de estatísticas
        stats = [
            ("Produtos", total_produtos, "#3498db"),
            ("Categorias", total_categorias, "#9b59b6"),
            ("Clientes", total_clientes, "#e74c3c"),
            ("Vendas", total_vendas, "#2ecc71"),
        ]
        
        for i, (label, value, color) in enumerate(stats):
            card = tk.Frame(stats_frame, bg=color, relief=tk.RAISED, bd=2)
            card.grid(row=i//2, column=i%2, padx=20, pady=20, sticky="nsew")
            
            lbl_value = tk.Label(
                card,
                text=str(value),
                font=("Arial", 36, "bold"),
                bg=color,
                fg="white"
            )
            lbl_value.pack(pady=(20, 5))
            
            lbl_text = tk.Label(
                card,
                text=label,
                font=("Arial", 14),
                bg=color,
                fg="white"
            )
            lbl_text.pack(pady=(0, 20))
        
        # Card de valor total de vendas
        card_vendas = tk.Frame(stats_frame, bg="#f39c12", relief=tk.RAISED, bd=2)
        card_vendas.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
        
        lbl_vendas_valor = tk.Label(
            card_vendas,
            text=f"R$ {valor_total_vendas:,.2f}",
            font=("Arial", 32, "bold"),
            bg="#f39c12",
            fg="white"
        )
        lbl_vendas_valor.pack(pady=(20, 5))
        
        lbl_vendas_text = tk.Label(
            card_vendas,
            text="Valor Total em Vendas",
            font=("Arial", 14),
            bg="#f39c12",
            fg="white"
        )
        lbl_vendas_text.pack(pady=(0, 20))
        
        # Configurar grid
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        
    def mostrar_produtos(self):
        """Mostra a tela de produtos"""
        self.limpar_conteudo()
        ProdutosFrame(self.content_frame, self.data_manager)
        
    def mostrar_categorias(self):
        """Mostra a tela de categorias"""
        self.limpar_conteudo()
        CategoriasFrame(self.content_frame, self.data_manager)
        
    def mostrar_clientes(self):
        """Mostra a tela de clientes"""
        self.limpar_conteudo()
        ClientesFrame(self.content_frame, self.data_manager)
        
    def mostrar_vendas(self):
        """Mostra a tela de vendas"""
        self.limpar_conteudo()
        VendasFrame(self.content_frame, self.data_manager)
        
    def mostrar_entrada_estoque(self):
        """Mostra a tela de entrada de estoque"""
        self.limpar_conteudo()
        EntradaEstoqueFrame(self.content_frame, self.data_manager)
    
    def run(self):
        """Inicia o aplicativo"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SistemaWA()
    app.run()
