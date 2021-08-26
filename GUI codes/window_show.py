from tkinter import *


def page_two():
    
    windowStart = Toplevel()
    windowStart.geometry("800x420+0+0")
    windowStart.title('start Form')
    windowStart.configure(bg='white')
    
#########################For Second window#############################
#this part for programing
##################################################
    def startDriving() :
        windowStart.destroy()
        import start_window
        start_window.page_three()

    def startShow() :
        windowStart.destroy()
        import Graph
        Graph.page_five()
######################################################
#This part for design
##################################################

    #imageFile ='24.jpg'
    #im = ImageTk.PhotoImage(Image.open(imageFile))
    im = PhotoImage(file="29.png")
    Lbim = Label(windowStart, image=im ,bg ='white')
    Lbim.pack()

    ####################################################
    btstart=Button(windowStart , text='Start',
                   width =30, height =3,
                   font=('Times New Roman (Headings CS)',10,'bold'),
                   bd=3 , bg='#BC3733',
                   activebackground = '#BC3733',
                   command = startDriving
                   )
    btstart.place(relx= 0.06,rely=0.8)
    ####################################################
    btshow=Button(windowStart , text='Show',
                  width=30, height=3,
                  font=('Times New Roman (Headings CS)',10,'bold'),
                  bd=3 , bg='#CC434C',
                  activebackground='#CC434C',
                  command = startShow )
    btshow.place(relx= 0.55,rely=0.8)



    windowStart.mainloop()
    
page_two()