"""
Módulo de gerenciamento de dados usando SQLite
Mantém compatibilidade com a interface antiga
"""

from typing import Dict, List, Optional
from database.database import Database


class DataManager:
    """Classe principal para gerenciar todos os dados do sistema usando SQLite"""
    
    def __init__(self):
        # Inicializar banco de dados
        self.db = Database()
        
    # ==================== CATEGORIAS ====================
    
    def criar_categoria(self, nome: str) -> int:
        """Cria uma nova categoria"""
        return self.db.criar_categoria(nome)
    
    def editar_categoria(self, categoria_id: int, novo_nome: str) -> bool:
        """Edita o nome de uma categoria"""
        return self.db.editar_categoria(categoria_id, novo_nome)
    
    def excluir_categoria(self, categoria_id: int) -> bool:
        """Exclui uma categoria e todos os produtos relacionados"""
        return self.db.excluir_categoria(categoria_id)
    
    def listar_categorias(self) -> List[Dict]:
        """Retorna lista de todas as categorias"""
        return self.db.listar_categorias()
    
    def buscar_categoria(self, categoria_id: int) -> Optional[Dict]:
        """Busca uma categoria por ID"""
        return self.db.buscar_categoria(categoria_id)
    
    # ==================== PRODUTOS ====================
    
    def criar_produto(self, nome: str, categoria_id: int, valor_unitario: float, 
                      quantidade_inicial: int) -> Optional[int]:
        """Cria um novo produto (requer categoria válida)"""
        return self.db.criar_produto(nome, categoria_id, valor_unitario, quantidade_inicial)
    
    def editar_produto(self, produto_id: int, nome: str, categoria_id: int, 
                       valor_unitario: float) -> bool:
        """Edita um produto existente"""
        return self.db.editar_produto(produto_id, nome, categoria_id, valor_unitario)
    
    def excluir_produto(self, produto_id: int) -> bool:
        """Exclui um produto"""
        return self.db.excluir_produto(produto_id)
    
    def listar_produtos(self) -> List[Dict]:
        """Retorna lista de todos os produtos com nome da categoria"""
        return self.db.listar_produtos()
    
    def buscar_produto(self, produto_id: int) -> Optional[Dict]:
        """Busca um produto por ID"""
        return self.db.buscar_produto(produto_id)
    
    def atualizar_estoque(self, produto_id: int, quantidade: int) -> bool:
        """Atualiza a quantidade em estoque (pode ser negativa para vendas)"""
        return self.db.atualizar_estoque(produto_id, quantidade)
    
    # ==================== CLIENTES ====================
    
    def criar_cliente(self, nome: str, data_nascimento: str, cpf: str, 
                      genero: str) -> int:
        """Cria um novo cliente"""
        return self.db.criar_cliente(nome, data_nascimento, cpf, genero)
    
    def editar_cliente(self, cliente_id: int, nome: str, data_nascimento: str, 
                       cpf: str, genero: str) -> bool:
        """Edita um cliente existente"""
        return self.db.editar_cliente(cliente_id, nome, data_nascimento, cpf, genero)
    
    def excluir_cliente(self, cliente_id: int) -> bool:
        """Exclui um cliente (mantém as vendas)"""
        return self.db.excluir_cliente(cliente_id)
    
    def listar_clientes(self) -> List[Dict]:
        """Retorna lista de todos os clientes"""
        return self.db.listar_clientes()
    
    def buscar_cliente(self, cliente_id: int) -> Optional[Dict]:
        """Busca um cliente por ID"""
        return self.db.buscar_cliente(cliente_id)
    
    # ==================== VENDAS ====================
    
    def criar_venda(self, cliente_id: int, produtos_vendidos: List[Dict], 
                    forma_pagamento: str) -> int:
        """
        Cria uma nova venda e atualiza o estoque
        produtos_vendidos: [{'produto_id': int, 'quantidade': int, 'valor_unitario': float}]
        """
        return self.db.criar_venda(cliente_id, produtos_vendidos, forma_pagamento)
    
    def editar_venda(self, venda_id: int, cliente_id: int, 
                     produtos_vendidos: List[Dict], forma_pagamento: str) -> bool:
        """Edita uma venda existente e ajusta o estoque"""
        return self.db.editar_venda(venda_id, cliente_id, produtos_vendidos, forma_pagamento)
    
    def excluir_venda(self, venda_id: int) -> bool:
        """Exclui uma venda e devolve os produtos ao estoque"""
        return self.db.excluir_venda(venda_id)
    
    def listar_vendas(self) -> List[Dict]:
        """Retorna lista de todas as vendas com nome do cliente"""
        return self.db.listar_vendas()
    
    def buscar_venda(self, venda_id: int) -> Optional[Dict]:
        """Busca uma venda por ID"""
        return self.db.buscar_venda(venda_id)
    
    # ==================== ENTRADA DE ESTOQUE ====================
    
    def criar_entrada_estoque(self, produto_id: int, quantidade: int) -> Optional[int]:
        """Registra uma entrada de estoque"""
        return self.db.criar_entrada_estoque(produto_id, quantidade)
    
    def listar_entradas_estoque(self) -> List[Dict]:
        """Retorna lista de todas as entradas de estoque com nome do produto"""
        return self.db.listar_entradas_estoque()

