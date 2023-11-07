import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_grayscale_image_histogram(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.convertScaleAbs(img, alpha=2.0, beta=0)
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    
    plt.plot(hist, color='gray', alpha=0.5)
    plt.xlabel('Nível das cores')
    plt.ylabel('Quantidade de Pixels')
    plt.title('Histograma Cinza')

    plt.savefig('PBM/output/HistogramaEntradaEscalaCinza')
    cv2.imwrite('PBM/output/SaidaEscalaCinza.pgm', img)
    plt.show()


def remove_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Erro ao remover {file_path}: {e}")

if __name__ == "__main__":
    remove_files("PBM/output/")
    generate_grayscale_image_histogram("PBM/assets/EntradaEscalaCinza.pgm")
