import cv2
import numpy as np
import os

def subtract_images(image_path, image_path2):
    img1 = cv2.imread(image_path)
    img2 = cv2.imread(image_path2)

    img_resultante = cv2.subtract(img1, img2)
    cv2.imwrite('PBM/output/subtractImagesByFps.jpg', img_resultante)

    cv2.imshow('Imagem Resultante', img_resultante)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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
    subtract_images("PBM/assets/run-frame1.png", "PBM/assets/run-frame2.png")
