import numpy as np
import os
import cv2
from PIL import Image


def bit_plane_slicing(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    mask = np.zeros_like(img)
    mask.fill(0b11100000)
    img_3bits = cv2.bitwise_and(img, mask)

    img_nova = np.zeros_like(img_3bits)
    img_nova.fill(255)
    img_nova = cv2.bitwise_and(img_nova, img_3bits)

    cv2.imwrite(f'PBM/output/100-dollars-3bits.tif', img_nova)

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
    bit_plane_slicing("PBM/assets/Fig0314(a)(100-dollars).tif")
