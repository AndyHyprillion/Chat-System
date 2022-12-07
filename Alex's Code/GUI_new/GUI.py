#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:36:58 2021

@author: bing
"""

# import all the required  modules
import threading
import select
from tkinter import *
import tkinter.messagebox
from tkinter import font
from tkinter import ttk
from chat_utils import *
import json
import random

# GUI class for the chat


class GUI:
    # constructor method
    def __init__(self, send, recv, sm, s):
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
        self.send = send
        self.recv = recv
        self.sm = sm
        self.socket = s
        self.my_msg = ""
        self.system_msg = ""
        self.image=PhotoImage(file="pict_1.png") #改这个路径即可
        

    #加入了账号密码判断,已经实现了只有在txt中的账号密码可以登录
    def login_flag(self):
        self.login_dict={self.entry_username.get():self.entry_password.get()}
        flag=0
        f=open("login.txt","r")
        line_list=f.readlines()
        data_dict={}
        for item in line_list:
            if item[-1] == '\n':
                item = item[:-1]
            temp_list=item.split(",")
            data_dict[temp_list[0]]=temp_list[1]
        f.close()
        for keys,values in data_dict.items():
            if keys==self.entry_username.get() and values==self.entry_password.get():
                flag=1
        return flag

    def login(self):
        # login window
        self.login = Toplevel()

        ws = self.login.winfo_screenwidth()
        hs = self.login.winfo_screenheight()
        windowWidth = 800
        windowHeight = 600
        x = (ws/2) - (windowWidth/2)
        y = (hs/2) - (windowHeight/2)

        #setting window size & position
        self.login.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,x,y))#width x height + startX + startY
        self.login.attributes("-alpha", 1)

        # set the title
        self.login.title("Welcome to [Undecided Name] Chat System")
        self.login.resizable(width=True,
                             height=True)
        self.login.configure(width=800,
                             height=600)
        # create a Label
        self.welcome = Label(self.login,
                         image=self.image,
                        #  text="Please login to continue",
                         justify=CENTER,
                         font=("Trebuchet MS", 14, "bold"))

        self.welcome.place(relheight=0.6,
                        relwidth=1,
                       relx=0,
                       rely=0)
        # create a Label
        self.label_user_name = Label(self.login,
                               text="Username",
                               font=("Trebuchet MS", 12))

        self.label_user_name.place(relheight=0.05,
                             relx=0.28,
                             rely=0.65)

        # create a entry box for
        # typing the message
        self.entry_username = Entry(self.login,
                               font=("Trebuchet MS",12))

        self.entry_username.place(relwidth=0.30,
                             relheight=0.05,
                             relx=0.4,
                             rely=0.65)

        # set the focus of the curser
        self.entry_username.focus()

        #第二个label
        self.label_password = Label(self.login,
                               text="Password",
                               font=("Trebuchet MS",12))

        self.label_password.place(relheight=0.05,
                             relx=0.28,
                             rely=0.75)

        #第二个entry
        self.entry_password = Entry(self.login,
                               font=("Trebuchet MS",12),
                               show="*")

        self.entry_password.place(relwidth=0.30,
                             relheight=0.05,
                             relx=0.4,
                             rely=0.75,
                             )

        self.entry_password.focus()

        #这个是continue button
        self.go = Button(self.login,
                         text="Login",
                         font=("Trebuchet MS", 14, "bold"),
                        #  command= self.goAhead(self.entry_username.get())
                        command= self.pressLogin
                         )

        self.go.place(relx=0.25,
                      rely=0.85)

        #这个是register button
        self.register=Button(self.login,
                              text="Register",
                              font=("Trebuchet MS", 14, "bold"),
                              command=self.reg)

        self.register.place(relx=0.55,
                            rely=0.85)
        
        self.Window.mainloop()

    def pressLogin(self):
        self.goAhead(self.entry_username.get())
        print(1111)


    def reg(self):

        self.reg = Toplevel()
        
        ws = self.reg.winfo_screenwidth()
        hs = self.reg.winfo_screenheight()
        windowWidth = 400
        windowHeight = 300
        x = (ws/2) - (windowWidth/2)
        y = (hs/2) - (windowHeight/2)

        #setting window size & position
        self.reg.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,x,y))#width x height + startX + startY
        print("here")

        # create a Label
        self.label_set_username = Label(self.reg,
                               text="Username",
                               font=("Trebuchet MS", 12),
                               textvariable=self.entry_username.get())

        self.label_set_username.focus()

        self.label_set_username.place(relheight=0.1,
                             relx=0.1,
                             rely=0.1)

        # create a entry box for
        # typing the message
        set_username=tkinter.StringVar()
        self.entry_set_username = Entry(self.reg,
                               font=("Trebuchet MS",12),
                               textvariable=set_username
                               )

        self.entry_set_username.place(relwidth=0.60,
                             relheight=0.1,
                             relx=0.3,
                             rely=0.1,
                             )


        #第二个label
        self.label_set_password = Label(self.reg,
                               text="Password",
                               font=("Trebuchet MS",12))

        self.label_set_password.place(relheight=0.1,
                             relx=0.1,
                             rely=0.3)

        #第二个entry
        set_password = tkinter.StringVar()
        self.entry_set_password = Entry(self.reg,
                               font=("Trebuchet MS",12),
                               textvariable = set_password
                                        )

        self.entry_set_password.place(relwidth=0.60,
                             relheight=0.1,
                             relx=0.3,
                             rely=0.3)

        self.entry_set_password.focus()

        #第3个label
        set_confirm_password = tkinter.StringVar()
        self.label_again_password = Label(self.reg,
                               text="Confirm",
                               font=("Trebuchet MS",12),
                               textvariable=set_confirm_password
                                          )

        self.label_again_password.place(relheight=0.1,
                             relx=0.1,
                             rely=0.5)

        #第3个entry
        self.entry_again_password = Entry(self.reg,
                               font=("Trebuchet MS",12))

        self.entry_again_password.place(relwidth=0.60,
                             relheight=0.1,
                             relx=0.3,
                             rely=0.5)

        #下面的confirm button
        self.register_confirm=Button(self.reg,
                              text="Confirm",
                              font=("Trebuchet MS", 14, "bold"),
                              command=self.update_data())

        self.register_confirm.place(relx=0.45,
                                    rely=0.75)

    #奇怪的是，它更新不下去，但它仍然能在文档中打出一个逗号，看来是get entry的问题。
    def update_data(self):
        if self.entry_set_password.get()==self.entry_again_password.get():
            flag_for_username = 0
            f = open("login.txt", "r")
            line_list = f.readlines()
            data_dict = {}
            for item in line_list:
                if item[-1] == '\n':
                    item = item[:-1]
                temp_list = item.split(",")
                data_dict[temp_list[0]] = temp_list[1]
            f.close()

            # tkinter.messagebox.showinfo(title='Hi', message="你好") ，可以拿这个东西来当print用，来debug

            for keys in data_dict.keys():
                if keys == self.entry_set_username.get():
                    flag_for_username = 1

            if flag_for_username != 1:    # 我发现这个if不运行，好像是因为一开始entry没有值，这怎么办？
                f = open("login.txt", "a")
                f.write(self.entry_set_username.get() + "," + self.entry_set_password.get() + "\n")
                f.close()

            else:
                tkinter.messagebox.showerror('Error', 'Please find another username!')
        else: #这个好像也不运行
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')


    def goAhead(self, name):
        if len(name) > 0 and self.login_flag()==1:
            msg = json.dumps({"action": "login", "name": name})
            self.send(msg)
            response = json.loads(self.recv())
            if response["status"] == 'ok':
                self.login.destroy()
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(name)
                self.layout(name)
                self.textCons.config(state=NORMAL)
                # self.textCons.insert(END, "hello" +"\n\n")
                self.textCons.insert(END, menu + "\n\n")
                self.textCons.config(state=DISABLED)
                self.textCons.see(END)
                # while True:
                #     self.proc()
        # the thread to receive messages
            process = threading.Thread(target=self.proc)
            process.daemon = True
            process.start()

#----------------------------------------------------------------------

    # The main layout of the chat
    def layout(self, name):

        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,
                              height=False)
        self.Window.configure(width=470,
                              height=550,
                              bg="#17202A")
        self.labelHead = Label(self.Window,
                               bg="#17202A",
                               fg="#EAECEE",
                               text=self.name,
                               font=("Trebuchet MS", 13, "bold"),
                               pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,
                          width=450,
                          bg="#ABB2B9")

        self.line.place(relwidth=1,
                        rely=0.07,
                        relheight=0.012)

        self.textCons = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font=("Trebuchet MS", 14),
                             padx=5,
                             pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.labelBottom = Label(self.Window,
                                 bg="#ABB2B9",
                                 height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                              bg="#2C3E50",
                              fg="#EAECEE",
                              font=("Trebuchet MS", 13))

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74,
                            relheight=0.06,
                            rely=0.008,
                            relx=0.011)

        self.entryMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text="Send",
                                font=("Trebuchet MS", 10, "bold"),
                                width=20,
                                bg="#ABB2B9",
                                command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.06,
                             relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

    # function to basically start the thread for sending messages

    def sendButton(self, msg):
        # self.textCons.config(state=DISABLED)
        self.my_msg = msg
        # print(msg)
        self.entryMsg.delete(0, END)
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, msg + "\n")
        self.textCons.config(state=DISABLED)
        self.textCons.see(END)

    def proc(self):
        # print(self.msg)
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            # print(self.msg)
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                # print(self.system_msg)
                self.system_msg = self.sm.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.textCons.config(state=NORMAL)
                self.textCons.insert(END, self.system_msg + "\n\n")
                self.textCons.config(state=DISABLED)
                self.textCons.see(END)

    def run(self):
        self.login()


# create a GUI class object
if __name__ == "__main__":
    # g = GUI()
    pass
