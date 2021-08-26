from datetime import date
from datetime import datetime
from datetime import timedelta
import matplotlib
import matplotlib.pyplot as plt
#connection to database#
import mysql.connector 
db=mysql.connector.connect(host="localhost",user="mohamed",
                  password="12345",db="dd")

#executing queries#
c=db.cursor()

#Show date in table
c.execute("SELECT tdate FROM distraction3")
myresult=c.fetchall()
for i in myresult:
    for j in range(len(i)):
        print(i[j])

#c.execute("SELECT * FROM distraction3")
#myresult=c.fetchall()
#for i in myresult:
   # for j in range(len(i)):
        #print(i[j])
#print(myresult)

c.execute("select tdate, counter from distraction3")
date= []
counter=[]
for i in c:
    date.append(i[0])
    counter.append(i[1])
#dates=matplotlib.dates.date2num(date)
#print(date)
#print(counter)
dates=[]
print(date)
for x in date:
    dates.append(x.strftime('%Y - %m - %d'))
#print    
plt.bar(dates, counter, width = .1)
#plt.gcf().autofmt_xdate()
plt.show()










#remove duplicated dates in tuple (use only if needed)
#b=set()
#result=[element for element in myresult
#        if not (tuple(element) in b
#                or b.add(tuple(element)))]
#print(str(result)