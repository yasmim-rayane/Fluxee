# Sistema WA - Versão com SQLite

## 🎉 ATUALIZAÇÃO IMPORTANTE

O sistema foi completamente atualizado para usar **SQLite** como banco de dados local, substituindo o armazenamento em memória.

---

## 📦 Nova Estrutura do Banco de Dados

### Tabelas Implementadas:

#### 1. **categorias**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- nome (TEXT, UNIQUE, NOT NULL)
```

#### 2. **produtos**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- nome (TEXT, NOT NULL)
- categoria_id (INTEGER, NOT NULL, FOREIGN KEY → categorias.id)
- valor_unitario (REAL, NOT NULL)
- quantidade_estoque (INTEGER, NOT NULL, DEFAULT 0)
- ON DELETE CASCADE (categoria)
```

#### 3. **clientes**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- nome (TEXT, NOT NULL)
- data_nascimento (TEXT, NOT NULL)
- cpf (TEXT, UNIQUE, NOT NULL)
- genero (TEXT, NOT NULL)
```

#### 4. **vendas**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- codigo (TEXT, UNIQUE, NOT NULL)
- data_hora (TEXT, NOT NULL)
- cliente_id (INTEGER, FOREIGN KEY → clientes.id)
- valor_total (REAL, NOT NULL)
- forma_pagamento (TEXT, NOT NULL)
- ON DELETE SET NULL (cliente)
```

#### 5. **itens_venda**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- venda_id (INTEGER, NOT NULL, FOREIGN KEY → vendas.id)
- produto_id (INTEGER, NOT NULL, FOREIGN KEY → produtos.id)
- quantidade (INTEGER, NOT NULL)
- valor_unitario (REAL, NOT NULL)
- ON DELETE CASCADE (venda)
```

#### 6. **entradas_estoque**
```sql
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- produto_id (INTEGER, NOT NULL, FOREIGN KEY → produtos.id)
- quantidade (INTEGER, NOT NULL)
- data_hora (TEXT, NOT NULL)
- ON DELETE CASCADE (produto)
```

---

## 🆕 Novos Arquivos

### **database.py** (NOVO)
Módulo completo de gerenciamento do banco de dados SQLite com:
- Criação automática das tabelas
- Funções CRUD para todas as entidades
- Tratamento de integridade referencial
- Dados de exemplo iniciais
- Controle de transações

### **data_manager.py** (ATUALIZADO)
Agora atua como uma camada de abstração que:
- Mantém compatibilidade com a interface antiga
- Delega todas as operações para o database.py
- Garante que as telas não precisem ser modificadas

### **main.py** (ATUALIZADO)
Pequenas alterações:
- Removida a criação manual de dados de exemplo
- Dashboard atualizado para usar listas ao invés de dicionários

---

## ✨ Funcionalidades Implementadas

### ✅ Persistência de Dados
- **Todos os dados são salvos permanentemente** no arquivo `sistema_wa.db`
- Os dados **não são mais perdidos** ao fechar o aplicativo
- Banco de dados local SQLite3 (sem necessidade de servidor)

### ✅ Integridade Referencial
- **CASCADE DELETE**: Ao excluir categoria, produtos são excluídos automaticamente
- **SET NULL**: Ao excluir cliente, vendas são mantidas (cliente_id = NULL)
- **Validação de Foreign Keys** ativada

### ✅ Controle de Duplicação
- **CPF único**: Não permite cadastrar clientes com CPF duplicado
- **Código de venda único**: Sistema gera códigos únicos automaticamente
- **Nome de categoria único**: Não permite categorias com mesmo nome

### ✅ Transações Seguras
- Operações complexas (vendas) usam transações
- Rollback automático em caso de erro
- Garantia de consistência dos dados

---

## 🔧 Regras de Negócio Implementadas

### 1. Categorias e Produtos
- ✅ Produto só pode ser cadastrado com categoria válida
- ✅ Ao excluir categoria, **todos os produtos** são excluídos (CASCADE)
- ✅ Entradas de estoque de produtos excluídos também são removidas

### 2. Estoque
- ✅ Estoque diminui automaticamente ao criar venda
- ✅ Estoque aumenta automaticamente ao registrar entrada
- ✅ Estoque é restaurado ao excluir venda
- ✅ Estoque é ajustado ao editar venda

### 3. Vendas e Clientes
- ✅ Ao excluir cliente, vendas são **mantidas** (SET NULL)
- ✅ Nome do cliente aparece como "Cliente Excluído" nas vendas
- ✅ Código de venda é gerado automaticamente (VND00001, VND00002...)
- ✅ Itens de venda são excluídos automaticamente (CASCADE)

### 4. Validações
- ✅ CPF não pode ser duplicado
- ✅ Categoria não pode ter nome duplicado
- ✅ Foreign Keys são validadas antes de inserir

---

## 📁 Estrutura de Arquivos

```
claude/
│
├── sistema_wa.db              # NOVO - Banco de dados SQLite
├── database.py                # NOVO - Módulo de BD
├── data_manager.py            # ATUALIZADO - Camada de abstração
├── main.py                    # ATUALIZADO - App principal
├── categorias_ui.py           # Sem alterações
├── produtos_ui.py             # Sem alterações
├── clientes_ui.py             # Sem alterações
├── vendas_ui.py               # Sem alterações
├── entrada_estoque_ui.py      # Sem alterações
├── README.md
├── GUIA_USUARIO.md
├── REQUIREMENTS.txt
├── RESUMO_PROJETO.md
└── iniciar.bat
```

---

## 🚀 Como Usar

### Primeira Execução
```bash
python main.py
```

O sistema irá:
1. Criar o arquivo `sistema_wa.db` automaticamente
2. Criar todas as tabelas
3. Inserir dados de exemplo iniciais
4. Abrir a interface gráfica

### Execuções Seguintes
```bash
python main.py
```

O sistema irá:
1. Conectar ao banco de dados existente
2. Carregar todos os dados salvos
3. Continuar de onde você parou

---

## 💾 Gerenciamento do Banco de Dados

### Localização
- O arquivo `sistema_wa.db` fica na mesma pasta do aplicativo

### Backup
Para fazer backup dos dados:
```bash
# Copie o arquivo do banco de dados
copy sistema_wa.db sistema_wa_backup.db
```

### Resetar Dados
Para começar do zero:
```bash
# Delete o arquivo do banco de dados
del sistema_wa.db

