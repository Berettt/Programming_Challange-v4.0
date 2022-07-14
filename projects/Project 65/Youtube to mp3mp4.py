from pytube import YouTube
from tkinter import *

window = Tk()
window.title('Youtube convert')
window.geometry("300x150")
window.resizable(False,False)

def MainWindow():
    def mp():
        UserInput = EntryText.get()
        if UserInput == 'mp3' or UserInput == 'MP3':
            mp3()
        if UserInput == 'mp4' or UserInput == 'MP4':
            mp4()
        
    def mp4():
        def mp4convert():
            mp4Input = mp4Entry.get()
            link = YouTube(mp4Input)
            link.streams.get_highest_resolution().download()
        mp4window = Tk()
        mp4window.resizable(False,False)
        mp4window.geometry('350x100')
        mp4window.title('mp4 yt download')
        mp4TextLabel = Label(mp4window,text='Paste the youtube url and click start',font=(10)).pack()
        mp4Entry = Entry(mp4window,width=50)
        mp4Entry.pack()
        mp4Entry.place(x=24,y=30)
        mp4button = Button(mp4window,text='Download',command=mp4convert)
        mp4button.pack()
        mp4button.place(x=150,y=60)

        mp4window.mainloop()
    def mp3():
        def mp3convert():
            mp3Input = mp3Entry.get()
            link = YouTube(mp3Input)
            mptri = link.streams.filter(only_audio=True).first()
            mptri.download()
        mp3window = Tk()
        mp3window.resizable(False,False)
        mp3window.geometry('350x100')
        mp3window.title('mp3 yt download')
        mp3TextLabel = Label(mp3window,text='Paste the youtube url and click start',font=(10)).pack()
        mp3Entry = Entry(mp3window,width=50)
        mp3Entry.pack()
        mp3Entry.place(x=24,y=30)
        mp3button = Button(mp3window,text='Download',command=mp3convert)
        mp3button.pack()
        mp3button.place(x=150,y=60)

        mp3window.mainloop()
    WelcomeLabel = Label(window,text='Youtube to mp3/mp4',font=(30))
    WelcomeLabel.pack()
    WelcomeLabel.place(x=60,y=10)
    TextLabel = Label(window,text='Download mp3 or mp4?')
    TextLabel.pack()
    TextLabel.place(x=85,y=50)
    EntryText = Entry(window,width=4)
    EntryText.pack()
    EntryText.place(x=140,y=80)
    Submit = Button(window,text='Next->',command=mp)
    Submit.pack()
    Submit.place(x=129,y=110)
    

MainWindow()

window.mainloop()

