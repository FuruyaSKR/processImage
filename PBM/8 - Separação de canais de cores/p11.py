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


def separate_colors_max(image_path):
    image = cv2.imread(image_path)

    b, g, r = cv2.split(image)

    img_r = cv2.merge((r, g * 255, b * 255))
    img_g = cv2.merge((r * 255, g, b * 255))
    img_b = cv2.merge((r * 255, g * 255, b))

    status_img_r = cv2.imwrite(
        "PBM/output/Imagem4_max.ppm", img_r, [cv2.IMWRITE_PXM_BINARY, 0]
    )
    status_img_g = cv2.imwrite(
        "PBM/output/Imagem5_max.ppm", img_g, [cv2.IMWRITE_PXM_BINARY, 0]
    )
    status_img_b = cv2.imwrite(
        "PBM/output/Imagem6_max.ppm", img_b, [cv2.IMWRITE_PXM_BINARY, 0]
    )

    print(
        "Status das imagens gravadas no sistema: ",
        status_img_r,
        status_img_g,
        status_img_b,
    )


if __name__ == "__main__":
    remove_files("PBM/output/")
    separate_colors_max("PBM/assets/Fig4.ppm")
