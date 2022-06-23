import cv2
cam = cv2.VideoCapture(2)
cam.set(3,1920)
cam.set(4,1080)
i = 0
while (cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('VideoTest', frame)
    # img = Image.fromarray(frame[0:int(frame.shape[0]),0:int(frame.shape[1])])  # 完成np.array向PIL.Image格式的转换
    ISBN = -1
    # if i == 0:

    # if cv2.waitKey(1) == ord("q"):
    #     break
    if cv2.waitKey(1) == ord("a"):
        cv2.imwrite('Img/test'+str(i)+'.jpg', frame)
        i = i + 1