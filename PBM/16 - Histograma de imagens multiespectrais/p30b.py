import matplotlib.pyplot as plt
import os
import cv2

def histogram_equalization(image_path):
    img = cv2.imread(image_path)
    r, g, b = cv2.split(img)

    r_eq = cv2.equalizeHist(r)
    g_eq = cv2.equalizeHist(g)
    b_eq = cv2.equalizeHist(b)

    img_eq = cv2.merge((r_eq, g_eq, b_eq))
    channels = [r_eq, g_eq, b_eq]
    colors=['red', 'blue', 'green']
    
    cv2.imwrite('PBM/output/Fig2.ppm', img_eq)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, channel in enumerate(channels):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        axs[i].plot(hist, color=colors[i])
        axs[i].set_xlim([0, 256])
        axs[i].set_xlabel('Intensidade de pixel')
        axs[i].set_ylabel('Número de pixels')
        axs[i].set_title(f'Histograma do canal {colors[i]}')

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
    histogram_equalization("PBM/assets/Fig2.ppm")

