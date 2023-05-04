from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("1366x768")
def my_command():
    messagebox.showinfo("hello", "see you again")
bg = PhotoImage(file = r"C:\Users\NGUYENHOAN\OneDrive\Desktop\thuc tap co so\THUC-TAP-CO-SO\picture\mainbg.png")
label1 = Label(top, image= bg)
click_btn = PhotoImage(file = r"C:\Users\NGUYENHOAN\OneDrive\Desktop\thuc tap co so\THUC-TAP-CO-SO\picture\button.png")
playBtn = Button(top, image = click_btn,command=my_command)
playBtn.place(x = 1200, y = 680)
label1.pack()
top.mainloop()