# -------importing required libraries---------

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
import time
from time import strftime
import sys
import math
import random
from tkinter import messagebox
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465


# ................................................................Entry box Variables.........................................................
class billing_r:
    def __init__(self, root):
        self.root = root
        self, root.configure(bg="red")
        self.root.title("Billing Software System")
        # self.root.geometry("1100x680+0+0")
        self.root.maxsize(width=1100, height=680)
        self.root.minsize(width=1100, height=680)

        # ...........................................................Customer Detail Variables........................................................
        self.CustomerName = StringVar()
        self.CustomerNumber = StringVar()

        self.BillingNumber = StringVar()
        x = random.randint(1000, 9999)
        self.BillingNumber.set(str(x))
        # .................................................................Snacks Variables..........................................................
        self.Samosa = IntVar()
        self.Springroll = IntVar()
        self.Burger = IntVar()
        self.Noodles = IntVar()
        self.Sandwitch = IntVar()
        self.PaneerPakoda = IntVar()
        self.MixPakoda = IntVar()
        self.Tikkichart = IntVar()
        self.DahiBhale = IntVar()
        # ................................................................Foods Variables....................................
        self.Paratha = IntVar()
        self.CholeChawal = IntVar()
        self.RajmaChawal = IntVar()
        self.Bhatoore = IntVar()
        self.Khadichawal = IntVar()
        self.Shahipaneer = IntVar()
        self.Biryani = IntVar()
        self.DumAloo = IntVar()
        self.FullThali = IntVar()
        # .................................................................Cold drink Variables.........................................
        self.Coca = IntVar()
        self.Limca = IntVar()
        self.Fanta = IntVar()
        self.Maza = IntVar()
        self.Pepsi = IntVar()
        self.Frooti = IntVar()
        self.Sprite = IntVar()
        self.up77 = IntVar()
        self.Mirinda = IntVar()
        # .................................................................Billing Menu Variables...............................................................
        self.snacksprice = StringVar()
        self.Foodprice = StringVar()
        self.coldrinkprice = StringVar()
        self.snackstax = StringVar()
        self.foodtax = StringVar()
        self.coldrinktext = StringVar()
        # .................................................................End Entry box Variables....................................................
        # .........................................Heading Frame......................................................................................
        T_frame = Frame(self.root, bd=10, relief=RIDGE, bg="midnight blue")
        T_frame.place(x=0, y=0, width=1349, height=100)
        I_lb1 = Label(T_frame, text=f"{dt.datetime.now():%a, %b %d %Y}", font=("times new roman", 15, "bold"),
                      bg='midnight blue', fg='white', bd=0).place(x=20, y=7)

        def clock():
            G_time = time.strftime("%H:%M:%S")
            clock_lb3.config(text=G_time)
            clock_lb3.after(1000, clock)

        clock_lb3 = Label(T_frame, font=("times new roman", 17, "bold"), bg='midnight blue', fg='white', bd=0)
        clock_lb3.place(x=950, y=7)
        clock()
        # ..............................................................................................................................................
        I_lb2 = Label(T_frame, text="RESTAURANT MENU", font=("times new roman", 20, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=420, y=4)
        # ..........................................Main Frame............................................................................
        M_frame = Frame(self.root, bd=10, relief=RIDGE, bg="midnight blue")
        M_frame.place(x=10, y=70, width=1080, height=605)
        # ...........................................Detail Frame.....................................................................................................
        D_frame = Frame(self.root, bd=10, relief=RIDGE, bg="midnight blue")
        D_frame.place(x=25, y=80, width=1050, height=100)

        I_lb3 = Label(D_frame, text="Customer_detail", font=("times new roman", 15, "bold"), bg='midnight blue',
                      fg='blue', bd=0).place(x=360, y=4)

        I_lb4 = Label(D_frame, text="Customer Name :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=10, y=40)
        self.CN = Entry(D_frame, textvariable=self.CustomerName, font=("times new roman", 15), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.CN.place(x=150, y=37, width=130, height=25)

        I_lb4 = Label(D_frame, text="Customer Contact :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=300, y=40)
        self.CC = Entry(D_frame, textvariable=self.CustomerNumber, font=("times new roman", 15), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.CC.place(x=450, y=35, width=130, height=25)

        I_lb4 = Label(D_frame, text="BiLL No. :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=600, y=40)
        self.BN = Entry(D_frame, textvariable=self.BillingNumber, font=("times new roman", 15), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.BN.place(x=690, y=35, width=130, height=25)

        self.btn_search = Button(D_frame, text="Search", command=self.search, font=("times new roman", 17), bg="blue",
                                 activebackground='midnight blue', fg="white", activeforeground='white', cursor='hand2')
        self.btn_search.place(x=860, y=30, width=120, height=30)

        # ........................................................Snacks Frame...................................................................
        M1_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="midnight blue")
        M1_frame.place(x=10, y=100, width=260, height=350)

        s_lb1 = Label(M1_frame, text="Snacks", font=("times new roman", 15, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=80, y=4)

        s_lb2 = Label(M1_frame, text="Samosha :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=40)
        self.S = Entry(M1_frame, textvariable=self.Samosa, font=("times new roman", 10), bg="#ECECEC", bd=5,
                       relief=GROOVE)
        self.S.place(x=130, y=40, width=100, height=25)

        s_lb3 = Label(M1_frame, text="Springroll:", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=70)
        self.Sp = Entry(M1_frame, textvariable=self.Springroll, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.Sp.place(x=130, y=70, width=100, height=25)

        s_lb3 = Label(M1_frame, text="Burger :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=100)
        self.BG = Entry(M1_frame, textvariable=self.Burger, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.BG.place(x=130, y=100, width=100, height=25)

        s_lb4 = Label(M1_frame, text="Noodles :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=130)
        self.Nd = Entry(M1_frame, textvariable=self.Noodles, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.Nd.place(x=130, y=130, width=100, height=25)

        s_lb5 = Label(M1_frame, text="Sandwitch :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white',
                      bd=0).place(x=2, y=160)
        self.SW = Entry(M1_frame, textvariable=self.Sandwitch, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.SW.place(x=130, y=160, width=100, height=25)

        s_lb6 = Label(M1_frame, text="Paneer Pakoda :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=190)
        self.PP = Entry(M1_frame, textvariable=self.PaneerPakoda, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.PP.place(x=130, y=190, width=100, height=25)

        s_lb7 = Label(M1_frame, text="Mix Pakoda :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=220)
        self.MP = Entry(M1_frame, textvariable=self.MixPakoda, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.MP.place(x=130, y=220, width=100, height=25)

        s_lb8 = Label(M1_frame, text="Tikki chart :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=250)
        self.TC = Entry(M1_frame, textvariable=self.Tikkichart, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.TC.place(x=130, y=250, width=100, height=25)

        s_lb9 = Label(M1_frame, text="Dahi bhale :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=280)
        self.DB = Entry(M1_frame, textvariable=self.DahiBhale, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.DB.place(x=130, y=280, width=100, height=25)
        # ............................................................................Foods.........................................................
        M2_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="midnight blue")
        M2_frame.place(x=270, y=100, width=260, height=350)

        s_lb1 = Label(M2_frame, text="Foods", font=("times new roman", 15, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=80, y=4)

        s_lb2 = Label(M2_frame, text="Paratha :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=40)
        self.PRT = Entry(M2_frame, textvariable=self.Paratha, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.PRT.place(x=130, y=40, width=100, height=25)

        s_lb3 = Label(M2_frame, text="Chole-chawal:", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=70)
        self.CChawal = Entry(M2_frame, textvariable=self.CholeChawal, font=("times new roman", 10), bg="#ECECEC", bd=5,
                             relief=GROOVE)
        self.CChawal.place(x=130, y=70, width=100, height=25)

        s_lb3 = Label(M2_frame, text="Rajma-chawal :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=100)
        self.RC = Entry(M2_frame, textvariable=self.RajmaChawal, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.RC.place(x=130, y=100, width=100, height=25)

        s_lb4 = Label(M2_frame, text="Bhatoore :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=130)
        self.BTR = Entry(M2_frame, textvariable=self.Bhatoore, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.BTR.place(x=130, y=130, width=100, height=25)

        s_lb5 = Label(M2_frame, text="Khadi-chawal :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=160)
        self.KC = Entry(M2_frame, textvariable=self.Khadichawal, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.KC.place(x=130, y=160, width=100, height=25)

        s_lb6 = Label(M2_frame, text="Shahi-Paneer :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=190)
        self.SHP = Entry(M2_frame, textvariable=self.Shahipaneer, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.SHP.place(x=130, y=190, width=100, height=25)

        s_lb7 = Label(M2_frame, text="Biryani :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=220)
        self.BRY = Entry(M2_frame, textvariable=self.Biryani, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.BRY.place(x=130, y=220, width=100, height=25)

        s_lb8 = Label(M2_frame, text="Dum Aloo :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=250)
        self.DA = Entry(M2_frame, textvariable=self.DumAloo, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.DA.place(x=130, y=250, width=100, height=25)

        s_lb9 = Label(M2_frame, text="Full-Thali :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=280)
        self.FT = Entry(M2_frame, textvariable=self.FullThali, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.FT.place(x=130, y=280, width=100, height=25)
        # ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, Cold Drink,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        M3_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="midnight blue")
        M3_frame.place(x=530, y=100, width=260, height=350)

        s_lb1 = Label(M3_frame, text="Cold Drink", font=("times new roman", 15, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=80, y=4)

        s_lb2 = Label(M3_frame, text="Coca-cola :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=40)
        self.COC = Entry(M3_frame, textvariable=self.Coca, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.COC.place(x=130, y=40, width=100, height=25)

        s_lb3 = Label(M3_frame, text="Limca:", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=70)
        self.LC = Entry(M3_frame, textvariable=self.Limca, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.LC.place(x=130, y=70, width=100, height=25)

        s_lb3 = Label(M3_frame, text="Fanta :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=100)
        self.FN = Entry(M3_frame, textvariable=self.Fanta, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.FN.place(x=130, y=100, width=100, height=25)

        s_lb4 = Label(M3_frame, text="Maza :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=130)
        self.MZ = Entry(M3_frame, textvariable=self.Maza, font=("times new roman", 10), bg="#ECECEC", bd=5,
                        relief=GROOVE)
        self.MZ.place(x=130, y=130, width=100, height=25)

        s_lb5 = Label(M3_frame, text="Pepsi :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=160)
        self.Psi = Entry(M3_frame, textvariable=self.Pepsi, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.Psi.place(x=130, y=160, width=100, height=25)

        s_lb6 = Label(M3_frame, text="Frooti :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=190)
        self.FOO = Entry(M3_frame, textvariable=self.Frooti, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.FOO.place(x=130, y=190, width=100, height=25)

        s_lb7 = Label(M3_frame, text="Sprite :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=220)
        self.Spri = Entry(M3_frame, textvariable=self.Sprite, font=("times new roman", 10), bg="#ECECEC", bd=5,
                          relief=GROOVE)
        self.Spri.place(x=130, y=220, width=100, height=25)

        s_lb8 = Label(M3_frame, text="7UP :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=250)
        self.up7 = Entry(M3_frame, textvariable=self.up77, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.up7.place(x=130, y=250, width=100, height=25)

        s_lb9 = Label(M3_frame, text="Mirinda :", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=2, y=280)
        self.Miri = Entry(M3_frame, textvariable=self.Mirinda, font=("times new roman", 10), bg="#ECECEC", bd=5,
                          relief=GROOVE)
        self.Miri.place(x=130, y=280, width=100, height=25)

        # ....................................................................Billing Area..................................................................
        M4_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="white")
        M4_frame.place(x=790, y=100, width=260, height=388)

        T_bill = Label(M4_frame, text="Billing Area", font=("times new roman", 15, "bold"), bg="white", fg='black',
                       bd=5)
        T_bill.place(x=20, y=0, width=200, height=20)

        self.Textarea = Text(M4_frame, font=("times new roman", 8, "bold"), height=320, width=150, bd=5)
        self.Textarea.place(x=0, y=20)

        # ....................................................................Billing Menu...................................................................
        M5_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="midnight blue")
        M5_frame.place(x=10, y=450, width=550, height=135)

        s_lb1 = Label(M5_frame, text="Billing Menu", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=260, y=0)

        snacks_price = Label(M5_frame, text="Snacks Price :", font=("times new roman", 13, "bold"), bg='midnight blue',
                             fg='white', bd=0).place(x=2, y=25)
        self.spr = Entry(M5_frame, textvariable=self.snacksprice, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.spr.place(x=150, y=25, width=100, height=25)

        s_lb3 = Label(M5_frame, text="Foods Price:", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=55)
        self.FOP = Entry(M5_frame, textvariable=self.Foodprice, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.FOP.place(x=150, y=55, width=100, height=25)

        s_lb3 = Label(M5_frame, text="Cold-drink Price:", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=2, y=85)
        self.CDP = Entry(M5_frame, textvariable=self.coldrinkprice, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.CDP.place(x=150, y=85, width=100, height=25)

        s_lb2 = Label(M5_frame, text="Snacks Tax :", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=270, y=25)
        self.SNT = Entry(M5_frame, textvariable=self.snackstax, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.SNT.place(x=410, y=25, width=100, height=25)

        s_lb3 = Label(M5_frame, text="Foods Tax:", font=("times new roman", 13, "bold"), bg='midnight blue', fg='white',
                      bd=0).place(x=270, y=55)
        self.FOT = Entry(M5_frame, textvariable=self.foodtax, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.FOT.place(x=410, y=55, width=100, height=25)

        s_lb3 = Label(M5_frame, text="Cold-drink Tax:", font=("times new roman", 13, "bold"), bg='midnight blue',
                      fg='white', bd=0).place(x=270, y=85)
        self.CDT = Entry(M5_frame, textvariable=self.coldrinktext, font=("times new roman", 10), bg="#ECECEC", bd=5,
                         relief=GROOVE)
        self.CDT.place(x=410, y=85, width=100, height=25)

        # ..............................................................Buttons.........................................................................
        M5_frame = Frame(M_frame, bd=10, relief=RIDGE, bg="midnight blue")
        M5_frame.place(x=565, y=490, width=490, height=95)

        self.btn_Add = Button(M5_frame, text="Generate-bill", command=self.billing, font=("times new roman", 17),
                              bg="blue", activebackground='midnight blue', fg="white", activeforeground='white',
                              cursor='hand2')
        self.btn_Add.place(x=5, y=15, width=120, height=40)

        self.btn_Add = Button(M5_frame, text="Total", command=self.total, font=("times new roman", 17), bg="blue",
                              activebackground='midnight blue', fg="white", activeforeground='white', cursor='hand2')
        self.btn_Add.place(x=135, y=15, width=100, height=40)

        self.btn_Add = Button(M5_frame, text="Clear", command=self.clear, font=("times new roman", 17), bg="blue",
                              activebackground='midnight blue', fg="white", activeforeground='white', cursor='hand2')
        self.btn_Add.place(x=245, y=15, width=100, height=40)

        self.btn_Add = Button(M5_frame, text="Exit", command=self.exit, font=("times new roman", 17), bg="blue",
                              activebackground='midnight blue', fg="white", activeforeground='white', cursor='hand2')
        self.btn_Add.place(x=360, y=15, width=100, height=40)

        self.welcome()
        # ........................................................Button operation..............................................................................

    def error(self):
        if self.S.get() == "" or self.Sp.get() == "" or self.BG.get() == "" or self.Nd.get() == "" or self.SW.get() == "" or self.PP.get() == "" or self.MP.get() == "" or self.TC.get() == "" or self.DB.get() == "":
            messagebox.showinfo("Notification", "Please Fill 0 OR Click Button")
            self.clear()

        if self.PRT.get() == "" or self.CChawal.get() == "" or self.RC.get() == "" or self.BTR.get() == "" or self.KC.get() == "" or self.SHP.get() == "" or self.BRY.get() == "" or self.DA.get() == "" or self.FT.get() == "":
            messagebox.showinfo("Notification", "Please Fill 0 OR Click clear Button")
            self.clear()

        if self.COC.get() == "" or self.LC.get() == "" or self.FN.get() == "" or self.MZ.get() == "" or self.Psi.get() == "" or self.FOO.get() == "" or self.Spri.get() == "" or self.up7.get() == "" or self.Miri.get() == "":
            messagebox.showinfo("Notification", "Please Fill 0 OR Click clear Button")
            self.clear()

        if self.CN.get() == "" or self.CC.get() == "" or self.BN.get() == "":
            messagebox.showinfo("Notification", "Please Fill Customer Detail")
            self.clear()
        # ........................................................for check empty or error handling.............................................................

    # ............................................................destroy root..............................................................................
    def exit(self):
        self.root.destroy()

    # .................................................................................clear or reset........................................................
    def clear(self):
        self.CustomerName.set("")
        self.CustomerNumber.set("")
        self.BillingNumber.set("")
        self.Samosa.set(0)
        self.Springroll.set(0)
        self.Burger.set(0)
        self.Noodles.set(0)
        self.Sandwitch.set(0)
        self.PaneerPakoda.set(0)
        self.MixPakoda.set(0)
        self.Tikkichart.set(0)
        self.DahiBhale.set(0)
        self.Paratha.set(0)
        self.CholeChawal.set(0)
        self.RajmaChawal.set(0)
        self.Bhatoore.set(0)
        self.Khadichawal.set(0)
        self.Shahipaneer.set(0)
        self.Biryani.set(0)
        self.DumAloo.set(0)
        self.FullThali.set(0)
        self.Coca.set(0)
        self.Limca.set(0)
        self.Fanta.set(0)
        self.Maza.set(0)
        self.Pepsi.set(0)
        self.Frooti.set(0)
        self.Sprite.set(0)
        self.up77.set(0)
        self.Mirinda.set(0)
        self.snacksprice.set("")
        self.Foodprice.set("")
        self.coldrinkprice.set("")
        self.snackstax.set("")
        self.foodtax.set("")
        self.coldrinktext.set("")

    # .........................................................End Clear Function...........................................................
    def total(self):
        self.error()
        self.ssm = self.Samosa.get() * 10
        self.ssp = self.Springroll.get() * 40
        self.sbgr = self.Burger.get() * 30
        self.sndl = self.Noodles.get() * 40
        self.ssnb = self.Sandwitch.get() * 30
        self.spp = self.PaneerPakoda.get() * 250
        self.smix = self.MixPakoda.get() * 230
        self.stkr = self.Tikkichart.get() * 30
        self.sdb = self.DahiBhale.get() * 30

        self.total_Snacks_price = float(
            self.ssm +
            self.ssp +
            self.sbgr +
            self.sndl +
            self.ssnb +
            self.spp +
            self.smix +
            self.stkr +
            self.sdb
        )
        self.snacksprice.set("Rs.  " + str(self.total_Snacks_price))
        self.snacks_tex = (round((self.total_Snacks_price * 0.02), 2))
        self.snackstax.set("Rs. " + str(self.snacks_tex))
        # .....................................................................................................................................
        self.fprt = self.Paratha.get() * 15
        self.fcc = self.CholeChawal.get() * 50
        self.frc = self.RajmaChawal.get() * 50
        self.ftr = self.Bhatoore.get() * 50
        self.fkd = self.Khadichawal.get() * 40
        self.fspn = self.Shahipaneer.get() * 150
        self.fbrn = self.Biryani.get() * 100
        self.fda = self.DumAloo.get() * 30
        self.ftli = self.FullThali.get() * 150

        self.total_Foods_price = float(
            self.fprt +
            self.fcc +
            self.frc +
            self.ftr +
            self.fkd +
            self.fspn +
            self.fbrn +
            self.fda +
            self.ftli
        )
        self.Foodprice.set("Rs.  " + str(self.total_Foods_price))
        self.food_tex = (round((self.total_Foods_price * 0.02), 2))
        self.foodtax.set("Rs. " + str(self.food_tex))
        # ......................................................................................................................................
        self.dcca = self.Coca.get() * 100
        self.dlca = self.Limca.get() * 90
        self.dfat = self.Fanta.get() * 80
        self.dmza = self.Maza.get() * 85
        self.dppi = self.Pepsi.get() * 30
        self.dfrt = self.Frooti.get() * 90
        self.dspi = self.Sprite.get() * 95
        self.du7 = self.up77.get() * 80
        self.dmrd = self.Mirinda.get() * 70

        self.total_drink_price = float(
            self.dcca +
            self.dlca +
            self.dfat +
            self.dmza +
            self.dppi +
            self.dfrt +
            self.dspi +
            self.du7 +
            self.dmrd
        )
        self.coldrinkprice.set("Rs.  " + str(self.total_drink_price))
        self.coldrink_tex = (round((self.total_drink_price * 0.02), 2))
        self.coldrinktext.set("Rs. " + str(self.coldrink_tex))

        self.total_amount = float(
            self.total_Snacks_price +
            self.total_Foods_price +
            self.total_drink_price +
            self.snacks_tex +
            self.food_tex +
            self.coldrink_tex
        )
        # ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Button Command,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def welcome(self):
        self.Textarea.delete("1.0", END)
        self.Textarea.insert(END, "\t  Billing Software system")
        self.Textarea.insert(END, f"\n       Customer Name. : {self.CustomerName.get()}")
        self.Textarea.insert(END, f"\n       Customer Email ID : {self.CustomerNumber.get()}")
        self.Textarea.insert(END, f"\n       Bill N0. : {self.BillingNumber.get()}")
        self.Textarea.insert(END, f"\n ............................................................")
        self.Textarea.insert(END, f"\n Product\t\tQTY\t  Price")
        self.Textarea.insert(END, f"\n ............................................................")

    # ..........................................................billing area................................................................
    def billing(self):
        x = random.randint(1, 9999)
        self.BillingNumber.set(str(x))
        self.error()
        self.welcome()
        self.total()

        # ..........................Snacks biil area...............
        if self.Samosa.get() != 0:
            self.Textarea.insert(END, f"\n Samosa :\t\t{self.Samosa.get()}\t{self.ssm}")

        if self.Springroll.get() != 0:
            self.Textarea.insert(END, f"\n Springroll :\t\t{self.Springroll.get()}\t{self.ssp}")

        if self.Burger.get() != 0:
            self.Textarea.insert(END, f"\n Burger :\t\t{self.Burger.get()}\t{self.sbgr}")

        if self.Noodles.get() != 0:
            self.Textarea.insert(END, f"\n Noodles :\t\t{self.Noodles.get()}\t{self.sndl}")

        if self.Sandwitch.get() != 0:
            self.Textarea.insert(END, f"\n Sandwitch :\t\t{self.Sandwitch.get()}\t{self.ssnb}")

        if self.PaneerPakoda.get() != 0:
            self.Textarea.insert(END, f"\n PaneerPakoda :\t\t{self.PaneerPakoda.get()}\t{self.spp}")

        if self.MixPakoda.get() != 0:
            self.Textarea.insert(END, f"\n MixPakoda :\t\t{self.MixPakoda.get()}\t{self.smix}")

        if self.Tikkichart.get() != 0:
            self.Textarea.insert(END, f"\n Tikkichart :\t\t{self.Tikkichart.get()}\t{self.stkr}")

        if self.DahiBhale.get() != 0:
            self.Textarea.insert(END, f"\n DahiBhale :\t\t{self.DahiBhale.get()}\t{self.sdb}")

        # ..................................................Foods bill area.............................

        if self.Paratha.get() != 0:
            self.Textarea.insert(END, f"\n Paratha :\t\t{self.Paratha.get()}\t{self.fprt}")

        if self.CholeChawal.get() != 0:
            self.Textarea.insert(END, f"\n CholeChawal :\t\t{self.CholeChawal.get()}\t{self.fcc}")

        if self.RajmaChawal.get() != 0:
            self.Textarea.insert(END, f"\n RajmaChawal :\t\t{self.RajmaChawal.get()}\t{self.frc}")

        if self.Bhatoore.get() != 0:
            self.Textarea.insert(END, f"\n Bhatoore :\t\t{self.Bhatoore.get()}\t{self.ftr}")

        if self.Khadichawal.get() != 0:
            self.Textarea.insert(END, f"\n Khadichawal :\t\t{self.Khadichawal.get()}\t{self.fkd}")

        if self.Shahipaneer.get() != 0:
            self.Textarea.insert(END, f"\n Shahipaneer :\t\t{self.Shahipaneer.get()}\t{self.fspn}")

        if self.Biryani.get() != 0:
            self.Textarea.insert(END, f"\n Biryani :\t\t{self.Biryani.get()}\t{self.fbrn}")

        if self.DumAloo.get() != 0:
            self.Textarea.insert(END, f"\n DumAloo :\t\t{self.DumAloo.get()}\t{self.fda}")

        if self.FullThali.get() != 0:
            self.Textarea.insert(END, f"\n FullThali :\t\t{self.FullThali.get()}\t{self.ftli}")

        # .........................................Cold drink area.........................................

        if self.Coca.get() != 0:
            self.Textarea.insert(END, f"\n Cocacola :\t\t{self.Coca.get()}\t{self.dcca}")

        if self.Limca.get() != 0:
            self.Textarea.insert(END, f"\n Limca :\t\t{self.Limca.get()}\t{self.dlca}")

        if self.Fanta.get() != 0:
            self.Textarea.insert(END, f"\n Fanta :\t\t{self.Fanta.get()}\t{self.dfat}")

        if self.Maza.get() != 0:
            self.Textarea.insert(END, f"\n Maza :\t\t{self.Maza.get()}\t{self.dmza}")

        if self.Pepsi.get() != 0:
            self.Textarea.insert(END, f"\n Pepsi :\t\t{self.Pepsi.get()}\t{self.dppi}")

        if self.Frooti.get() != 0:
            self.Textarea.insert(END, f"\n Frooti :\t\t{self.Frooti.get()}\t{self.dfrt}")

        if self.Sprite.get() != 0:
            self.Textarea.insert(END, f"\n Sprite :\t\t{self.Sprite.get()}\t{self.dspi}")

        if self.up77.get() != 0:
            self.Textarea.insert(END, f"\n 7up :\t\t{self.up77.get()}\t{self.du7}")

        if self.Mirinda.get() != 0:
            self.Textarea.insert(END, f"\n Mirinda :\t\t{self.Mirinda.get()}\t{self.dmrd}")

        if self.SNT.get() != "Rs. 0.0":
            self.Textarea.insert(END, f"\n ............................................................")
            self.Textarea.insert(END, f"\n SnacksTex\t\t{self.snackstax.get()}")

        if self.FOT.get() != "Rs. 0.0":
            self.Textarea.insert(END, f"\n ............................................................")
            self.Textarea.insert(END, f"\n FoodTex\t\t{self.foodtax.get()}")

        if self.CDT.get() != "Rs. 0.0":
            self.Textarea.insert(END, f"\n ............................................................")
            self.Textarea.insert(END, f"\n ColdrinkTex\t\t{self.coldrinktext.get()}")

        self.Textarea.insert(END, f"\n ............................................................")
        self.Textarea.insert(END, f"\n Total Amount\t\t{self.total_amount}")
        self.savebill()

        # .....................................................................saved bill................................................................................

    def savebill(self):
        ask = messagebox.askyesno("Save Bill", "Do you want to save bill")
        if ask > 0:
            self.bill_data = self.Textarea.get("1.0", END)
            file = open("customer_data/" + str(self.BillingNumber.get()) + ".txt", "w")
            file.write(self.bill_data)
            file.close()
            messagebox.showinfo("Saved", f"Bill No.: {self.BillingNumber.get()} Saved Succesfully")




            reciever=self.CustomerNumber.get()
            sender = 'billing.software.system@gmail.com'
            password = '8thsemproject'
            subject='Billing'
            
            msg=MIMEMultipart()
            msg['From']=sender
            msg['To'] =reciever
            msg['Subject'] =subject
            
            body=self.bill_data
            msg.attach(MIMEText(body,'plain'))
            text=msg.as_string()
            print("Starting to send")
            with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
                server.login(sender, password)
                server.sendmail('billing.software.system@gmail.com',reciever, text)

            print("sent email!")

        else:
            return

    # ..............................................open old bill....................................................................................................
    def search(self):
        for i in os.listdir("customer_data/"):
            if i.split('.')[0] == self.BillingNumber.get():
                file = open(f"customer_data/{i}", "r")
                self.Textarea.delete('1.0', END)
                for a in file:
                    self.Textarea.insert(END, a)
                file.close()


root = Tk()
obj = billing_r(root)
root.mainloop()





