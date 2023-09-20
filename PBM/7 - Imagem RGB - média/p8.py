from PIL import Image


def clear_folder(folder_name):
    ...


def convert_saturation(image_path):
    entrada = Image.open(image_path)

    largura, altura = entrada.size
    nova_imagem = Image.new("P", (largura, altura))

    for y in range(altura):
        for x in range(largura):
            r, g, b = entrada.getpixel((x, y))
            media_rgb = int((r + g + b) // 3)

            nova_imagem.putpixel((x, y), (media_rgb, media_rgb, media_rgb))

    nova_imagem.save("PBM/output/Fig1_media_rgb", format="PPM")


if __name__ == "__main__":
    convert_saturation("PBM/assets/Fig1.ppm")
