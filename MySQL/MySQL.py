import pymysql as mysql
import re
import string

#利用正则表达式去除返回内容的标点符号
remove_chars = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~+]'

# mydb = mysql.connect(host = "sh-cynosdbmysql-grp-kxswlvau.sql.tencentcdb.com",
#                      port = 20483,
#                      user = "root",
#                      passwd = "2022abcd!",
#                      database = "IBAS")

#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#   print(x)


def register(user_id, user_passwd, mycursor):
    mycursor.execute(("SELECT user_pwd FROM user_tbl WHERE user_id = %d" %user_id))
    pwd = -1
    for x in mycursor:
        pwd = x[0]
    print(pwd)
    if(pwd == -1):
        print("不存在此用户id")
        str = "不存在此用户id"
        return -1,str
    if(pwd == user_passwd):
        print("登录成功")
        str = "登录成功"
        return 1,str
    else:
        print("密码错误")
        str = "密码错误"
        return 0,str

# register(1,'123456')

def searchISBN(ISBN, mycursor):
    mycursor.execute("SELECT name,author,memo FROM booklibrary WHERE isbn=%s LIMIT 1 OFFSET 0" %ISBN)
    i = 0
    for x in mycursor:
        i = i + 1
        name = x[0]
        author = x[1]
        memo = x[2]
    if i == 0:
        return -1,-1
    else:
        name1 = re.sub(remove_chars," ",name)
        author1 = re.sub(remove_chars," ",author)
        return name1,author1

def uploadbook(user_id, book_name, mycursor):
    mycursor.execute(("SELECT read_time FROM book_tbl WHERE user_id = '{}' AND book_name = '{}'" .format(user_id,book_name)))
    read_time = -1
    for x in mycursor:
        read_time = x[0]
    print(read_time)
    if(read_time == -1):
        mycursor.execute("INSERT INTO book_tbl(user_id,book_name,read_time) values('{}','{}','{}')" .format(user_id,book_name,0))
    return read_time

