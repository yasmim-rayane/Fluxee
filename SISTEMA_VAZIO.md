# Sistema WA - Versão 2.0 (SQLite - Sem Dados de Exemplo)

## ✅ ATUALIZAÇÃO: Sistema inicia vazio

O sistema foi atualizado para iniciar **sem dados de exemplo**. O banco de dados é criado vazio na primeira execução.

---

## 🆕 O que mudou?

### Antes
- ✅ Sistema criava automaticamente:
  - 3 categorias (Eletrônicos, Alimentos, Vestuário)
  - 4 produtos
  - 2 clientes

### Agora
- ✅ Sistema inicia **completamente vazio**
- ✅ Você começa do zero
- ✅ Cadastre seus próprios dados

---

## 🚀 Primeira Execução

```bash
python main.py
```

O sistema irá:
1. Criar o arquivo `sistema_wa.db`
2. Criar todas as 6 tabelas vazias
3. **Não inserir nenhum dado**
4. Abrir a interface gráfica

**Dashboard mostrará zeros em todas as estatísticas.**

---

## 📝 Primeiros Passos

### 1. Cadastre Categorias
- Vá em "📂 Categorias"
- Adicione suas categorias (ex: Eletrônicos, Roupas, Alimentos)

### 2. Cadastre Produtos
- Vá em "📦 Produtos"
- Adicione produtos (requer categoria)

### 3. Cadastre Clientes
- Vá em "👥 Clientes"
- Adicione seus clientes

### 4. Faça Vendas
- Vá em "💰 Vendas"
- Realize suas primeiras vendas

### 5. Registre Entradas
- Vá em "📥 Entrada Estoque"
- Registre entradas de mercadoria

---

## 🔄 Dados de Exemplo (Opcional)

Se você quiser **adicionar dados de exemplo** para testar, pode:

### Opção 1: Adicionar Manualmente
Use a interface para cadastrar:
- Algumas categorias
- Alguns produtos
- Alguns clientes

### Opção 2: Código (Avançado)
No arquivo `database.py`, descomente o método `_inserir_dados_exemplo()`:

1. Abra `database.py`
2. Encontre o método `_inserir_dados_exemplo()`
3. Descomente as linhas comentadas
4. Delete `sistema_wa.db`
5. Execute `python main.py` novamente

---

## 💡 Vantagens de Iniciar Vazio

### ✅ Pronto para Produção
- Sem necessidade de limpar dados de teste
- Inicie direto com seus dados reais

### ✅ Flexibilidade Total
- Escolha suas próprias categorias
- Defina sua estrutura de produtos
- Cadastre apenas o necessário

### ✅ Aprendizado Gradual
- Entenda cada funcionalidade
- Veja o sistema crescer com seus dados

---

## 📊 Dashboard Inicial

Na primeira execução, o Dashboard mostrará:

```
Produtos: 0
Categorias: 0
Clientes: 0
Vendas: 0
Valor Total em Vendas: R$ 0,00
```

**Isso é normal!** Comece cadastrando suas categorias e produtos.

---

## 🗄️ Estrutura do Banco

O banco é criado com 6 tabelas vazias:

```sql
✅ categorias (0 registros)
✅ produtos (0 registros)
✅ clientes (0 registros)
✅ vendas (0 registros)
✅ itens_venda (0 registros)
✅ entradas_estoque (0 registros)
```

---

## ⚠️ Importante

### Primeira Categoria é Obrigatória
Antes de cadastrar produtos, você **deve** cadastrar ao menos uma categoria.

### CPF Único
Não é possível cadastrar dois clientes com o mesmo CPF.

### Estoque
- Produtos começam com estoque definido no cadastro
- Vendas diminuem estoque automaticamente
- Entradas aumentam estoque

---

## 🔧 Comandos Úteis

### Verificar Dados
```bash
# Abrir banco no DB Browser
# Menu: File → Open Database → sistema_wa.db
```

### Resetar Tudo
```bash
# Deletar banco e recomeçar
del sistema_wa.db
python main.py
```

### Backup
```bash
# Fazer backup dos dados
copy sistema_wa.db backup_$(Get-Date -Format "yyyy-MM-dd").db
```

---

## 📚 Fluxo Recomendado

```
1. Abrir Sistema
   ↓
2. Cadastrar Categorias (mínimo 1)
   ↓
3. Cadastrar Produtos
   ↓
4. Cadastrar Clientes
   ↓
5. Realizar Vendas
   ↓
6. Registrar Entradas de Estoque
```

---

## ✅ Benefícios da Mudança

| Aspecto | Benefício |
|---------|-----------|
| **Produção** | Sem dados fictícios |
| **Personalização** | 100% seus dados |
| **Limpeza** | Não precisa limpar exemplos |
| **Profissional** | Pronto para uso real |

---

## 🎯 Sistema Pronto para Uso Real

Com esta atualização, o Sistema WA está **pronto para uso em ambiente de produção**:

- ✅ Banco de dados limpo
- ✅ Sem dados de teste
- ✅ Interface completa
- ✅ Todas as funcionalidades
- ✅ Documentação atualizada

---

**Sistema WA - Versão 2.0**  
**Data: Outubro 2025**  
**Status: Pronto para Produção (Sem dados de exemplo)**
