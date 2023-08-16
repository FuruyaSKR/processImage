import random


def randomPixelColor():
    return f"{random.randint(0, 255)} {random.randint(0, 255)} {random.randint(0, 255)}"


def createPPMImage(fileName, width, height):
    with open(f"PBM/output/{fileName}", "w") as ppm:
        ppm.write(f"P3\n{width} {height}\n255\n")

        for _ in range(height):
            row = " ".join([randomPixelColor() for _ in range(width)])
            ppm.write(row + "\n")


createPPMImage("p3-example_400x400.ppm", 400, 400)
createPPMImage("p3-example_1000x1000.ppm", 1000, 1000)
