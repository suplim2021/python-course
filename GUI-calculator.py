# GUI-calculator.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() # T ใหญ่ k เล็ก
GUI.title('โปรแกรมคำนวณพื้นที่')
GUI.geometry('700x600')

LM = Label(GUI,text='ปรแกรมคำนวณพื้นที่', font=('Sarabun',14))
LM.pack()

bg = PhotoImage(file='construction.png')
#GUI.pack(padx=20, pady=20)

BG = Label(GUI, image=bg)
BG.pack()


L1 = Label(GUI,text='กรอกความกว้าง (เมตร)', font=('Sarabun',14))
L1.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=('Sarabun',12))
E1.pack()

L2 = Label(GUI,text='กรอกความยาว (เมตร)', font=('Sarabun',14))
L2.pack()

v2_quantity = StringVar()
E2 = ttk.Entry(GUI, textvariable=v2_quantity, font=('Sarabun',12))
E2.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        f1 = quan
        quan = float(v2_quantity.get())
        f2 = quan
        calc = f1 * f2
        messagebox.showinfo('ผลลัพธ์','มีพื้นที่ {} เมตร'.format(calc))
        E1.focus()
    except:
        messagebox.showinfo('ผิดพลาด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('')
        v2_quantity.set('')
        E1.focus()
          
B = ttk.Button(GUI, text='คำนวณ', command=Cal)
B.pack(ipadx=10,ipady=10)

GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา
