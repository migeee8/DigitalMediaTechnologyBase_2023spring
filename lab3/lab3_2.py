import cv2

cap = cv2.VideoCapture('./data/cat.avi')
while True:
    ret, im = cap.read()
    cv2.imshow('video test', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('vid_result.jpg',im)
cap.release()
cv2.destroyAllWindows()