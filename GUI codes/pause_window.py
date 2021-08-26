from tkinter import *
#from PIL import Image, ImageTk

def page_four():
    ##################### continue Window ######################################

    window_pause = Toplevel()
    window_pause.geometry("800x420+0+0")
    window_pause.title('Driving Form')
    window_pause.configure(bg='#F7F7F7')
    
    ##################################################


    ### for pause & Continue button
    # statVar = StringVar(value="Pause")
    def continuevideo():
        window_pause.destroy()
        import start_window
        start_window.page_three()



    def startShow_3():
        window_pause.destroy()  # destroy
        import Graph
        Graph.page_five()

    ##################################For continue window ###############################################

    ##############################################
    #imageFile ='Pause.jpeg'
    #im = ImageTk.PhotoImage(Image.open(imageFile))
    im = PhotoImage(file="28.png")
    Lbim = Label(window_pause, image=im , bg = 'white' ,bd=0 )
    Lbim.pack()
    ###########################################
    btcont = Button(window_pause,
                    width=30, height=3,
                    text='Continue',
                    font=('Times New Roman (Headings CS)', 10, 'bold'),
                    bd=3, bg='#00ADEF',
                    foreground='black',
                    activebackground='#00ADEF',
                    command=continuevideo
                    )
    btcont.place(relx=0.06, rely=0.8)

    ####################################################
    btStop2 = Button(window_pause, text='Stop',
                     width=30, height=3,
                     font=('Times New Roman (Headings CS)', 10, 'bold'),
                     bd=3, bg='#00ADEF',
                     activebackground='#00ADEF',
                     command=startShow_3)
    btStop2.place(relx=0.55, rely=0.8)
    window_pause.mainloop()
