#DOWNLOAD_MANAGER
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
import requests
import os
import time

okno = Tk()
okno.geometry('450x220')
okno.title('Download Manager')
okno.resizable(False,False)
okno.config(bg='black')

Err = False
url = None

def UrlScript():
    UrlInput = UrlENTRY.get()
    global url
    url = UrlInput

    if Err is True:
     error = tkinter.messagebox.showwarning(title='error',message='An error occured')

    if Err is False:

        if url[-4:] == '.pdf':
            
            pdf = url
            request = requests.get(pdf, stream = True)
            with open("download-manager.pdf","wb") as i:
                for x in request.iter_content(chunk_size=1024):
                     if x:
                        i.write(x)

            time.sleep(1.5)
            info = Label(okno,text='Download pdf success!',font=(20),fg='red',bg='black')
            info.pack()
            info.place(x=120,y=180)
            
            
        else:
            pic = url
            request = requests.get(pic)
            
            with open('download-manager.jpg','wb') as i:
                i.write(request.content)
            
            time.sleep(1)
            
            info = Label(okno,text='Download picture success!',font=(20),fg='red',bg='black')
            info.pack()
            info.place(x=110,y=180)
            

            


UrlLabel = LabelFrame(okno,bg='#4B4747')
UrlLabel.pack()
UrlLabel.place(x=50,y=20,width=350,height=50)
UrlText = Label(UrlLabel,text='Url: ',font=(10),bg='#4B4747',fg='white')
UrlText.pack()
UrlText.place(x=5,y=8)
UrlENTRY = Entry(UrlLabel,width=40)
UrlENTRY.pack()
UrlENTRY.place(x=45,y=13)
UrlButton = Button(UrlLabel,text='GO',bg='black',fg='white',command=UrlScript)
UrlButton.pack()
UrlButton.place(x=300,y=10)

ProgressFrame = LabelFrame(okno,bg='#4B4747')
ProgressFrame.pack()
ProgressFrame.place(x=75,y=80,width=300,height=100)
DownloadInfo = Label(ProgressFrame,text='Feel free to download simple ',font=(15),fg='white',bg='#4B4747').pack()
DownloadInfo2 = Label(ProgressFrame,text='pictures and large files ',font=(15),fg='white',bg='#4B4747').pack()
DownloadInfo3 = Label(ProgressFrame,text=' such as pdf',font=(15),fg='white',bg='#4B4747').pack()

okno.mainloop()