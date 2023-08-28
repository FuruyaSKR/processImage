# pip install Pillow
from PIL import Image


size = {
    "main": (480, 320),
    "hd": (1280, 720),
    "fullHD": (1920, 1080),
    "4k": (3840, 2160),
    "8k": (7680, 4320),
}


def resize_image(image_path, size_type):
    img = Image.open(image_path)
    try:
        img_resized = img.resize(size.get(size_type))
        img_resized.save(f"PBM/output/imagem_{size_type}.pgm")
    except TypeError:
        raise TypeError("Tamanho não permitido")


def scale_image(image_path, scale):
    img = Image.open(image_path)
    w, h = img.size
    new_w = int(w / scale)
    new_h = int(h / scale)
    img_resized = img.resize((new_w, new_h))
    img_resized.save(f"PBM/output/SaidaEscalaCinza{scale}.pgm")


if __name__ == "__main__":
    scale_image("PBM/assets/EntradaEscalaCinza.pgm", 10)
    for resize in size.keys():
        resize_image("PBM/assets/EntradaEscalaCinza.pgm", resize)
