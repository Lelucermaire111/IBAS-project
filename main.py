from ASR import asr_test
from ASS import audiotestpy
from Barcode import scancode

from MySQL import MySQL
import pyttsx3
import pymysql as mysql
mydb = mysql.connect(host = "sh-cynosdbmysql-grp-kxswlvau.sql.tencentcdb.com",
                     port = 20483,
                     user = "root",
                     passwd = "2022abcd!",
                     database = "IBAS")
mycursor = mydb.cursor()
#register(user_id, user_pwd)
registerStatus , str = MySQL.register(1,'123456',mycursor)
if(registerStatus == 1):
    image_path = 'bookback.jpg'
    ISBN = scancode.ISBNScan(image_path)
    name,author = MySQL.searchISBN(ISBN,mycursor)
    engine = pyttsx3.init()
    engine.say("您当前阅读的书目为："+name)
    engine.runAndWait()
    print(author)
    engine.say("作者为："+author)
    engine.runAndWait()


