# Guia do Usuário - Sistema WA

## Bem-vindo ao Sistema WA de Gestão de Estoque e Vendas!

Este guia irá ajudá-lo a usar todas as funcionalidades do sistema.

---

## 🏠 Dashboard (Tela Inicial)

Ao abrir o sistema, você verá o Dashboard com estatísticas em tempo real:
- Total de produtos cadastrados
- Total de categorias
- Total de clientes
- Total de vendas realizadas
- Valor total em vendas

---

## 📂 Categorias

### Adicionar Nova Categoria
1. Clique em "📂 Categorias" no menu lateral
2. Digite o nome da categoria no campo
3. Clique em "➕ Adicionar"

### Editar Categoria
1. Clique na categoria desejada na tabela
2. Altere o nome no campo
3. Clique em "✏️ Editar"
4. Ou clique em "❌ Cancelar" para desistir

### Excluir Categoria
1. Clique na categoria desejada na tabela
2. Clique em "🗑️ Excluir Categoria"
3. Confirme a exclusão
4. **⚠️ ATENÇÃO**: Todos os produtos desta categoria também serão excluídos!

---

## 📦 Produtos

### Adicionar Novo Produto
1. Clique em "📦 Produtos" no menu lateral
2. Preencha os campos:
   - Nome do Produto
   - **Categoria** (obrigatória - selecione uma existente)
   - Valor Unitário (use ponto ou vírgula para decimais)
   - Quantidade Inicial
3. Clique em "➕ Adicionar Produto"

### Editar Produto
1. Clique no produto desejado na tabela
2. Altere as informações necessárias
3. Clique em "✏️ Salvar Edição"
4. **Nota**: A quantidade não pode ser editada aqui (use Entrada de Estoque)

### Excluir Produto
1. Selecione o produto na tabela
2. Clique em "🗑️ Excluir Produto"
3. Confirme a exclusão

---

## 👥 Clientes

### Cadastrar Cliente
1. Clique em "👥 Clientes" no menu lateral
2. Preencha os campos:
   - Nome Completo
   - CPF (formato: XXX.XXX.XXX-XX)
   - Data de Nascimento (formato: DD/MM/AAAA)
   - Gênero
3. Clique em "➕ Adicionar Cliente"

### Editar Cliente
1. Selecione o cliente na tabela
2. Altere as informações
3. Clique em "✏️ Salvar Edição"

### Excluir Cliente
1. Selecione o cliente na tabela
2. Clique em "🗑️ Excluir Cliente"
3. Confirme a exclusão
4. **Nota**: As vendas do cliente não serão excluídas

---

## 💰 Vendas

### Realizar Nova Venda

#### Passo 1: Selecionar Cliente e Pagamento
1. Clique em "💰 Vendas" no menu lateral
2. Selecione o cliente no combo
3. Selecione a forma de pagamento

#### Passo 2: Adicionar Produtos ao Carrinho
1. Selecione o produto desejado
2. O sistema mostra o estoque disponível
3. Digite a quantidade
4. Clique em "➕ Adicionar ao Carrinho"
5. Repita para adicionar mais produtos

#### Passo 3: Revisar e Finalizar
1. Confira os produtos no carrinho
2. Verifique o valor total
3. Para remover um produto, selecione-o e clique em "➖ Remover Selecionado"
4. Clique em "✅ Finalizar Venda"
5. Um código de venda será gerado (ex: VND00001)

### Excluir Venda
1. Selecione a venda no histórico
2. Clique em "🗑️ Excluir Venda Selecionada"
3. Confirme a exclusão
4. **Os produtos retornarão ao estoque automaticamente**

---

## 📥 Entrada de Estoque

### Registrar Entrada
1. Clique em "📥 Entrada Estoque" no menu lateral
2. Selecione o produto
3. O sistema mostra o estoque atual
4. Digite a quantidade a adicionar
5. O sistema calcula e mostra o novo estoque
6. Clique em "✅ Registrar Entrada"

### Visualizar Histórico
- Todas as entradas ficam registradas na tabela
- Mostra: ID, Produto, Quantidade adicionada, Data e Hora

---

## 💡 Dicas e Regras Importantes

### ✅ Regras do Sistema

1. **Categorias e Produtos**
   - Um produto só pode ser criado se houver pelo menos uma categoria
   - Ao excluir uma categoria, TODOS os produtos dela são excluídos

2. **Estoque**
   - O estoque diminui automaticamente ao finalizar uma venda
   - O estoque aumenta automaticamente ao registrar entrada
   - Não é possível vender mais do que há em estoque

3. **Vendas e Clientes**
   - Uma venda precisa ter pelo menos um produto
   - Ao excluir uma venda, os produtos voltam ao estoque
   - Ao excluir um cliente, as vendas dele permanecem no sistema

4. **Códigos e IDs**
   - Cada venda recebe um código único (VND00001, VND00002, etc.)
   - Todos os registros têm IDs únicos automáticos

### 🎯 Fluxo Recomendado

1. **Configuração Inicial**
   - Cadastre as categorias
   - Cadastre os produtos com estoque inicial
   - Cadastre os clientes

2. **Operação Diária**
   - Registre vendas conforme ocorrem
   - Registre entradas de estoque quando receber mercadorias
   - Acompanhe o Dashboard

3. **Manutenção**
   - Edite informações quando necessário
   - Exclua registros obsoletos com cuidado
   - Verifique o histórico regularmente

---

## ⚠️ Avisos Importantes

### Perda de Dados
- **TODOS os dados são perdidos ao fechar o aplicativo**
- Este sistema não tem banco de dados persistente
- Os dados existem apenas na memória durante a execução

### Backup
- Para preservar dados importantes, anote manualmente
- Ou tire screenshots das informações críticas
- Considere adicionar um banco de dados real no futuro

### Validações
- CPF deve ter 11 dígitos
- Datas devem estar no formato DD/MM/AAAA
- Valores monetários aceitam ponto ou vírgula
- Quantidades devem ser números inteiros positivos

---

## 🆘 Resolução de Problemas

### O programa não abre
- Verifique se Python está instalado
- Verifique se Tkinter está disponível
- Execute: `python main.py` no terminal

### Erro ao adicionar produto
- Certifique-se de que existe ao menos uma categoria
- Verifique se todos os campos estão preenchidos
- Valor deve ser um número válido

### Erro ao finalizar venda
- Verifique se selecionou um cliente
- Verifique se selecionou forma de pagamento
- Certifique-se de que há produtos no carrinho
- Verifique se há estoque suficiente

### Interface não atualiza
- Use os botões do menu lateral para navegar
- Após operações, a tela é atualizada automaticamente

---

## 📞 Suporte

Para dúvidas ou problemas:
- Consulte o arquivo README.md
- Verifique o arquivo REQUIREMENTS.txt
- Revise o código-fonte (está bem comentado)

---

**Sistema desenvolvido para a Empresa WA**  
**Versão 1.0 - Outubro 2025**
