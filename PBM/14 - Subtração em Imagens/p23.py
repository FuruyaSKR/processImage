import numpy as np
import os
import cv2
from PIL import Image


def subtract_images(image_path, image_path2):
    white_image = Image.new('RGB', (500, 500), (255, 255, 255))
    white_image2 = Image.new('RGB', (500, 500), (255, 255, 255))

    existing_image = Image.open(image_path)
    existing_image2 = Image.open(image_path2)
    
    x1 = 100
    y1 = 100

    x2 = -100
    y2 = -100
    
    white_image.paste(existing_image, (x1, y1), existing_image)
    white_image2.paste(existing_image2, (x2, y2), existing_image2)

    image_np = np.array(white_image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    image_np2 = np.array(white_image2)
    image_cv2 = cv2.cvtColor(image_np2, cv2.COLOR_RGB2BGR)

    img_resultante = cv2.subtract(image_cv, image_cv2)
    cv2.imshow('Imagem Resultante', img_resultante)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('PBM/output/subtractDistinctImages.jpg', img_resultante)



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
    subtract_images("PBM/assets/run-frame1.png", "PBM/assets/brain_app.jpg")
