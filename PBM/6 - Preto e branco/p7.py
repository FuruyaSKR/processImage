from PIL import Image


def convert_saturation(image_path):
    entrada = Image.open(image_path)
    saida_blackNwhite = entrada.convert("1")

    saida_blackNwhite.save(f"PBM/output/SaidaBlackAndWhite.pbm")


if __name__ == "__main__":
    convert_saturation("PBM/assets/EntradaEscalaCinza.pgm")
