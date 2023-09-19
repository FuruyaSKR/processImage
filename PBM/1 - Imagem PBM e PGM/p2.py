import random


def createPGMImage(width, height):
    pgmImage = []
    maxIntensity = 15
    for _ in range(height):
        row = [str(random.randint(0, maxIntensity)) for _ in range(width)]
        pgmImage.append(" ".join(row))

    with open("PBM/output/p2-example.pbm", "w") as pgm:
        pgm.write(f"P2\n{width} {height}\n{maxIntensity}\n")
        pgm.write("\n".join(pgmImage))


createPGMImage(400, 400)
