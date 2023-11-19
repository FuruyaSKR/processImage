import numpy as np
import os
import cv2
from PIL import Image


def bit_plane_slicing(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bits = []
    for i in range(8):
        bit = cv2.bitwise_and(gray, 2**i)
        bit = np.uint8(bit * 255 / 2**i)
        bits.append(bit)
    
    for i, bit in enumerate(bits):
        cv2.imwrite(f'PBM/output/bit_{i+1}.jpg', bit)

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
