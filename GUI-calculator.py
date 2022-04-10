# GUI-calculator.py

from tkinter import *
from tkinter import ttk, messagebox
from turtle import width

GUI = Tk() # T ใหญ่ k เล็ก
GUI.title('โปรแกรมคำนวณหาพื้นที่')
GUI.geometry('600x520')

LM = Label(GUI,text='โปรแกรมคำนวณหาพื้นที่', font=('Sarabun',14))
LM.pack()

bg = PhotoImage(file='construction.png')
BG = Label(GUI, image=bg)
BG.pack()

L1 = Label(GUI,text='ความกว้าง (เมตร)', font=('Sarabun',14))
L1.pack()

width_v = StringVar() #ตัวแปรเก็บความกว้าง
E1 = ttk.Entry(GUI, textvariable=width_v, font=('Sarabun',12))
E1.pack()

L2 = Label(GUI,text='ความยาว (เมตร)', font=('Sarabun',14))
L2.pack()

length_v = StringVar() #ตัวแปรเก็บความยาว
E2 = ttk.Entry(GUI, textvariable=length_v, font=('Sarabun',12))
E2.pack()

def Cal():
    try: # คำนวณ
        width = float(width_v.get())
        length = float(length_v.get())
        calc = width * length # กว้าง * ยาว
        messagebox.showinfo('ผลลัพธ์','มีพื้นที่ {} ตารางเมตร'.format(calc))
        width_v.set('') # ล้างค่าช่อง width_v
        length_v.set('') # ล้างค่าช่อง length_v
        E1.focus() # โฟกัสที่ช่องสำหรับกรอกข้อความช่องแรก
    except: # ผิดพลาด
        messagebox.showinfo('ผิดพลาด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        width_v.set('') # ล้างค่าช่อง width_v
        length_v.set('') # ล้างค่าช่อง length_v
        E1.focus() # โฟกัสที่ช่องสำหรับกรอกข้อความช่องแรก
          
B = ttk.Button(GUI, text='คำนวณ', command=Cal) #เมื่อกดปุ่ม ใช้ Cal
B.pack(ipadx=10,ipady=10) # padx 10, pady 10

GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา
