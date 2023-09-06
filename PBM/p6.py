from PIL import Image, ImageEnhance


def convert_bitrate(image_path, bit_range, brightness):
    entrada = Image.open(image_path)
    largura, altura = entrada.size
    saida = Image.new("L", (largura, altura))

    for x in range(largura):
        for y in range(altura):
            valor = entrada.getpixel((x, y))
            novo_valor = round(valor * 2**bit_range / (2**8))
            saida.putpixel((x, y), novo_valor)

    enhancer = ImageEnhance.Brightness(saida)
    saida = enhancer.enhance(brightness)
    saida.save(f"PBM/output/EscalaCinzaBrightness.pgm")


if __name__ == "__main__":
    convert_bitrate("PBM/assets/EntradaEscalaCinza.pgm", 8, 1.2)
