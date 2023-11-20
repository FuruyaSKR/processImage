import numpy as np
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def highlighting_by_histogram(image_path):
    img = cv2.imread(image_path)
    img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
    hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

    cv2.imwrite('PBM/output/SaidaFig0316(1)(top_left).tif',hist_equalization_result)

    hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_result = cv2.calcHist([hist_equalization_result], [0], None, [256], [0, 256])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.hist(img.ravel(), 256, [0, 256])
    ax1.set_title('Histograma da Imagem Original')

    ax2.hist(hist_equalization_result.ravel(), 256, [0, 256])
    ax2.set_title('Histograma da Imagem Resultante')

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
    highlighting_by_histogram("PBM/assets/Fig0316(1)(top_left).tif")

