import numpy
import cv2
import os


def readFileName():
    arr = os.listdir("./originalDataset")
    cArr = []
    for i in arr:
        cArr.append("./originalDataset/" + i)
    
    print(cArr)
    return cArr

def convertNA(fileName):
    stream = open(fileName, "rb")
    bytes = bytearray(stream.read())
    numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
    img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

    blurred1 = cv2.medianBlur(img, 3)
    subbed2 = numpy.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            subbed2[i][j] =  img[i][j] - blurred1[i][j]
    return subbed2

def convertDatasetNA(fileName,i):
    path = "./dataset/"
    name = str(i) + ".jpg"

    stream = open(fileName, "rb")
    bytes = bytearray(stream.read())
    numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
    img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    cv2.imwrite(name, img)

    naImg = convertNA(name)
    cv2.imwrite(f'{path}{name}', naImg)

    os.remove("./"+name)

if __name__ == '__main__':
    arr = readFileName()
    for i in range(len(arr)):
        convertDatasetNA(arr[i], i) 
