from tkinter import *



class Window():
    def __init__(self):
        self.master=self
        self.master.title('Monday Update Client')
        self.master.geometry('500x600')
        self.master.iconbitmap('img/OIP .ico')

        #Window frame widgets format config
        #create menubar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        file_menu=Menu(menubar,tearoff=False)


        #add menu item
        menubar.add_cascade(
            label="Menu",
            menu=file_menu,
            underline=0
        )
        default="Connect to a board"
        self.text = Label(self.master,height=3, width=70, text="", font='android 15 bold',wraplength=500, justify="center")
        title = Label(self.master, text="Status Update Station",fg='#0f5b9e',font='android 20 bold')
        self.boardName = Label(self.master, text="Connected to: """,fg='#00b200',font='android 10 bold')
        titleOrder = Label(self.master, text="ORDER NUMBER:",fg='#0f5b9e',font='android 20 bold')
        titleColumn = Label(self.master, text="COLUMN:",fg='#0f5b9e',font='android 20 bold')
        titleStatus = Label(self.master, text="STATUS",fg='#0f5b9e',font='android 20 bold')
        enterButton= Button(self.master, text="Update")
        setVariables= Button(self.master,text="Change Boards")
        version= Label(self.master, text="Version 2",fg='#0f5b9e',font='android 8')

        #sub menu items
        file_menu.add_command(label='Monday.com')
        file_menu.add_command(label='Create New Board')
        file_menu.add_command(label='Change Board')
        file_menu.add_command(label='Refresh')
        file_menu.add_command(label='Exit')

        #Text entry widgets UI config Main
        self.orderUI= Entry(self.master, width=25, borderwidth=2, validate="key")
        self.columnUI= Entry(self.master,width=25,borderwidth=2, validate="key")
        self.statusUI= Entry(self.master,width=25,borderwidth=2,validate="key")

        #UI widgets pack
        title.pack(pady=20)
        self.boardName.pack(pady=5)
        titleOrder.pack()
        self.orderUI.pack(pady=12)
        titleColumn.pack()
        self.columnUI.pack(pady=12)
        titleStatus.pack()
        self.statusUI.pack(pady=12)
        enterButton.pack(pady=12)
        setVariables.pack(pady=12)
        version.pack(pady=10,side=BOTTOM)
        self.master.mainloop()







a= Tk()
Start=Window
Start.__init__(a)