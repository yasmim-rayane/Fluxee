"""
Módulo de gerenciamento do banco de dados SQLite
Contém todas as operações CRUD e estrutura do banco
"""

import sqlite3
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import os


class Database:
    """Classe para gerenciar o banco de dados SQLite"""
    
    def __init__(self, db_name: str = "sistema_wa.db"):
        """Inicializa a conexão com o banco de dados"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._conectar()
        self._criar_tabelas()
        self._inserir_dados_exemplo()
    
    def _conectar(self):
        """Estabelece conexão com o banco de dados"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        # Habilitar foreign keys
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()
    
    def _criar_tabelas(self):
        """Cria todas as tabelas do banco de dados"""
        
        # Tabela de categorias
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL
            )
        """)
        
        # Tabela de produtos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria_id INTEGER NOT NULL,
                valor_unitario REAL NOT NULL,
                quantidade_estoque INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
            )
        """)
        
        # Tabela de clientes
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                genero TEXT NOT NULL
            )
        """)
        
        # Tabela de vendas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE NOT NULL,
                data_hora TEXT NOT NULL,
                cliente_id INTEGER,
                valor_total REAL NOT NULL,
                forma_pagamento TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE SET NULL
            )
        """)
        
        # Tabela de itens_venda
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venda_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                valor_unitario REAL NOT NULL,
                FOREIGN KEY (venda_id) REFERENCES vendas(id) ON DELETE CASCADE,
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """)
        
        # Tabela de entradas_estoque
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entradas_estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data_hora TEXT NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE CASCADE
            )
        """)
        
        self.conn.commit()
    
    def _inserir_dados_exemplo(self):
        """Método para inserir dados de exemplo (atualmente desabilitado)"""
        # Sistema inicia sem dados de exemplo
        # Para adicionar dados de exemplo, descomente o código abaixo:
        
        # Verificar se já existem dados
        # self.cursor.execute("SELECT COUNT(*) FROM categorias")
        # if self.cursor.fetchone()[0] == 0:
        #     # Inserir categorias
        #     categorias = ["Eletrônicos", "Alimentos", "Vestuário"]
        #     for cat in categorias:
        #         self.cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (cat,))
        #     
        #     # Inserir produtos
        #     produtos = [
        #         ("Notebook Dell", 1, 3500.00, 10),
        #         ("Mouse Logitech", 1, 89.90, 50),
        #         ("Arroz 5kg", 2, 25.90, 100),
        #         ("Camiseta Polo", 3, 79.90, 30)
        #     ]
        #     for prod in produtos:
        #         self.cursor.execute(
        #             "INSERT INTO produtos (nome, categoria_id, valor_unitario, quantidade_estoque) VALUES (?, ?, ?, ?)",
        #             prod
        #         )
        #     
        #     # Inserir clientes
        #     clientes = [
        #         ("João Silva", "15/03/1990", "123.456.789-00", "Masculino"),
        #         ("Maria Santos", "22/07/1985", "987.654.321-00", "Feminino")
        #     ]
        #     for cliente in clientes:
        #         self.cursor.execute(
        #             "INSERT INTO clientes (nome, data_nascimento, cpf, genero) VALUES (?, ?, ?, ?)",
        #             cliente
        #         )
        #     
        #     self.conn.commit()
        pass
    
    # ==================== CATEGORIAS ====================
    
    def criar_categoria(self, nome: str) -> Optional[int]:
        """Cria uma nova categoria"""
        try:
            self.cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # Categoria duplicada
    
    def editar_categoria(self, categoria_id: int, novo_nome: str) -> bool:
        """Edita o nome de uma categoria"""
        try:
            self.cursor.execute(
                "UPDATE categorias SET nome = ? WHERE id = ?",
                (novo_nome, categoria_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def excluir_categoria(self, categoria_id: int) -> bool:
        """Exclui uma categoria (CASCADE exclui produtos automaticamente)"""
        self.cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def listar_categorias(self) -> List[Dict]:
        """Retorna lista de todas as categorias"""
        self.cursor.execute("SELECT id, nome FROM categorias ORDER BY nome")
        rows = self.cursor.fetchall()
        return [{"id": row[0], "nome": row[1]} for row in rows]
    
    def buscar_categoria(self, categoria_id: int) -> Optional[Dict]:
        """Busca uma categoria por ID"""
        self.cursor.execute("SELECT id, nome FROM categorias WHERE id = ?", (categoria_id,))
        row = self.cursor.fetchone()
        return {"id": row[0], "nome": row[1]} if row else None
    
    # ==================== PRODUTOS ====================
    
    def criar_produto(self, nome: str, categoria_id: int, valor_unitario: float,
                      quantidade_inicial: int) -> Optional[int]:
        """Cria um novo produto"""
        try:
            self.cursor.execute(
                """INSERT INTO produtos (nome, categoria_id, valor_unitario, quantidade_estoque)
                   VALUES (?, ?, ?, ?)""",
                (nome, categoria_id, valor_unitario, quantidade_inicial)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
    
    def editar_produto(self, produto_id: int, nome: str, categoria_id: int,
                       valor_unitario: float) -> bool:
        """Edita um produto existente"""
        try:
            self.cursor.execute(
                """UPDATE produtos SET nome = ?, categoria_id = ?, valor_unitario = ?
                   WHERE id = ?""",
                (nome, categoria_id, valor_unitario, produto_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def excluir_produto(self, produto_id: int) -> bool:
        """Exclui um produto"""
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def listar_produtos(self) -> List[Dict]:
        """Retorna lista de todos os produtos com nome da categoria"""
        self.cursor.execute("""
            SELECT p.id, p.nome, p.categoria_id, p.valor_unitario, p.quantidade_estoque, c.nome
            FROM produtos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
            ORDER BY p.nome
        """)
        rows = self.cursor.fetchall()
        return [{
            "id": row[0],
            "nome": row[1],
            "categoria_id": row[2],
            "valor_unitario": row[3],
            "quantidade_estoque": row[4],
            "categoria_nome": row[5] or "N/A"
        } for row in rows]
    
    def buscar_produto(self, produto_id: int) -> Optional[Dict]:
        """Busca um produto por ID"""
        self.cursor.execute(
            """SELECT id, nome, categoria_id, valor_unitario, quantidade_estoque
               FROM produtos WHERE id = ?""",
            (produto_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "nome": row[1],
                "categoria_id": row[2],
                "valor_unitario": row[3],
                "quantidade_estoque": row[4]
            }
        return None
    
    def atualizar_estoque(self, produto_id: int, quantidade: int) -> bool:
        """Atualiza a quantidade em estoque (pode ser negativa para vendas)"""
        self.cursor.execute(
            """UPDATE produtos SET quantidade_estoque = quantidade_estoque + ?
               WHERE id = ?""",
            (quantidade, produto_id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    # ==================== CLIENTES ====================
    
    def criar_cliente(self, nome: str, data_nascimento: str, cpf: str,
                      genero: str) -> Optional[int]:
        """Cria um novo cliente"""
        try:
            self.cursor.execute(
                """INSERT INTO clientes (nome, data_nascimento, cpf, genero)
                   VALUES (?, ?, ?, ?)""",
                (nome, data_nascimento, cpf, genero)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # CPF duplicado
    
    def editar_cliente(self, cliente_id: int, nome: str, data_nascimento: str,
                       cpf: str, genero: str) -> bool:
        """Edita um cliente existente"""
        try:
            self.cursor.execute(
                """UPDATE clientes SET nome = ?, data_nascimento = ?, cpf = ?, genero = ?
                   WHERE id = ?""",
                (nome, data_nascimento, cpf, genero, cliente_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def excluir_cliente(self, cliente_id: int) -> bool:
        """Exclui um cliente (vendas são mantidas com SET NULL)"""
        self.cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def listar_clientes(self) -> List[Dict]:
        """Retorna lista de todos os clientes"""
        self.cursor.execute(
            "SELECT id, nome, data_nascimento, cpf, genero FROM clientes ORDER BY nome"
        )
        rows = self.cursor.fetchall()
        return [{
            "id": row[0],
            "nome": row[1],
            "data_nascimento": row[2],
            "cpf": row[3],
            "genero": row[4]
        } for row in rows]
    
    def buscar_cliente(self, cliente_id: int) -> Optional[Dict]:
        """Busca um cliente por ID"""
        self.cursor.execute(
            "SELECT id, nome, data_nascimento, cpf, genero FROM clientes WHERE id = ?",
            (cliente_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "nome": row[1],
                "data_nascimento": row[2],
                "cpf": row[3],
                "genero": row[4]
            }
        return None
    
    # ==================== VENDAS ====================
    
    def criar_venda(self, cliente_id: int, produtos_vendidos: List[Dict],
                    forma_pagamento: str) -> Optional[int]:
        """Cria uma nova venda e atualiza o estoque"""
        try:
            # Gerar código único
            self.cursor.execute("SELECT MAX(id) FROM vendas")
            max_id = self.cursor.fetchone()[0] or 0
            codigo = f"VND{max_id + 1:05d}"
            
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Calcular valor total
            valor_total = sum(item['quantidade'] * item['valor_unitario'] 
                            for item in produtos_vendidos)
            
            # Inserir venda
            self.cursor.execute(
                """INSERT INTO vendas (codigo, data_hora, cliente_id, valor_total, forma_pagamento)
                   VALUES (?, ?, ?, ?, ?)""",
                (codigo, data_hora, cliente_id, valor_total, forma_pagamento)
            )
            venda_id = self.cursor.lastrowid
            
            # Inserir itens da venda
            for item in produtos_vendidos:
                self.cursor.execute(
                    """INSERT INTO itens_venda (venda_id, produto_id, quantidade, valor_unitario)
                       VALUES (?, ?, ?, ?)""",
                    (venda_id, item['produto_id'], item['quantidade'], item['valor_unitario'])
                )
                
                # Atualizar estoque
                self.atualizar_estoque(item['produto_id'], -item['quantidade'])
            
            self.conn.commit()
            return venda_id
        except sqlite3.IntegrityError:
            self.conn.rollback()
            return None
    
    def editar_venda(self, venda_id: int, cliente_id: int,
                     produtos_vendidos: List[Dict], forma_pagamento: str) -> bool:
        """Edita uma venda existente e ajusta o estoque"""
        try:
            # Buscar itens antigos para devolver ao estoque
            self.cursor.execute(
                "SELECT produto_id, quantidade FROM itens_venda WHERE venda_id = ?",
                (venda_id,)
            )
            itens_antigos = self.cursor.fetchall()
            
            # Devolver produtos ao estoque
            for produto_id, quantidade in itens_antigos:
                self.atualizar_estoque(produto_id, quantidade)
            
            # Excluir itens antigos
            self.cursor.execute("DELETE FROM itens_venda WHERE venda_id = ?", (venda_id,))
            
            # Calcular novo valor total
            valor_total = sum(item['quantidade'] * item['valor_unitario']
                            for item in produtos_vendidos)
            
            # Atualizar venda
            self.cursor.execute(
                """UPDATE vendas SET cliente_id = ?, valor_total = ?, forma_pagamento = ?
                   WHERE id = ?""",
                (cliente_id, valor_total, forma_pagamento, venda_id)
            )
            
            # Inserir novos itens
            for item in produtos_vendidos:
                self.cursor.execute(
                    """INSERT INTO itens_venda (venda_id, produto_id, quantidade, valor_unitario)
                       VALUES (?, ?, ?, ?)""",
                    (venda_id, item['produto_id'], item['quantidade'], item['valor_unitario'])
                )
                
                # Retirar do estoque
                self.atualizar_estoque(item['produto_id'], -item['quantidade'])
            
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            self.conn.rollback()
            return False
    
    def excluir_venda(self, venda_id: int) -> bool:
        """Exclui uma venda e devolve os produtos ao estoque"""
        try:
            # Buscar itens para devolver ao estoque
            self.cursor.execute(
                "SELECT produto_id, quantidade FROM itens_venda WHERE venda_id = ?",
                (venda_id,)
            )
            itens = self.cursor.fetchall()
            
            # Devolver produtos ao estoque
            for produto_id, quantidade in itens:
                self.atualizar_estoque(produto_id, quantidade)
            
            # Excluir venda (CASCADE exclui itens automaticamente)
            self.cursor.execute("DELETE FROM vendas WHERE id = ?", (venda_id,))
            
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception:
            self.conn.rollback()
            return False
    
    def listar_vendas(self) -> List[Dict]:
        """Retorna lista de todas as vendas com nome do cliente"""
        self.cursor.execute("""
            SELECT v.id, v.codigo, v.data_hora, v.cliente_id, v.valor_total, v.forma_pagamento, c.nome
            FROM vendas v
            LEFT JOIN clientes c ON v.cliente_id = c.id
            ORDER BY v.id DESC
        """)
        rows = self.cursor.fetchall()
        
        vendas = []
        for row in rows:
            venda = {
                "id": row[0],
                "codigo": row[1],
                "data_hora": row[2],
                "cliente_id": row[3],
                "valor_total": row[4],
                "forma_pagamento": row[5],
                "cliente_nome": row[6] or "Cliente Excluído"
            }
            
            # Buscar produtos da venda
            self.cursor.execute(
                """SELECT p.nome, iv.quantidade, iv.valor_unitario
                   FROM itens_venda iv
                   LEFT JOIN produtos p ON iv.produto_id = p.id
                   WHERE iv.venda_id = ?""",
                (row[0],)
            )
            itens = self.cursor.fetchall()
            venda['produtos'] = [{
                'produto_id': None,
                'nome': item[0] or "Produto Excluído",
                'quantidade': item[1],
                'valor_unitario': item[2]
            } for item in itens]
            
            vendas.append(venda)
        
        return vendas
    
    def buscar_venda(self, venda_id: int) -> Optional[Dict]:
        """Busca uma venda por ID"""
        self.cursor.execute(
            """SELECT id, codigo, data_hora, cliente_id, valor_total, forma_pagamento
               FROM vendas WHERE id = ?""",
            (venda_id,)
        )
        row = self.cursor.fetchone()
        if row:
            venda = {
                "id": row[0],
                "codigo": row[1],
                "data_hora": row[2],
                "cliente_id": row[3],
                "valor_total": row[4],
                "forma_pagamento": row[5]
            }
            
            # Buscar produtos
            self.cursor.execute(
                """SELECT produto_id, quantidade, valor_unitario
                   FROM itens_venda WHERE venda_id = ?""",
                (venda_id,)
            )
            venda['produtos'] = [{
                'produto_id': item[0],
                'quantidade': item[1],
                'valor_unitario': item[2]
            } for item in self.cursor.fetchall()]
            
            return venda
        return None
    
    # ==================== ENTRADA DE ESTOQUE ====================
    
    def criar_entrada_estoque(self, produto_id: int, quantidade: int) -> Optional[int]:
        """Registra uma entrada de estoque"""
        try:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            self.cursor.execute(
                """INSERT INTO entradas_estoque (produto_id, quantidade, data_hora)
                   VALUES (?, ?, ?)""",
                (produto_id, quantidade, data_hora)
            )
            entrada_id = self.cursor.lastrowid
            
            # Atualizar estoque do produto
            self.atualizar_estoque(produto_id, quantidade)
            
            self.conn.commit()
            return entrada_id
        except sqlite3.IntegrityError:
            self.conn.rollback()
            return None
    
    def listar_entradas_estoque(self) -> List[Dict]:
        """Retorna lista de todas as entradas de estoque"""
        self.cursor.execute("""
            SELECT e.id, e.produto_id, e.quantidade, e.data_hora, p.nome
            FROM entradas_estoque e
            LEFT JOIN produtos p ON e.produto_id = p.id
            ORDER BY e.id DESC
        """)
        rows = self.cursor.fetchall()
        return [{
            "id": row[0],
            "produto_id": row[1],
            "quantidade": row[2],
            "data_hora": row[3],
            "produto_nome": row[4] or "Produto Excluído"
        } for row in rows]
    
    # ==================== UTILIDADES ====================
    
    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
    
    def __del__(self):
        """Fecha a conexão ao destruir o objeto"""
        self.fechar_conexao()
