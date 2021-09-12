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
        self.master.mainloop()

        #add menu item
        menubar.add_cascade(
            label="Menu",
            menu=file_menu,
            underline=0
        )







a= Tk()
Start=Window
Start.__init__(a)