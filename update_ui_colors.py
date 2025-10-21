"""
Script para atualizar cores nos arquivos de UI
"""

import re

# Mapea mento de cores antigas para novas
color_map = {
    '"white"': 'self.colors["white"]',
    '"#2c3e50"': 'self.colors["text_dark"]',
    '"#27ae60"': 'self.colors["success"]',
    '"#f39c12"': 'self.colors["warning"]',
    '"#95a5a6"': '"#6B7280"',
    '"#e74c3c"': 'self.colors["danger"]',
    '"#3498db"': 'self.colors["info"]',
    '"Arial"': '"Segoe UI"',
}

files_to_update = [
    'clientes_ui.py',
    'produtos_ui.py',
    'vendas_ui.py',
    'entrada_estoque_ui.py'
]

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Aplicar substituições
        for old, new in color_map.items():
            content = content.replace(f'bg={old}', f'bg={new}')
            content = content.replace(f'fg={old}', f'fg={new}')
            content = content.replace(f'font=({old}', f'font=({new}')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✓ {filename} atualizado')
    except Exception as e:
        print(f'✗ Erro em {filename}: {e}')

print('\nAtualização concluída!')
