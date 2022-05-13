import pymysql as mysql
from Barcode import scancode
mydb = mysql.connect(host = "sh-cynosdbmysql-grp-kxswlvau.sql.tencentcdb.com",
                     port = 20483,
                     user = "root",
                     passwd = "2022abcd!",
                     database = "IBAS")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


def register(user_id, user_passwd):
    mycursor.execute(("SELECT user_pwd FROM user_tbl WHERE user_id = %d" %user_id))
    pwd = -1
    for x in mycursor:
        pwd = x
    if(pwd == -1):
        print("不存在此用户id")
        return
    if(pwd == user_passwd):
        print("登陆成功")
    else:
        print("密码错误")

# register(1,'123456')

def searchISBN():
    ISBN = scancode.ISBNScan()
    mycursor.execute("SELECT name,author,memo FROM booklibrary WHERE isbn=%s LIMIT 1 OFFSET 0" %ISBN)
    i = 0
    for x in mycursor:
        i = i + 1
        name = x[0]
        author = x[1]
        memo = x[2]

    if i == 0:
        return -1
    else:
        return name,author,memo

name,author,memo = searchISBN()
print(name,author,memo)
