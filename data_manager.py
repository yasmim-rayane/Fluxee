"""
Módulo de gerenciamento de dados em memória
Mantém todas as estruturas de dados do sistema
"""

from datetime import datetime
from typing import Dict, List, Optional


class DataManager:
    """Classe principal para gerenciar todos os dados do sistema"""
    
    def __init__(self):
        # Estruturas de dados em memória
        self.categorias: Dict[int, Dict] = {}
        self.produtos: Dict[int, Dict] = {}
        self.clientes: Dict[int, Dict] = {}
        self.vendas: Dict[int, Dict] = {}
        self.entradas_estoque: List[Dict] = []
        
        # Contadores para IDs
        self.next_categoria_id = 1
        self.next_produto_id = 1
        self.next_cliente_id = 1
        self.next_venda_id = 1
        self.next_entrada_id = 1
        
    # ==================== CATEGORIAS ====================
    
    def criar_categoria(self, nome: str) -> int:
        """Cria uma nova categoria"""
        categoria_id = self.next_categoria_id
        self.categorias[categoria_id] = {
            'id': categoria_id,
            'nome': nome
        }
        self.next_categoria_id += 1
        return categoria_id
    
    def editar_categoria(self, categoria_id: int, novo_nome: str) -> bool:
        """Edita o nome de uma categoria"""
        if categoria_id in self.categorias:
            self.categorias[categoria_id]['nome'] = novo_nome
            return True
        return False
    
    def excluir_categoria(self, categoria_id: int) -> bool:
        """Exclui uma categoria e todos os produtos relacionados"""
        if categoria_id in self.categorias:
            # Excluir todos os produtos desta categoria
            produtos_para_excluir = [
                pid for pid, prod in self.produtos.items() 
                if prod['categoria_id'] == categoria_id
            ]
            for pid in produtos_para_excluir:
                del self.produtos[pid]
            
            # Excluir a categoria
            del self.categorias[categoria_id]
            return True
        return False
    
    def listar_categorias(self) -> List[Dict]:
        """Retorna lista de todas as categorias"""
        return list(self.categorias.values())
    
    def buscar_categoria(self, categoria_id: int) -> Optional[Dict]:
        """Busca uma categoria por ID"""
        return self.categorias.get(categoria_id)
    
    # ==================== PRODUTOS ====================
    
    def criar_produto(self, nome: str, categoria_id: int, valor_unitario: float, 
                      quantidade_inicial: int) -> Optional[int]:
        """Cria um novo produto (requer categoria válida)"""
        if categoria_id not in self.categorias:
            return None  # Categoria inválida
        
        produto_id = self.next_produto_id
        self.produtos[produto_id] = {
            'id': produto_id,
            'nome': nome,
            'categoria_id': categoria_id,
            'valor_unitario': valor_unitario,
            'quantidade_estoque': quantidade_inicial
        }
        self.next_produto_id += 1
        return produto_id
    
    def editar_produto(self, produto_id: int, nome: str, categoria_id: int, 
                       valor_unitario: float) -> bool:
        """Edita um produto existente"""
        if produto_id not in self.produtos or categoria_id not in self.categorias:
            return False
        
        self.produtos[produto_id].update({
            'nome': nome,
            'categoria_id': categoria_id,
            'valor_unitario': valor_unitario
        })
        return True
    
    def excluir_produto(self, produto_id: int) -> bool:
        """Exclui um produto"""
        if produto_id in self.produtos:
            del self.produtos[produto_id]
            return True
        return False
    
    def listar_produtos(self) -> List[Dict]:
        """Retorna lista de todos os produtos com nome da categoria"""
        produtos_lista = []
        for prod in self.produtos.values():
            prod_info = prod.copy()
            categoria = self.categorias.get(prod['categoria_id'])
            prod_info['categoria_nome'] = categoria['nome'] if categoria else 'N/A'
            produtos_lista.append(prod_info)
        return produtos_lista
    
    def buscar_produto(self, produto_id: int) -> Optional[Dict]:
        """Busca um produto por ID"""
        return self.produtos.get(produto_id)
    
    def atualizar_estoque(self, produto_id: int, quantidade: int) -> bool:
        """Atualiza a quantidade em estoque (pode ser negativa para vendas)"""
        if produto_id in self.produtos:
            self.produtos[produto_id]['quantidade_estoque'] += quantidade
            return True
        return False
    
    # ==================== CLIENTES ====================
    
    def criar_cliente(self, nome: str, data_nascimento: str, cpf: str, 
                      genero: str) -> int:
        """Cria um novo cliente"""
        cliente_id = self.next_cliente_id
        self.clientes[cliente_id] = {
            'id': cliente_id,
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'genero': genero
        }
        self.next_cliente_id += 1
        return cliente_id
    
    def editar_cliente(self, cliente_id: int, nome: str, data_nascimento: str, 
                       cpf: str, genero: str) -> bool:
        """Edita um cliente existente"""
        if cliente_id in self.clientes:
            self.clientes[cliente_id].update({
                'nome': nome,
                'data_nascimento': data_nascimento,
                'cpf': cpf,
                'genero': genero
            })
            return True
        return False
    
    def excluir_cliente(self, cliente_id: int) -> bool:
        """Exclui um cliente (mantém as vendas)"""
        if cliente_id in self.clientes:
            del self.clientes[cliente_id]
            return True
        return False
    
    def listar_clientes(self) -> List[Dict]:
        """Retorna lista de todos os clientes"""
        return list(self.clientes.values())
    
    def buscar_cliente(self, cliente_id: int) -> Optional[Dict]:
        """Busca um cliente por ID"""
        return self.clientes.get(cliente_id)
    
    # ==================== VENDAS ====================
    
    def criar_venda(self, cliente_id: int, produtos_vendidos: List[Dict], 
                    forma_pagamento: str) -> int:
        """
        Cria uma nova venda e atualiza o estoque
        produtos_vendidos: [{'produto_id': int, 'quantidade': int, 'valor_unitario': float}]
        """
        venda_id = self.next_venda_id
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Calcular valor total
        valor_total = sum(
            item['quantidade'] * item['valor_unitario'] 
            for item in produtos_vendidos
        )
        
        # Criar venda
        self.vendas[venda_id] = {
            'id': venda_id,
            'codigo': f"VND{venda_id:05d}",
            'data_hora': data_hora,
            'cliente_id': cliente_id,
            'produtos': produtos_vendidos,
            'valor_total': valor_total,
            'forma_pagamento': forma_pagamento
        }
        
        # Atualizar estoque
        for item in produtos_vendidos:
            self.atualizar_estoque(item['produto_id'], -item['quantidade'])
        
        self.next_venda_id += 1
        return venda_id
    
    def editar_venda(self, venda_id: int, cliente_id: int, 
                     produtos_vendidos: List[Dict], forma_pagamento: str) -> bool:
        """Edita uma venda existente e ajusta o estoque"""
        if venda_id not in self.vendas:
            return False
        
        venda_antiga = self.vendas[venda_id]
        
        # Devolver produtos ao estoque (cancelar venda antiga)
        for item in venda_antiga['produtos']:
            self.atualizar_estoque(item['produto_id'], item['quantidade'])
        
        # Calcular novo valor total
        valor_total = sum(
            item['quantidade'] * item['valor_unitario'] 
            for item in produtos_vendidos
        )
        
        # Atualizar venda
        self.vendas[venda_id].update({
            'cliente_id': cliente_id,
            'produtos': produtos_vendidos,
            'valor_total': valor_total,
            'forma_pagamento': forma_pagamento
        })
        
        # Retirar produtos do estoque (nova venda)
        for item in produtos_vendidos:
            self.atualizar_estoque(item['produto_id'], -item['quantidade'])
        
        return True
    
    def excluir_venda(self, venda_id: int) -> bool:
        """Exclui uma venda e devolve os produtos ao estoque"""
        if venda_id not in self.vendas:
            return False
        
        venda = self.vendas[venda_id]
        
        # Devolver produtos ao estoque
        for item in venda['produtos']:
            self.atualizar_estoque(item['produto_id'], item['quantidade'])
        
        del self.vendas[venda_id]
        return True
    
    def listar_vendas(self) -> List[Dict]:
        """Retorna lista de todas as vendas com nome do cliente"""
        vendas_lista = []
        for venda in self.vendas.values():
            venda_info = venda.copy()
            cliente = self.clientes.get(venda['cliente_id'])
            venda_info['cliente_nome'] = cliente['nome'] if cliente else 'Cliente Excluído'
            vendas_lista.append(venda_info)
        return vendas_lista
    
    def buscar_venda(self, venda_id: int) -> Optional[Dict]:
        """Busca uma venda por ID"""
        return self.vendas.get(venda_id)
    
    # ==================== ENTRADA DE ESTOQUE ====================
    
    def criar_entrada_estoque(self, produto_id: int, quantidade: int) -> Optional[int]:
        """Registra uma entrada de estoque"""
        if produto_id not in self.produtos:
            return None
        
        entrada_id = self.next_entrada_id
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        entrada = {
            'id': entrada_id,
            'produto_id': produto_id,
            'quantidade': quantidade,
            'data_hora': data_hora
        }
        
        self.entradas_estoque.append(entrada)
        
        # Atualizar estoque do produto
        self.atualizar_estoque(produto_id, quantidade)
        
        self.next_entrada_id += 1
        return entrada_id
    
    def listar_entradas_estoque(self) -> List[Dict]:
        """Retorna lista de todas as entradas de estoque com nome do produto"""
        entradas_lista = []
        for entrada in self.entradas_estoque:
            entrada_info = entrada.copy()
            produto = self.produtos.get(entrada['produto_id'])
            entrada_info['produto_nome'] = produto['nome'] if produto else 'Produto Excluído'
            entradas_lista.append(entrada_info)
        return entradas_lista
