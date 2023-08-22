from PIL import Image

img = Image.open('Capa Manipulando Imagens.png')
width = img.width // 10
height = img.height // 10
img_resized = img.resize((width, height))
img_resized.save('Capa Redimensionada.png')