# 📁 Estrutura de Pastas - Sistema Fluxee

## 🗂️ Organização do Projeto

```
claude/
│
├── 📄 main.py                    # ⭐ ARQUIVO PRINCIPAL - Execute este
├── 📄 README.md                  # Documentação principal
├── 📄 iniciar.bat                # Atalho Windows
├── 💾 sistema_wa.db              # Banco de dados SQLite
│
├── 📁 ui/                        # INTERFACES GRÁFICAS
│   ├── categorias_ui.py          # Interface de categorias
│   ├── produtos_ui.py            # Interface de produtos
│   ├── clientes_ui.py            # Interface de clientes (+ validação CPF)
│   ├── vendas_ui.py              # Interface de vendas
│   ├── entrada_estoque_ui.py     # Interface de entrada de estoque
│   └── __init__.py               # Módulo Python
│
├── 📁 database/                  # GERENCIAMENTO DE DADOS
│   ├── database.py               # Gerenciamento SQLite
│   ├── data_manager.py           # Camada de abstração
│   └── __init__.py               # Módulo Python
│
├── 📁 assets/                    # RECURSOS VISUAIS
│   ├── fluxee_logo.png           # Logo (substituir pela real)
│   └── README.md                 # Info sobre assets
│
├── 📁 docs/                      # DOCUMENTAÇÃO COMPLETA
│   ├── START_HERE.md             # ⭐ Comece por aqui
│   ├── GUIA_USUARIO.md           # Manual de uso
│   ├── VALIDACAO_CPF.md          # Validação de CPF
│   ├── COMO_ADICIONAR_LOGO.md    # Substituir logo
│   ├── RESUMO_MODERNIZACAO.md    # Detalhes da modernização
│   ├── MODERNIZACAO_VISUAL.md    # Arquitetura visual
│   ├── PROJETO_CONCLUIDO.md      # Status do projeto
│   ├── README_SQLITE.md          # Estrutura do banco
│   ├── CONVERSAO_COMPLETA.md     # Migração SQLite
│   ├── GUIA_USUARIO.md           # Manual completo
│   ├── REQUIREMENTS.txt          # Dependências
│   └── ... (outros docs)
│
└── 📁 scripts/                   # SCRIPTS AUXILIARES
    ├── criar_logo_placeholder.py # Gera logo temporária
    ├── update_ui_colors.py       # Atualiza cores
    └── consultas_uteis.sql       # Queries SQL úteis
```

---

## 🚀 Como Usar

### Executar Sistema:
```bash
python main.py
```

### Consultar Documentação:
- Início rápido: `docs/START_HERE.md`
- Manual completo: `docs/GUIA_USUARIO.md`

### Adicionar Logo Real:
- Ver: `docs/COMO_ADICIONAR_LOGO.md`

---

## 📝 Arquivos Principais na Raiz

| Arquivo | Descrição |
|---------|-----------|
| **main.py** | Aplicação principal - EXECUTE ESTE |
| **README.md** | Documentação geral do projeto |
| **iniciar.bat** | Atalho para Windows |
| **sistema_wa.db** | Banco de dados (gerado automaticamente) |

---

## 🎯 Estrutura Limpa

✅ Apenas arquivos essenciais na raiz  
✅ Código organizado em pastas temáticas  
✅ Documentação separada em `/docs/`  
✅ Scripts auxiliares em `/scripts/`  
✅ Fácil navegação e manutenção  

---

**Sistema Fluxee v2.0 - Organizado e Profissional**
