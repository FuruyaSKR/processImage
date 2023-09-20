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


def separate_colors_min(image_path):
    image = cv2.imread(image_path)

    b, g, r = cv2.split(image)

    img_r = cv2.merge((r, g * 0, b * 0))
    img_g = cv2.merge((r * 0, g, b * 0))
    img_b = cv2.merge((r * 0, g * 0, b))

    status_img_r = cv2.imwrite(
        "PBM/output/ImagemR_min.ppm", img_r, [cv2.IMWRITE_PXM_BINARY, 0]
    )
    status_img_g = cv2.imwrite(
        "PBM/output/ImagemG_min.ppm", img_g, [cv2.IMWRITE_PXM_BINARY, 0]
    )
    status_img_b = cv2.imwrite(
        "PBM/output/ImagemB_min.ppm", img_b, [cv2.IMWRITE_PXM_BINARY, 0]
    )

    print(
        "Status das imagens gravadas no sistema: ",
        status_img_r,
        status_img_g,
        status_img_b,
    )


if __name__ == "__main__":
    remove_files("PBM/output/")
    separate_colors_min("PBM/assets/Fig4.ppm")
