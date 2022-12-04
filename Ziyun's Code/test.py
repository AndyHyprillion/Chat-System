# import time      
# from tkinter import*
# tk=Tk()                                                         #建立一个框架对象tk
# canvas=Canvas(tk,width=500,height=500) #建立一个画布对象canvas，属于tk对象
# canvas.pack()                                               #将画布对象更新显示在框架中
# canvas.create_polygon(10,10,10,60,50,35) 

# #建立多边形，顶点坐标（x1,y1,x2,y2,x3,y3），属于canvas对象，

# #默认图形编号为1，用于函数调用，以后的图形编号顺序类推。
# for i in range(0,60):                 #建立一个60次的循环 ，循环区间[0,59）
#     canvas.move(1,5,0)              #canvas对象中的编号“1”图形调用移动函数，x轴5个像素点，y轴不变
#     tk.update()                           #更新框架，强制显示改变
#     time.sleep(0.05)                   #睡眠0.05秒，制造帧与帧间的间隔时间
# for i in range(0,60):                                                   
#     canvas.move(1,0,5)
#     tk.update()
#     time.sleep(0.05)
# for i in range(0,60):
#     canvas.move(1,-5,0)
#     tk.update()
#     time.sleep(0.05)
# for i in range(0,60):
#     canvas.move(1,0,-5)
#     tk.update()
#     time.sleep(0.05)

# !/usr/bin/env python
# coding:utf-8
# python3.3
import tkinter as tk
#import tkFileDialog 
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)
class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.attributes("-transparentcolor","blue")
        self.attributes("-topmost",1)
        self.attributes("-alpha", 0.5)
#        self.label = tk.Label(self, text="Click on the grip to move")
#        self.grip = tk.Label(self, bitmap="gray25")
#        self.grip.pack(side="left", fill="y")
#        self.label.pack(side="right", fill="both", expand=True)
        self.canvas = tk.Canvas(self, width=300, height=200)
        #self.canvas.pack(side="bottom",fill="both",expand=True)
        self.canvas.create_rectangle(0, 0, 300, 200, fill="blue")
        self.canvas.create_text(50,10,text='tkinter',font=("Fixdsys",15,"bold"),fill="yellow")
        self.canvas.grid(column=0,row=0)
        self.canvas.bind("<ButtonPress-1>", self.StartMove)
        self.canvas.bind("<ButtonRelease-1>", self.StopMove)
        self.canvas.bind("<B1-Motion>", self.OnMotion)
    def StartMove(self, event):
        self.x = event.x
        self.y = event.y
    def StopMove(self, event):
        self.x = None
        self.y = None
    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))
 
if __name__=="__main__":
     
    app=App()
    app.mainloop()