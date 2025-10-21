# Sistema WA - Gerenciamento de Estoque e Vendas

Sistema completo de gerenciamento de estoque e vendas desenvolvido em Python com Tkinter.

## 📋 Funcionalidades

### 1. Dashboard
- Visualização de estatísticas em tempo real
- Total de produtos, categorias, clientes e vendas
- Valor total em vendas

### 2. Gerenciamento de Categorias
- ✅ Criar novas categorias
- ✅ Editar categorias existentes
- ✅ Excluir categorias (exclui produtos relacionados automaticamente)
- Interface simples e intuitiva

### 3. Gerenciamento de Produtos
- ✅ Cadastrar produtos com nome, categoria, valor e quantidade inicial
- ✅ Editar informações de produtos
- ✅ Excluir produtos
- ✅ Visualizar estoque atual
- ✅ **Validação**: Produto só pode ser cadastrado com categoria válida
- ✅ **Regra**: Ao excluir categoria, produtos relacionados são excluídos

### 4. Gerenciamento de Clientes
- ✅ Cadastrar clientes (Nome, CPF, Data de Nascimento, Gênero)
- ✅ Editar informações de clientes
- ✅ Excluir clientes
- ✅ Validação de CPF e data de nascimento
- ✅ **Regra**: Ao excluir cliente, vendas não são excluídas

### 5. Gerenciamento de Vendas
- ✅ Criar vendas com seleção de cliente e produtos
- ✅ Carrinho de compras interativo
- ✅ Cálculo automático de totais
- ✅ Múltiplas formas de pagamento
- ✅ Código único para cada venda (VND00001, VND00002, etc.)
- ✅ Data e hora automáticas
- ✅ Excluir vendas (devolve produtos ao estoque)
- ✅ **Regra**: Ao vender, quantidade em estoque diminui automaticamente
- ✅ Validação de estoque antes de finalizar venda

### 6. Entrada de Estoque
- ✅ Registrar entrada de produtos
- ✅ Cálculo automático do novo estoque
- ✅ Histórico de todas as entradas
- ✅ Data e hora automáticas
- ✅ **Regra**: Ao registrar entrada, quantidade em estoque aumenta

## 🎨 Design

Interface moderna e intuitiva inspirada em design profissional com:
- Menu lateral de navegação
- Cores organizadas e consistentes
- Ícones para melhor usabilidade
- Tabelas com scrollbar
- Formulários validados
- Mensagens de confirmação e erro

### Paleta de Cores
- **Principal**: #2c3e50 (Azul escuro)
- **Secundário**: #34495e (Cinza azulado)
- **Sucesso**: #27ae60 (Verde)
- **Aviso**: #f39c12 (Laranja)
- **Erro**: #e74c3c (Vermelho)
- **Info**: #3498db (Azul)

## 🚀 Como Executar

### Requisitos
- Python 3.7 ou superior
- Tkinter (geralmente já incluído no Python)

### Execução
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
claude/
│
├── main.py                    # Arquivo principal - inicia a aplicação
├── data_manager.py            # Gerenciamento de dados em memória
├── categorias_ui.py           # Interface de categorias
├── produtos_ui.py             # Interface de produtos
├── clientes_ui.py             # Interface de clientes
├── vendas_ui.py               # Interface de vendas
├── entrada_estoque_ui.py      # Interface de entrada de estoque
└── README.md                  # Este arquivo
```

## 💾 Armazenamento de Dados

O sistema utiliza estruturas de dados em memória (dicionários e listas) para armazenar todas as informações:
- **Categorias**: Dicionário com ID como chave
- **Produtos**: Dicionário com ID como chave
- **Clientes**: Dicionário com ID como chave
- **Vendas**: Dicionário com ID como chave
- **Entradas de Estoque**: Lista de dicionários

**Nota**: Os dados são perdidos ao fechar o aplicativo (não há persistência em banco de dados).

## 🔒 Regras de Negócio Implementadas

1. ✅ Produto não pode ser cadastrado sem categoria
2. ✅ Ao excluir categoria, produtos relacionados são excluídos
3. ✅ Ao vender, quantidade em estoque diminui
4. ✅ Ao registrar entrada de estoque, quantidade aumenta
5. ✅ Ao excluir cliente, vendas não são excluídas (apenas o nome aparece como "Cliente Excluído")
6. ✅ Ao excluir venda, produtos retornam ao estoque
7. ✅ Validação de estoque antes de finalizar venda
8. ✅ IDs únicos e automáticos para todas as entidades

## 🧪 Dados de Exemplo

O sistema inicia com alguns dados de exemplo para facilitar os testes:

- **3 Categorias**: Eletrônicos, Alimentos, Vestuário
- **4 Produtos**: Notebook Dell, Mouse Logitech, Arroz 5kg, Camiseta Polo
- **2 Clientes**: João Silva, Maria Santos

## 🎯 Funcionalidades Extras Implementadas

- Dashboard com estatísticas em tempo real
- Histórico completo de vendas e entradas de estoque
- Carrinho de compras interativo
- Cálculo automático de totais e subtotais
- Validações de CPF e datas
- Interface responsiva e amigável
- Mensagens de confirmação para ações destrutivas
- Atualização automática de combos e listas

## 👨‍💻 Desenvolvido para

**Empresa WA** - Sistema de Gestão de Estoque e Vendas

---

**Versão**: 1.0  
**Tecnologia**: Python + Tkinter  
**Data**: Outubro 2025
