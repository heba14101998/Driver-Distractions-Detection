from tkinter import *
from tkinter import ttk,Button
from tkinter import StringVar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from pandas import DataFrame


####################### For Database #############
from datetime import date
from datetime import datetime
from datetime import timedelta
import mysql.connector

Classes = [ 'safe driving', ' texting - right', 'talking on the phone - right',
       'texting - left', 'talking on the phone - left', 'operating the radio',
       'drinking', 'reaching behind', 'hair and makeup', 'talking to passenger']



def page_five():
    windowGr = Tk()
    windowGr.title('Driving Form')
    windowGr.configure(bg='white')
    windowGr.geometry("800x420+0+0")
    
    
    global Classes


   

####################################################
##################################For Graphic window ###############################################

###############################################
    def exittt():
        
        windowGr.destroy()

    
    def goStart():
        windowGr.destroy()
        import window_show
        window_show.page_two()
    
    
    ####################################################
    
    ntb = ttk.Notebook(windowGr,width=1000, height=1000
                      )
    ntb.pack()
    fm1 = Frame(ntb, width=1000,
                height=1000,bg='white',
                bd = 1,relief = 'flat'
                )
    fm2 = Frame(ntb,width=1000,
                height=1000,bg='white',
                bd = 1,relief = 'flat'
                )
    fm3 = Frame(ntb,width=1000,
                height=1000,bg='white',
                bd = 1,relief = 'flat'
                )
    
    
    ntb.add(fm1,text='Distruction per day')
    ntb.add(fm2,text='Type of distruction today ')
    ntb.add(fm3,text='Driving Rate')


    #######################################################
    btstart = Button(windowGr,text='Go to start',
                     width=10,height=2,
                     font=('Times New Roman (Headings CS)',10,'bold'),
                     bd=3,bg='white',
                     activebackground='white',
                     command=goStart
                     )
    btstart.place(relx=0.84,rely=0.74)
    
    ######################################################
    btex = Button(windowGr,text='Exit',
                     width=10,height=2,
                     font=('Times New Roman (Headings CS)',10,'bold'),
                     bd=3,bg='white',
                     activebackground='white',
                     command=exittt
                     )
    btex.place(relx=0.84,rely=0.87)
    
    
    #############################################
    ###################Execute data from database###########################

    # connection to database#

    db = mysql.connector.connect(host="localhost", user="mohamed",
                                 password="12345", db="dd")

    # executing queries#
    c = db.cursor()
    today = date.today()
    

    # Show date in table
    ########################################################
    c.execute("select tdate, Total_counter from distraction")
    myresult=c.fetchall()
    dates = []
    counter = []
    z = 0 
    for i in myresult:
        dates.append(i[0])
        counter.append(i[1])
      
    print(dates)
    day =[]
    for x in dates:
        day.append(x.strftime('%Y - %m - %d'))
    
    import collections

    #dates = ['2021-7-7', '2021-7-7', '2021-7-7', '2021-7-7', '2021-7-8', '2021-7-8', '2021-7-8']
    #counter = [7, 5, 3, 9, 4, 6, 8]

    dic = collections.Counter(day)

    x = 0
    dic_2 = dic
    # print(dic)
    for key, value in dic.items():
        dic_2[key] = 0
        for i in range(value):
            dic_2[key] += counter[x]
            x += 1

    print(dic_2)

    fig = plt.Figure(figsize=(6, 4))
    a = fig.add_subplot(111)
    a.bar(dic_2.keys(), dic_2.values(), width=.1, color='#00ADEF')
    a.set_title("Distraction per Day", fontsize=16)
    a.set_ylabel("Total distraction", fontsize=14)
    a.set_xlabel("Day", fontsize=14)
    #a.set_xticklabels(a.get_xticks(), rotation=45)

    a = plt.gca()
    plt.gcf().autofmt_xdate(rotation=30)
    # stepsize = 2592000 # 30 days
    # stepsize = 864000 # 10 days
    stepsize = 86400  # 1 day
    # stepsize = 3600 # 1 hour
    start, end = a.get_xlim()
    a.xaxis.set_ticks(np.arange((end - end % 3600), start, -stepsize))

    def timestamp(x, pos):
        return (datetime.datetime.fromtimestamp(x)).strftime('%Y-%m-%d')
        # return (datetime.datetime.fromtimestamp(x)).strftime('%m/%d %H:%M')

    a.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(timestamp))
    # plt.bar(day, counter, width = .1)
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, master=fm1)
    canvas.get_tk_widget().pack()
    canvas.draw()    
    ''''
    print(str(day))
    fig = plt.Figure(figsize=(6, 4))
    a = fig.add_subplot(111)
    a.bar(day, counter, width = .1 ,color='#00ADEF')
    a.set_title("Distraction per Day", fontsize=16)
    a.set_ylabel("Total distraction", fontsize=14)
    a.set_xlabel("Day", fontsize=14)
    a.set_xticklabels(a.get_xticks(), rotation = 45)
    #plt.bar(day, counter, width = .1)
    #plt.show()

    canvas = FigureCanvasTkAgg(fig, master=fm1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    '''''
    ####################################################
    
    x = "SELECT  texting_right ,talking_on_the_phone_right ,texting_left , talking_on_the_phone_left , operating_the_radio ,drinking , reaching_behind , hair_and_makeup , talking_to_passenger  From distraction WHERE tdate = %s"
    y=(today,)
    c.execute(x,y)
    myresult=c.fetchall()
    texting_right=0
    talking_on_the_phone_right =0
    texting_left =0
    talking_on_the_phone_left =0
    operating_the_radio=0
    drinking =0
    reaching_behind=0
    hair_and_makeup =0
    talking_to_passenger =0

    Counter = []
    for i in myresult :
        texting_right += i[0]
        talking_on_the_phone_right += i[1]
        texting_left += i[2]
        talking_on_the_phone_left += i[3]
        operating_the_radio += i[4]
        drinking += i[5]
        reaching_behind += i[6]
        hair_and_makeup += i[7]
        talking_to_passenger += i[8]
            
    Counter = [texting_right,
                talking_on_the_phone_right ,
                texting_left,
                talking_on_the_phone_left ,
                operating_the_radio,
                drinking ,
                reaching_behind,
                hair_and_makeup ,
                talking_to_passenger]
    
    tree = ttk.Treeview(fm2, column=("c1", "c2"), show='headings')

    tree.column("#1", anchor=CENTER)

    tree.heading("#1", text="Type Of Distraction")

    tree.column("#2", anchor=CENTER)

    tree.heading("#2", text=" Counter")
    
    for i in range(min(len(Classes),len(Counter))):
        #write data
        tree.insert('', i, values=(Classes[i], Counter[i]))

    tree.pack()
    #########################################
    
    
    x="SELECT  Total_counter,safe_driving From distraction WHERE tdate = %s"
    y=(today,)
    c.execute(x,y)
    myresult=c.fetchall()
    
    Total_counter = 0
    safe_driving = 0
    for i in myresult:
        Total_counter +=i[0]
        safe_driving  +=i[1]
    
    labels = 'Safe Driving ', 'Distraction'
    sizes = [safe_driving, Total_counter]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvas = FigureCanvasTkAgg(fig1, master=fm3)
    canvas.get_tk_widget().pack()
    canvas.draw()
#######################################################    
    windowGr.mainloop()
    #########################################################
    
