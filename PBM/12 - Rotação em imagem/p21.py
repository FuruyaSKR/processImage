import cv2
import os

def rotate_image(image_path):
    img = cv2.imread(image_path)

    img_rotated = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imwrite('PBM/output/Rotated180SaidaRGB.ppm', img_rotated)

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
    rotate_image("PBM/assets/EntradaRGB.ppm")
