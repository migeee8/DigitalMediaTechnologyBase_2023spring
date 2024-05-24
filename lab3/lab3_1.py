import cv2
import numpy as np

#从本地读取一段视频
cap=cv2.VideoCapture('./data/cat.avi')

#获取帧数，帧率以及时长
nbFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
duration =(nbFrames/fps)

print('Num.Frames = ' ,nbFrames)
print('Frame Rate = ',fps,'fps')
print('Duration = ', duration, 'sec')


