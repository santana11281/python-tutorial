import os
import imageio


def getSpecific(fileType, array):
    newArr = []
    for item in array:
        if fileType in item:
            newArr.append(item)
    return newArr


def convertAll(array):
    for item in array:
        img = imageio.imread(item)
        imageio.imwrite(f'{item[0:-3]}.ico', img)


convertAll(getSpecific("png", os.listdir()))
