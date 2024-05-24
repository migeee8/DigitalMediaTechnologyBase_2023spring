import cv2
import numpy as np

#将视频读取到 NumPy 数组中
cap = cv2.VideoCapture("./data/dog.mp4")
wid = int(cap.get(3))#CV_CAP_PROP_FRAME_WIDTH
hei = int(cap.get(4))#CV_CAP_PROP_FRAME_HEIGHT
framerate = int(cap.get(5))#cv2.CAP_PROP_FPS
framenum = int(cap.get(7))#cv2.CAP_PROP_FRAME_COUNT
video = np.zeros((framenum,hei,wid,3),dtype='float16')
cnt = 0
while(cap.isOpened()):
    a, b = cap.read()
    if a:
        cv2.imshow('%d'%cnt, b)
        cv2.waitKey(20)
        b = b.astype('float16')/255
        video[cnt]=b
        cnt += 1
    else:
        break
