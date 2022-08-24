import pyautogui
import threading
import time
import keyboard
from tkinter import *


class AutoKeyGUI:

    def pressing(self,key):
        while True:
            pyautogui.press(key)
            if keyboard.is_pressed('/'):
                break
    
    def holding(self,key):
        while True:
            pyautogui.keyDown(key)

            if keyboard.is_pressed('/'):
                    pyautogui.keyUp(key)
                    break

    def activate_the_key(self):
        if self.keyone_pressed == True:
            t1= threading.Thread(target=self.pressing,args=(self.user),)
            t1.start()

        if self.keytwo_pressed == True:
            t2 = threading.Thread(target=self.pressing,args=(self.userr),)
            t2.start()

        if self.keythree_pressed == True:
            t3 = threading.Thread(target=self.pressing,args=(self.userrr),)
            t3.start()
       
        if self.keyone_hold == True:
            t1h = threading.Thread(target=self.holding,args=(self.userh),)
            t1h.start()

        if self.keytwo_hold == True:
            t2h = threading.Thread(target=self.holding,args=(self.userrhh),)
            t2h.start()
        

        #t1= threading.Thread(target=self.pressing,args=(self.user),)
        #t2 = threading.Thread(target=self.pressing,args=(self.userr),)
        #t3 = threading.Thread(target=self.pressing,args=(self.userrr),)
        #t1h = threading.Thread(target=self.activate_the_key,args=(self.userh),)
        #t1h.start()
        #t1.start()
        #t2.start()
        #t3.start()
        #t1.join()
        #t2.join()
        #t3.join()
        pass


    def button_key1(self):
        self.user = self.Inputt.get()
        self.keyone_pressed = True


    def button_key2(self):
        self.userr = self.Inputtt.get()
        self.keytwo_pressed = True

    def button_key3(self):
        self.userrr = self.Inputttt.get()
        self.keythree_pressed = True

    def button_key1hold(self):
        self.userh = self.Inputh.get()
        self.keyone_hold = True

    def button_key2hold(self):
        self.userrhh = self.Inputthh.get()
        self.keytwo_hold = True

    def assign_keyonehold(self):
        windowk = Tk()
        windowk.geometry('200x150')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputh = Entry(windowk,width=5)
        self.Inputh.pack()
        confirminput = Button(windowk,text='ASSERT',command=self.button_key1hold).pack()

        Example = Label(windowk,text='for example:').pack()
        Examples = Label(windowk,text='space q w r leftctrl enter').pack()

    def assign_keytwohold(self):
        windowk = Tk()
        windowk.geometry('200x150')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputthh = Entry(windowk,width=5)
        self.Inputthh.pack()
        confirminput = Button(windowk,text='ASSERT',command=self.button_key2hold).pack()

        Example = Label(windowk,text='for example:').pack()
        Examples = Label(windowk,text='space q w r leftctrl enter').pack()

    def assign_keyone(self):
        windowk = Tk()
        windowk.geometry('200x150')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputt = Entry(windowk,width=10)
        self.Inputt.pack()
        confirminput = Button(windowk,text='ASSERT',command=self.button_key1).pack()

        Example = Label(windowk,text='for example:').pack()
        Examples = Label(windowk,text='space q w r leftctrl enter').pack()
        
        windowk.mainloop()

    def assign_keytwo(self):
        windowk = Tk()
        windowk.geometry('200x150')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputtt = Entry(windowk,width=1)
        self.Inputtt.pack()
        confirminput = Button(windowk,text='ASSERT',command=self.button_key2).pack()

        Example = Label(windowk,text='for example:').pack()
        Examples = Label(windowk,text='space q w r leftctrl enter').pack()
        
        windowk.mainloop()

    def assign_keytri(self):
        windowk = Tk()
        windowk.geometry('200x150')
        windowk.title('Add keys')
        windowk.resizable(False,False)

        self.Inputttt = Entry(windowk,width=1)
        self.Inputttt.pack()
        confirminput = Button(windowk,text='ASSERT',command=self.button_key3).pack()

        Example = Label(windowk,text='for example:').pack()
        Examples = Label(windowk,text='space q w r leftctrl enter').pack()
        
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


        TextLabelHOLD = Label(windowk,text='-------HOLDING KEY--------')
        TextLabelHOLD.pack()
        TextLabelHOLD.config(font=("Courier", 10))

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 1',command=self.assign_keyonehold)
        ButtonChoseKey1.pack()

        ButtonChoseKey1 = Button(windowk,text='Click to assign the key 2',command=self.assign_keytwohold)
        ButtonChoseKey1.pack()


        windowk.mainloop()

    def gui(self):

        self.keyone_pressed = False
        self.keytwo_pressed = False
        self.keythree_pressed = False
        self.keyone_hold = False
        self.keytwo_hold = False

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
        TextLabel.config(font=("Courier", 30))

        Buttonn = Button(window,text='START',width=15,command=self.activate_the_key,height=2)
        Buttonn.pack()
        Buttonn.place(x=101,y=110)
        ButtonnLabel = LabelFrame(window)
        ButtonnLabel.pack()
        ButtonnLabel.place(x=100,y=165)
        ButtonnText = Label(ButtonnLabel,text='to turn off hold "/"').pack()

        window.mainloop()

if __name__ == '__main__':
    GUI = AutoKeyGUI()
    GUI.gui()