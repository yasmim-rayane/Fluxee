"""
Sistema de Gerenciamento de Estoque e Vendas - Fluxee
Interface principal com Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from database.data_manager import DataManager
from ui.categorias_ui import CategoriasFrame
from ui.produtos_ui import ProdutosFrame
from ui.clientes_ui import ClientesFrame
from ui.vendas_ui import VendasFrame
from ui.entrada_estoque_ui import EntradaEstoqueFrame


class SistemaWA:
    """Classe principal do sistema"""
    
    # Cores baseadas na identidade visual Fluxee
    COLORS = {
        'primary': '#00D4FF',      # Azul ciano brilhante (logo)
        'secondary': '#0EA5E9',    # Azul céu
        'dark': '#1E3A8A',         # Azul marinho escuro
        'darker': '#1F2937',       # Cinza escuro (backgrounds)
        'light': '#F0F9FF',        # Azul muito claro
        'white': '#FFFFFF',
        'text_dark': '#1F2937',
        'success': '#10B981',      # Verde
        'warning': '#F59E0B',      # Laranja
        'danger': '#EF4444',       # Vermelho
        'info': '#3B82F6'          # Azul
    }
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fluxee & WA - Sistema de Gestão de Estoque e Vendas")
        self.root.geometry("1400x800")
        self.root.configure(bg=self.COLORS['light'])
        
        # Instanciar gerenciador de dados
        self.data_manager = DataManager()
        
        # Configurar interface
        self._criar_interface()
        
    def _criar_interface(self):
        """Cria a interface principal"""
        # Frame superior com logo e título
        top_frame = tk.Frame(self.root, bg=self.COLORS['darker'], height=100)
        top_frame.pack(fill=tk.X, side=tk.TOP)
        top_frame.pack_propagate(False)
        
        # Container para logo e título
        header_container = tk.Frame(top_frame, bg=self.COLORS['darker'])
        header_container.pack(expand=True)
        
        # Tentar carregar logo
        logo_label = None
        logo_path = os.path.join('assets', 'fluxee_logo.png')
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                logo_img = logo_img.resize((60, 60), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                logo_label = tk.Label(
                    header_container,
                    image=self.logo_photo,
                    bg=self.COLORS['darker']
                )
                logo_label.pack(side=tk.LEFT, padx=(0, 15))
            except Exception as e:
                print(f"Erro ao carregar logo: {e}")
        
        # Título
        title_container = tk.Frame(header_container, bg=self.COLORS['darker'])
        title_container.pack(side=tk.LEFT)
        
        title_label = tk.Label(
            title_container, 
            text="FLUXEE", 
            font=("Segoe UI", 28, "bold"),
            bg=self.COLORS['darker'], 
            fg=self.COLORS['primary']
        )
        title_label.pack(anchor="w")
        
        subtitle_label = tk.Label(
            title_container, 
            text="Sistema de Gestão de Estoque e Vendas", 
            font=("Segoe UI", 11),
            bg=self.COLORS['darker'], 
            fg=self.COLORS['white']
        )
        subtitle_label.pack(anchor="w")
        
        # Frame principal com menu lateral e conteúdo
        main_frame = tk.Frame(self.root, bg=self.COLORS['light'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Menu lateral
        menu_frame = tk.Frame(main_frame, bg=self.COLORS['dark'], width=240)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        menu_frame.pack_propagate(False)
        
        # Título do menu
        menu_title = tk.Label(
            menu_frame,
            text="MENU",
            font=("Segoe UI", 12, "bold"),
            bg=self.COLORS['dark'],
            fg=self.COLORS['primary'],
            pady=20
        )
        menu_title.pack(fill=tk.X)
        
        # Botões do menu
        menu_buttons = [
            ("🏠  Dashboard", self.mostrar_dashboard),
            ("📂  Categorias", self.mostrar_categorias),
            ("📦  Produtos", self.mostrar_produtos),
            ("📥  Entrada Estoque", self.mostrar_entrada_estoque),
            ("👥  Clientes", self.mostrar_clientes),
            ("💰  Vendas", self.mostrar_vendas),
            ("🚪  Sair", self.root.quit)
        ]
        
        self.menu_buttons = []
        for text, command in menu_buttons:
            btn = tk.Button(
                menu_frame,
                text=text,
                command=command,
                font=("Segoe UI", 12),
                bg=self.COLORS['dark'],
                fg=self.COLORS['white'],
                activebackground=self.COLORS['primary'],
                activeforeground=self.COLORS['darker'],
                bd=0,
                pady=18,
                cursor="hand2",
                anchor="w",
                padx=25
            )
            btn.pack(fill=tk.X, pady=1)
            self.menu_buttons.append(btn)
            
            # Efeito hover
            def on_enter(e, button=btn):
                if button['bg'] != self.COLORS['primary']:
                    button.config(bg=self.COLORS['darker'])
            
            def on_leave(e, button=btn):
                if button['bg'] != self.COLORS['primary']:
                    button.config(bg=self.COLORS['dark'])
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
        
        # Frame de conteúdo
        self.content_frame = tk.Frame(main_frame, bg=self.COLORS['white'])
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Mostrar dashboard inicial
        self.mostrar_dashboard()
        
    def limpar_conteudo(self):
        """Limpa o frame de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_dashboard(self):
        """Mostra o dashboard com estatísticas"""
        self.limpar_conteudo()
        self._highlight_menu_button(0)
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="Dashboard",
            font=("Segoe UI", 26, "bold"),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_dark']
        )
        title.pack(pady=(0, 30), anchor="w")
        
        # Frame para cards de estatísticas
        stats_frame = tk.Frame(self.content_frame, bg=self.COLORS['white'])
        stats_frame.pack(pady=0, padx=0, fill=tk.BOTH, expand=True)
        
        # Calcular estatísticas
        total_produtos = len(self.data_manager.listar_produtos())
        total_categorias = len(self.data_manager.listar_categorias())
        total_clientes = len(self.data_manager.listar_clientes())
        total_vendas = len(self.data_manager.listar_vendas())
        valor_total_vendas = sum(v['valor_total'] for v in self.data_manager.listar_vendas())
        
        # Cards de estatísticas com novo design
        stats = [
            ("Produtos", total_produtos, self.COLORS['info'], "📦"),
            ("Categorias", total_categorias, self.COLORS['secondary'], "📂"),
            ("Clientes", total_clientes, self.COLORS['primary'], "👥"),
            ("Vendas", total_vendas, self.COLORS['success'], "💰"),
        ]
        
        for i, (label, value, color, icon) in enumerate(stats):
            # Card moderno com sombra
            card_container = tk.Frame(stats_frame, bg=self.COLORS['white'])
            card_container.grid(row=i//2, column=i%2, padx=15, pady=15, sticky="nsew")
            
            card = tk.Frame(card_container, bg=color, relief=tk.FLAT, bd=0)
            card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            # Ícone
            lbl_icon = tk.Label(
                card,
                text=icon,
                font=("Segoe UI", 40),
                bg=color,
                fg=self.COLORS['white']
            )
            lbl_icon.pack(pady=(25, 10))
            
            # Valor
            lbl_value = tk.Label(
                card,
                text=str(value),
                font=("Segoe UI", 42, "bold"),
                bg=color,
                fg=self.COLORS['white']
            )
            lbl_value.pack(pady=(0, 5))
            
            # Label
            lbl_text = tk.Label(
                card,
                text=label,
                font=("Segoe UI", 15),
                bg=color,
                fg=self.COLORS['white']
            )
            lbl_text.pack(pady=(0, 25))
        
        # Card de valor total de vendas (destaque)
        card_vendas_container = tk.Frame(stats_frame, bg=self.COLORS['white'])
        card_vendas_container.grid(row=2, column=0, columnspan=2, padx=15, pady=15, sticky="ew")
        
        card_vendas = tk.Frame(card_vendas_container, bg=self.COLORS['warning'], relief=tk.FLAT, bd=0)
        card_vendas.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        lbl_vendas_icon = tk.Label(
            card_vendas,
            text="💵",
            font=("Segoe UI", 45),
            bg=self.COLORS['warning'],
            fg=self.COLORS['white']
        )
        lbl_vendas_icon.pack(pady=(25, 10))
        
        lbl_vendas_valor = tk.Label(
            card_vendas,
            text=f"R$ {valor_total_vendas:,.2f}",
            font=("Segoe UI", 38, "bold"),
            bg=self.COLORS['warning'],
            fg=self.COLORS['white']
        )
        lbl_vendas_valor.pack(pady=(0, 5))
        
        lbl_vendas_text = tk.Label(
            card_vendas,
            text="Valor Total em Vendas",
            font=("Segoe UI", 16),
            bg=self.COLORS['warning'],
            fg=self.COLORS['white']
        )
        lbl_vendas_text.pack(pady=(0, 25))
        
        # Configurar grid
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_rowconfigure(0, weight=1)
        stats_frame.grid_rowconfigure(1, weight=1)
        stats_frame.grid_rowconfigure(2, weight=1)
    
    def _highlight_menu_button(self, index):
        """Destaca o botão do menu ativo"""
        for i, btn in enumerate(self.menu_buttons):
            if i == index:
                btn.config(bg=self.COLORS['primary'], fg=self.COLORS['darker'])
            else:
                btn.config(bg=self.COLORS['dark'], fg=self.COLORS['white'])
        
    def mostrar_produtos(self):
        """Mostra a tela de produtos"""
        self.limpar_conteudo()
        self._highlight_menu_button(2)
        ProdutosFrame(self.content_frame, self.data_manager, self.COLORS)
        
    def mostrar_categorias(self):
        """Mostra a tela de categorias"""
        self.limpar_conteudo()
        self._highlight_menu_button(1)
        CategoriasFrame(self.content_frame, self.data_manager, self.COLORS)
        
    def mostrar_clientes(self):
        """Mostra a tela de clientes"""
        self.limpar_conteudo()
        self._highlight_menu_button(4)
        ClientesFrame(self.content_frame, self.data_manager, self.COLORS)
        
    def mostrar_vendas(self):
        """Mostra a tela de vendas"""
        self.limpar_conteudo()
        self._highlight_menu_button(5)
        VendasFrame(self.content_frame, self.data_manager, self.COLORS)
        
    def mostrar_entrada_estoque(self):
        """Mostra a tela de entrada de estoque"""
        self.limpar_conteudo()
        self._highlight_menu_button(3)
        EntradaEstoqueFrame(self.content_frame, self.data_manager, self.COLORS)
    
    def run(self):
        """Inicia o aplicativo"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SistemaWA()
    app.run()
