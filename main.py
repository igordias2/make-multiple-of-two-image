import os,sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = 999345200


def checkAndAdjustImage(img, name):
    xMF = img.size[0] % 4
    yMF = img.size[1] % 4
    if xMF != 0 or yMF != 0:
        x = img.size[0] - xMF
        y = img.size[1] - yMF
        print(x,y)
        nSize = (x, y)
        out = img.resize(nSize)
        out.save(name + "_ajustado.jpg")


def main():
    entries = os.listdir('./')
    for entry in entries:
        splitedEntry = entry.split('.')
        if splitedEntry[1] == "png" or splitedEntry[1] == "jpg":
            i = Image.open(entry)
            checkAndAdjustImage(i, splitedEntry[0])

main()