import pyautogui
import threading
import time
import keyboard
from tkinter import *


class AutoKeyGUI:

    def press_the_key(self):
        while True:
            pyautogui.press(self.user)
            pyautogui.press(self.userr)
            pyautogui.press(self.userrr)
            pyautogui.press(self.userrrr)


    def button_key1(self):
        self.user = self.Inputt.get()

    def button_key2(self):
        self.userr = self.Inputtt.get()

    def button_key3(self):
        self.userrr = self.Inputttt.get()
    
    def button_key4(self):
        self.userrrr = self.Inputtttt.get()

    def assign_keyone(self):
        windowk = Tk()
        windowk.geometry('250x200')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputt = Entry(windowk)
        self.Inputt.pack()
        confirminput = Button(windowk,command=self.button_key1).pack()
        
        windowk.mainloop()

    def assign_keytwo(self):
        windowk = Tk()
        windowk.geometry('250x200')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputtt = Entry(windowk)
        self.Inputtt.pack()
        confirminput = Button(windowk,command=self.button_key2).pack()
        
        windowk.mainloop()

    def assign_keytri(self):
        windowk = Tk()
        windowk.geometry('250x200')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputttt = Entry(windowk)
        self.Inputttt.pack()
        confirminput = Button(windowk,command=self.button_key3).pack()
        
        windowk.mainloop()

    def assign_keyfour(self):
        windowk = Tk()
        windowk.geometry('250x200')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputtttt = Entry(windowk)
        self.Inputtttt.pack()
        confirminput = Button(windowk,command=self.button_key4).pack()
        
        windowk.mainloop()


    def add_keys(self):
        windowk = Tk()
        windowk.geometry('250x500')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        TextLabelPRESS = Label(windowk,text='-------PRESSING KEY--------')
        TextLabelPRESS.pack()
        TextLabelPRESS.config(font=("Courier", 10))

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 1',command=self.assign_keyone)
        ButtonChoseKey1.pack()

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 2',command=self.assign_keytwo)
        ButtonChoseKey1.pack()

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 3',command=self.assign_keytri)
        ButtonChoseKey1.pack()

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 4',command=self.assign_keyfour)
        ButtonChoseKey1.pack()

        TextLabelHOLD = Label(windowk,text='-------HOLDING KEY--------')
        TextLabelHOLD.pack()
        TextLabelHOLD.config(font=("Courier", 10))

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 1',command='')
        ButtonChoseKey1.pack()

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 2',command='')
        ButtonChoseKey1.pack()

        windowk.mainloop()

    def gui(self):
        window = Tk()
        window.geometry('250x220')
        window.title('AutoPressKey')
        window.resizable(False,False)

        menubar = Menu(window)
        window.config(menu=menubar)

        filemenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=filemenu)
        #filemenu.add_separator()
        filemenu.add_command(label='Exit',command=quit)

        settingsmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Settings',menu=settingsmenu)
        settingsmenu.add_command(label='Add keys',command=self.add_keys)

        TextLabel = Label(window,text='AUTOKEY')
        TextLabel.pack()
        TextLabel.place()
        TextLabel.config(font=("Courier", 20))

        Buttonn = Button(window,text='START',width=10,command=self.press_the_key)
        Buttonn.pack()
        Buttonn.place(x=120,y=130)
        ButtonnLabel = LabelFrame(window)
        ButtonnLabel.pack()
        ButtonnLabel.place(x=120,y=165)
        ButtonnText = Label(ButtonnLabel,text='or press "/"').pack()

        window.mainloop()


GUI = AutoKeyGUI()
GUI.gui()