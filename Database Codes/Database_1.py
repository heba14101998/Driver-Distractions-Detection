#sudo apt update
#sudo apt upgrade
#sudo apt install mariadb-server
#sudo mysql_secure_installation
#all y
#sudo mysql -u root -p
#CREATE DATABASE dd;
#CREATE USER 'mohamed'@'localhost' IDENTIFIED BY '12345';
#GRANT ALL PRIVILEGES ON *.* TO 'mohamed'@'localhost';
#FLUSH PRIVILEGES
#pip3 install mysql-connector-python
###################

from datetime import date
from datetime import datetime
from datetime import timedelta
#connection to database#
import mysql.connector 
db=mysql.connector.connect(host="localhost",user="mohamed",
                  password="12345",db="dd")

#executing queries#
c=db.cursor()

#show databases

#c.execute("SHOW DATABASES")
#myresult=c.fetchall()
#for i in myresult:
#    print(i)

#create table one time then remove

#c.execute("CREATE TABLE distraction (tdate DATE , ttime TIME , Total_counter int , safe_driving int, texting_right int,talking_on_the_phone_right int,texting_left int, talking_on_the_phone_left int, operating_the_radio int,drinking int, reaching_behind int, hair_and_makeup int, talking_to_passenger int)")

#check if table is created terminal
#mysql -u mohamed -p
#password : 12345
#USE dd;
#SHOW TABLES;

#INSERT INTO TABLE
#today = date.today()
#now = datetime.now()
#t1= now.strftime("%H:%M:%S")
#distraction_Type ="sleeping"
#count=2
#sql="INSERT INTO distraction3 (tdate , ttime , type , counter , var_counter) VALUES (%s , %s, %s , %s , %s)"
#data=(today , t1, distraction_Type , count  )
#c.execute(sql,data)
#db.commit()

#show contents of table
#c.execute("SELECT * FROM distraction3")
#myresult=c.fetchall()
#print(myresult)

#show one only
#myresult=c.fetchone()    only 1 
#print(myresult[0])     specific

#show time in table
#c.execute("SELECT ttime FROM distraction3")
#myresult=c.fetchall()
#for i in myresult:
#    for j in range(len(i)):
#        print(i[j])  

#show specific columns which share the same date
#c.execute("SELECT type FROM distraction3 WHERE tdate='2021-6-28'")
#myresult=c.fetchall()
#for i in myresult:
#   print(i)

#user manual input
#sql="SELECT * FROM distraction3 WHERE tdate=%s"
#data=('2021-6-29',)
#c.execute(sql , data)
#result=c.fetchall()
#for i in result:
#    for j in range(len(i)):
#        print(i[j])
        
#fetch similar name
#c.execute("SELECT * FROM distraction3 WHERE date like %2021-6-28%")







# DON'T USE 
#delete
#c.execute("DELETE distraction3 WHERE n='name'")

