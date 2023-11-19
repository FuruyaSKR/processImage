import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

def generate_rgb_image_histogram(image_path):
    img = cv2.imread(image_path, 0)
    equ = cv2.equalizeHist(img)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    hist2, bins2 = np.histogram(equ.flatten(), 256, [0, 256])

    plt.figure(figsize=(10,10))
    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(equ, cmap='gray')
    plt.title('Imagem Equalizada'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.hist(img.flatten(), 256, [0, 256])
    plt.title('Histograma Imagem Original'), plt.xlim([0, 256])
    plt.subplot(224), plt.hist(equ.flatten(), 256, [0, 256])
    plt.title('Histograma Imagem Equalizada'), plt.xlim([0, 256])

    plt.savefig('PBM/output/EqualizateHist-1(top_left).png')
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
    generate_rgb_image_histogram("PBM/assets/Fig0316(1)(top_left).tif")
