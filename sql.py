import csv
import MySQLdb

#todo: change date to datetime, implement sql.py in data_pipe.py, remove unwanted empty spaces from csv, check how bad sent databases were


db = MySQLdb.connect(host="localhost",user="root", passwd="pazzzword99iot",db="less_friction_db")

cur = db.cursor()

create_table = "CREATE TABLE IF NOT EXISTS customer2_data (Region VARCHAR(25), Kontakter SMALLINT,Varavnya_kontakter SMALLINT,Varav_kontakter_storkund SMALLINT,Varav_kontakter_prio SMALLINT,Besok SMALLINT,Telemoten SMALLINT,Webmoten SMALLINT,Bokn_besok SMALLINT,Bokn_telemoten SMALLINT, Bokn_webmoten SMALLINT,Offerter SMALLINT,Inringda_avtal SMALLINT,Seminarieavtal SMALLINT, Eget_avtal SMALLINT,Mailat_avtal SMALLINT,Partneravtal SMALLINT,Premier SMALLINT,Date VARCHAR(25))"

cur.execute(create_table)
db.commit()

with open("j4362q - sep 11.csv") as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(type(row))
        #print(row)
        #row[1:len(row)-1] = [int(item) for item in row[1:len(row)-1]]
        print(row)
        cur.execute("INSERT INTO customer2_data VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,%s,%s, %s, %s, %s)", row)
db.commit()

db.close()


"""
with open("clean_data/j4362q - sep 11.csv") as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
"""

#lista = ['ciao','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','gatto']
#tupla = tuple(lista)
#cur.execute("INSERT INTO customer1_data VALUES('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s', '%s')", lista)

#execute (" INSERT INTO anooog1 VALUES ('%s','%s') ", (188,90))



