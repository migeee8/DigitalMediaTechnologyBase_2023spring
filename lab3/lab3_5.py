import cv2

# 打开视频文件
cap = cv2.VideoCapture('./data/carflow.mp4')

# 读取第一帧
ret, frame1 = cap.read()

# 对第一帧进行灰度转换和高斯模糊
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

# 开始循环
while True:
    # 读取下一帧
    ret, frame2 = cap.read()

    # 判断是否到达视频末尾
    if not ret:
        break

    # 对当前帧进行灰度转换和高斯模糊
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # 计算当前帧与前一帧的差异
    diff = cv2.absdiff(gray1, gray2)

    # 对差异图像进行二值化处理
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # 去除二值图像中的噪声
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.erode(thresh, None, iterations=2)

    # 在原始帧上绘制前景的轮廓
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 创建一个窗口，大小为640x480
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640, 480)
    cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('thresh', 640, 480)

    # 显示原始帧和分析结果
    cv2.imshow('frame', frame2)
    cv2.imshow('thresh', thresh)

    # 更新前一帧
    gray1 = gray2.copy()

    # 按下 q 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频文件句柄和窗口
cap.release()
cv2.destroyAllWindows()
