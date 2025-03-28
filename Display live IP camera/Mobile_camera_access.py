import urllib.request
import cv2
import numpy as np
import imutils

url='http://192.0.0.4:8080/shot.jpg'
while True:
    imgpath=urllib.request.urlopen(url)
    imgnp=np.array(bytearray (imgpath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    img=imutils.resize(img,width=800)
    cv2.imshow("CameraFeed",img)
    if ord('q')==cv2.waitKey(1):
        exit(0)