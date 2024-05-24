import cv2

cap = cv2.VideoCapture('./data/cat.avi')
while True:
    ret, im = cap.read()
    if not ret:
        break

    blur = cv2.GaussianBlur(im,(25,25),5)
    #src ==im ：要进行模糊的输入图像。
    #ksize == (25,25) ：高斯核的大小。它应该是一个奇数，比如 (3, 3)、(5, 5)、(7, 7) 等。这个值决定了模糊的程度。
    #sigmaX =5 ：高斯核在 X 方向上的标准差。
    cv2.imshow('blur',blur)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()