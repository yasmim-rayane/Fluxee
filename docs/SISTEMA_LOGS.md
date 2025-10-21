# 📝 Sistema de Logs - Fluxee

## 📋 Descrição

O sistema possui um módulo de registro de operações que grava automaticamente todas as transações importantes em arquivo de texto.

## 📁 Localização

```
logs/
└── registro.txt    # Arquivo de log principal
```

## 🔧 Módulo Logger

**Arquivo:** `database/logger.py`

O módulo `logger.py` é responsável por registrar todas as operações do sistema.

### Funções:

```python
registrar_operacao(
    tipo_operacao: str,      # Tipo da operação
    nome_produto: str,       # Nome do produto
    quantidade: int,         # Quantidade
    estoque_restante: int,   # Estoque após operação
    valor_total: float       # Valor total (opcional)
)
```

## 📊 Operações Registradas

### 1. NOVO PRODUTO
Registrado quando um produto é criado com estoque inicial.

**Exemplo:**
```
[2025-10-21 16:30:45] NOVO PRODUTO | Produto: Notebook Dell | Quantidade: 10 | Total: R$ 35000.00 | Estoque Restante: 10
```

### 2. VENDA
Registrado a cada venda de produto.

**Exemplo:**
```
[2025-10-21 16:45:12] VENDA | Produto: Mouse Logitech | Quantidade: 5 | Total: R$ 449.75 | Estoque Restante: 45
```

### 3. ENTRADA ESTOQUE
Registrado quando há entrada de produtos no estoque.

**Exemplo:**
```
[2025-10-21 17:20:30] ENTRADA ESTOQUE | Produto: Arroz 5kg | Quantidade: 50 | Total: R$ 1295.00 | Estoque Restante: 150
```

### 4. CANCELAMENTO VENDA
Registrado quando uma venda é excluída (devolução ao estoque).

**Exemplo:**
```
[2025-10-21 17:35:18] CANCELAMENTO VENDA | Produto: Camiseta Polo | Quantidade: 3 | Estoque Restante: 33
```

## 📝 Formato do Log

Cada linha do log segue o padrão:

```
[TIMESTAMP] TIPO_OPERAÇÃO | Produto: NOME | Quantidade: X | Total: R$ XX.XX | Estoque Restante: Y
```

### Componentes:

- **TIMESTAMP**: Data e hora no formato `YYYY-MM-DD HH:MM:SS`
- **TIPO_OPERAÇÃO**: Tipo da operação realizada
- **Produto**: Nome do produto envolvido
- **Quantidade**: Quantidade de itens na operação
- **Total**: Valor total (quando aplicável)
- **Estoque Restante**: Quantidade em estoque após a operação

## 🔄 Integração com o Sistema

O logger é chamado automaticamente em:

### DataManager (Versão Memória)
- `criar_produto()` - NOVO PRODUTO
- `criar_venda()` - VENDA
- `excluir_venda()` - CANCELAMENTO VENDA
- `criar_entrada_estoque()` - ENTRADA ESTOQUE

### Database (Versão SQLite)
**Nota:** A versão SQLite atual não integra o logger. Para adicionar:

1. Importar o logger em `database/database.py`:
```python
from database.logger import registrar_operacao
```

2. Chamar `registrar_operacao()` nos métodos apropriados

## 📊 Utilidades do Log

### Auditoria
- Rastreamento completo de movimentações
- Histórico de todas as operações
- Identificação de padrões de venda

### Análise
- Produtos mais vendidos
- Horários de pico
- Volume de operações

### Controle
- Verificação de estoque
- Validação de vendas
- Identificação de inconsistências

## 🛠️ Personalização

### Modificar Formato

Edite a função em `database/logger.py`:

```python
def registrar_operacao(...):
    # Personalizar formato aqui
    log_entry = f"[{timestamp}] {tipo_operacao}"
    # Adicionar/remover campos conforme necessário
```

### Múltiplos Arquivos

Para separar logs por tipo:

```python
# Log de vendas
arquivo_vendas = "logs/vendas.txt"

# Log de entradas
arquivo_entradas = "logs/entradas.txt"
```

### Rotação de Logs

Implementar rotação diária/mensal:

```python
from datetime import datetime

data_atual = datetime.now().strftime("%Y-%m-%d")
arquivo_log = f"logs/registro_{data_atual}.txt"
```

## ⚠️ Observações

1. **Encoding UTF-8**: O arquivo é gravado com encoding UTF-8 para suportar caracteres especiais
2. **Modo Append**: Registros são adicionados ao final do arquivo (não sobrescreve)
3. **Thread-Safe**: Adequado para múltiplas operações simultâneas
4. **Performance**: Mínimo impacto no desempenho do sistema

## 📂 Backup

Recomenda-se fazer backup regular do arquivo `registro.txt`:

```bash
# Criar backup diário
copy logs\registro.txt logs\backup\registro_2025-10-21.txt
```

## 🔍 Consulta de Logs

### Buscar por Produto
```powershell
Select-String -Path "logs\registro.txt" -Pattern "Mouse Logitech"
```

### Buscar por Tipo de Operação
```powershell
Select-String -Path "logs\registro.txt" -Pattern "VENDA"
```

### Buscar por Data
```powershell
Select-String -Path "logs\registro.txt" -Pattern "2025-10-21"
```

---

## ✅ Status

- ✅ Logger implementado e funcional
- ✅ Formato padronizado
- ✅ Integrado com versão em memória
- ⏳ Integração pendente com versão SQLite

---

**Sistema Fluxee v2.0 - Logging Completo**
