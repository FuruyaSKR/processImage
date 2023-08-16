import random


def createPBMImage(width, height):
    pbmImage = []
    for _ in range(height):
        row = ["1" if random.random() > 0.5 else "0" for _ in range(width)]
        pbmImage.append(" ".join(row))

    with open("PBM/output/p1-example.pbm", "w") as pbm:
        pbm.write(f"P1\n{width} {height}\n")
        pbm.write("\n".join(pbmImage))


createPBMImage(400, 400)
