# 🎯 Sistema Fluxee - Gestão de Estoque e Vendas

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-production-brightgreen)

**Sistema completo de gerenciamento com interface moderna e profissional**

[Iniciar](#-instalação) • [Documentação](#-documentação) • [Funcionalidades](#-funcionalidades) • [Visual](#-visual-modernizado)

</div>

---

## 📋 Sobre o Projeto

O **Sistema Fluxee** é uma aplicação desktop completa para gestão de estoque e vendas, desenvolvida em Python com interface gráfica moderna baseada na identidade visual Fluxee.

### ✨ Destaques v2.0

- 🎨 **Interface Modernizada** com paleta de cores Fluxee (azul ciano)
- 🖼️ **Logo Integrada** no cabeçalho
- ✅ **Validação de CPF** com algoritmo oficial brasileiro
- 💾 **Banco SQLite** com relacionamentos e constraints
- 📊 **Dashboard** com estatísticas em tempo real
- 🔄 **Controle de Estoque** automático nas vendas

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos

```bash
# 1. Clone ou baixe o repositório
cd claude

# 2. Instale as dependências
pip install Pillow

# 3. Execute o sistema
python main.py
```

**Ou simplesmente**:
- Windows: Clique duplo em `iniciar.bat`

---

## 💎 Funcionalidades

### 🏠 Dashboard
- Visão geral do sistema
- Estatísticas de produtos, categorias, clientes e vendas
- Card especial com valor total de vendas
- Interface com cards coloridos e modernos

### 📂 Categorias
- Criar, editar e excluir categorias
- Validação de nomes únicos
- Exclusão em cascata (remove produtos associados)

### 📦 Produtos
- Gerenciamento completo de produtos
- Vinculação obrigatória a categorias
- Controle de estoque integrado
- Preço e quantidade

### 👥 Clientes
- Cadastro com validação de CPF (algoritmo oficial)
- Data de nascimento e gênero
- CPF único no sistema
- Validação de formato DD/MM/AAAA

### 💰 Vendas
- Sistema completo de PDV
- Adicionar múltiplos produtos
- Cálculo automático de totais
- Formas de pagamento variadas
- Baixa automática no estoque

### 📥 Entrada de Estoque
- Registro de entradas
- Incremento automático no estoque
- Histórico com data/hora

---

## 🎨 Visual Modernizado

### Paleta de Cores Fluxee

```css
Primária:    #00D4FF  /* Azul ciano brilhante */
Secundária:  #0EA5E9  /* Azul céu */
Escuro:      #1E3A8A  /* Azul marinho */
Menu:        #1F2937  /* Cinza escuro */
Sucesso:     #10B981  /* Verde */
Alerta:      #F59E0B  /* Laranja */
Perigo:      #EF4444  /* Vermelho */
```

### Layout

```
┌────────────────────────────────────────────┐
│  [Logo] FLUXEE                             │
│          Sistema de Gestão                 │
├─────────┬──────────────────────────────────┤
│ MENU    │  Conteúdo Principal              │
│ 🏠 Dash │                                  │
│ 📂 Cat  │  • Dashboard com cards           │
│ 📦 Prod │  • Formulários modernos          │
│ 📥 Est  │  • Tabelas organizadas           │
│ 👥 Cli  │  • Botões coloridos             │
│ 💰 Vend │                                  │
└─────────┴──────────────────────────────────┘
```

---

## 📚 Documentação

### Guias Principais

| Documento | Descrição |
|-----------|-----------|
| **START_HERE.md** | Início rápido e visão geral |
| **RESUMO_MODERNIZACAO.md** | Detalhes da modernização visual |
| **COMO_ADICIONAR_LOGO.md** | Substituir logo placeholder |
| **VALIDACAO_CPF.md** | Como funciona a validação de CPF |
| **GUIA_USUARIO.md** | Manual completo de uso |

### Documentos Técnicos

- `MODERNIZACAO_VISUAL.md` - Arquitetura visual
- `README_SQLITE.md` - Estrutura do banco de dados
- `CONVERSAO_COMPLETA.md` - Migração para SQLite

---

## 🗂️ Estrutura do Projeto

```
claude/
├── assets/
│   ├── fluxee_logo.png          # Logo (substituir pela real)
│   └── README.md
├── main.py                      # ⭐ Aplicação principal
├── database.py                  # Gerenciamento SQLite
├── data_manager.py              # Camada de abstração
├── categorias_ui.py             # Interface categorias
├── produtos_ui.py               # Interface produtos
├── clientes_ui.py               # Interface clientes (+ validação CPF)
├── vendas_ui.py                 # Interface vendas
├── entrada_estoque_ui.py        # Interface estoque
├── sistema_wa.db                # Banco de dados
├── iniciar.bat                  # Atalho Windows
└── [documentação...]
```

---

## 💾 Banco de Dados

### Tabelas

- **categorias** - Categorias de produtos
- **produtos** - Produtos com estoque
- **clientes** - Clientes com CPF único
- **vendas** - Registro de vendas
- **itens_venda** - Itens de cada venda
- **entradas_estoque** - Histórico de entradas

### Relacionamentos

- Produtos → Categorias (CASCADE DELETE)
- Vendas → Clientes (SET NULL)
- Itens Venda → Vendas (CASCADE DELETE)
- Entradas → Produtos (CASCADE DELETE)

---

## ✅ Validações Implementadas

### CPF
- ✔️ Formato com 11 dígitos
- ✔️ Rejeita sequências iguais (111.111.111-11)
- ✔️ Valida primeiro dígito verificador
- ✔️ Valida segundo dígito verificador
- ✔️ Aceita com ou sem pontuação

### Formulários
- ✔️ Campos obrigatórios
- ✔️ Formatos de data (DD/MM/AAAA)
- ✔️ Valores numéricos positivos
- ✔️ Unicidade (CPF, códigos)

---

## 🎯 Tecnologias

- **Python 3.11+** - Linguagem principal
- **Tkinter** - Interface gráfica
- **SQLite3** - Banco de dados
- **Pillow** - Processamento de imagens
- **ttk** - Widgets avançados

---

## 🖼️ Adicionar Logo Real

Atualmente o sistema usa uma logo placeholder (círculo com "F").

### Para adicionar a logo Fluxee:

1. Salve a imagem como `fluxee_logo.png`
2. Coloque em `assets/fluxee_logo.png`
3. Reinicie o sistema

**Guia completo**: `COMO_ADICIONAR_LOGO.md`

---

## 🔒 Segurança

- Validação de entrada em todos os formulários
- Constraints do banco (UNIQUE, FK, NOT NULL)
- Transações com rollback em erros
- Sanitização de dados

---

## 📊 Status do Projeto

- ✅ Interface completa e funcional
- ✅ Banco de dados implementado
- ✅ Validações ativas
- ✅ Visual modernizado
- ✅ Documentação completa
- ⏳ Aguardando logo real Fluxee

---

## 🤝 Contribuindo

Este é um projeto educacional. Sugestões são bem-vindas!

---

## 📝 Licença

MIT License - Livre para uso e modificação

---

## 🎊 Pronto para Usar!

O sistema está **100% funcional** e pronto para produção!

### Checklist:

- ✅ Instalar dependências: `pip install Pillow`
- ✅ Executar: `python main.py` ou `iniciar.bat`
- ⏳ Adicionar logo real (opcional)
- ✅ Começar a usar!

---

<div align="center">

**Sistema Fluxee v2.0**

*Desenvolvido com ❤️ usando Python + Tkinter + SQLite*

[⬆ Voltar ao topo](#-sistema-fluxee---gestão-de-estoque-e-vendas)

</div>
