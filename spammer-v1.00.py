from tkinter import *
from pyautogui import *
import keyboard

pencere = Tk()
pencere.geometry('400x115')
pencere.title("Spammer v1.00")
#for i in range(250):
 #   typewrite("31", interval=0.05)
  #  press("enter")

def spamla():
    textcagir=entry.get()
    sayicagir=metin.get()
    for x in range(int(sayicagir)):
        typewrite(textcagir, interval=0.05)
        press("enter")

sabityazi2=Label(pencere)
sabityazi2.config(text='Kaç Kere Sapamlanacak:', font=("Arial",10))
sabityazi2.place(x=10, y=40)


metin=Entry(pencere)
metin.pack()
metin.place(x=200, y=40,width=35,height=22)

buton=Button(pencere)
buton.pack()
buton.place(x= 240, y=40,height=22,width=100)
buton.config(text='Spamla!', command=spamla)
keyboard.add_hotkey('ctrl+ç', spamla)
sabityazi=Label(pencere)
sabityazi.config(text='Spamlanacak Metni Giriniz:', font=("Arial",10))
sabityazi.place(x=10, y=10)
def on_text_changed(*args):
    entry_width = len(text_var.get())
    entry.config(width=entry_width)

sabityazi=Label(pencere)
sabityazi.config(text='Spamlamak İçin Ctrl+m', font=("Arial",10))
sabityazi.place(x=10, y=70)

entry = Entry(pencere)
entry.pack()
entry.place(x=215,y=10)

text_var = StringVar()
entry['textvariable'] = text_var

text_var.trace('w', on_text_changed)
pencere.grab_release()
mainloop()
