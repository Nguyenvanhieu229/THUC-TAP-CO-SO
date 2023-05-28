from tkinter import *
import main

top = Tk()
top.geometry("1366x768")


def my_command():
    #top.destroy()
    game = main.GamePlay()
    game.play()


bg1 = PhotoImage(file=r"picture\342397817_715529440345909_3965517901682078266_n.png")
label1 = Label(top, image=bg1)
click_btn = PhotoImage(file=r"picture\342483983_974369890373765_7370958653130376131_n.png")
playBtn = Button(top, image=click_btn, command=my_command)
playBtn.place(x=1200, y=680)
label1.pack()
top.mainloop()
