import cv2
import os, numpy, PIL
from PIL import Image

DATADIR = 'data'
DATAPATH = os.getcwd() +"\\" +DATADIR
INPUT = 'vid3.mp4'
OUTPUT = 'average3.png'

def extractFrames(pathIn, pathOut):

    os.mkdir(pathOut)
    cap = cv2.VideoCapture(pathIn)
    count = 0

    print("Reading Frames")
    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret == True:
            # print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def generateAverage():

    allfiles=os.listdir(DATAPATH)
    imlist=[(DATAPATH + "\\" + filename) for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]

    w,h=Image.open( imlist[0] ).size
    N=len(imlist)

    arr=numpy.zeros((h,w,3),numpy.float)

    print("Calculating Average")
    for im in imlist:
        imarr=numpy.array(Image.open(im),dtype=numpy.float)
        arr=arr+imarr/N

    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    out=Image.fromarray(arr,mode="RGB")
    out.save(OUTPUT)


if __name__=="__main__":
    extractFrames(INPUT, DATADIR)
    generateAverage()
