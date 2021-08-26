from tkinter import*
from tkinter import StringVar

######################### Definations ###################################

##################### Login Window ######################################
window = Tk()
#window.geometry('300x200+600+300')
window.title('Login Form')
window.configure(bg='white'  )
window.resizable(0,0)
# Gets the requested values of the height and widht.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
window.geometry("300x200+{}+{}".format(positionRight, positionDown))

###################################For First window############################

im = PhotoImage(file='10.png')
Lbim = Label(window , image=im , width = 300 ,height = 200)
Lbim.pack(fill = 'both' , expand = True)

#this part for programing
##################################################
Var=StringVar()
username=StringVar()
password=StringVar()
######################################################
def do():
    if username.get()=='haidy' and password.get()=='777':
        Var.set("welcome to  your account")
        window.state('withdrawn')
        import window_show
        window_show.page_two()
    else:
         Var.set("invalid Password, Try again ")
#####################################################
#This part for design
##################################################
lbusername=Label(window,text='Username',bg = 'white' ,fg= 'black',
             font=('Times New Roman (Headings CS)',10,'bold')
             )
lbusername.place(x=20 , y=30)
entusername=Entry(window , bg='white',
              fg= 'black',
              state='normal',bd=3 ,
              relief = 'groove',
              font=('Times New Roman (Headings CS)',10,'bold'),
              textvariable=username
              )

entusername.place(x=100 , y=30)
###################################################
lbpass=Label(window,text='password',fg= 'black',
             bg='white',font=('Times New Roman (Headings CS)',10,'bold')
             )
lbpass.place(x=20 , y=70)
entpass=Entry(window , bg='white',
              fg= 'black',
              state='normal',bd=3 ,
              relief = 'groove',
              font=('Times New Roman (Headings CS)',10,'bold'),
              show='*',
              textvariable=password
              )
entpass.place(x=100 , y=70)
####################################################
btlogin=Button(window , text='Login',
               font=('Times New Roman (Headings CS)',10,'bold'),
               bd=1 , bg='white', fg= 'black',
               command=do
               )
btlogin.place(x=120,y=110)
#####################################################
lbinfo=Label(window , bg='white',fg= 'black',
             font=('Times New Roman (Headings CS)',10,'bold'),
             textvariable=Var
             )
lbinfo.place(x=60,y=160)



window.mainloop()