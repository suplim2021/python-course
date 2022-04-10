#GUI-mouse.py
from tkinter import * # Lib: TK Interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฏิทิน')
GUI.geometry('500x300')

def Calendar():
    pg.click(1826,1061)

B1 = Button(GUI,text='Calendar1',command=Calendar)
B1.pack(ipadx=20, ipady=10, pady=20)

def Youtube():
    webbrowser.open('https://www.youtube.com')

B2 = ttk.Button(GUI,text='Youtube',command=Youtube)
B2.pack(ipadx=20, ipady=10, pady=20)

def Google():
    webbrowser.open('https://www.google.com')

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20, ipady=10, pady=20)

GUI.mainloop()
