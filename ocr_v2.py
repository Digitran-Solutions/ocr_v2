# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:53:41 2021

@author: nobin
"""
import pytesseract,PIL.Image,cv2
from PIL import ImageTk
from tkinter import *
def output():
    img=cv2.imread(str(d_id.get()))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    img=cv2.medianBlur(img,5)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text=pytesseract.image_to_string(img)
    t=Text(window,bg='white',fg='black',font='Helvetica 15 bold',width=50,height=6)
    t.insert(END, text)
    t.place(x=10,y=200)
    
    
window=Tk()
window.geometry('600x420')
window.title("OCR App")
im1 = PIL.Image.open("bg1.jpeg")
im=im1.resize((600,420))
ph = ImageTk.PhotoImage(im)
background_label =Label(window, image=ph).place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text='DIGITRAN SOLUTIONS OCR APP',font='Helvetica 18 bold',bg='white').grid(row=0,column=0)
window.columnconfigure(0, weight=1)
clicked=StringVar()
d_id=StringVar()
Label(window,text='Enter the path of the document',bg='white').place(x=10,y=30)
idbox=Entry(window,textvariable = d_id, font=('calibre',10,'normal'),width=30).place(x=10,y=50)
Select=Button(window,text='Submit',bg='black',command=output,fg='white').place(x=150,y=100)
window.mainloop()