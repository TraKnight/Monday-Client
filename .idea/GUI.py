from tkinter import *


#GUI Object
class Window(Frame):

    def __init__(self,master):
        #Window config
        self.master=master
        master.title('Monday Update Client')
        master.geometry('500x600')
        master.iconbitmap('img/cloud.ico')

        #create menubar
        menubar = Menu(self.master)
        master.config(menu=menubar)
        file_menu=Menu(menubar,tearoff=False)
        profile_menu=Menu(menubar,tearoff=False)

        #add menu item
        menubar.add_cascade(
            label="Menu",
            menu=file_menu,
            underline=0
        )

        #Frame widgets config /start
        default=""
        text = Label(master,height=3, width=70, text="Monday Update Client", font='android 15 bold',wraplength=500, justify="center")
        title = Label(master, text="Status Update Station",fg='#0f5b9e',font='android 20 bold')
        boardName = Label(master, text="Connected to: "+default+"",fg='#00b200',font='android 10 bold')
        titleOrder = Label(master, text="ORDER NUMBER:",fg='#0f5b9e',font='android 20 bold')
        titleColumn = Label(master, text="COLUMN:",fg='#0f5b9e',font='android 20 bold')
        titleStatus = Label(master, text="STATUS",fg='#0f5b9e',font='android 20 bold')
        enterButton= Button(master, text="Update")
        setVariables= Button(master,text="Change Boards")
        version= Label(master, text="Version 2",fg='#0f5b9e',font='android 8')
        #sub menu items
        file_menu.add_command(label='Monday.com')
        file_menu.add_command(label='Create New Board')
        file_menu.add_command(label='Change Board',command=self.submenu)
        file_menu.add_command(label='Refresh')
        file_menu.add_command(label='Close')


        #Text entry widgets Vars
        self.orderUI= Entry(master, width=25, borderwidth=2, validate="key")
        self.columnUI= Entry(master,width=25,borderwidth=2, validate="key")
        self.statusUI= Entry(master,width=25,borderwidth=2,validate="key")

        #UI widgets pack
        title.pack(pady=20)
        boardName.pack(pady=5)
        titleOrder.pack()
        self.orderUI.pack(pady=12)
        titleColumn.pack()
        self.columnUI.pack(pady=12)
        titleStatus.pack()
        self.statusUI.pack(pady=12)
        enterButton.pack(pady=12)
        setVariables.pack(pady=12)
        version.pack(pady=10,side=BOTTOM)

        #Frame widgets format config /end

        master.mainloop()


    #Sub Menu items
    def submenu(self):
        global getApi
        global getBoard
        windowSub=Toplevel(self.master)
        windowSub.geometry('300x300')
        windowSub.resizable(False,False)
        windowSub.iconbitmap('img/cloud.ico')
        windowSub.title("MSUS Configure")
        #set default value for board config
        defaultBoardValue=StringVar(windowSub)
        #default config api
        defaultApiValue=StringVar(windowSub)
        apiLabel = Label(windowSub, text="API Key",fg='#0f5b9e',font='android 10 bold')
        boardLabel = Label(windowSub, text="Board Number",fg='#0f5b9e',font='android 10 bold')
        enterButton= Button(windowSub, text="Update")
        apiText= Entry(windowSub, width=25, borderwidth=2, textvariable=defaultApiValue,show="*")
        boardText= Entry(windowSub, width=25, borderwidth=2, textvariable=defaultBoardValue)
        apiLabel.pack(pady=15)
        apiText.pack(pady=10)
        boardLabel.pack(pady=15)
        boardText.pack(pady=10)
        enterButton.pack(pady=10)
        windowSub.grab_set()
        lbl=Label(windowSub,text="")
        lbl.pack()
        getApi=apiText
        getBoard=boardText
        windowSub.mainloop()










root= Tk()
Start=Window(root)
Start.__init__(Start,a)
