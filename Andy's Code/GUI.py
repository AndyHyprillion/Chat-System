'''
Author: AndyYe
Date: 2022-12-01 14:49:20
LastEditors: AndyYe
LastEditTime: 2022-12-01 17:08:28
FilePath: \GroupWork\GUI.py
Description: 

Copyright (c) 2022 by AndyYe, All Rights Reserved. 
'''
from tkinter import *


class chatSystem:
    def __init__(self, parent):

        #heading 1
        self.title = Label(
            parent, 
            text="ICS Chat System",
            font=("Trebuchet MS", 20, "bold"),
            bg="darkblue",
            fg = "white"
            )
        self.title.place(width=windowWidth, height=windowHeight/4,x=0,y=0)

        #button 1
        self.hello_button = Button(parent, text="Say", command=self.say_hi, justify="center",font=("Trebuchet MS", 20, "bold"),)
        self.hello_button.place(width = 400, height = 150, x = 0, y = 150)

        #button 2
        self.quit_button = Button(parent, text="Quit", fg="red", command=parent.destroy,font=("Trebuchet MS", 20, "bold"),)
        self.quit_button.place(width = 400, height = 150, x = 400, y = 150)
             

        
    def say_hi(self):
        print("Hi there")

    def destory(self):
        pass


def enter(event):
    print('Mouse Enter the Window')

def exit_(event):
    print('Mouse Leave the Window')

def button1Pressed(event):
    print('Button-1 pressed at x = % d, y = % d' % (event.x, event.y))
    mouseEffect = Canvas(root,width=500,height=500)

    mouseOval1 = mouseEffect.create_oval(100,100,300,300,
        outline="#33252f",# 边框颜色
        fill='pink',# 填充颜色
        width=4#
        )
    print(mouseOval1)
    mouseEffect.place(x=event.x, y=event.y)


def button3Pressed(event):
    print('Button-3 pressed at x = % d, y = % d' % (event.x, event.y))

def windowResize(event):
    settingWidth = windowWidth

    if settingWidth!= root.winfo_width():

        windowWidth = root.winfo_width()
        # windowHeight = root.winfo_height()




root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
windowWidth = 800
windowHeight = 600
x = (ws/2) - (windowWidth/2)
y = (hs/2) - (windowHeight/2)

#setting window size & position
root.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,x,y))#width x height + startX + startY

#window title
root.title("ICS Chat System")

root.bind('<Enter>', enter)
root.bind('<Leave>', exit_)
root.bind('<Button-1>', button1Pressed)
root.bind('<Button-3>', button3Pressed)
root.attributes("-alpha", 0.90)#window transparency
# root.bind('<Configure>', windowResize)
root.resizable(0,0)#banned user zoom the window
app = chatSystem(root)
root.mainloop()