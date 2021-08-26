from datetime import date
from datetime import datetime
from datetime import timedelta
#connection to database#
import mysql.connector 
db=mysql.connector.connect(host="localhost",user="mohamed",
                  password="12345",db="dd")

#executing queries#
c=db.cursor()

#SHOW DATABASES#
#c.execute("SHOW DATABASES")
#myresult=c.fetchall()
#for i in myresult:
#    print(i)
    
#INSERT a distraction INTO TABLE
#today = date.today()
#now = datetime.now()
#t1= now.strftime("%H:%M:%S")
#a="holding phone"                         #distraction type string
#sql="INSERT INTO distraction (tdate , ttime , type) VALUES (%s , %s, %s)"
#data=(today , t1, a )
#c.execute(sql,data)
#db.commit()


#Show date in table
#c.execute("SELECT tdate FROM distraction")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])  

#show time in table
#c.execute("SELECT ttime FROM distraction")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])

#show types in table
#c.execute("SELECT type FROM distraction")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])
        
#count all distractions
#c.execute("SELECT COUNT('type') FROM distraction")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])

#count specific type of distraction
#c.execute("SELECT COUNT(*) FROM distraction WHERE type='drinking'")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])


#count specific type at specific date
#c.execute("SELECT COUNT(*) FROM distraction WHERE type='holding phone' AND tdate='2021-07-05'")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])