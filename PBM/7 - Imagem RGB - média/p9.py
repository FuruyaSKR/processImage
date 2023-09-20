import cv2
import os


def remove_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Erro ao remover {file_path}: {e}")


def calculate_average_rgb(image_path):
    image = cv2.imread(image_path)

    height = image.shape[0]
    width = image.shape[1]
    b, g, r = cv2.split(image)

    for y in range(height):
        for x in range(width):
            average = int((int(b[y][x]) + int(g[y][x]) + int(r[y][x])) / 3)
            b[y][x] = average
            g[y][x] = average
            r[y][x] = average

    new_image = cv2.merge((b, g, r))

    status_new_image = cv2.imwrite(
        "PBM/output/Fig4_average_rgb.ppm", new_image, [cv2.IMWRITE_PXM_BINARY, 0]
    )

    print("Status da Imagem gravada no sistema: ", status_new_image)


if __name__ == "__main__":
    remove_files("PBM/output/")
    calculate_average_rgb("PBM/assets/Fig4.ppm")
