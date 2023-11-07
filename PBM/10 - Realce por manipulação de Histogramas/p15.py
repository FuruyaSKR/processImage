import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

def generate_rgb_image_histogram(image_path):
    img = cv2.imread(image_path)
    img = cv2.convertScaleAbs(img, alpha=2.0, beta=0)
    r, g, b = cv2.split(img)

    hist_r, bins = np.histogram(r.ravel(), 256, [0, 256])
    hist_g, bins = np.histogram(g.ravel(), 256, [0, 256])
    hist_b, bins = np.histogram(b.ravel(), 256, [0, 256])

    plt.plot(hist_r, color='red', alpha=0.5)
    plt.plot(hist_g, color='green', alpha=0.5)
    plt.plot(hist_b, color='blue', alpha=0.5)

    plt.xlabel('Nível das cores')
    plt.ylabel('Quantidade de Pixels')
    plt.title('Histograma RGB')

    plt.savefig('PBM/output/HistogramaRGB')
    cv2.imwrite('PBM/output/SaidaRGB.ppm', img)
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
    generate_rgb_image_histogram("PBM/assets/EntradaRGB.ppm")
