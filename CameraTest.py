import cv2
from PIL import Image
from Barcode import scancode

cam = cv2.VideoCapture(3)
cam.set(3,1920)
cam.set(4,1080)
i = 0
while(cam.isOpened()):
    ret,frame = cam.read()
    cv2.imshow('VideoTest', frame)
    #img = Image.fromarray(frame[0:int(frame.shape[0]),0:int(frame.shape[1])])  # 完成np.array向PIL.Image格式的转换
    barcode = -1
    #if i == 0:
    cv2.imwrite('test.jpg',frame)
    barcode = scancode.ISBNScan('./test.jpg')
    # if cv2.waitKey(1) == ord("q"):
    #     break
    if barcode != -1 or cv2.waitKey(1) == ord("q"):
        break
