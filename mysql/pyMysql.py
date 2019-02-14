# coding=utf-8
import mysql.connector as mdb


config = {
    'host': '112.74.179.40',
    'user': 'root',
    'password': 'Jif_123_cn',
    'port': 3306,
    'database': 'mediciedb',
    'charset': 'utf8'
}
try:
    cnn = mdb.connect(**config)
    r = cnn.cursor();
    r.execute('insert into md_user(name,age,money) values(%s,%s,%s)',('Lack',25,1000))
    r.execute('select * from mD_user')
    rows = r.fetchall();

    for row in rows:

        print row[0],row[1],row[2],row[3]
    cnn.commit()
    cnn.close()
except mdb.Error,e:
    print e