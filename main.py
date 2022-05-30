from ASR import asr_test
from Request import Request
from ASS import audiotestpy
from Barcode import scancode
from MySQL import MySQL
import pyttsx3
import audioapi
import pymysql as mysql
import cv2
import VoiceRecord
from pydub import AudioSegment
from pydub.playback import play
from OCR import ocr_test

# 定义播放wav文件函数
def soundplay(path):
    sound = AudioSegment.from_wav(path)
    play(sound)

mode = 0
mydb = mysql.connect(host = "sh-cynosdbmysql-grp-kxswlvau.sql.tencentcdb.com",
                     port = 20483,
                     user = "root",
                     passwd = "2022abcd!",
                     database = "IBAS")
mycursor = mydb.cursor()
##读取语音
while(True):
    end = 0
    while(True):
        VoiceRecord.my_record()
        result = asr_test.asr()
        if(result == '你好。'):
            soundplay("sound/begin.wav")
            break
        elif(result == '再见。'):
            end = 1
        else:
            continue
    if(end == 1):
        break
    while(True):
        VoiceRecord.my_record()
        result = asr_test.asr()
        if(result == "阅读模式。"):
            mode = 1
            break
        elif(result == "文档模式。"):
            mode = 2
            break
        elif(result == "看图说话。"):
            mode = 3
            break
        else:
            continue
    if(mode == 1):
        cam = cv2.VideoCapture(0)
        cam.set(3,1920)
        cam.set(4,1080)
        i = 0

        hint = AudioSegment.from_wav('sound/hint_bookcode.wav')
        play(hint)

        while(cam.isOpened()):
            ret,frame = cam.read()
            cv2.imshow('VideoTest', frame)
            #img = Image.fromarray(frame[0:int(frame.shape[0]),0:int(frame.shape[1])])  # 完成np.array向PIL.Image格式的转换
            ISBN = -1
            #if i == 0:
            cv2.imwrite('test.jpg',frame)
            ISBN = scancode.ISBNScan('./test.jpg')
            # if cv2.waitKey(1) == ord("q"):
            #     break
            if ISBN != -1 or cv2.waitKey(1) == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()

        #register(user_id, user_pwd)
        user_id = 1
        user_pwd = '123456'
        registerStatus , str = MySQL.register(user_id,user_pwd,mycursor)

        if(registerStatus == 1):
            #用户登录成功
            image_path = 'test.jpg'
            #ISBN = scancode.ISBNScan(image_path)
            name,author = MySQL.searchISBN(ISBN,mycursor)
            if name == -1:
                soundplay("sound/db_nobook.wav")
                print("目前系统数据库中暂无该书目")
            else:
                audioapi.audioplay_nobook("您当前阅读的书目为："+name+"。作者为："+author)
                soundplay("sound/result.wav")
                MySQL.uploadbook(user_id,name,mycursor)
                mydb.commit()
                while (True):
                    VoiceRecord.my_record()
                    result = asr_test.asr()
                    if (result == '开始阅读。'):
                        soundplay("sound/begin.wav")
                        cam = cv2.VideoCapture(0)
                        cam.set(3, 1920)
                        cam.set(4, 1080)
                        while (cam.isOpened()):
                            ret, frame = cam.read()
                            cv2.imshow('VideoTest', frame)
                            cv2.imwrite('test.jpg', frame)
                            break
                        cam.release()
                        cv2.destroyAllWindows()
                        ocr_test.mainOCR('test.jpg')
                        audioapi.audioplay()
                        continue
                    elif(result == '退出。'):
                        break
                    else:
                        continue
                #print(0)
            # engine = pyttsx3.init()
            # engine.say("您当前阅读的书目为："+name)
            # engine.runAndWait()
            # print(author)
            # engine.say("作者为："+author)
            # engine.runAndWait()
        elif(registerStatus == -1):
            #不存在此用户ID
            sound = AudioSegment.from_wav('sound/no_user.wav')
            play(sound)
        else:
            #密码错误
            sound = AudioSegment.from_wav('sound/passwd_error.wav')
            play(sound)

    elif(mode == 2):
        print()
    elif(mode == 3):
        cam = cv2.VideoCapture(0)
        cam.set(3, 1920)
        cam.set(4, 1080)
        while(cam.isOpened()):
            ret,frame = cam.read()
            cv2.imshow('VideoTest', frame)
            cv2.imwrite('scene.jpg',frame)
            result = Request.post('D:\IBAS project\scene.jpg')
            engine = pyttsx3.init()
            engine.say(result)
            engine.runAndWait()
        cam.release()
        cv2.destroyAllWindows()

