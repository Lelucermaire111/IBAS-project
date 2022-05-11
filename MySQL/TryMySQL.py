import pymysql as mysql
mydb = mysql.connect(host = "sh-cynosdbmysql-grp-kxswlvau.sql.tencentcdb.com",
                     port = 20483,
                     user = "root",
                     passwd = "0126Lesnb",
                     database = "Project")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)