# Execute o sistema novamente
python main.py
```

### Visualizar Dados
Você pode abrir o banco com ferramentas como:
- **DB Browser for SQLite** (recomendado)
- **SQLite Studio**
- **DBeaver**
- Linha de comando: `sqlite3 sistema_wa.db`

---

## 🔍 Consultas SQL Úteis

### Ver todas as vendas
```sql
SELECT v.*, c.nome as cliente_nome
FROM vendas v
LEFT JOIN clientes c ON v.cliente_id = c.id;
```

### Ver produtos com baixo estoque
```sql
SELECT nome, quantidade_estoque
FROM produtos
WHERE quantidade_estoque < 10
ORDER BY quantidade_estoque;
```

### Ver produtos por categoria
```sql
SELECT c.nome as categoria, p.nome as produto, p.quantidade_estoque
FROM produtos p
JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nome, p.nome;
```

### Ver histórico de vendas de um cliente
```sql
SELECT v.codigo, v.data_hora, v.valor_total, v.forma_pagamento
FROM vendas v
WHERE v.cliente_id = 1
ORDER BY v.data_hora DESC;
```

---

## ⚙️ Configurações Técnicas

### PRAGMA foreign_keys
```sql
PRAGMA foreign_keys = ON;
```
- Ativado automaticamente ao conectar
- Garante integridade referencial

### Transações
- Todas as operações complexas usam transações
- Commit automático em operações simples
- Rollback em caso de erro

### IDs Automáticos
- Todas as tabelas usam AUTOINCREMENT
- IDs nunca são reutilizados
- Geração automática pelo SQLite

---

## 🎯 Melhorias Implementadas

### Antes (Em Memória)
- ❌ Dados perdidos ao fechar
- ❌ Sem backup
- ❌ Sem histórico persistente
- ❌ Reinicialização manual

### Agora (SQLite)
- ✅ Dados persistentes
- ✅ Backup simples (copiar arquivo)
- ✅ Histórico completo
- ✅ Continuidade automática
- ✅ Integridade referencial
- ✅ Transações seguras
- ✅ Consultas SQL disponíveis

---

## 🛠️ Funções do database.py

### Categorias
- `criar_categoria(nome)`
- `editar_categoria(id, novo_nome)`
- `excluir_categoria(id)`
- `listar_categorias()`
- `buscar_categoria(id)`

### Produtos
- `criar_produto(nome, categoria_id, valor, quantidade)`
- `editar_produto(id, nome, categoria_id, valor)`
- `excluir_produto(id)`
- `listar_produtos()`
- `buscar_produto(id)`
- `atualizar_estoque(id, quantidade)`

### Clientes
- `criar_cliente(nome, data_nasc, cpf, genero)`
- `editar_cliente(id, nome, data_nasc, cpf, genero)`
- `excluir_cliente(id)`
- `listar_clientes()`
- `buscar_cliente(id)`

### Vendas
- `criar_venda(cliente_id, produtos, forma_pagamento)`
- `editar_venda(id, cliente_id, produtos, forma_pagamento)`
- `excluir_venda(id)`
- `listar_vendas()`
- `buscar_venda(id)`

### Entrada de Estoque
- `criar_entrada_estoque(produto_id, quantidade)`
- `listar_entradas_estoque()`

---

## 📊 Dados de Exemplo

O sistema cria automaticamente na primeira execução:

**Categorias (3)**:
- Eletrônicos
- Alimentos
- Vestuário

**Produtos (4)**:
- Notebook Dell (Eletrônicos) - R$ 3.500,00 - Estoque: 10
- Mouse Logitech (Eletrônicos) - R$ 89,90 - Estoque: 50
- Arroz 5kg (Alimentos) - R$ 25,90 - Estoque: 100
- Camiseta Polo (Vestuário) - R$ 79,90 - Estoque: 30

**Clientes (2)**:
- João Silva - CPF: 123.456.789-00
- Maria Santos - CPF: 987.654.321-00

---

## ✅ Checklist de Implementação

### Requisitos Atendidos
- [x] Banco de dados SQLite com todas as tabelas
- [x] Campos corretos em cada tabela
- [x] Primary Keys e Foreign Keys
- [x] Constraints (UNIQUE, NOT NULL)
- [x] ON DELETE CASCADE para categorias→produtos
- [x] ON DELETE SET NULL para clientes→vendas
- [x] Arquivo database.py separado
- [x] Funções CRUD completas
- [x] Interface Tkinter funcional
- [x] Sem uso de ORM (apenas sqlite3)
- [x] Validação de duplicação (CPF, código de venda)
- [x] Atualização automática de estoque
- [x] Transações seguras

### Funcionalidades Extras
- [x] Dados de exemplo automáticos
- [x] Tratamento de erros robusto
- [x] Rollback em transações
- [x] Documentação completa
- [x] Compatibilidade com interface antiga

---

## 🎓 Tecnologias

- **Python 3.7+**
- **sqlite3** (biblioteca padrão)
- **Tkinter** (interface gráfica)
- **SQL** (consultas e estrutura)

---

## 📝 Notas Importantes

1. **Backup Regular**: Faça backup do arquivo `sistema_wa.db` regularmente
2. **Não Edite Manualmente**: Evite editar o banco diretamente, use a interface
3. **Performance**: SQLite é eficiente para milhares de registros
4. **Portabilidade**: O arquivo .db pode ser copiado para outro computador
5. **Versionamento**: Adicione `*.db` ao `.gitignore` se usar Git

---

**Sistema desenvolvido para a Empresa WA**  
**Versão: 2.0 (Com SQLite)**  
**Data: Outubro 2025**  
**Tecnologia: Python + Tkinter + SQLite**
