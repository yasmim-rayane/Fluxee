# Validação de CPF - Sistema WA

## 📋 Descrição

O sistema agora possui validação completa de CPF utilizando o algoritmo oficial brasileiro de verificação de dígitos.

## ✅ Funcionalidades da Validação

### 1. Verificações Implementadas

A validação de CPF realiza as seguintes verificações:

1. **Formato**: Verifica se o CPF possui exatamente 11 dígitos numéricos
2. **CPFs Conhecidamente Inválidos**: Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11, 000.000.000-00)
3. **Primeiro Dígito Verificador**: Valida usando o algoritmo oficial brasileiro
4. **Segundo Dígito Verificador**: Valida usando o algoritmo oficial brasileiro

### 2. Formato Aceito

O sistema aceita CPF em qualquer um dos formatos:
- **Com pontuação**: `123.456.789-10`
- **Sem pontuação**: `12345678910`

A validação remove automaticamente caracteres não numéricos antes de processar.

## 🔍 Algoritmo de Validação

### Cálculo do Primeiro Dígito Verificador

```
Posições:  1   2   3   4   5   6   7   8   9
CPF:       1   1   1   4   4   4   7   7   7
Peso:     10   9   8   7   6   5   4   3   2

Soma = (1×10) + (1×9) + (1×8) + (4×7) + (4×6) + (4×5) + (7×4) + (7×3) + (7×2)
Resto = Soma % 11
Se Resto < 2: Dígito = 0
Senão: Dígito = 11 - Resto
```

### Cálculo do Segundo Dígito Verificador

```
Posições:  1   2   3   4   5   6   7   8   9   10
CPF:       1   1   1   4   4   4   7   7   7   3
Peso:     11  10   9   8   7   6   5   4   3   2

Soma = (1×11) + (1×10) + (1×9) + (4×8) + (4×7) + (4×6) + (7×5) + (7×4) + (7×3) + (3×2)
Resto = Soma % 11
Se Resto < 2: Dígito = 0
Senão: Dígito = 11 - Resto
```

## 🧪 Exemplos de CPFs

### CPFs Válidos para Teste

- `111.444.777-35` ✅
- `529.982.247-25` ✅
- `123.456.789-09` ✅

### CPFs Inválidos

- `111.111.111-11` ❌ (todos os dígitos iguais)
- `123.456.789-00` ❌ (dígitos verificadores incorretos)
- `123` ❌ (menos de 11 dígitos)
- `12345678901234` ❌ (mais de 11 dígitos)

## 💻 Implementação

### Arquivo Modificado

- **`clientes_ui.py`**: Método `_validar_cpf()` atualizado com algoritmo completo

### Método de Validação

```python
def _validar_cpf(self, cpf):
    """Validação completa de CPF (formato e dígitos verificadores)"""
    # Remove caracteres não numéricos
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf_numeros) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf_numeros == cpf_numeros[0] * 11:
        return False
    
    # Validação dos dígitos verificadores...
    return True
```

## 🎯 Uso no Sistema

### Ao Adicionar Cliente

1. Preencha os dados do cliente
2. Digite o CPF (com ou sem pontuação)
3. Clique em "Adicionar Cliente"
4. Se o CPF for inválido, uma mensagem de erro será exibida: **"CPF inválido! Verifique se o CPF está correto."**

### Ao Editar Cliente

1. Selecione um cliente na lista
2. Modifique o CPF se necessário
3. Clique em "Salvar Edição"
4. A mesma validação será aplicada

## 🔒 Validações Complementares

Além da validação de CPF, o sistema também verifica:

- CPF é obrigatório (não pode estar vazio)
- CPF deve ser único no banco de dados (UNIQUE constraint)
- Nome completo é obrigatório
- Data de nascimento deve estar no formato DD/MM/AAAA
- Gênero deve ser selecionado

## ⚠️ Observações

- A validação ocorre apenas no frontend (clientes_ui.py)
- O banco de dados garante unicidade do CPF através de constraint UNIQUE
- Caracteres especiais (pontos e hífen) são automaticamente removidos
- A validação segue rigorosamente o algoritmo oficial da Receita Federal do Brasil

## 📚 Referências

- [Algoritmo de Validação de CPF - Receita Federal](https://www.receita.fazenda.gov.br/)
- Regra do Módulo 11 para cálculo dos dígitos verificadores
