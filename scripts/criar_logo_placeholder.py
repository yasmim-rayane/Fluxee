"""
Criar uma imagem placeholder para a logo Fluxee
Este script cria uma logo temporária até que a logo real seja adicionada
"""

from PIL import Image, ImageDraw, ImageFont

# Criar imagem 200x200 com fundo transparente
img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Desenhar círculo de fundo (azul escuro)
draw.ellipse([20, 20, 180, 180], fill='#1E3A8A')

# Desenhar círculo interno (azul ciano)
draw.ellipse([40, 40, 160, 160], fill='#00D4FF')

# Tentar adicionar texto
try:
    font = ImageFont.truetype("arial.ttf", 60)
except:
    font = ImageFont.load_default()

# Desenhar "F" no centro
text = "F"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (200 - text_width) // 2
y = (200 - text_height) // 2 - 10

draw.text((x, y), text, fill='#1F2937', font=font)

# Salvar
img.save('assets/fluxee_logo.png')
print('✓ Logo placeholder criada em assets/fluxee_logo.png')
print('  Substitua por sua logo real do Fluxee!')
