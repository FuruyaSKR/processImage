from PIL import Image


def convert_saturation(image_path):
    entrada = Image.open(image_path)

    imagem_rgb = entrada.convert("RGB")
    largura, altura = entrada.size

    for y in range(largura):
        for x in range(altura):
            r, g, b = imagem_rgb.getpixel((x, y))
            media_rgb = int((r + g + b) // 3)
            entrada.putpixel((x, y), (media_rgb, media_rgb, media_rgb))

    entrada.save("PBM/output/Fig4_media_rgb.ppm")


if __name__ == "__main__":
    convert_saturation("PBM/assets/Fig4.ppm")
