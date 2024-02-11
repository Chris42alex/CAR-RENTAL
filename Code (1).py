import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk, Image
import mysql.connector as m
from prettytable import PrettyTable
from tkinter.messagebox import showerror, showwarning, showinfo
import smtplib
from email.message import EmailMessage
import random
import time
import pandas
import csv
from tkcalendar import Calendar
from dateutil.parser import parse
import math
import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import matplotlib.pyplot as plt


mdb = m.connect(host='localhost', user='root', password='12345')
mc = mdb.cursor()
local = ''
set1 = ''
phone = ''
buy_date = ''
return_date = ''
tprice = 0
car_class = ''
s_price = 0
e_price = 0
vat = 0
auth_code = ''
sevicec = ''
range_km = ''


def createall():
    # create database
    mc.execute('CREATE DATABASE car1')
    mc.execute('USE car1')
    # creating car record table in car1 (for user and manager)
    mc.execute('CREATE TABLE record (CCODE CHAR(6) PRIMARY KEY,CCOMPANY VARCHAR(20), CNAME VARCHAR(50) NOT NULL, CCOLOUR VARCHAR(35), CTYPE VARCHAR(15), CTRANSMISSION VARCHAR(10) DEFAULT "Automatic",CDOORS VARCHAR(10) DEFAULT "5 Doors",CCLASS VARCHAR(20),CPRICE_MONTH INT,CYEAR INT,AVAILABILITY VARCHAR(20),IMAGECODE VARCHAR(50),CFUEL VARCHAR(20) DEFAULT "Petrol",CPRICE_DAY INT, CDISTANCE INT DEFAULT 5)')
    # inserting basic records into record
    # SUV
    mc.execute("INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES('CDR001','Toyota','LandCruiser','Silver Metallic','7 Seater','SUV',2275,2020,'Available','./images/suv/tlc.png')")
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR002","Buick","Enclave","Pearl white","7 Seater","SUV",2500,2021,"Available","./images/suv/be.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR003","Chevrolet","Tahoe","Crystal White","7 Seater","SUV",2655,2022,"Available","./images/suv/ct.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR004","Hyundai","Tucson","Midnight Blue","5 Seater","SUV",2246,2022,"Available","./images/suv/ht.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR005","Infiniti","QX60","Pearlescent White","7 Seater","SUV",2570,2021,"Available","./images/suv/iqx60.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR006","Jaguar","E-Pace","Silky Silver","5 Seater","SUV",2390,2023,"Available","./images/suv/je-p.png")')
    # SEDAN
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR011","Audi","A3","Adriatic Dark Blue","5 Seater","Sedan",2188,2020,"Available","4 Doors","./images/cars/aae.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR012","Alpha Romeo","Giulia","Magnetic Red","5 Seater","Sedan",2267,2021,"Available","4 Doors","./images/cars/ag.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR013","BMW","4-Series","Sangria Red","5 Seater","Sedan",2399,2021,"Available","4 Doors","./images/cars/b4-s.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR014","Chevrolet","Impala","Flame Red","5 Seater","Sedan",2297,2021,"Available","4 Doors","./images/cars/cm.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR015","Honda","Accord","Pearl White","5 Seater","Sedan",2208,2022,"Available","4 Doors","./images/cars/ha.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE,CFUEL) VALUES("CDR016","Tesla","Model 3","Dynamic Blue","5 Seater","Sedan",2588,2021,"Available","4 Doors","./images/cars/tm3.png","Electricity")')
    # COUPE
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR021","BMW","Z4","Lightning Blue","2 Seater","Coupe",2702,2021,"Available","2 Doors","./images/coupe/bz4.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR022","Chevrolet","Corvette","Plasma Yellow","2 Seater","Coupe",2769,2022,"Available","2 Doors","./images/coupe/cc.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR023","Chevrolet","Camaro","White Crystal","2 Seater","Coupe",2699,2021,"Available","2 Doors","./images/coupe/cc22.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR024","Ford","Mustang","Midnight Black","2 Seater","Coupe",2689,2020,"Available","2 Doors","./images/coupe/fm.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR025","Mercedes-Benz","GT","Red Metallic","2 Seater","Coupe",2899,2022,"Available","2 Doors","./images/coupe/mbgt.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR026","Subaru","BRZ","Silver Grey","2 Seater","Coupe",2788,2023,"Available","2 Doors","./images/coupe/sbrx.png")')
    # HATCHBACK
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR031","Nissan","Leaf","Steel Silver","5 Seater","HatchBack",1879,2022,"Available","./images/cpo/nl.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR032","Chevrolet","Spark","Onyx Black","5 Seater","HatchBack",1895,2020,"Available","3 Doors","./images/cpo/cs.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR033","Mitsubhishi","Mirage","Midnight Black","5 Seater","HatchBack",1769,2021,"Available","./images/cpo/mm.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR034","Subaru","Brezza","Midnight Black","5 Seater","HatchBack",1840,2020,"Available","./images/cpo/sb.png")')
    # PICKUP
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR041","Chevrolet","Colorado","Adriatic Blue","5 Seater","Ute",2689,2020,"Available","4 Doors","./images/trucks/cc.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR042","Ford","Ranger","Midnight Black","5 Seater","Ute",2587,2020,"Available","4 Doors","./images/trucks/fr.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR044","Hyundai","Santa Cruz","Ocean Blue","5 Seater","Ute",2457,2022,"Available","4 Doors","./images/trucks/hsc.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR045","Jeep","Gladiator","Red Metallic","5 Seater","Ute",2771,2021,"Available","4 Doors","./images/trucks/jg.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,CDOORS,IMAGECODE) VALUES("CDR046","Nissan","Frontier","White","5 Seater","Ute",2499,2020,"Available","4 Doors","./images/trucks/nf.png")')
    # MINIVAN
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR101","Chrysler","Pacifica Hybrid","Grey Metallic","7 Seater","MiniVan",2455,2022,"Available","./images/vans/chp.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR102","Honda","Odyssey","Cosmos Black","7 Seater","MiniVan",2356,2020,"Available","./images/vans/ho.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR103","Kia","Carnival","Deep Blue Pearl","7 Seater","MiniVan",2467,2022,"Available","./images/vans/kc.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR104","Toyota","Sienna","Metallic Black","7 Seater","MiniVan",2367,2021,"Available","./images/vans/ts.png")')
    # LUXURY
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR201","Bentley","Bentagaya","Pearl Bronze","5 Seater","Luxury SUV",3100,2022,"Available","./images/luxury/bb.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR202","Lincoln","Aviator","Metallic Black","7 Seater","Luxury SUV",3200,2020,"Available","./images/luxury/la.png")')
    mc.execute('INSERT INTO record (CCODE,CCOMPANY,CNAME,CCOLOUR,CTYPE,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE) VALUES("CDR203","Rolls Royce","Cullinan","Deep Black","5 Seater","Luxury SUV",3700,2022,"Available","./images/luxury/rrc.png")')
    # inserting common values together
    mc.execute('UPDATE record SET CPRICE_DAY=100 WHERE CCLASS="SUV"')
    mc.execute('UPDATE record SET CPRICE_DAY=90 WHERE CCLASS="Sedan"')
    mc.execute('UPDATE record SET CPRICE_DAY=95 WHERE CCLASS="Coupe"')
    mc.execute('UPDATE record SET CPRICE_DAY=85 WHERE CCLASS="HatchBack"')
    mc.execute('UPDATE record SET CPRICE_DAY=97 WHERE CCLASS="Ute"')
    mc.execute('UPDATE record SET CPRICE_DAY=93 WHERE CCLASS="MiniVan"')
    mc.execute('UPDATE record SET CPRICE_DAY=130 WHERE CCLASS="Luxury SUV"')
    # creating user record table in car1 (for manager)
    mc.execute("CREATE TABLE user (PHONE CHAR(10) PRIMARY KEY, FSTNME VARCHAR(20), SNDNME VARCHAR(20), EMAIL VARCHAR(50), DOB DATE, LICENSE VARCHAR(20), LISSUDATE DATE, ADDRESS VARCHAR(100), PASSWORD VARCHAR(15))")
    # creating placed orders -> buy table in car1 (for manager and owner)
    mc.execute("CREATE TABLE buy (INVOICE CHAR(7) PRIMARY KEY, CCODE CHAR(6), PHONE CHAR(10), CBUYDATE DATE, CRETURN DATE, TPRICE DECIMAL(10,4), REMARK VARCHAR(30))")
    # creating service table in car1 (for technician and owner)
    mc.execute("CREATE TABLE service (SERVICECODE CHAR(6) PRIMARY KEY, CCODE CHAR(6), SERVICEEX CHAR(100), SERV_EXPENSE DECIMAL(10,4), REPAIREX VARCHAR(100), REP_EXPENSE DECIMAL(10,4))")
    # creating owner table in car1 (for owner only)
    mc.execute(
        "CREATE TABLE owner (INVOICE VARCHAR(7) PRIMARY KEY, TPRICE DECIMAL(10,2), DATOP DATE)")
    # creating workers table in car1 (for owner only)
    mc.execute("CREATE TABLE workers (AUTH_CODE CHAR(6) PRIMARY KEY, NAME_W VARCHAR(30), E_MAIL VARCHAR(50), SALARY DECIMAL(10,4), DESIGNATION VARCHAR(25))")
    # inserting basic values into workers
    mc.execute(
        "INSERT INTO workers VALUES('O_*n@1','Dhris Raj Xavier','dh_chr_xr22@voiture.com',0,'Owner')")
    mc.execute(
        "INSERT INTO workers VALUES('Ac_09@','Alex John Kattoor','al_1999@gmail.com',10000,'Accountant')")
    mc.execute(
        "INSERT INTO workers VALUES('Mn_0A1','Adwaith Sharma Naik','adwai1999.sn@gmail.com',11500,'Manager')")
    mc.execute(
        "INSERT INTO workers VALUES('Tc@09A','Mohammed Moby Dular','mobycrazy@hotmail.com',9800,'Technician')")
    # committing/adding all tables into database
    mdb.commit()


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = 'voiture.cr2022@gmail.com'
    msg['from'] = user
    password = 'bmqoadrkeywuaisq'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('voiture.cr2022@gmail.com', 'bmqoadrkeywuaisq')
    server.send_message(msg)
    server.quit()


def invcecreation():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    a1 = random.choice(alpha)
    a2 = random.choice(alpha)
    a3 = random.choice(digit)
    a4 = random.choice(digit)
    a5 = random.choice(alpha)
    a6 = random.choice(digit)
    a7 = random.choice(digit)
    invoice = a1 + a2 + a3 + a4 + a5 + a6 + a7
    mc.execute('SELECT * FROM buy')
    f = mc.fetchall()
    for i in f:
        if invoice in i:
            invcecreation()
        else:
            continue
    return invoice


def printed(w1, phone, lisc):
    w1.destroy()
    w1 = Tk()
    w1.title('Bill')
    w1.geometry('1000x500')
    img = Image.open('bill2.png')
    photo = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo, borderwidth=0).place(x=0, y=0, anchor='nw')
    mc.execute(
        'SELECT FSTNME, SNDNME, EMAIL FROM user WHERE PHONE="{}"'.format(phone))
    f = mc.fetchone()
    p = f[0] + ' ' + f[1]
    email_to = f[2]
    temp = p.capitalize()
    today = datetime.datetime.now()
    dt = parse(str(today))
    j = dt.date()
    dsp_1 = Label(w1, text=temp, font=('dubai', 8),
                  bg='white').place(x=84, y=378, anchor='sw')
    dsp_2 = Label(w1, text=j, font=('dubai', 8),
                  bg='white').place(x=72, y=89, anchor='sw')
    dsp_3 = Label(w1, text=phone, font=('dubai', 8),
                  bg='white').place(x=89, y=471, anchor='sw')
    dsp_4 = Label(w1, text=buy_date.date(), font=('dubai', 8),
                  bg='#f1f4ff').place(x=700, y=133, anchor='w')
    dsp_5 = Label(w1, text=return_date.date(), font=('dubai', 8),
                  bg='#f1f4ff').place(x=800, y=133, anchor='w')
    invoice = invcecreation()
    reason = 'Booked Only'
    mc.execute('INSERT INTO buy VALUES ("{}","{}","{}","{}","{}",{},"{}")'.format(
        invoice, local, phone, buy_date, return_date, tprice, reason))
    mc.execute(
        'UPDATE record SET AVAILABILITY="UNAVAILABLE" WHERE CCODE="{}"'.format(local))
    mdb.commit()
    dsp_6 = Label(w1, text=invoice, font=('dubai', 8),
                  bg='white').place(x=102, y=121, anchor='sw')
    mc.execute('SELECT CCOMPANY,CNAME FROM record WHERE CCODE="{}"'.format(local))
    k = mc.fetchone()
    l = k[0] + ' ' + k[1]
    n_pr = tprice - vat
    dsp_7 = Label(w1, text=l, font=('dubai', 8),
                  bg='#f1f4ff').place(x=480, y=133, anchor='w')
    dsp_9 = Label(w1, text=vat, font=('dubai', 7),
                  bg='#f1f4ff').place(x=900, y=192, anchor='w')
    dsp_8 = Label(w1, text=tprice, font=('dubai', 7),
                  bg='#f1f4ff').place(x=900, y=219, anchor='w')
    dsp_8 = Label(w1, text=n_pr, font=('dubai', 7),
                  bg='#f1f4ff').place(x=900, y=135, anchor='w')
    dsp_8 = Label(w1, text=n_pr, font=('dubai', 7),
                  bg='#f1f4ff').place(x=900, y=165, anchor='w')
    but_1 = Button(w1, text='(Home)', fg='black', bg='white', relief='flat',
                   command=lambda:  home(w1)).place(x=980, y=10, anchor='ne')
    mc.execute('SELECT LICENSE,ADDRESS FROM user WHERE PHONE="{}"'.format(phone))
    j = mc.fetchone()
    li = j[0]
    ad = j[1].title()
    dsp_8 = Label(w1, text=li, font=('dubai', 8),
                  bg='white').place(x=106, y=409, anchor='sw')
    dsp_8 = Label(w1, text=ad, font=('dubai', 8),
                  bg='white').place(x=98, y=439, anchor='sw')
    dsp_8 = Label(w1, text="Voiture Car Rental", font=(
        'dubai', 8), bg='white').place(x=106, y=199, anchor='sw')
    dsp_8 = Label(w1, text="Al Khan Khalidiya", font=('dubai', 8),
                  bg='white').place(x=98, y=229, anchor='sw')
    dsp_8 = Label(w1, text="Sharjah", font=('dubai', 8),
                  bg='white').place(x=138, y=260, anchor='sw')
    dsp_8 = Label(w1, text="056-5669102 / 055-9634200",
                  font=('dubai', 8), bg='white').place(x=85, y=291, anchor='sw')
    email_sub = "Your Booking Has Been Confirmed"
    email_text = ''' VOITURE CAR RENTAL
    
    BOOKING DETAILS:          
    CUSTOMER NAME = ''' + temp + '''
    CUSTOMER PHONE = ''' + phone + '''
    CUSTOMER INVOCE = ''' + invoice + '''
    
    CAR DETAILS:
    CAR NAME = ''' + l + '''
    TOTAL RENTING PRICE = ''' + str(tprice) + '''
    CAR COLLECTION DATE = ''' + str(buy_date) + '''
    CAR RETURNING DATE = ''' + str(return_date) + '''
    
    Regards,
    Team Of Voiture'''
    email_alert(email_sub, email_text, email_to)
    w1.mainloop()


def printreciept(w1, phone, lisc, pas, rdate):
    end_date = buy_date + datetime.timedelta(days=rdate)
    global return_date
    return_date = end_date
    mc.execute('SELECT LICENSE FROM user WHERE PHONE="{}"'.format(phone))
    f = mc.fetchone()
    if f == None:
        showerror(title='Error', message='Invalid Phone Number or Username')
        paymentpg(w1, rdate)
        j = False
    elif lisc in f:
        mc.execute('SELECT PASSWORD FROM user WHERE PHONE="{}"'.format(phone))
        i = mc.fetchone()
        if pas in i:
            printed(w1, phone, lisc)
        else:
            showerror(title='Error', message='Invalid Password')
            paymentpg(w1, rdate)
            j = False
    else:
        showerror(title='Error', message='Invalid License Number')
        paymentpg(w1, rdate)
        j = False


def paymentpg(w1, dates):
    w1.destroy()
    w1 = Tk()
    w1.title('Verify')
    w1.geometry('1000x500')
    photo = Image.open('bgforall2.png')
    photo1 = ImageTk.PhotoImage(photo)
    phone_v = StringVar(w1)
    lisc_v = StringVar(w1)
    pass_v = StringVar(w1)
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp1 = Label(w1, text='Complete Booking', bg='#131311', fg='white',
                 font='ariel 20 bold').place(x=500, y=170, anchor='center')
    dsp1 = Label(w1, bg='#131311', fg='white', text='RE-ENTER THE FOLLOWING',
                 font=('dubai', 7)).place(x=500, y=200, anchor='center')
    phone = Label(w1, bg='black', fg='white', text='Phone Number : ').place(
        x=380, y=260, anchor='nw')
    phone_e = ttk.Entry(w1, textvariable=phone_v).place(
        x=485, y=260, anchor='nw')
    lisc = Label(w1, bg='black', fg='white', text='License Number : ').place(
        x=380, y=290, anchor='nw')
    lisc_e = ttk.Entry(w1, textvariable=lisc_v).place(
        x=485, y=290, anchor='nw')
    pas = Label(w1, bg='black', fg='white', text='Password : ').place(
        x=380, y=320, anchor='nw')
    pas_e = ttk.Entry(w1, textvariable=pass_v,
                      show='*').place(x=485, y=320, anchor='nw')
    but1 = Button(w1, width=30, fg='white', bg='#E74B10', relief='flat', text='Verify', command=lambda: printreciept(
        w1, phone_v.get(), lisc_v.get(), pass_v.get(), dates)).place(x=500, y=420, anchor='s')
    but2 = Button(w1, bg='black', fg='white', relief='flat', text='(Revert)',
                  command=lambda: home(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def checkdate(w1, date, dates):
    format = '%m/%d/%y'
    lastconnection = datetime.datetime.strptime(date, format)
    d = lastconnection.strftime('%Y-%m-%d')
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])
    k = datetime.datetime(year, month, day)
    ans = k.weekday()
    today = datetime.datetime.now()
    val = k > today
    global buy_date
    buy_date = k
    if ans > 4:
        showerror(title='Date Error', message='We are off on this day')
        dateforcollect(w1, dates)
    elif val == False:
        showerror(title='Date Error', message='This day is not available')
        dateforcollect(w1, dates)
    else:
        paymentpg(w1, dates)


def dateforcollect(w1, date):
    today = str(datetime.datetime.now())
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:11])
    cal = Calendar(w1, font="ariel 8", selectmode='day',
                   year=year, month=month, day=day)
    cal.place(x=50, y=290, anchor='nw')
    msg = '''SELECT A DATE FOR COLLECTING YOUR VOITURE'''
    dso_1 = Label(w1, text=msg, fg='white', bg='black').place(
        x=310, y=287, anchor='nw')
    msg2 = '''
* We are off on Saturdays amd Sundays

All rentals subject to VOITURE Terms and Conditions.
Car return date will be calculated and printed in 
your invoice. Only 29 minutes grace period is provided
for car return and each extra day will be charged.'''
    dso_1 = Label(w1, text=msg2, fg='white', bg='black',
                  font='ariel 8').place(x=310, y=307, anchor='nw')
    but_1 = Button(w1, text='Get This Date', fg='white', bg='#E74B10', relief='flat', width=30,
                   command=lambda: checkdate(w1, cal.get_date(), date)).place(x=330, y=465, anchor='sw')
    w1.mainloop()


def numbofentity(w1, k):
    msg = 'Enter Number of ' + k + ' :      '
    j = StringVar(w1)
    dsp_1 = Label(w1, text=msg, fg='#ffba83', bg='black').place(
        x=50, y=100, anchor='nw')
    ent_1 = ttk.Entry(w1, textvariable=j).place(x=210, y=97, anchor='nw')
    but_2 = Button(w1, text='Check Price', fg='white', bg='#E74B10', relief='flat',
                   width=20, command=lambda: calculator(w1, j.get(), k)).place(x=470, y=94, anchor='n')


def calculator(w1, q, k):
    global local
    j = local
    mc.execute(
        'SELECT CPRICE_MONTH,CPRICE_DAY FROM record WHERE CCODE="{}"'.format(j))
    f = mc.fetchone()
    p = int(f[0])
    m = int(f[1])
    if k == 'Weeks' and q.isdigit():
        l = int(q)
        price = m*7
        tprice_cust = math.ceil(price * l)
        days = l*7
    elif k == 'Days' and q.isdigit():
        l = int(q)
        price = m
        tprice_cust = math.ceil(price * l)
        days = l
    elif k == 'Months' and q.isdigit():
        l = int(q)
        price = p
        tprice_cust = math.ceil(price * l)
        days = l*30
    else:
        showerror(title='Value Error',
                  message='Invalid Entry in place of Number')
        usagedates(w1)
    global tprice, vat
    vat = tprice_cust*0.05
    tprice = tprice_cust + vat
    msg1 = '     Total  Price  is  AED  ' + str(tprice) + ' ( VAT  inc. )'
    dsp_1 = Label(w1, text=msg1, fg='white', bg='black').place(
        x=287, y=163, anchor='ne')
    but_1 = Button(w1, text='Continue', fg='white', bg='#E74B10', relief='flat', width=20,
                   command=lambda: dateforcollect(w1, days)).place(x=327, y=160, anchor='nw')
    if car_class != '':
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: bringchoice(car_class, w1)).place(x=980, y=20, anchor='ne')
    else:
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: bringchoice2(s_price, e_price, w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def usagedates(w1):
    mc.execute("SELECT AVAILABILITY FROM record WHERE CCODE='{}'".format(local))
    f = mc.fetchone()
    if 'UNAVAILABLE' in f:
        showerror(title='Error', message='This car is already rented')
        bringchoice(car_class, w1)
    else:
        w1.destroy()
        w1 = Tk()
        w1.title('Period')
        w1.geometry('1000x500')
        photo = Image.open('bgforall.png')
        photo1 = ImageTk.PhotoImage(photo)
        dsp_0 = Label(w1, borderwidth=0, image=photo1).place(
            x=0, y=0, anchor='nw')
        selection = StringVar(w1)
        j = local
        s = ttk.Style(w1)
        s.map('C.TButton', foreground=[
              ('pressed', 'red'), ('active', 'green')])
        dsp_1 = Label(w1, text='Rental Period:', fg='white', bg='black', font=(
            'Ariel', 20, 'bold')).place(x=20, y=20, anchor='nw')
        but_1 = ttk.Button(w1, text="Daily", width=12, style='C.TButton',
                           command=lambda:  numbofentity(w1, 'Days')).place(x=245, y=25, anchor='nw')
        but_2 = ttk.Button(w1, text="Weekly", width=12, style='C.TButton',
                           command=lambda: numbofentity(w1, 'Weeks')).place(x=375, y=25, anchor='nw')
        but_3 = ttk.Button(w1, text="Monthly", width=12, style='C.TButton',
                           command=lambda: numbofentity(w1, 'Months')).place(x=505, y=25, anchor='nw')
        w1.mainloop()


def picanddetails(o, l, w1):
    j = ImageTk.PhotoImage(Image.open(l))
    dsp_1 = Label(w1, bg='black').grid(row=0, column=0)
    dsp_1 = Label(w1, bg='black').grid(row=1, column=1)
    dsp_1 = Label(w1, bg='black').grid(row=2, column=2)
    dsp_1 = Label(w1, bg='black').grid(row=3, column=3)
    dsp_1 = Label(w1, bg='black').grid(row=4, column=4)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=5)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=6)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=7)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=8)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=9)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=10)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=11)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=12)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=13)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=14)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=15)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=16)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=17)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=18)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=19)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=20)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=21)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=22)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=23)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=24)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=25)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=26)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=27)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=28)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=29)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=30)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=31)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=32)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=33)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=34)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=35)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=36)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=37)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=38)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=39)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=40)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=41)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=42)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=43)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=44)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=45)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=46)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=47)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=48)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=49)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=50)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=51)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=52)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=53)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=54)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=55)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=56)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=57)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=58)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=59)
    dsp_1 = Label(w1, bg='black').grid(row=5, column=60)
    fram2 = LabelFrame(w1, text=o, padx=10, pady=10, bg='black', fg='white')
    fram2.grid(row=6, column=61)
    if set1 == '':
        m = Button(fram2, image=j, relief='flat', command=lambda: login(w1))
        m.pack()
    else:
        m = Button(fram2, image=j, relief='flat',
                   command=lambda: usagedates(w1))
        m.pack()
    mc.execute('SELECT CCODE FROM record WHERE IMAGECODE="{}"'.format(l))
    f = mc.fetchone()
    p = f[0]
    global local
    local = p
    mc.execute('SELECT * FROM record WHERE CCODE="{}"'.format(p))
    f = mc.fetchone()
    dsp_1 = Label(w1, text='Car Details', fg='#ffba83', bg='black', font=(
        'Candara', 15)).place(x=500, y=90, anchor='center')
    dsp_n1 = Label(w1, text='Car Name : ', fg='#ffba83',
                   bg='black').place(x=60, y=160, anchor='nw')
    dsp_n = Label(w1, text=f[1] + ' ' + f[2] + '           ',
                  fg='#ffba83', bg='black').place(x=200, y=160, anchor='nw')
    dsp_c1 = Label(w1, text='Colour : ', fg='#ffba83',
                   bg='black').place(x=60, y=190, anchor='nw')
    dsp_c = Label(w1, text=f[3] + '                    ',
                  fg='#ffba83', bg='black').place(x=200, y=190, anchor='nw')
    dsp_t1 = Label(w1, text='Type : ', fg='#ffba83',
                   bg='black').place(x=60, y=220, anchor='nw')
    dsp_t = Label(w1, text=f[4], fg='#ffba83', bg='black').place(
        x=200, y=220, anchor='nw')
    dsp_tr1 = Label(w1, text='Transmission Type : ', fg='#ffba83',
                    bg='black').place(x=60, y=250, anchor='nw')
    dsp_tr = Label(w1, text=f[5], fg='#ffba83', bg='black').place(
        x=200, y=250, anchor='nw')
    dsp_cl1 = Label(w1, text='Class : ', fg='#ffba83',
                    bg='black').place(x=60, y=280, anchor='nw')
    dsp_cl = Label(w1, text=f[7], fg='#ffba83', bg='black').place(
        x=200, y=280, anchor='nw')
    dsp_y1 = Label(w1, text='Model Year : ', fg='#ffba83',
                   bg='black').place(x=695, y=160, anchor='nw')
    dsp_y = Label(w1, text=f[9], fg='#ffba83', bg='black').place(
        x=835, y=160, anchor='nw')
    dsp_s1 = Label(w1, text='Doors : ', fg='#ffba83',
                   bg='black').place(x=695, y=190, anchor='nw')
    dsp_s = Label(w1, text=f[6], fg='#ffba83', bg='black').place(
        x=835, y=190, anchor='nw')
    dsp_a1 = Label(w1, text='Availability : ', fg='#ffba83',
                   bg='black').place(x=695, y=220, anchor='nw')
    dsp_a = Label(w1, text=f[10] + '            ', fg='#ffba83',
                  bg='black').place(x=835, y=220, anchor='nw')
    dsp_p1 = Label(w1, text='Price / Month : ', fg='#ffba83',
                   bg='black').place(x=695, y=250, anchor='nw')
    dsp_p = Label(w1, text=f[8], fg='#ffba83', bg='black').place(
        x=835, y=250, anchor='nw')
    dsp_f1 = Label(w1, text='Fuel Type : ', fg='#ffba83',
                   bg='black').place(x=695, y=280, anchor='nw')
    dsp_f = Label(w1, text=f[12], fg='#ffba83', bg='black').place(
        x=835, y=280, anchor='nw')
    dsp_chan = Label(w1, text='All descriptions are subject to change without notice. Some features illustrated on this page subject to availability.',
                     fg='white', bg='black', font=('ariel', 8)).place(x=500, y=359, anchor='n')
    dsp_chan = Label(w1, text='Click on image to continue', fg='white',
                     bg='black', font=('ariel', 8)).place(x=500, y=343, anchor='n')
    w1.mainloop()


def menucar(f, w1, mb):
    j = dict()
    l = []
    for i in f:
        j[i[0] + ' ' + i[1]] = i[2]
        l += [i[0] + ' ' + i[1]]
    mb.place(x=200, y=40, anchor='center')
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    for cars in l:
        mb.menu.add_command(
            label=cars, command=lambda d=cars: picanddetails(d, j[d], w1))
    mb.place(x=500, y=30, anchor='n')
    if s_price == 0:
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: classorprice(w1)).place(x=980, y=20, anchor='ne')
    else:
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: classorprice(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def bringchoice(l, w1):
    global car_class
    car_class = l
    w1.destroy()
    w1 = Tk()
    w1.title('Car Choose')
    w1.geometry('1000x500')
    image1 = Image.open('bg.png')
    photo1 = ImageTk.PhotoImage(image1)
    dsp1 = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    if l == 'SUV':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="SUV"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your SUV")
        menucar(f, w1, mb)
    elif l == 'SEDAN':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="Sedan"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your SEDAN")
        menucar(f, w1, mb)
    elif l == 'COUPE':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="Coupe"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your CUT")
        menucar(f, w1, mb)
    elif l == 'HATCH':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="HatchBack"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your HATCH")
        menucar(f, w1, mb)
    elif l == 'MPV':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="MiniVan"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your MPV")
        menucar(f, w1, mb)
    elif l == 'UTE':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS="Ute"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your UTE")
        menucar(f, w1, mb)
    elif l == 'LX':
        mc.execute(
            'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CCLASS LIKE "LUXURY%"')
        f = mc.fetchall()
        mb = ttk.Menubutton(w1, text="Select Your LX")
        menucar(f, w1, mb)
    w1.mainloop()


def bringchoice2(start, end, w1):
    global s_price, e_price
    s_price = start
    e_price = end
    w1.destroy()
    w1 = Tk()
    w1.title('Car Choose')
    w1.geometry('1000x500')
    image1 = Image.open('bg.png')
    photo1 = ImageTk.PhotoImage(image1)
    dsp1 = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    mc.execute(
        'SELECT CCOMPANY,CNAME, IMAGECODE FROM RECORD WHERE CPRICE_MONTH BETWEEN {} AND {}'.format(start, end))
    f = mc.fetchall()
    mb = ttk.Menubutton(w1, text="Select Your VEHICLE")
    menucar(f, w1, mb)
    w1.mainloop()


def CC_CPsearch(w1, value):
    img = Image.open('black.png')
    img2 = img.resize((300, 500))
    photo = ImageTk.PhotoImage(img2)
    dsp = Label(w1, image=photo, borderwidth=0).place(
        x=190, y=110, anchor='nw')
    selection = StringVar()
    if value == 'CP':
        begin = IntVar()
        end = IntVar()
        dsp_1 = Label(w1, text='Enter Price For', fg='#ffba83', bg='black', font=(
            'Candara', 15)).place(x=317, y=230, anchor='center')
        dsp_2 = Label(w1, text='Range Beginning :', fg='#ffba83',
                      bg='black').place(x=300, y=280, anchor='e')
        entryprb = ttk.Entry(w1, textvariable=begin).place(
            x=310, y=280, anchor='w')
        dsp_3 = Label(w1, text='Range End :', fg='#ffba83',
                      bg='black').place(x=300, y=320, anchor='e')
        entrypre = ttk.Entry(w1, textvariable=end).place(
            x=310, y=320, anchor='w')
        dsp_4 = Label(w1, text='(FOR A MONTH)', fg='#ffba83', bg='black', font=(
            'dubai', 8)).place(x=317, y=350, anchor='n')
        button1 = Button(w1, text='FIND CAR', width=20, fg='white', bg='#E74B10', relief='flat',
                         command=lambda: bringchoice2(begin.get(), end.get(), w1)).place(x=317, y=430, anchor='s')
    else:
        selection = StringVar()
        s = ttk.Style()
        s.configure('Wild.TRadiobutton', background='black',
                    foreground='#ffba83')
        dsp_1 = Label(w1, text='Select Class', fg='#ffba83', bg='black', font=(
            'Candara', 15)).place(x=317, y=180, anchor='center')
        buttonsuv = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="Sports Utility Vehicles (SUV)",
                                    variable=selection, value='SUV').place(x=232, y=205, anchor='nw')
        buttonsedan = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="Saloon Vehicles (SEDAN)",
                                      variable=selection, value='SEDAN').place(x=232, y=230, anchor='nw')
        buttoncut = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="Coupes (CUT)",
                                    variable=selection, value='COUPE').place(x=232, y=255, anchor='nw')
        buttonhatch = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="HatchBack Vehicles (HATCH)",
                                      variable=selection, value='HATCH').place(x=232, y=280, anchor='nw')
        buttonmpv = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="Multi Purpose Vehicles (MPV)",
                                    variable=selection, value='MPV').place(x=232, y=305, anchor='nw')
        buttonute = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="PickUp Trucks (UTE)",
                                    variable=selection, value='UTE').place(x=232, y=330, anchor='nw')
        buttonlx = ttk.Radiobutton(w1, style='Wild.TRadiobutton', text="Luxury Vehicle (LX)",
                                   variable=selection, value='LX').place(x=232, y=355, anchor='nw')
        button1 = Button(w1, text='FIND CAR', width=20, fg='white', bg='#E74B10', relief='flat',
                         command=lambda: bringchoice(selection.get(), w1)).place(x=317, y=430, anchor='s')
    w1.mainloop()


def spl(w1):
    global local
    local = ''
    home(w1)

def classorprice(w1):
    w1.destroy()
    w1 = Tk()
    w1.title('Search By')
    w1.geometry('1000x500')
    image1 = Image.open('bgforall.png')
    photo1 = ImageTk.PhotoImage(image1)
    dsp1 = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    dsp2 = Label(w1, text='Search Voiture By', fg='white', bg='black', font=(
        'Ariel', 20, 'bold')).place(x=317, y=40, anchor='center')
    s = ttk.Style(w1)
    s.map('C.TButton', foreground=[('pressed', 'red'), ('active', 'green')])
    button3 = ttk.Button(w1, text='Class', style='C.TButton', width=15,
                         command=lambda: CC_CPsearch(w1, 'CC')).place(x=292, y=75, anchor='ne')
    button4 = ttk.Button(w1, text='Price', width=15, style='C.TButton',
                         command=lambda: CC_CPsearch(w1, 'CP')).place(x=342, y=75, anchor='nw')
    if set1 == 'logged':
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: spl(w1)).place(x=980, y=20, anchor='ne')
    else:
        button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                         command=lambda: temporary2(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def temporary(w1):
    global set1
    set1 = ''
    exit()


def remove(invoice, ccode, w1):
    mc.execute('DELETE FROM buy WHERE INVOICE="{}"'.format(invoice))
    mc.execute('DELETE FROM owner WHERE INVOICE="{}"'.format(invoice))
    mc.execute(
        'UPDATE record SET AVAILABILITY="Available" WHERE CCODE ="{}"'.format(ccode))
    mdb.commit()
    mc.execute('SELECT EMAIL FROM user WHERE PHONE="{}"'.format(phone))
    f = mc.fetchone()
    email = f[0]
    msg = '''VOITURE CAR RENTAL

    Dear Customer,
        Your order referring to invoice ''' + invoice + ''' has been cancelled successfully.

    Regards
    Team of Voiture'''
    sub = 'Rental Cancellation'
    email_alert(sub, msg, email)
    showinfo(title='Cancelled', message='SUCCESSFULLY DELETED')
    home(w1)


def cancel(w1, invoice, ccode, date):
    date1 = datetime.datetime.strptime(date, '%Y-%m-%d')
    today = datetime.datetime.now()
    if today > date1:
        showerror(title='Date Error',
                  message='This car has been delivered\nPlease Return Car to auto-cancel')
        checkinvoice(w1)
    else:
        tk = tkinter.messagebox.askquestion(
            'Cancel Order', 'Are you sure you want to cancel the order - ' + invoice, icon='warning')
        if tk == 'yes':
            remove(invoice, ccode, w1)
        else:
            home(w1)


def modify_db(w1, in_vo, t_price, ex_date, f, val, bx_date):
    tk = tkinter.messagebox.askquestion(
        'Modify', 'Are you sure you want to modify order - ' + in_vo, icon='warning')
    if tk == 'yes':
        charge = t_price + 50
        msg = '''Voiture Car Rental

Your order corresponding to invoice ''' + in_vo + ''' has been successfully modified

Car Name : ''' + f[0] + f[1] + ''' 
Total Price : ''' + str(charge) + ''' AED
Current Car Returning Date : ''' + str(ex_date) + '''

Dear Customer,
     A charge of AED 50 has been added for extra modification in your order.

Regards,
Team of Voiture.'''
        sub = 'Order Modification'
        mc.execute('SELECT EMAIL FROM user WHERE PHONE="{}"'.format(phone))
        m = mc.fetchone()
        eml = m[0]
        email_alert(sub, msg, eml)
        mc.execute(
            'UPDATE buy SET CRETURN="{}" WHERE INVOICE="{}"'.format(ex_date, in_vo))
        mc.execute(
            'UPDATE buy SET CBUYDATE="{}" WHERE INVOICE="{}"'.format(bx_date, in_vo))
        mc.execute(
            'UPDATE owner SET DATOP="{}" WHERE INVOICE="{}"'.format(bx_date, in_vo))
        mc.execute(
            'UPDATE buy SET TPRICE="{}" WHERE INVOICE="{}"'.format(charge, in_vo))
        mc.execute(
            'UPDATE owner SET TPRICE="{}" WHERE INVOICE="{}"'.format(charge, in_vo))
        mdb.commit()
        showinfo(title='Successfull', message="The order have been modified.")
        home(w1)
    else:
        checkinvoice(w1, val)


def update_extra(w1, val, already, in_vo, ccode, d_b, valmain):
    totaldays = valmain + int(already.days)
    ex_date = datetime.datetime.strptime(
        d_b, "%Y-%m-%d") + datetime.timedelta(days=totaldays)
    mc.execute(
        'SELECT CCOMPANY,CNAME,CPRICE_MONTH FROM record WHERE CCODE="{}"'.format(ccode))
    f = mc.fetchone()
    price = f[2]/31
    t_price = math.ceil(price*totaldays)
    dsp1 = Label(w1, text='Your car return date will be extended to ' +
                 str(ex_date), fg='#FFAB71', bg='black').place(x=317, y=335, anchor='n')
    dsp1 = Label(w1, text='Total price will become ' + str(t_price) +
                 ' AED', fg='#FFAB71', bg='black').place(x=317, y=365, anchor='n')
    button1 = Button(w1, text='Modify', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: modify_db(
        w1, in_vo, t_price, ex_date, f, val, d_b)).place(x=317, y=440, anchor='s')
    w1.mainloop()


def update_extra2(w1, val, dys, in_no, ccde, new_value):
    mc.execute(
        'SELECT CCOMPANY,CNAME,CPRICE_MONTH FROM record WHERE CCODE="{}"'.format(ccde))
    f = mc.fetchone()
    c_name = f[0] + f[1]
    format = '%m/%d/%y'
    lastconnection = datetime.datetime.strptime(new_value, format)
    d = lastconnection.strftime('%Y-%m-%d')
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])
    k = datetime.datetime(year, month, day)
    t_dates = k + datetime.timedelta(days=dys.days)
    dsp1 = Label(w1, text='Your car return date will be extended to ' +
                 str(t_dates), fg='#FFAB71', bg='black').place(x=317, y=410, anchor='n')
    button1 = Button(w1, text='Modify', fg='white', bg='#E74B10', relief='flat', width=20,
                     command=lambda: modify_db(w1, in_no, f[2], t_dates, f, val, d)).place(x=317, y=440, anchor='n')
    w1.mainloop()


def modify_en(w1, val, in_no, ccde, dys, d_b, d_r, val2):
    img = Image.open('black.png')
    img2 = img.resize((400, 500))
    photo = ImageTk.PhotoImage(img2)
    dsp = Label(w1, image=photo, borderwidth=0).place(
        x=100, y=100, anchor='nw')
    if val2 == 'IDOU':
        new_value = IntVar()
        dsp1 = Label(w1, text='You had booked the car for ' + str(dys.days) +
                     ' days.', fg='#FFAB71', bg='black').place(x=317, y=180, anchor='n')
        dsp2 = Label(w1, text='Enter EXCESS USAGE DAYS :',
                     fg='#ffba83', bg='black').place(x=310, y=221, anchor='ne')
        ent1 = ttk.Entry(w1, width=25, textvariable=new_value).place(
            x=324, y=220, anchor='nw')
        button1 = Button(w1, text='Add', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: update_extra(
            w1, val, dys, in_no, ccde, d_b, new_value.get())).place(x=317, y=295, anchor='s')
    else:
        date1 = datetime.datetime.strptime(d_b, '%Y-%m-%d')
        today = datetime.datetime.now()
        if today > date1:
            showerror(title='Date Error',
                      message='This car has been collected')
            checkinvoice(w1)
        else:
            dsp1 = Label(w1, text='You had booked to collect car on ' + str(d_b),
                         fg='#FFAB71', bg='black').place(x=317, y=130, anchor='n')
            today = str(datetime.datetime.now())
            year = int(today[0:4])
            month = int(today[5:7])
            day = int(today[8:11])
            cal = Calendar(w1, font="ariel 8", selectmode='day',
                           year=year, month=month, day=day)
            cal.place(x=317, y=160, anchor='n')
            button1 = Button(w1, text='Add', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: update_extra2(
                w1, val, dys, in_no, ccde, cal.get_date())).place(x=317, y=355, anchor='n')
    w1.mainloop()


def modify(w1, val, invoive_no, ccode, date_b, date_r):
    days = datetime.datetime.strptime(
        date_r, "%Y-%m-%d") - datetime.datetime.strptime(date_b, "%Y-%m-%d")
    img = Image.open('bgforall.png')
    photo = ImageTk.PhotoImage(img)
    ds = Label(w1, image=photo, borderwidth=0).place(x=0, y=0, anchor='nw')
    w1.geometry('1000x500')
    dsp2 = Label(w1, text='Modify By', fg='white', bg='black', font=(
        'Ariel', 20, 'bold')).place(x=317, y=40, anchor='center')
    s = ttk.Style(w1)
    s.map('C.TButton', foreground=[('pressed', 'red'), ('active', 'green')])
    but_1 = ttk.Button(w1, text="Increase Days of Usage", width=30, style='C.TButton',  command=lambda:  modify_en(
        w1, val, invoive_no, ccode, days, date_b, date_r, 'IDOU')).place(x=300, y=70, anchor='ne')
    but_2 = ttk.Button(w1, text="Extend Day of Collection", width=30, style='C.TButton', command=lambda: modify_en(
        w1, val, invoive_no, ccode, days, date_b, date_r, 'EDOC')).place(x=334, y=70, anchor='nw')
    button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                     command=lambda: checkinvoice(w1, val)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def detailstodel(invoiceno, k, w1, val):
    ccode = k[0]
    phone = k[1]
    date = k[2]
    date1 = date.strftime('%Y-%m-%d')
    date2 = k[3]
    date3 = date2.strftime('%Y-%m-%d')
    tprice = str(k[4])
    mc.execute(
        'SELECT CCOMPANY,CNAME FROM record WHERE CCODE = "{}"'.format(ccode))
    m = mc.fetchone()
    name = m[0] + ' ' + m[1]
    dsp1 = Label(w1, text='Invoice No:', fg='#FFAB71',
                 bg='black').place(x=200, y=200, anchor='nw')
    dsp_1 = Label(w1, text=invoiceno, fg='#FFAB71',
                  bg='black').place(x=370, y=200, anchor='nw')
    dsp5 = Label(w1, text='Car Name:', fg='#FFAB71',
                 bg='black').place(x=200, y=230, anchor='nw')
    dsp_5 = Label(w1, text=name + '       ', fg='#FFAB71',
                  bg='black').place(x=370, y=230, anchor='nw')
    dsp2 = Label(w1, text='Car Delivery Date:', fg='#FFAB71',
                 bg='black').place(x=200, y=260, anchor='nw')
    dsp_2 = Label(w1, text=date1, fg='#FFAB71', bg='black').place(
        x=370, y=260, anchor='nw')
    dsp3 = Label(w1, text='Car Returning Date:', fg='#FFAB71',
                 bg='black').place(x=200, y=290, anchor='nw')
    dsp_3 = Label(w1, text=date3, fg='#FFAB71', bg='black').place(
        x=370, y=290, anchor='nw')
    dsp4 = Label(w1, text='Total Price:', fg='#FFAB71',
                 bg='black').place(x=200, y=320, anchor='nw')
    dsp_4 = Label(w1, text=tprice + '        ', fg='#FFAB71',
                  bg='black').place(x=370, y=320, anchor='nw')
    if val == "can":
        button1 = Button(w1, text='Cancel', fg='white', bg='#E74B10', relief='flat', width=20,
                         command=lambda: cancel(w1, invoiceno, ccode, date1)).place(x=317, y=400, anchor='center')
    else:
        button1 = Button(w1, text='Modify', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: modify(
            w1, val, invoiceno, ccode, date1, date3)).place(x=317, y=400, anchor='center')
    w1.mainloop()


def menuinvoice(f, w1, mb, val):
    j = dict()
    l = []
    for i in f:
        l += [i[0]]
        j[i[0]] = (i[1], i[2], i[3], i[4], i[5])
    mb.place(x=317, y=140, anchor='center')
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    for invoice in l:
        mb.menu.add_command(
            label=invoice, command=lambda d=invoice: detailstodel(d, j[d], w1, val))
    mb.place()
    w1.mainloop()


def checkinvoice(w1, val):
    w1.destroy()
    w1 = Tk()
    img = Image.open('bgforall.png')
    photo = ImageTk.PhotoImage(img)
    ds = Label(w1, image=photo, borderwidth=0).place(x=0, y=0, anchor='nw')
    w1.geometry('1000x500')
    if val == 'can':
        w1.title('Cancel Booking')
        dsp = Label(w1, text='Select Invoice To Delete', fg='white', bg='black', font=(
            'Ariel', 20, 'bold')).place(x=317, y=30, anchor='n')
    else:
        w1.title('Modify Booking')
        dsp = Label(w1, text='Select Invoice To Modify', fg='white', bg='black', font=(
            'Ariel', 20, 'bold')).place(x=317, y=30, anchor='n')
    mc.execute('SELECT * FROM buy WHERE PHONE="{}"'.format(phone))
    f = mc.fetchall()
    mb = ttk.Menubutton(w1, text='Invoice(s)')
    button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                     command=lambda: home(w1)).place(x=980, y=20, anchor='ne')
    menuinvoice(f, w1, mb, val)


def updatedetail(val2, w1, val, var):
    try:
        mc.execute(
            'UPDATE user SET {}="{}" WHERE PHONE="{}"'.format(val, var, phone))
        mdb.commit()
        showinfo(title='Successful', message=val2 + ' has been updated.')
        home(w1)
    except:
        showerror(title='Error', message=val2 + ' Could\'nt be Updated.')


def addentry(item, value, w1):
    new_value = StringVar()
    dsp1 = Label(w1, text='Enter Details', fg='#ffba83', bg='black',
                 font=('candara', 15)).place(x=317, y=280, anchor='center')
    dsp2 = Label(w1, text='Enter New ' + item, fg='#ffba83',
                 bg='black').place(x=217, y=315, anchor='nw')
    ent1 = ttk.Entry(w1, width=32, textvariable=new_value).place(
        x=220, y=340, anchor='nw')
    button2 = Button(w1, text='Submit', fg='white', bg='#E74B10', relief='flat', width=20,
                     command=lambda: updatedetail(item, w1, value, new_value.get())).place(x=317, y=430, anchor='s')
    w1.mainloop()


def updatedetail2(lno, ld, w1):
    try:
        mc.execute(
            'UPDATE user SET LICENSE="{}" WHERE PHONE="{}"'.format(lno, phone))
        mc.execute(
            'UPDATE user SET LISSUDATE="{}" WHERE PHONE="{}"'.format(ld, phone))
        mdb.commit()
        showinfo(title='Successful', message='License Details has been updated.')
        home(w1)
    except:
        showerror(title='Error', message='License Details Could\'nt be Changed.')
        updateenter('License', w1)


def updatedetail3(oldph, newph, w1):
    mc.execute('SELECT * FROM user WHERE PHONE="{}"'.format(oldph))
    i = mc.fetchone()
    if i == None:
        showerror(title='Error', message='Invalid Phone Number')
        updateenter('Phone Number', w1)
    else:
        try:
            mc.execute(
                'UPDATE user SET PHONE="{}" WHERE PHONE="{}"'.format(newph, oldph))
            mdb.commit()
            showinfo(title='Successful',
                     message='Phone Number Changed Successfully.')
            global phone
            phone = newph
        except:
            showerror(title='Error',
                      message='Phone Number Could\'nt be Changed.')
            updateenter('Phone Number', w1)
        home(w1)


def updatedetail4(oldpas, newpas, w1):
    mc.execute('SELECT * FROM user WHERE PASSWORD="{}"'.format(oldpas))
    i = mc.fetchone()
    if i == None:
        showerror(title='Error', message='Invalid Password')
        updateenter('Password', w1)
    else:
        try:
            mc.execute(
                'UPDATE user SET PASSWORD="{}" WHERE PASSWORD="{}"'.format(newpas, oldpas))
            mdb.commit()
            showinfo(title='Successful',
                     message='Password Changed Successfully.')
            global set1
            set1 = ''
        except:
            showerror(title='Error', message='Password Could\'nt be Changed.')
            updateenter('Phone Number', w1)
        login(w1)


def addentry1(value, val, w1):
    new_value = StringVar()
    new_value2 = StringVar()
    dsp1 = Label(w1, text='Enter Details', fg='#ffba83', bg='black',
                 font=('candara', 15)).place(x=317, y=250, anchor='center')
    dsp2 = Label(w1, text='Enter Old ' + value, fg='#ffba83',
                 bg='black').place(x=217, y=275, anchor='nw')
    dsp3 = Label(w1, text='Enter New ' + value, fg='#ffba83',
                 bg='black').place(x=217, y=335, anchor='nw')
    if val == 'PASS':
        ent1 = ttk.Entry(w1, width=32, textvariable=new_value,
                         show='*').place(x=220, y=300, anchor='nw')
        ent2 = ttk.Entry(w1, width=32, textvariable=new_value2,
                         show='*').place(x=220, y=360, anchor='nw')
        button2 = Button(w1, text='Submit', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: updatedetail4(
            new_value.get(), new_value2.get(), w1)).place(x=317, y=440, anchor='s')
    else:
        ent1 = ttk.Entry(w1, width=32, textvariable=new_value).place(
            x=220, y=300, anchor='nw')
        ent2 = ttk.Entry(w1, width=32, textvariable=new_value2).place(
            x=220, y=360, anchor='nw')
        button2 = Button(w1, text='Submit', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: updatedetail3(
            new_value.get(), new_value2.get(), w1)).place(x=317, y=440, anchor='s')
    w1.mainloop()


def updateenter(value, w1):
    img1 = Image.open('black.png')
    img = img1.resize((500, 500))
    photo1 = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo1, borderwidth=0).place(
        x=70, y=170, anchor='nw')
    if value == 'First Name':
        val = 'FSTNME'
        addentry(value, val, w1)
    elif value == 'Second Name':
        val = 'SNDNME'
        addentry(value, val, w1)
    elif value == 'Email':
        val = 'EMAIL'
        addentry(value, val, w1)
    elif value == 'DOB':
        new_value = StringVar()
        dsp1 = Label(w1, text='Enter Details', fg='#ffba83', bg='black', font=(
            'Candara', 15)).place(x=317, y=260, anchor='center')
        dsp2 = Label(w1, text='Enter New ' + value, fg='#ffba83',
                     bg='black').place(x=217, y=305, anchor='nw')
        ent1 = ttk.Entry(w1, width=32, textvariable=new_value).place(
            x=220, y=330, anchor='nw')
        dsp4 = Label(w1, text='(YYYY-MM-DD)', font=('dubai', 8),
                     fg='#ffba83', bg='black').place(x=217, y=354, anchor='nw')
        button2 = Button(w1, text='Submit', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: updatedetail(
            value, w1, value, new_value.get())).place(x=317, y=420, anchor='s')
        w1.mainloop()
    elif value == 'Address':
        val = 'ADDRESS'
        addentry(value, val, w1)
    elif value == 'Password':
        val = 'PASS'
        addentry1(value, val, w1)
    elif value == 'Phone Number':
        val = 'PHONE'
        addentry1(value, val, w1)
    elif value == 'License':
        new_value = StringVar()
        new_value2 = StringVar()
        dsp1 = Label(w1, text='Enter Details', fg='#ffba83', bg='black', font=(
            'candara', 15)).place(x=317, y=230, anchor='center')
        dsp2 = Label(w1, text='Enter New ' + value + ' Number',
                     fg='#ffba83', bg='black').place(x=217, y=255, anchor='nw')
        ent1 = ttk.Entry(w1, width=32, textvariable=new_value).place(
            x=220, y=280, anchor='nw')
        dsp3 = Label(w1, text='Enter New ' + value + ' Expiry Date',
                     fg='#ffba83', bg='black').place(x=217, y=320, anchor='nw')
        ent2 = ttk.Entry(w1, width=32, textvariable=new_value2).place(
            x=220, y=345, anchor='nw')
        dsp4 = Label(w1, text='(YYYY-MM-DD)', font=('dubai', 8),
                     fg='#ffba83', bg='black').place(x=217, y=370, anchor='nw')
        button2 = Button(w1, text='Submit', fg='white', bg='#E74B10', relief='flat', width=20, command=lambda: updatedetail2(
            new_value.get(), new_value2.get(), w1)).place(x=317, y=450, anchor='s')
        w1.mainloop()


def whatistobe(w1):
    w1.destroy()
    w1 = Tk()
    w1.title('Select Details')
    w1.geometry('1000x500')
    image1 = Image.open('bgforall.png')
    photo1 = ImageTk.PhotoImage(image1)
    dsp1 = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    selection = StringVar()
    s = ttk.Style(w1)
    s.configure('Wild.TRadiobutton', background='black', foreground='#ffba83')
    dsp2 = Label(w1, text='Update By', fg='white', bg='black', font=(
        'Ariel', 20, 'bold')).place(x=317, y=40, anchor='center')
    rbutton1 = ttk.Radiobutton(w1, text='Phone Number', style='Wild.TRadiobutton',
                               variable=selection, value='Phone Number').place(x=75, y=70, anchor='nw')
    rbutton2 = ttk.Radiobutton(w1, text='First Name', style='Wild.TRadiobutton',
                               variable=selection, value='First Name').place(x=75, y=95, anchor='nw')
    rbutton3 = ttk.Radiobutton(w1, text='Second Name', style='Wild.TRadiobutton',
                               variable=selection, value='Second Name').place(x=213, y=95, anchor='nw')
    rbutton4 = ttk.Radiobutton(w1, text='E-mail', style='Wild.TRadiobutton',
                               variable=selection, value='Email').place(x=489, y=70, anchor='nw')
    rbutton5 = ttk.Radiobutton(w1, text='Date Of Birth', style='Wild.TRadiobutton',
                               variable=selection, value='DOB').place(x=351, y=95, anchor='nw')
    rbutton6 = ttk.Radiobutton(w1, text='License Details', style='Wild.TRadiobutton',
                               variable=selection, value='License').place(x=351, y=70, anchor='nw')
    rbutton7 = ttk.Radiobutton(w1, text='Address',  style='Wild.TRadiobutton',
                               variable=selection, value='Address').place(x=489, y=95, anchor='nw')
    rbutton8 = ttk.Radiobutton(w1, text='Password', style='Wild.TRadiobutton',
                               variable=selection, value='Password').place(x=213, y=70, anchor='nw')
    button1 = Button(w1, text='UPDATE', width=20, fg='white', bg='#E74B10', relief='flat',
                     command=lambda: updateenter(selection.get(), w1)).place(x=317, y=135, anchor='n')
    button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                     command=lambda: home(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def view(w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Personal Details')
    mc.execute('SELECT * FROM user WHERE PHONE="{}"'.format(phone))
    m = mc.fetchone()
    image1 = Image.open('bgforall.png')
    photo1 = ImageTk.PhotoImage(image1)
    dsp1 = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    dsp2 = Label(w1, text='Your Personal Details', fg='white', bg='black', font=(
        'Ariel', 20, 'bold')).place(x=317, y=100, anchor='center')
    pne = m[0]
    nme = m[1] + ' ' + m[2]
    eml = m[3]
    dob = m[4]
    lno = m[5]
    nds = m[6]
    add = m[7]
    dspph = Label(w1, text='Customer Mobile : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=190, anchor='ne')
    dspph = Label(w1, text=pne, fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=190, anchor='nw')
    dspph = Label(w1, text='Customer Name : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=220, anchor='ne')
    dspph = Label(w1, text=nme.title(), fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=220, anchor='nw')
    dspph = Label(w1, text='E-mail : ', fg='#ffba83', bg='black',
                  font=('Century Gothic', 14)).place(x=317, y=250, anchor='ne')
    dspph = Label(w1, text=eml, fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=250, anchor='nw')
    dspph = Label(w1, text='Date Of Birth : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=280, anchor='ne')
    dspph = Label(w1, text=dob, fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=280, anchor='nw')
    dspph = Label(w1, text='License Number : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=310, anchor='ne')
    dspph = Label(w1, text=lno, fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=310, anchor='nw')
    dspph = Label(w1, text='License Expiry Date : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=340, anchor='ne')
    dspph = Label(w1, text=nds, fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=340, anchor='nw')
    dspph = Label(w1, text='Customer Address : ', fg='#ffba83', bg='black', font=(
        'Century Gothic', 14)).place(x=317, y=370, anchor='ne')
    dspph = Label(w1, text=add.title(), fg='#ffba83', bg='black', font=(
        'Century Gothic', 12)).place(x=340, y=370, anchor='nw')
    button2 = Button(w1, text='(Revert)', fg='white', bg='black', relief='flat',
                     command=lambda: home(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def logout(w1):
    w1.destroy()
    global set1, phone, local, buy_date, return_date, tprice, car_class, s_price, e_price
    local = ''
    set1 = ''
    phone = ''
    buy_date = ''
    return_date = ''
    tprice = ''
    car_class = ''
    s_price = 0
    e_price = 0
    cover()


def close(w1):
    w1.destroy()
    cover()


def home(w1):
    w1.destroy()
    w1 = Tk()
    global set1
    set1 = 'logged'
    img = Image.open('main.png')
    w1.title('Home')
    w1.geometry('1000x505')
    photo1 = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo1, borderwidth=0).place(x=0, y=0, anchor='nw')
    mc.execute('SELECT FSTNME, SNDNME FROM user WHERE PHONE="{}"'.format(phone))
    f = mc.fetchone()
    p = f[0] + ' ' + f[1]
    img = Image.open('log.png')
    img2 = img.resize((30, 30))
    img3 = ImageTk.PhotoImage(img2)
    dsp_1 = Label(w1, text='Welcome', font=('dubai', 11),
                  fg='black', bg='#FCFCFC').place(x=935, y=12, anchor='ne')
    dsp1 = Label(w1, text=p.upper(), font=('ariel', 18, 'bold'),
                 fg='#E74B10', bg='#FCFCFC').place(x=935, y=32, anchor='ne')
    but1 = Button(w1, text='Book Voiture', width=30, fg='white', bg='#E74B10',
                  relief='flat', command=lambda: classorprice(w1)).place(x=310, y=420, anchor='ne')
    but2 = Button(w1, text='Modify Bookings', width=30, fg='white', bg='#E74B10', relief='flat',
                  command=lambda: checkinvoice(w1, "mod")).place(x=395, y=400, anchor='nw')
    but1 = Button(w1, text='Cancel Bookings', width=30, fg='white', bg='#E74B10', relief='flat',
                  command=lambda: checkinvoice(w1, "can")).place(x=395, y=440, anchor='nw')
    but1 = Button(w1, image=img3, borderwidth=0, bg="#FCFCFC", relief='flat',
                  command=lambda: logout(w1)).place(x=980, y=26, anchor='ne')
    but1 = Button(w1, text='View Details', fg='black', bg='#FCFCFC',
                  relief='flat', command=lambda: view(w1)).place(x=935, y=70, anchor='ne')
    but1 = Button(w1, text='Update Personal Details', fg='white', bg='#E74B10', relief='flat',
                  width=30, command=lambda: whatistobe(w1)).place(x=690, y=420, anchor='nw')
    w1.mainloop()


def validatelogin(user, pas, w1):
    mc.execute('SELECT PHONE,PASSWORD FROM user WHERE PHONE="{}"'.format(user))
    f = mc.fetchone()
    if f == None:
        showerror(title='Error', message='This is an Invalid Password or Username')
    else:
        user1 = f[0]
        pass1 = f[1]
        if user1 == user and pass1 == pas:
            global phone
            phone = user
            global set1
            set1 = "logged"
            if local == '':
                home(w1)
            else:
                usagedates(w1)
        else:
            showerror(title='Error',
                      message='This is an Invalid Password or Username')


def temporary2(w1):
    global set1
    set1 = ''
    w1.destroy()
    cover()


def dateformat(v1):
    try:
        d1 = datetime.datetime.strptime(v1, '%Y-%m-%d')
    except:
        showerror(title='Error', message='Invalid Date Format')


def resetcode():
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'h', 'i', 'j', 'k', 'l']
    r = random.choice(l)
    j = random.choice(l)
    k = random.choice(l)
    p = random.choice(l)
    q = random.choice(l)
    o = random.choice(a)
    otp = r + j + k + p + q + o
    return otp


def otp():
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    r = random.choice(l)
    j = random.choice(l)
    k = random.choice(l)
    p = random.choice(l)
    q = random.choice(l)
    otp = r+j+k+p+q
    return otp


def checkotp(otp_e, otp_c, w1, all_values):
    if otp_e == otp_c:
        try:
            phone = all_values[0]
            fstnme = all_values[1].capitalize()
            sndnme = all_values[2].capitalize()
            email = all_values[3]
            d_o_b = all_values[4]
            licno = all_values[5]
            licd_es = all_values[6]
            address = all_values[7]
            password = all_values[8]
            mc.execute('INSERT INTO user VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                phone, fstnme, sndnme, email, d_o_b, licno, licd_es, address, password))
            mdb.commit()
            showinfo(title='Saved', message='All records saved successfully')
        except:
            showerror(title='Error', message='Records could\'nt be saved')
        login(w1)
    else:
        showerror(title='Error', message='OTP does not match')


def otpentry(otppr, w1, all_values, eml):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('OTP Check')
    photo = Image.open('otp.png')
    photo1 = ImageTk.PhotoImage(photo)
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    otp2 = StringVar(w1)
    dsp2 = Label(w1, text=eml, bg='#ffffff', fg="#909497",
                 font='calibri 11').place(x=540, y=168, anchor='w')
    entr = Entry(w1, textvariable=otp2, relief='flat', fg="black",
                 bg="#fbfbfb", width=75).place(x=278, y=311, anchor='w')
    button = Button(w1, text='Validate OTP', bg='#00a0d2', fg='white', relief='flat', width=20, height=2,
                    command=lambda: checkotp(otp2.get(), otppr, w1, all_values)).place(x=263, y=368, anchor='w')
    but2 = Button(w1, text='(Revert)', bg='#c3c3c3', fg='white', relief='flat',
                  command=lambda: signin(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def emailvalid(eml, w1, all_values, otpcomp):
    if '.com' in eml:
        if '@' in eml:
            otpentry(otpcomp, w1, all_values, eml)
        else:
            showerror(title='Error', message='E-mail has some mistakes')
    else:
        showerror(title='Error', message='E-mail has some mistakes')


def validate(password):
    if len(password) >= 8:
        if ('_' in password) or ('@' in password) or ('#' in password) or ('.' in password) or ('$' in password) or ('!' in password) or ('&' in password):
            if password in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwqyz1234567890~!@#$%^&*()_+=<>?P{}:':
                showinfo(title='Validate', message='Password is strong enough')
            else:
                showinfo(title='Weak',
                         message='Password is weak.\nCan be made strong')
        else:
            showinfo(title='Weak', message='Password is weak.\nCan be made strong')
    else:
        showerror(title='Error', message='Password must 8 character long')


def validate_all_entry(fne, sne, eml, pas, pne, dob, lno, les, add, w1, otpcomp):
    mc.execute('SELECT * FROM user WHERE EMAIL="{}"'.format(eml))
    f = mc.fetchone()
    mc.execute('SELECT * FROM user WHERE PASSWORD="{}"'.format(pas))
    g = mc.fetchone()
    mc.execute('SELECT * FROM user WHERE PHONE="{}"'.format(pne))
    h = mc.fetchone()
    mc.execute('SELECT * FROM user WHERE LICENSE="{}"'.format(lno))
    j = mc.fetchone()
    dateformat(dob)
    dateformat(les)
    today = datetime.datetime.now()
    dt = parse(str(today))
    l = dt.date()
    p = str(l)
    All_values = [pne, fne, sne, eml, dob, lno, les, add, pas]
    if f == None and g == None and h == None and j == None:
        if les > p:
            if len(pas) >= 8:
                msg = '''VOITURE CAR RENTAL
        
    Dear Customer,
       Your one-time-password for sigining in to voiture is ''' + otpcomp + '''.
        
    Regards,
    Team of Voiture.'''
                sub = 'OTP for logging in'
                email_alert(sub, msg, eml)
                emailvalid(eml, w1, All_values, otpcomp)
            else:
                showerror(title='Error',
                          message='Password must be 8 characters long')
        else:
            showerror(title='Error', message='License already expired.')
    else:
        if f != None:
            showerror(title='Error', message='This Email already exists.')
        elif g != None:
            showerror(title='Error', message='This Password already exists.')
        elif h != None:
            showerror(title='Error', message='This Phone Number already exists.')
        elif j != None:
            showerror(title='Error', message='This License already exists.')


def signin(w1):
    w1.destroy()
    w1 = Tk()
    w1.title('Create Account')
    w1.geometry('1000x500')
    fname = StringVar()
    sname = StringVar()
    email = StringVar()
    pas = StringVar()
    phone = StringVar()
    dob = StringVar()
    ln = StringVar()
    dis = StringVar()
    add = StringVar()
    photo = Image.open('signin.png')
    photo1 = ImageTk.PhotoImage(photo)
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp_1 = Label(w1, text='First Name: ', bg='#ffba83').place(
        x=65, y=76, anchor='nw')
    ent_1 = ttk.Entry(w1, width=50, textvariable=fname).place(
        x=500, y=77, anchor='ne')
    dsp_2 = Label(w1, text='Second Name: ', bg='#ffba83').place(
        x=65, y=106, anchor='nw')
    ent_3 = ttk.Entry(w1, width=50, textvariable=sname).place(
        x=500, y=107, anchor='ne')
    dsp_2 = Label(w1, text='E-mail: ',
                  bg='#ffba83').place(x=65, y=136, anchor='nw')
    ent_4 = ttk.Entry(w1, width=50, textvariable=email).place(
        x=500, y=137, anchor='ne')
    dsp_2 = Label(w1, text='Password: ', bg='#ffba83').place(
        x=65, y=166, anchor='nw')
    ent_5 = ttk.Entry(w1, width=50, textvariable=pas,
                      show='*').place(x=500, y=167, anchor='ne')
    but_1 = ttk.Button(w1, text='Validate Password', width=20, command=lambda: validate(
        pas.get())).place(x=500, y=196, anchor='ne')
    dsp_2 = Label(w1, text='Phone Number: ', bg='#ffba83').place(
        x=65, y=230, anchor='nw')
    ent_6 = ttk.Entry(w1, width=50, textvariable=phone).place(
        x=500, y=229, anchor='ne')
    dsp_2 = Label(w1, text='Date of Birth: ', bg='#ffba83').place(
        x=65, y=260, anchor='nw')
    ent_7 = ttk.Entry(w1, width=50, textvariable=dob).place(
        x=500, y=259, anchor='ne')
    dsp_2 = Label(w1, text='(YYYY-MM-DD)', font=('dubai', 8),
                  bg='#ffba83').place(x=275, y=280, anchor='ne')
    dsp_2 = Label(w1, text='License Number: ', bg='#ffba83').place(
        x=65, y=309, anchor='nw')
    ent_6 = ttk.Entry(w1, width=50, textvariable=ln).place(
        x=500, y=310, anchor='ne')
    dsp_2 = Label(w1, text='License Expiry Date: ',
                  bg='#ffba83').place(x=65, y=339, anchor='nw')
    ent_7 = ttk.Entry(w1, width=50, textvariable=dis).place(
        x=500, y=340, anchor='ne')
    dsp_2 = Label(w1, text='(YYYY-MM-DD)', bg='#ffba83',
                  font=('dubai', 8)).place(x=275, y=361, anchor='ne')
    dsp_2 = Label(w1, text='Address: ', bg='#ffba83').place(
        x=65, y=391, anchor='nw')
    ent_7 = ttk.Entry(w1, width=50, textvariable=add).place(
        x=500, y=394, anchor='ne', height=30)
    otppr = otp()
    s = ttk.Style(w1)
    s.map('C.TButton', foreground=[('pressed', 'red'), ('active', 'green')])
    button1 = ttk.Button(w1, text='Sign Up', width=30, style="C.TButton", command=lambda: validate_all_entry(fname.get(), sname.get(
    ), email.get(), pas.get(), phone.get(), dob.get(), ln.get(), dis.get(), add.get(), w1, otppr)).place(x=284, y=472, anchor='s')
    button2 = Button(w1, text='(Revert)', bg='white', fg='black', relief='flat',
                     command=lambda: login(w1)).place(x=980, y=100, anchor='ne')
    w1.mainloop()


def check_pass(pne, pas1, pasr, w1):
    if pas1 == pasr:
        try:
            mc.execute(
                'UPDATE user SET PASSWORD="{}" WHERE PHONE="{}"'.format(pas1, pne))
            mdb.commit()
        except:
            showerror(title='Error', message='Password could\'nt be updated')
        login(w1)
    else:
        showerror(title='Error', message='Passwords do not match')


def nw_pass_entry(phone1, w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('300x400')
    w1.title('Reset Password')
    photo = Image.open('bg4.png')
    photo0 = photo.resize((300, 190))
    photo1 = ImageTk.PhotoImage(photo0)
    new_pass = StringVar()
    new_pass_re = StringVar()
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp_1 = Label(w1, text='New Password').place(x=50, y=220, anchor='nw')
    ent_1 = ttk.Entry(w1, textvariable=new_pass, width=32,
                      show='*').place(x=53, y=245, anchor='nw')
    dsp_2 = Label(w1, text='Re-enter Password').place(x=50, y=275, anchor='nw')
    ent_2 = ttk.Entry(w1, textvariable=new_pass_re, width=32,
                      show='*').place(x=53, y=300, anchor='nw')
    but_1 = ttk.Button(w1, text='SAVE', width=30, command=lambda: check_pass(
        phone1, new_pass.get(), new_pass_re.get(), w1)).place(x=150, y=375, anchor='s')
    w1.mainloop()


def checkrc(pne, rc_e, rc_c, w1):
    if rc_e == rc_c:
        nw_pass_entry(pne, w1)
    else:
        showerror(title='Error', message='Reset code error')


def resetentry(w1, pne, otp, eml):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Code Check')
    photo = Image.open('otp.png')
    photo1 = ImageTk.PhotoImage(photo)
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    otp2 = StringVar(w1)
    dsp2 = Label(w1, text=eml, bg='#ffffff', fg="#909497",
                 font='calibri 11').place(x=540, y=168, anchor='w')
    entr = Entry(w1, textvariable=otp2, relief='flat', fg="black",
                 bg="#fbfbfb", width=75).place(x=278, y=311, anchor='w')
    button = Button(w1, text='Validate Reset Code', bg='#00a0d2', fg='white', relief='flat', width=20,
                    height=2, command=lambda: checkrc(pne, otp2.get(), otp, w1)).place(x=263, y=368, anchor='w')
    but2 = Button(w1, text='(Revert)', bg='#c3c3c3', fg='white', relief='flat',
                  command=lambda: enter_phone(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def validate_email(eml, phne, w1):
    mc.execute('SELECT EMAIL FROM user WHERE PHONE="{}"'.format(phne))
    f = mc.fetchone()
    if f == None:
        showerror(title='Error', message='Invalid Phone Number')
    elif f[0] == eml:
        p = resetcode()
        msg = '''VOITURE CAR RENTAL
    Dear Customer,
        Your reset code for password recovery is ''' + p + '''
        
    Regards,
    Team of Voiture.'''
        sub = 'Password Reset'
        email_alert(sub, msg, f[0])
        resetentry(phne, w1, p, eml)
    else:
        showerror(title='Error', message='Invlid Email')


def enter_phone(w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Reset Password')
    photo = Image.open('bgforall2.png')
    photo1 = ImageTk.PhotoImage(photo)
    e_mail = StringVar()
    phone1 = StringVar()
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp0 = Label(w1, text='Forgot Password', bg='#131311', fg='white',
                 font='ariel 20 bold').place(x=500, y=170, anchor='center')
    dsp_1 = Label(w1, bg='#131311', fg='white', text='We will send a 6 character code to your email').place(
        x=500, y=200, anchor='center')
    dsp1 = Label(w1, text='E-mail', bg='black',
                 fg='white').place(x=395, y=240, anchor='nw')
    ent1 = ttk.Entry(w1, textvariable=e_mail, width=32).place(
        x=398, y=265, anchor='nw')
    dsp2 = Label(w1, text='Phone Number', bg='black',
                 fg='white').place(x=395, y=295, anchor='nw')
    ent2 = ttk.Entry(w1, textvariable=phone1, width=32).place(
        x=398, y=320, anchor='nw')
    but1 = Button(w1, text='Send Code', width=30, fg='white', bg='#E74B10', relief='flat',
                  command=lambda: validate_email(e_mail.get(), phone1.get(), w1)).place(x=500, y=420, anchor='s')
    but2 = Button(w1, text='(Revert)', bg='black', fg='white', relief='flat',
                  command=lambda: login(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def login(w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Login')
    w1.config(bg='white')
    user = StringVar()
    pas = StringVar()
    icon1 = PhotoImage(file="logologin.png")
    photo1 = ImageTk.PhotoImage(Image.open('bglogin.png'))
    dsp_1 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp_2 = Label(w1, text='Phone Number', bg='#fffcf7', fg='#989590',
                  font='calibri 10').place(x=112, y=200, anchor='nw')
    dsp_3 = Label(w1, text='Password', bg='#fffcf7', fg='#989590',
                  font='calibri 10').place(x=112, y=263, anchor='nw')
    ent_1 = Entry(w1, width=40, textvariable=user, relief='flat',
                  bg='#fffcf7').place(x=114, y=219, anchor='nw')
    ent_2 = Entry(w1, width=40, textvariable=pas, show='*',
                  relief='flat', bg='#fffcf7').place(x=114, y=282, anchor='nw')
    but_6 = Button(w1, width=12, relief='flat', bg='#feb06e', fg='white', text='LOGIN', font='calibri 11',
                   command=lambda: validatelogin(user.get(), pas.get(), w1)).place(x=116, y=335, anchor='nw')
    but_7 = Button(w1, relief='flat', bg='#ffba83', fg='white', text='(Revert)',
                   command=lambda: temporary2(w1)).place(x=980, y=20, anchor='ne')
    but_8 = Button(w1, text='Forgot Password', relief='flat', bg='#fffcf7',
                   fg='blue', command=lambda: enter_phone(w1)).place(x=296, y=305, anchor='n')
    but_5 = Button(w1, text='SIGN UP', bg='#fffcf7', fg='#feb06e', relief='flat', font=(
        'airel', 9, 'bold'), command=lambda: signin(w1)).place(x=240, y=383, anchor='nw')
    w1.mainloop()


def pp(w1):
    w1.destroy()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.resize(1200, 500)
    web.setWindowTitle("Privacy Policy")
    web.load(QUrl(
        "file:///C:/Users/ds_20/Desktop/Car%20Rental%20System/privacy%20policy.html"))
    web.show()
    cover()


def abtus(w1, val):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    photo = Image.open(val)
    photo1 = ImageTk.PhotoImage(photo)
    sp_1 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    if val == 'aboutus.png':
        w1.title('About Us')
        but2 = Button(w1, text='(Revert)', bg='#D3E6FB', fg='black', relief='flat',
                      command=lambda: close(w1)).place(x=980, y=10, anchor='ne')
        sp_2 = Label(w1, bg='#D3E6FB', fg='black', text="In UAE we are tied with THRIFTY RENTAL COMPANY and follow their",
                     font='dubai 7').place(x=10, y=495, anchor='sw')
        but3 = Button(w1, text='Privacy Policy', bg='#D3E6FB', fg='black', font=(
            'dubai', 7), relief='flat', command=lambda: pp(w1)).place(x=270, y=498, anchor='sw')
    else:
        w1.title('Contact us')
        sp_2 = Label(w1, bg='#CCE3D3', fg='black', text="In UAE we are tied with THRIFTY RENTAL COMPANY and follow their",
                     font='dubai 7').place(x=10, y=495, anchor='sw')
        but3 = Button(w1, text='Terms and Conditions', bg='#CCE3D3', fg='black', font=(
            'dubai', 7), relief='flat', command=lambda: terms(w1)).place(x=270, y=498, anchor='sw')
        but2 = Button(w1, text='(Revert)', bg='#A8D2B5', fg='black', relief='flat',
                      command=lambda: close(w1)).place(x=980, y=10, anchor='ne')
    w1.mainloop()


def terms(w1):
    w1.destroy()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.resize(1200, 500)
    web.setWindowTitle("Terms and Conditions")
    web.load(QUrl("file:///C:/Users/ds_20/Desktop/Car%20Rental%20System/terms.html"))
    web.show()
    cover()


def faq(w1):
    w1.destroy()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.resize(1200, 500)
    web.setWindowTitle("FAQ's")
    web.load(QUrl("file:///C:/Users/ds_20/Desktop/Car%20Rental%20System/faq2.html"))
    web.show()
    cover()


def why(w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    photo = Image.open("whychoseus.png")
    w1.title('Why Choose Voiture')
    photo1 = ImageTk.PhotoImage(photo)
    sp_1 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    but2 = Button(w1, text='(Revert)', bg='#d8f5f9', fg='black', relief='flat',
                  command=lambda: close(w1)).place(x=980, y=10, anchor='ne')
    w1.mainloop()


def authorization(w1):
    w1.destroy()
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Admin Entry')
    photo = Image.open('bgforall2.png')
    photo1 = ImageTk.PhotoImage(photo)
    auth = StringVar()
    dsp_0 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    dsp0 = Label(w1, text='Authorized Personnel', bg='#131311', fg='white',
                 font='ariel 20 bold').place(x=500, y=170, anchor='center')
    sp1 = Label(w1, text='Authorization Code', bg='black',
                fg='white').place(x=395, y=275, anchor='nw')
    ent1 = ttk.Entry(w1, textvariable=auth, width=32).place(
        x=398, y=300, anchor='nw')
    but1 = Button(w1, text='Validate Code', width=30, fg='white', bg='#E74B10', relief='flat',
                  command=lambda: validate_auth(w1, auth.get())).place(x=500, y=420, anchor='s')
    but2 = Button(w1, text='(Revert)', bg='black', fg='white', relief='flat',
                  command=lambda: close(w1)).place(x=980, y=20, anchor='ne')
    w1.mainloop()


def fn(user):
    global auth_code
    auth_code = user


def validate_auth(w1, acode):
    w1.destroy()
    if acode == "manGER_2045":
        print()
        print('_'*162)
        print()
        print(' '*73, 'WELCOME MANAGER')
        print('_'*162)
        temp = True
        while temp == True:
            print()
            print()
            user = input(' '*69 + 'Enter Username : ')
            pas1 = input(' '*67 + 'Enter Password : ')
            print()
            print('_'*162)
            with open('adminman.csv', 'r') as csvfile:
                datareader = csv.reader(csvfile)
                for row in datareader:
                    if user in row:
                        if pas1 in row:
                            fn(user)
                            options()
                else:
                    showerror(title='Error',
                              message='Invalid Username or Password')
    elif acode == "TEChni_7890":
        print()
        print('_'*162)
        print()
        print(' '*72, 'WELCOME TECHNICIAN')
        print('_'*162)
        temp = True
        while temp == True:
            print()
            print()
            user = input(' '*69 + 'Enter Username : ')
            pas1 = input(' '*67 + 'Enter Password : ')
            print()
            print('_'*162)
            with open('admintech.csv', 'r') as csvfile:
                datareader = csv.reader(csvfile)
                for row in datareader:
                    if user in row:
                        if pas1 in row:
                            fn(user)
                            options2()
                else:
                    showerror(title='Error',
                              message='Invalid Username or Password')
    elif acode == "oWNer_2098.3":
        print()
        print('_'*162)
        print()
        print(' '*74, 'WELCOME OWNER')
        print('_'*162)
        temp = True
        while temp == True:
            print()
            print()
            user = input(' '*69 + 'Enter Username : ')
            pas1 = input(' '*67 + 'Enter Password : ')
            print()
            print('_'*162)
            with open('adminown.csv', 'r') as csvfile:
                datareader = csv.reader(csvfile)
                for row in datareader:
                    if user in row:
                        if pas1 in row:
                            fn(user)
                            options3()
                else:
                    showerror(title='Error',
                              message='Invalid Username or Password')
    elif acode == "Acc_nt@23._0":
        print()
        print('_'*162)
        print()
        print(' '*73, 'WELCOME CASHIER')
        print('_'*162)
        temp = True
        while temp == True:
            print()
            print()
            user = input(' '*69 + 'Enter Username : ')
            pas1 = input(' '*67 + 'Enter Password : ')
            print()
            print('_'*162)
            with open('adminacc.csv', 'r') as csvfile:
                datareader = csv.reader(csvfile)
                for row in datareader:
                    if user in row:
                        if pas1 in row:
                            fn(user)
                            options4()
                else:
                    showerror(title='Error',
                              message='Invalid Username or Password')
    else:
        showerror(title='Invaid Entry', message='Invalid Authorization Code')
        cover()


def opentxt():
    print()
    print()
    with open('instructions.txt') as f:
        contents = f.read()
        print(contents)
    print()
    print('_'*162)


def return_w2(w1):
    w1.destroy()
    byethebye()


def add_pass(w1,au_code, password, desg):
    l = [au_code,password]
    if desg == 'Manager':
        with open('adminman.csv','a',newline='\n') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(l)
            showinfo(title='Successful', message='Password successfully added')
    elif desg == 'Technician':
        with open('admintech.csv','a',newline='\n') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(l)
            showinfo(title='Successful', message='Password successfully added')
    elif desg == 'Owner':
        with open('adminown.csv','a',newline='\n') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(l)
            showinfo(title='Successful', message='Password successfully added')
    elif desg == 'Cashier':
        with open('adminacc.csv','a',newline='\n') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(l)
            showinfo(title='Successful', message='Password successfully added')
    else:
        showwarning(title='Password Not Added', message='The entered Designation has no section to access in AUTHORIZED PERSONNEL')
    return_w2(w1)


def validate_all_entry_work(w1, au_code, worker_name, worker_gmail, worker_sal, desg, password):
    if '@' in worker_gmail:
        if worker_sal.isdigit():
            if desg in ('Manager','Owner','Technician','Salesman','Driver','Accountant'):
                try:
                    mc.execute('INSERT INTO workers VALUES("{}","{}","{}",{},"{}")'.format(au_code, worker_name, worker_gmail, worker_sal, desg))
                    mdb.commit()
                    showinfo(title='Successful',message='Records saved Successfully')
                    add_pass(w1, au_code, password, desg)
                except:
                    showerror(title='Error', message='Records Could\'nt be saved')
            else:
                showerror(title='Error', message='Invalid Worker Designation')
        else:
            showerror(title='Error', message='Invalid Salary Entered')
    else:
        showerror(title='Error', message='Invalid Email Detected')


def doing():
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Performa')
    img = Image.open('performa3.png')
    photo = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo, borderwidth=0).place(x=0, y=0, anchor='nw')
    acde = StringVar()
    entcde = Entry(w1, textvariable=acde, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=518, y=178, anchor='w')
    wnme = StringVar()
    entcom = Entry(w1, textvariable=wnme, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=518, y=235, anchor='w')
    wgml = StringVar()
    entnme = Entry(w1, textvariable=wgml, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=518, y=295, anchor='w')
    wsal = StringVar()
    entclr = Entry(w1, textvariable=wsal, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=518, y=355, anchor='w')
    wpass = StringVar()
    entclr = Entry(w1, textvariable=wpass, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=518, y=410, anchor='w')
    desg = StringVar()
    entclr = Entry(w1, textvariable=desg, fg='black', bg='white', relief='flat', font=(
        'century gothic', '10'), width=38).place(x=706, y=477, anchor='w')
    but2 = Button(w1, text='(Submit)', bg='#ffba83', fg='black', relief='flat', command=lambda: validate_all_entry_work(
        w1, acde.get(), wnme.get(), wgml.get(), wsal.get(), desg.get(), wpass.get())).place(x=980, y=20, anchor='ne')
    but3 = Button(w1, text='(Revert)', bg='#ffba83', fg='black', relief='flat',
                  command=lambda: return_w2(w1)).place(x=20, y=20, anchor='nw')
    w1.mainloop()


def byethebye():
    temp2 = True
    while temp2 == True:
        print()
        print()
        print(' '*60, 'You have the following options to execute.')
        print()
        print(' '*70 + '1. Add New Workers')
        print(' '*70 + '2. Remove Workers')
        print(' '*70 + '3. Update Worker Salary')
        print(' '*70 + '4. Display Workers')
        print(' '*70 + '5. Display on Code Search')
        print(' '*70 + '6. Calculate Total Salary')
        print(' '*70 + '7. To Revert')
        print()
        print('_'*162)
        print()
        print()
        choice2 = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice2 == '1':
            print()
            print()
            print(' '*69, 'Process Done In Perfoma')
            print()
            print('_'*162)
            doing()
        elif choice2 == '2':
            print()
            print()
            a_code2 = input(' '*63 + 'Enter Worker Authorized User Code : ')
            print()
            print('_'*162)
            mc.execute(
                'SELECT * FROM workers WHERE AUTH_CODE="{}"'.format(a_code2))
            f = mc.fetchone()
            if f == None:
                showerror(title='Error', message='Invalid Username')
            else:
                try:
                    mc.execute(
                        'DELETE FROM workers WHERE AUTH_CODE="{}"'.format(a_code2))
                    mdb.commit()
                    showinfo(title='Successfull',
                             message='Worker Removed Successfully')
                except:
                    showerror(title='Unsuccessful',
                              message='Worker not Removed')
        elif choice2 == '4':
            print()
            print()
            print('All Company Worker Details have been displayed.')
            table = PrettyTable(['Username Code', 'Worker Name',
                                'Worker E-mail', 'Worker Salary', 'Worker Designation'])
            print()
            mc.execute('SELECT * FROM workers')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
        elif choice2 == '5':
            print()
            print()
            acode2 = input(' '*63 + 'Enter Worker Authorized User Code : ')
            print()
            print('_'*162)
            mc.execute(
                'SELECT * FROM workers WHERE AUTH_CODE="{}"'.format(acode2))
            f = mc.fetchall()
            if f == None:
                showerror(title='Error', message='Invalid Username')
            else:
                print()
                print()
                print('All Company Worker Details have been displayed.')
                table = PrettyTable(
                    ['Username Code', 'Worker Name', 'Worker E-mail', 'Worker Salary', 'Worker Designation'])
                print()
                for i in f:
                    table.add_row(i)
                print(table)
                print()
                print('_'*162)
                time.sleep(10)
        elif choice2 == '3':
            print()
            print()
            a_code2 = input(' '*63 + 'Enter Worker Authorized User Code : ')
            print()
            print('_'*162)
            mc.execute(
                'SELECT SALARY FROM workers WHERE AUTH_CODE="{}"'.format(a_code2))
            f = mc.fetchone()
            if f == None:
                showerror(title='Error', message='Invalid Username')
            else:
                print()
                print()
                print(' '*66 + 'Current Worker SALARY - ' + str(f[0]))
                print()
                sal = input(' '*66 + 'Enter New Worker Salary : ')
                print()
                print('_'*162)
                if sal.isdigit():
                    try:
                        mc.execute(
                            'UPDATE workers SET SALARY={} WHERE AUTH_CODE="{}"'.format(sal, a_code2))
                        mdb.commit()
                        showinfo(title='Successful',
                                 message='Updation Successful')
                    except:
                        showerror(title='Unsuccessful',
                                  message='Updation Unsuccessful')
                else:
                    showerror(title='Error', message='Invalid Entry Detected')
        elif choice2 == '6':
            mc.execute('SELECT SUM(SALARY) FROM workers')
            f = mc.fetchone()
            t_sal = f[0]
            print()
            print()
            print(' '*50, 'TOTAL MONEY TO BE GIVEN BY VOTURE AS SALARY IS - ' + str(t_sal))
            print()
            print('_'*162)
        elif choice2 == '7':
            temp2 = False
            options3()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def options3():
    mc.execute('SELECT NAME_W FROM workers WHERE AUTH_CODE="{}"'.format(auth_code))
    f = mc.fetchone()
    name = f[0]
    print()
    print()
    print('Hello', name + '. You are given the following commands to execute. Read through the options carefully and enter your choice in the given area of query.')
    print()
    print()
    print(' '*69, '1. See RENTALS Database')
    print(' '*69, '2. See SERVICE Database')
    print(' '*69, '3. See OWNERS Database')
    print(' '*69, '4. See Company Performance')
    print(' '*69, '5. Read Given Instructions')
    print(' '*69, '6. Go To Workers DB')
    print(' '*69, '7. Change Password')
    print(' '*69, '8. Sign Out from Owner')
    print()
    print('_'*162)
    temp = True
    while temp == True:
        print()
        print()
        choice = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice == '1':
            print()
            print()
            print('All Placed Orders Table have been displayed along with their expected return date for rentals without remark - \'Rental Completed\'')
            print()
            table = PrettyTable(['INVOICE NUMBER', 'CAR CODE', 'BUYER PHONE',
                                'CAR COLLECT DATE', 'CAR RETURN DATE (EXPECTED)', 'TOTAL PRICE', 'REMARK'])
            mc.execute('SELECT * FROM buy')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            options3()
        elif choice == '2':
            print()
            print()
            print('All Service Records Details have been displayed.')
            print()
            table = PrettyTable(['SERVICE CODE', 'CAR CODE', 'SERVICE REPORT',
                                'SERVICE EXPENSE', 'SPL. REPAIR REPORT', 'SPL. REPAIR EXPENSE'])
            mc.execute('SELECT * FROM service')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            options3()
        elif choice == '3':
            print()
            print()
            print('All Company Profits(+) and Loss(-)  have been displayed.')
            table = PrettyTable(
                ['PROFIT/LOSS CODE', 'TOTAL PRICE', 'DATE OF MONEY ENTRY'])
            print()
            mc.execute('SELECT * FROM owner')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            options3()
        elif choice == '4':
            today = datetime.datetime.today()
            year = today.year
            mc.execute('select SUM(TPRICE),MONTHNAME(DATOP) from owner where TPRICE>0 and YEAR(DATOP)={} GROUP BY MONTH(DATOP) ORDER BY MONTH(DATOP)'.format(year))
            f = mc.fetchall()
            month = []
            profit = []
            tprofit = 0
            for i in f:
                tprofit += i[0]
                profit.append(i[0])
                month.append(i[1])
            mc.execute('select SUM(TPRICE),MONTHNAME(DATOP) from owner where TPRICE<0 and YEAR(DATOP)={} GROUP BY MONTH(DATOP) ORDER BY MONTH(DATOP)'.format(year))
            j = mc.fetchall()
            month2 = []
            loss = []
            tloss = 0
            for i in j:
                tloss += i[0]
                loss.append(abs(i[0]))
                month2.append(i[1])
            if month == month2:
                # plot bars in stack manner
                plt.bar(month, profit, color='r')
                plt.bar(month, loss, bottom=profit, color='b')
                plt.xlabel("Months")
                plt.ylabel("AED")
                plt.legend(["Profit", "Loss"])
                plt.title(
                    "Company Monthly Performance for the Year " + str(year))
                plt.show()
            return_c = tprofit + tloss
            today = datetime.datetime.today()
            today2 = today.strftime('%Y-%m-%d')
            print()
            print()
            print(' '*56, 'PROFIT OF COMPANY TILL ', today2, ' IS : ', tprofit)
            print(' '*56, 'EXPENSE OF COMPANY TILL ',
                  today2, ' IS : ', abs(tloss))
            print(' '*56, 'TOTAL RETURN OF COMPANY TILL DATE : ', return_c)
            print()
            print('_'*162)
            time.sleep(5)
            options3()
        elif choice == '6':
            byethebye()
        elif choice == '5':
            opentxt()
        elif choice == '7':
            changepass("adminown.csv")
        elif choice == '8':
            showinfo(title='Signed Out',
                     message='Technician Successfully Signed Out')
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            cover()
        elif choice == '6':
            doing()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def email_sent(w1, carcode, servicecode):
    w1.destroy()
    sub = 'Service Report Filed'
    msg = '''VOITURE TECHNICIAN
    
Hello Manager,
The car you have spaced in the garage has been successfully serviced.
The Service Report has also been filed under the number ''' + servicecode + ''' .
Car Code : ''' + carcode + '''

Regards,
Technician'''
    email_alert(sub, msg, 'cashiers.voiture22@gmail.com')
    options2()


def validate_ser(w1, car_code, service_code, service_reason, service_exp, repair_reason, repair_exp):
    mc.execute('SELECT * FROM service WHERE SERVICECODE="{}"'.format(service_code))
    f = mc.fetchone()
    if f == None:
        if 'CD' in car_code and len(car_code) == 6:
            if 'CD' in service_code and len(car_code) == 6:
                if service_reason != '':
                    if str(service_exp).isdigit():
                        try: 
                            expense = -abs(int(service_exp))
                            today = datetime.datetime.today()
                            today2 = today.strftime('%y-%m-%d')
                            mc.execute('INSERT INTO service VALUES("{}","{}","{}",{},"{}",{})'.format(service_code, car_code, service_reason, service_exp, repair_reason, repair_exp))
                            mc.execute('INSERT INTO owner VALUES("{}",{},"{}")'.format(service_code, expense, today2))
                            mdb.commit()
                            showinfo(title='Successful',
                                     message='Service Report Filed Successfully')
                            email_sent(w1, car_code, service_code)
                        except:
                            showerror(title='Error',
                                  message='Report Not Saved')
                    else:
                        showerror(title='Error',
                                  message='Invalid Entry in Service Expense')
                else:
                    showerror(title='Error',
                              message='Dont leave Service Explanation empty')
            else:
                showerror(title='Error',
                          message='Invalid Entry in Service Code')
        else:
            showerror(title='Error', message='Invalid Entry in Car Code')
    else:
        showerror(title='Error', message='This Service Code already exist.')


def return_w3(w1):
    w1.destroy()
    options2()


def options2():
    mc.execute('SELECT NAME_W FROM workers WHERE AUTH_CODE="{}"'.format(auth_code))
    f = mc.fetchone()
    name = f[0]
    print()
    print()
    print('Hello', name + '. You are given the following commands to execute. Read through the options carefully and enter your choice in the given area of query.')
    temp = True
    print()
    print()
    print(' '*67, '1. File a Service Report')
    print(' '*67, '2. See Service Database')
    print(' '*67, '3. Search for Service in DB')
    print(' '*67, '4. Read given Instructions')
    print(' '*67, '5. Change Password')
    print(' '*67, '6. Sign Out from technician')
    print()
    print('_'*162)
    while temp == True:
        print()
        print()
        choice = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice == '1':
            print()
            print()
            print(' '*69, 'Process Done In Perfoma')
            print()
            print('_'*162)
            w1 = Tk()
            w1.geometry('1000x500')
            w1.title('Service Report')
            img = Image.open('performa2.png')
            photo = ImageTk.PhotoImage(img)
            dsp = Label(w1, image=photo, borderwidth=0).place(
                x=0, y=0, anchor='nw')
            ccode = StringVar()
            entcde = Entry(w1,  textvariable=ccode, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=218, y=282, anchor='w')
            scode = StringVar()
            entcde = Entry(w1,  textvariable=scode, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=218, y=328, anchor='w')
            s_reason = StringVar()
            entcde = Entry(w1,  textvariable=s_reason, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=218, y=388, anchor='w')
            r_exp = IntVar()
            entcde = Entry(w1,  textvariable=r_exp, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=218, y=445, anchor='w')
            s_reason_sp = StringVar()
            entcde = Entry(w1,  textvariable=s_reason_sp, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=696, y=338, anchor='w')
            r_exp_sp = IntVar()
            entcde = Entry(w1,  textvariable=r_exp_sp, fg='black', bg='#f6f6f6', relief='flat', font=(
                'century gothic', '11'), width=29).place(x=696, y=400, anchor='w')
            but = Button(w1, text='Submit', bg='white', fg='red', relief='flat', width=30, font=('Century Gothic', 12), command=lambda: validate_ser(
                w1, ccode.get(), scode.get(), s_reason.get(), r_exp.get(), s_reason_sp.get(), r_exp_sp.get())).place(x=942, y=436, anchor='ne')
            but2 = Button(w1, text='(Revert)', bg='white', fg='black', relief='flat',
                          command=lambda: return_w3(w1)).place(x=20, y=20, anchor='nw')
            w1.mainloop()
        elif choice == '2':
            print()
            print()
            print('All Service Records have been displayed.')
            print()
            table = PrettyTable(['SERVICE CODE', 'CAR CODE', 'SERVICE REPORT',
                                'SERVICE EXPENSE', 'SPL. REPAIR REPORT', 'SPL. REPAIR EXPENSE'])
            mc.execute('SELECT * FROM service')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            options2()
        elif choice == '3':
            print()
            print()
            print(' '*61, 'You have two methods to search through.')
            print()
            print(' '*73, '1. Service Code')
            print(' '*73, '2. Car Code')
            print()
            print('_'*162)
            print()
            print()
            choice4 = input(' '*70 + 'Enter your choice : ')
            print()
            print('_'*162)
            if choice4 == '1':
                print()
                print()
                ccde = input(' '*64 + 'Enter Car Code to Search : ')
                print()
                print('_'*162)
                table = PrettyTable(['SERVICE CODE', 'CAR CODE', 'SERVICE REPORT',
                                    'SERVICE EXPENSE', 'SPL. REPAIR REPORT', 'SPL. REPAIR EXPENSE'])
                mc.execute(
                    'SELECT * FROM service WHERE CCODE="{}"'.format(ccde))
                f = mc.fetchall()
                if f == None:
                    showerror(title='Error',
                              message='Invalid Car Code Entered')
                    options2()
                else:
                    for i in f:
                        table.add_row(i)
                    print()
                    print()
                    print('All Service Details have been displayed.')
                    print()
                    print(table)
                    print()
                    print()
                    print('_'*162)
                    time.sleep(10)
                    options2()
            elif choice4 == '2':
                print()
                print()
                scde = input(' '*64 + 'Enter Service Code in DB : ')
                print()
                print('_'*162)
                table = PrettyTable(['SERVICE CODE', 'CAR CODE', 'SERVICE REPORT',
                                    'SERVICE EXPENSE', 'SPL. REPAIR REPORT', 'SPL. REPAIR EXPENSE'])
                mc.execute(
                    'SELECT * FROM service WHERE SERVICECODE="{}"'.format(scde))
                f = mc.fetchall()
                if f == None:
                    showerror(title='Error',
                              message='Invalid Service Code Entered')
                    options2()
                else:
                    for i in f:
                        table.add_row(i)
                    print()
                    print()
                    print('All Service Details have been displayed.')
                    print()
                    print(table)
                    print()
                    print()
                    print('_'*162)
                    time.sleep(10)
                    options2()
            else:
                showerror(title='Error', message='Invalid entry Detected')
                options2()
        elif choice == '4':
            opentxt()
        elif choice == '5':
            changepass("admintech.csv")
        elif choice == '6':
            showinfo(title='Signed Out',message='Technician Successfully Signed Out')
            temp = False
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            cover()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def cover():
    def disable_event():
        pass
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('VOITURE')
    w1.config(bg='white')
    icon1 = PhotoImage(file="logologin.png")
    img1 = Image.open('bgmain.png')
    photo1 = ImageTk.PhotoImage(img1)
    dsp_1 = Label(w1, borderwidth=0, image=photo1).place(x=0, y=0, anchor='nw')
    w1.iconphoto(True, icon1)
    img2 = Image.open('authorized.png')
    photo = img2.resize((20, 20))
    photo2 = ImageTk.PhotoImage(photo)
    button1 = Button(w1, text='CAR LISTING', bg='#111111', fg='white', font=(
        'calibri', 8, 'bold'), relief='flat', command=lambda: classorprice(w1)).place(x=285, y=93, anchor='center')
    button2 = Button(w1, text='LOGIN/REGISTER',  bg='#FA2837', fg='white', font=('calibri', 8, 'bold'),
                     relief='flat', width=22, height=1, command=lambda: login(w1)).place(x=848, y=38, anchor='center')
    button3 = Button(w1, text='EXODUS', bg='#111111', fg='white', font=(
        'calibri', 8, 'bold'), relief='flat', command=lambda: exodus(w1)).place(x=125, y=93, anchor='center')
    button4 = Button(w1, text='ABOUT US', bg='#111111', fg='white', font=('calibri', 8, 'bold'),
                     relief='flat', command=lambda: abtus(w1, "aboutus.png")).place(x=200, y=93, anchor='center')
    button5 = Button(w1, text='CONTACT US', bg='#111111', fg='white', font=('calibri', 8, 'bold'),
                     relief='flat', command=lambda: abtus(w1, "contactus.png")).place(x=425, y=93, anchor='center')
    button6 = Button(w1, text='FAQs', bg='#111111', fg='white', font=(
        'calibri', 8, 'bold'), relief='flat', command=lambda: faq(w1)).place(x=355, y=93, anchor='center')
    button7 = Button(w1, text='Read More', bg='#FA2837', fg='white', font=('calibri', 11, 'bold'),
                     relief='flat', width=15, command=lambda: why(w1)).place(x=715, y=374, anchor='center')
    button8 = Button(w1, image=photo2, relief='flat', borderwidth=0, bg="#111111",
                     command=lambda: authorization(w1)).place(x=970, y=93, anchor='center')
    w1.protocol("WM_DELETE_WINDOW", disable_event)
    w1.mainloop()


def changepass(file):
    print('_'*162)
    print()
    print()
    oldpass = input(' '*67 + 'Enter Old Password : ')
    newpass = input(' '*67 + 'Enter New Password : ')
    print()
    print('_'*162)
    f = open(file, 'r')
    csvr = csv.reader(f)
    for i in csvr:
        if oldpass in i:
            df = pandas.read_csv(file, index_col='User')
            df.loc[auth_code, 'Password'] = newpass
            df.to_csv(file)
            showinfo(title='Successful',
                     message='Password Changed Successfully')
            showinfo(title='Signed Out',
                     message='Please Login Again with New Password')
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            cover()
    else:
        showerror(title='Error', message='Invalid Old Password')
        return


def options():
    mc.execute('SELECT NAME_W FROM workers WHERE AUTH_CODE="{}"'.format(auth_code))
    f = mc.fetchone()
    name = f[0]
    print()
    print()
    print('  Hello', name + '. You are given the following commands to execute. Read through the options carefully and enter your choice in the given area of query.')
    temp = True
    print()
    print()
    print(' '*68, '1. Modify Cars Database')
    print(' '*68, '2. Modify Users Database')
    print(' '*68, '3. Display Orders Database')
    print(' '*68, '4. Read given Instructions')
    print(' '*68, '5. Change current Password')
    print(' '*68, '6. Sign Out from manager')
    print()
    print('_'*162)
    while temp == True:
        print()
        print()
        choice = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice == '1':
            choicevalued1()
        elif choice == '2':
            choicevalued2()
        elif choice == '3':
            print()
            print()
            print('All Placed Orders Table along with their expected return date : ')
            print()
            table = PrettyTable(['Invoice Number', 'Collection Date', 'Return Date',
                                'Total Price', 'Car Code', 'Car Company', 'Car Name', 'Buyer Phone', 'Remarks'])
            mc.execute('select a.INVOICE,a.CBUYDATE,a.CRETURN,a.TPRICE,a.CCODE,b.CCOMPANY,b.CNAME,a.PHONE,a.REMARK from buy as a inner join record as b on a.CCODE=b.CCODE inner join user as c on a.PHONE=c.PHONE;')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            options()
        elif choice == '4':
            opentxt()
        elif choice == '5':
            changepass("adminman.csv")
        elif choice == '6':
            showinfo(title='Signed Out',
                     message='Manager Successfully Signed Out')
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            cover()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def return_w4(w1):
    w1.destroy()
    options4()


def display_bill(tprice_collect, invno, car_code, extra, kn_charge, total_price):
    mc.execute('SELECT REPAIREX FROM service WHERE SERVICECODE="{}"'.format(servicec))
    j = mc.fetchone()
    reson = j[0]
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Complete Bill')
    img = Image.open('billmain.png')
    photo = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo, borderwidth=0).place(x=0,y=0,anchor='nw')
    today = str(datetime.date.today())
    mc.execute('SELECT CCOMPANY, CNAME FROM record WHERE CCODE="{}"'.format(car_code))
    f = mc.fetchone()
    mc.execute('SELECT PHONE FROM buy WHERE INVOICE="{}"'.format(invno))
    j = mc.fetchone()
    phone = j[0]
    car_name = f[0] + ' ' + f[1]
    tprice_collect_09 = tprice_collect - extra
    dspnme = Label(w1, text=car_name, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=193,y=149,anchor='w')
    dspnme = Label(w1, text=phone, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=681,y=149,anchor='w')
    dspnme = Label(w1, text=today, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=803,y=68,anchor='w')
    dspnme = Label(w1, text=total_price, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=725,y=250,anchor='w')
    dspnme = Label(w1, text=extra, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=725,y=299,anchor='w')
    dspnme = Label(w1, text=kn_charge, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=725,y=347,anchor='w')
    dspnme = Label(w1, text=tprice_collect, bg="#F2FFF0",fg='red',font=('Century Gothic',15)).place(x=725,y=397,anchor='w')
    dspnme = Label(w1, text=invno, bg="#F2FFF0",fg='red',font=('Century Gothic',10)).place(x=427,y=71,anchor='w')
    dspnme = Label(w1, text=reson, bg="#f6f6f6",fg='red',font=('Century Gothic',10)).place(x=39,y=462,anchor='w')
    but2 = Button(w1, text='(Submit)', bg='#F2FFF0', fg='black', relief='flat', command=lambda: final_step(w1,tprice_collect_09, today, invno, car_code)).place(x=990, y=10, anchor='ne')
    but3 = Button(w1, text='(Revert)', bg='#F2FFF0', fg='black', relief='flat',
                  command=lambda: return_w4(w1)).place(x=10, y=10, anchor='nw')
    w1.mainloop()


def final_step(w1,tprice_collect, today, invno, car_code):
    w1.destroy()
    tk = tkinter.messagebox.askquestion(
        'Final Step', 'Is the total money ' + str(tprice_collect) + ' collected.')
    if tk == 'yes':
        try:
            mc.execute(
                'UPDATE buy SET CRETURN="{}" WHERE INVOICE="{}"'.format(today, invno))
            mc.execute('UPDATE buy SET TPRICE={} WHERE INVOICE="{}"'.format(
                tprice_collect, invno))
            mc.execute(
                'UPDATE buy SET REMARK="Rental Completed" WHERE INVOICE="{}"'.format(invno))
            mc.execute('UPDATE owner SET TPRICE={} WHERE INVOICE="{}"'.format(
                tprice_collect, invno))
            mc.execute(
                'UPDATE record SET CDISTANCE={} WHERE CCODE="{}"'.format(range_km,car_code))
            mc.execute(
                'UPDATE owner SET DATOP="{}" WHERE INVOICE="{}"'.format(today, invno))
            mc.execute(
                'UPDATE record SET AVAILABILITY="Available" WHERE CCODE="{}"'.format(car_code))
            mdb.commit()
            showinfo(title='Successful', message='Car Successfully Returned ')
        except:
            showerror(title='Unsuccessful',
                      message='Car Could\'nt be Returned')
    options4()


def options4():
    mc.execute('SELECT NAME_W FROM workers WHERE AUTH_CODE="{}"'.format(auth_code))
    f = mc.fetchone()
    name = f[0]
    print()
    print()
    print('  Hello', name + '. You are given the following commands to execute. Read through the options carefully and enter your choice in the given area of query.')
    temp = True
    print()
    print()
    print(' '*67, '1. Return Delivered Cars')
    print(' '*67, '2. Change Password')
    print(' '*67, '3. Read Given Instructions')
    print(' '*67, '4. Sign Out from Cashier')
    print()
    print('_'*162)
    while temp == True:
        print()
        print()
        choice = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice == '1':
            return_process1()
        elif choice == '2':
            changepass("adminacc.csv")
        elif choice == '3':
            opentxt()
        elif choice == '4':
            showinfo(title='Signed Out',
                     message='Cashier Successfully Signed Out')
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            print('\n'*10)
            cover()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def return_process1():
    yes_no = tkinter.messagebox.askquestion(
        'Serviced?', 'Is the car service completed by technician.')
    if yes_no == 'yes':
        print()
        print()
        print(' '*65 + 'Enter 0 In Both Entries To Exit')
        invno = input(' '*65 + ' Enter the Invoice No : ')
        servc = input(' '*64 + 'Enter the Service Code : ')
        print()
        print('_'*162)
        if invno == 0 and servc == 0:
            options4()
        else:
            mc.execute(
                'SELECT CRETURN,CCODE,TPRICE FROM buy WHERE INVOICE="{}"'.format(invno))
            m = mc.fetchone()
            if m == None:
                showwarning(title='Invalid', message='Invalid Invoice Number')
                options4()
            else:
                return_date = m[0]
                date = return_date.strftime('%Y-%m-%d')
                car_code = m[1]
                total_price = m[2]
                mc.execute(
                    'Select REPAIREX FROM service WHERE CCODE="{}" and SERVICECODE="{}"'.format(m[1], servc))
                f = mc.fetchone()
        if f == None:
            showwarning(title='Invalid', message='Invalid Service Code')
            options4()
        else:
            global servicec
            servicec = servc
            temp = True
            while temp == True:
                print()
                print()
                km = input(' '*62 + 'Enter Current Kilo-Meter Count : ')
                print()
                print('_'*162)
                if km.isdigit():
                    mc.execute('SELECT CDISTANCE FROM record WHERE CCODE="{}"'.format(car_code))
                    f = mc.fetchone()
                    already_km = f[0]
                    global range_km
                    range_km = km
                    t_km_ran = int(km) - already_km
                    if t_km_ran >150:
                        km2 = t_km_ran - 150
                        kn_charge = km2*1.50
                        year = int(date[0:4])
                        month = int(date[5:7])
                        day = int(date[8:10])
                        date2 = datetime.date(year, month, day)
                        today = datetime.date.today()
                        age = today - date2
                        if age.days < 0:
                            ret_money = 70
                            total_money_ret = ret_money*abs(age.days)
                            if f[0] == 'NIL':
                                tprice_collect = total_price - total_money_ret + kn_charge
                                showinfo(
                                    title='Total', message='Total Money to be collected : ' + str(tprice_collect))
                                total_price = total_price - total_money_ret
                                display_bill(tprice_collect, invno, car_code, 0, kn_charge, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price - total_money_ret + extra + kn_charge
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.')
                                total_price = total_price - total_money_ret
                                display_bill(tprice_collect, invno, car_code, extra, kn_charge, total_price)
                        elif age.days > 0:
                            mc.execute(
                                'SELECT CPRICE_DAY FROM record WHERE CCODE="{}"'.format(car_code))
                            n = mc.fetchone()
                            charge = n[0]
                            total_money_col = charge*abs(age.days)
                            if f[0] == 'NIL':
                                tprice_collect = total_price + total_money_col + kn_charge
                                showinfo(title='Total', message='Total Money to be collected : ' +
                                        str(tprice_collect) + '.\nIncluding Late Return Charges.')
                                total_price = total_price + total_money_col
                                display_bill(tprice_collect, invno, car_code, 0, kn_charge, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price + total_money_col + extra + kn_charge
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.\nIncluding Late Return Charges.')
                                total_price = total_price + total_money_col
                                display_bill(tprice_collect, invno, car_code, extra, kn_charge, total_price)
                        elif age.days == 0:
                            if f[0] == 'NIL':
                                tprice_collect = total_price + kn_charge
                                showinfo(
                                    title='Total', message='Total Money to be collected : ' + str(tprice_collect))
                                display_bill(tprice_collect, invno, car_code, 0, kn_charge, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price + extra + kn_charge
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.')
                                display_bill(tprice_collect, invno, car_code, extra, kn_charge, total_price)
                    else:
                        year = int(date[0:4])
                        month = int(date[5:7])
                        day = int(date[8:10])
                        date2 = datetime.date(year, month, day)
                        today = datetime.date.today()
                        age = today - date2
                        print(age)
                        if age.days < 0:
                            ret_money = 70
                            total_money_ret = ret_money*abs(age.days)
                            if f[0] == 'NIL':
                                tprice_collect = total_price - total_money_ret 
                                showinfo(
                                    title='Total', message='Total Money to be collected : ' + str(tprice_collect))
                                total_price = tprice_collect
                                display_bill(tprice_collect, invno, car_code, 0, 0, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price - total_money_ret + extra
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.')
                                total_price = tprice_collect - extra
                                display_bill(tprice_collect, invno, car_code, extra, 0, total_price)
                        elif age.days > 0:
                            mc.execute(
                                'SELECT CPRICE_DAY FROM record WHERE CCODE="{}"'.format(car_code))
                            n = mc.fetchone()
                            charge = n[0]
                            total_money_col = charge*abs(age.days)
                            if f[0] == 'NIL':
                                tprice_collect = total_price + total_money_col
                                showinfo(title='Total', message='Total Money to be collected : ' +
                                        str(tprice_collect) + '.\nIncluding Late Return Charges.')
                                total_price = tprice_collect
                                display_bill(tprice_collect, invno, car_code, 0, 0, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price + total_money_col + extra
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.\nIncluding Late Return Charges.')
                                total_price = tprice_collect - extra
                                display_bill(tprice_collect, invno, car_code, extra, 0, total_price)
                        elif age.days == 0:
                            if f[0] == 'NIL':
                                tprice_collect = total_price
                                showinfo(
                                    title='Total', message='Total Money to be collected : ' + str(tprice_collect))
                                display_bill(tprice_collect, invno, car_code, 0, 0, total_price)
                            else:
                                mc.execute(
                                    'SELECT REP_EXPENSE FROM service WHERE SERVICECODE="{}"'.format(servc))
                                j = mc.fetchone()
                                extra = j[0]
                                tprice_collect = total_price + extra
                                showinfo(title='Total', message='Total Money to be collected : ' + str(tprice_collect) +
                                        '.\nAs there is a damage in the car after rental, charges has been levied.')
                                total_price = tprice_collect - extra
                                display_bill(tprice_collect, invno, car_code, extra, 0, total_price)
                else:
                    showerror(title='Error',message='Invalid Km Count')
    else:
        print()
        print()
        invo = input(' '*65 + 'Enter the Invoice Number : ')
        print()
        print('_'*162)
        mc.execute('Select CCODE FROM buy WHERE INVOICE="{}"'.format(invo))
        j = mc.fetchone()
        if j == None:
            showerror(title='Error',
                      message='This Invoice Number does not exist')
            return_process1()
        else:
            ccode = j[0]
        mc.execute(
            'Select AVAILABILITY FROM record WHERE CCODE="{}"'.format(ccode))
        f = mc.fetchone()
        if f == None:
            showwarning(title='Invalid',
                        message='A Car with this Code does\'nt Exist')
            options4()
        else:
            if f[0] == 'UNAVAILABLE':
                sub = 'Request For Service'
                msg = '''VOITURE MANAGER

Hello Technician,
A car has been returned after rental and spaced in the garage.
You are required to examine the car immediately and file a 'Serivce Report' for car return.
Car Code : ''' + ccode + '''

Regards,
Manager.'''
                eml = 'technicians.voiture22@gmail.com'
                email_alert(sub, msg, eml)
                showinfo(
                    title='Submitted', message='Request for Service is Submitted. Come Back when its done')
                options4()
            else:
                showwarning(title='Invalid',
                            message='Car with this Code is not Rented')


def choicevalued2():
    temp1 = True
    while temp1 == True:
        print()
        print()
        print(' '*26, 'You have the following options to modify the USER RECORDS DATABASE. Please enter an option in the query down.')
        print()
        print(' '*68 + '1. Display Users Database')
        print(' '*68 + '2. Remove Users from DB')
        print(' '*68 + '3. Search Users in DB')
        print(' '*68 + '4. To Revert')
        print()
        print('_'*162)
        print()
        print()
        choice2 = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice2 == '1':
            print()
            print()
            print('All User Records have been displayed.')
            print()
            table = PrettyTable(['Phone Number', 'First Name', 'Second Name', 'E-mail',
                                'Date of Birth', 'License Number', 'License Expiry Date', 'Address'])
            mc.execute(
                'SELECT PHONE,FSTNME,SNDNME,EMAIL,DOB,LICENSE,LISSUDATE,ADDRESS FROM user')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            choicevalued2()
        elif choice2 == '2':
            print()
            print()
            pne = input(' '*56 + 'Enter Phone Number of User to Delete : ')
            print()
            print('_'*162)
            mc.execute('Select EMAIL FROM user WHERE PHONE="{}"'.format(pne))
            f = mc.fetchone()
            if f == None:
                showwarning(title='Invalid',
                            message='A User with this Phone does\'nt Exist')
                choicevalued2()
            else:
                sub = "Deleting Your Account"
                msg = '''VOITURE CAR RENTAL

Dear Customer,
    Your account in Voiture referring to phone number ''' + pne + '''
is being deleted by manager either on request or on less account activity.

Regards,
Team of Voiture.'''
                email_alert(sub,msg,f[0])
                try:
                    mc.execute('DELETE FROM user WHERE PHONE="{}"'.format(pne))
                    mdb.commit()
                    showinfo(title='Successful',
                             message='User Deleted Successfully')
                    choicevalued2()
                except:
                    mdb.rollback()
                    showerror(title='Error', message='Updation Unsuccessful')
        elif choice2 == '3':
            print()
            print()
            pne = input(' '*56 + 'Enter Phone Number of User to Search : ')
            print()
            print('_'*162)
            print()
            print()
            print('All User Records have been displayed.')
            print()
            table = PrettyTable(['Phone Number', 'First Name', 'Second Name', 'E-mail',
                                'Date of Birth', 'License Number', 'License Expiry Date', 'Address'])
            mc.execute(
                'SELECT PHONE,FSTNME,SNDNME,EMAIL,DOB,LICENSE,LISSUDATE,ADDRESS FROM user WHERE PHONE="{}"'.format(pne))
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print('_'*162)
            time.sleep(10)
            choicevalued2()
        elif choice2 == '4':
            options()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def return_w1(w1):
    w1.destroy()
    choicevalued1()


def choicevalued1():
    temp1 = True
    while temp1 == True:
        print()
        print()
        print(' '*27, 'You have the following options to modify the CAR RECORDS DATABASE. Please enter an option in the query down.')
        print()
        print(' '*69 + '1. Add New Cars into DB')
        print(' '*69 + '2. Remove Old Cars')
        print(' '*69 + '3. Update Car Details')
        print(' '*69 + '4. Display Cars Details')
        print(' '*69 + '5. Display on Car Code')
        print(' '*69 + '6. Display on Car Class')
        print(' '*69 + '7. To Revert')
        print()
        print('_'*162)
        print()
        print()
        choice2 = input(' '*70 + 'Enter your choice : ')
        print()
        print('_'*162)
        if choice2 == '1':
            print()
            print()
            print(' '*69, 'Process Done In Perfoma')
            print()
            print('_'*162)
            enter_new_value()
        elif choice2 == '2':
            print()
            print()
            ccde = input(' '*64 + 'Enter Car Code to Delete : ')
            print()
            print('_'*162)
            mc.execute('Select * FROM record WHERE CCODE="{}"'.format(ccde))
            f = mc.fetchone()
            if f == None:
                showwarning(title='Invalid',
                            message='A Car with this Code does\'nt Exist')
                choicevalued1()
            else:
                try:
                    mc.execute(
                        'DELETE FROM record WHERE CCODE="{}"'.format(ccde))
                    mdb.commit()
                    showinfo(title='Successful',
                             message='Car Deleted Successfully')
                    choicevalued1()
                except:
                    mdb.rollback()
                    showerror(title='Error', message='Updation Unsuccessful')
                    choicevalued1()
        elif choice2 == '3':
            print()
            print()
            ccde = input(' '*64 + 'Enter Car Code to Update : ').capitalize()
            print()
            print('_'*162)
            mc.execute(
                'Select CPRICE_MONTH,CCOLOUR FROM record WHERE CCODE="{}"'.format(ccde))
            f = mc.fetchone()
            if f == None:
                showwarning(title='Invalid',
                            message='A Car with this Code does\'nt Exist')
                choicevalued1()
            else:
                temp2 = True
                while temp2 == True:
                    print()
                    print()
                    print(' '*55, 'You have only the two following options to update.')
                    print()
                    print(' '*67 + '1. Update Monthly Price')
                    print(' '*67 + '2. Update Car\'s Colour')
                    print(' '*67 + '3. To Revert')
                    print()
                    print('_'*162)
                    print()
                    print()
                    choice = input(' '*70 + 'Enter Your Choice : ')
                    print()
                    print('_'*162)
                    if choice == '1':
                        print()
                        print()
                        print(' '*67 + 'Current Car Price is - ' + str(f[0]))
                        print()
                        p2 = input(' '*65 + 'Enter New Price/Month  : ')
                        p3 = input(' '*65 + 'Enter New Price/Day  : ')
                        print()
                        print('_'*162)
                        if str(p2).isdigit():
                            try:
                                mc.execute(
                                    'UPDATE record SET CPRICE_MONTH={} WHERE CCODE="{}"'.format(p2, ccde))
                                mc.execute(
                                    'UPDATE record SET CPRICE_DAY={} WHERE CCODE="{}"'.format(p3, ccde))
                                mdb.commit()
                                showinfo(title='Successful',
                                         message='Updation Successful')
                            except:
                                showerror(title="Error",
                                          message='Updation Unsuccessful')
                            choicevalued1()
                        else:
                            showerror(title='Error',
                                      message='Invalid Entry Detected')
                            choicevalued1()
                    elif choice == '2':
                        print()
                        print()
                        print(' '*54, 'Current Car Colour is - ', f[1])
                        print()
                        print()
                        print()
                        c2 = input(' '*59 + 'Enter New Car-Colour : ').title()
                        i2 = input(
                            ' '*50 + 'Enter Image Code with New Colour : ')
                        print()
                        print('_'*162)
                        if './images/' in i2:
                            try:
                                mc.execute(
                                    'UPDATE record SET CCOLOUR="{}" WHERE CCODE="{}"'.format(c2, ccde))
                                mc.execute(
                                    'UPDATE record SET IMAGECODE="{}" WHERE CCODE="{}"'.format(i2, ccde))
                                mdb.commit()
                                showinfo(title='Successful',
                                         message='Updation Successful')
                            except:
                                mdb.rollback()
                                showerror(title='Error',
                                          message='Updation Unsuccessful')
                            choicevalued1()
                        else:
                            showerror(title='Error',
                                      message='Invalid Image Code Detected')
                    elif choice == '3':
                        choicevalued1()
                    else:
                        showerror(title='Error',
                                  message='Invalid Entry Detected')
        elif choice2 == '4':
            print()
            print()
            print('All Car Details Table have been displayed. Car Doors, Transmission Type, Car Type and Fuel Type columns have been displayed separately.')
            print()
            table = PrettyTable(['Car Code', 'Car Comapany', 'Car Name', 'Car Colour', 'Car Class',
                                'Price/Month', 'Model Year', 'Availability', 'Image Code', 'Price/Day'])
            mc.execute(
                'SELECT CCODE,CCOMPANY,CNAME,CCOLOUR,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE,CPRICE_DAY FROM record')
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print(table)
            print()
            print()
            table2 = PrettyTable(['Car Code', 'Car Comapany', 'Car Name',
                                 'Car Doors', 'Trasmission Type', 'Car Type', 'Car Fuel Type'])
            mc.execute(
                'SELECT CCODE,CCOMPANY,CNAME,CDOORS,CTRANSMISSION,CTYPE,CFUEL FROM record')
            f = mc.fetchall()
            for i in f:
                table2.add_row(i)
            print(table2)
            print()
            print('_'*162)
            time.sleep(10)
            choicevalued1()
        elif choice2 == '6':
            print()
            print()
            print(' '*63, 'You have the following Car Classes')
            print(' '*75 + '1. SUV')
            print(' '*75 + '2. Sedan')
            print(' '*75 + '3. Coupe')
            print(' '*75 + '4. MiniVan')
            print(' '*75 + '5. HatchBack')
            print(' '*75 + '6. Ute')
            print(' '*75 + '7. Luxury')
            print()
            print('_'*162)
            print()
            print()
            entry = input(' '*64 + 'Enter Car Code to Display : ')
            print()
            print('_'*162)
            if entry == '1':
                choice3 = 'SUV'
            elif entry == '2':
                choice3 = 'Sedan'
            elif entry == '3':
                choice3 = 'Coupe'
            elif entry == '4':
                choice3 = 'MiniVan'
            elif entry == '5':
                choice3 = 'HatchBack'
            elif entry == '6':
                choice3 = 'Ute'
            elif entry == '7':
                choice3 = 'Luxury%'
                table = PrettyTable(['Car Code', 'Car Comapany', 'Car Name', 'Car Colour', 'Car Class',
                                    'Price/Month', 'Model Year', 'Availability', 'Image Code', 'Price/Day'])
                mc.execute(
                    'SELECT CCODE,CCOMPANY,CNAME,CCOLOUR,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE,CPRICE_DAY FROM record WHERE CCLASS LIKE "{}"'.format(choice3))
                f = mc.fetchall()
                for i in f:
                    table.add_row(i)
                print()
                print('All Car Details Table have been displayed. Car Doors, Transmission Type, Car Type and Fuel Type columns have been displayed separately.')
                print()
                print(table)
                print()
                print()
                table2 = PrettyTable(['Car Code', 'Car Comapany', 'Car Name',
                                     'Car Doors', 'Trasmission Type', 'Car Type', 'Car Fuel Type'])
                mc.execute(
                    'SELECT CCODE,CCOMPANY,CNAME,CDOORS,CTRANSMISSION,CTYPE,CFUEL FROM record WHERE CCLASS LIKE"{}"'.format(choice3))
                f = mc.fetchall()
                for i in f:
                    table2.add_row(i)
                print(table2)
                print()
                print('_'*162)
                time.sleep(10)
                choicevalued1()
            else:
                showerror(title='Error', message='Invalid Entry Detected')
                choicevalued1()
            table = PrettyTable(['Car Code', 'Car Comapany', 'Car Name', 'Car Colour', 'Car Class',
                                'Price/Month', 'Model Year', 'Availability', 'Image Code', 'Price/Day'])
            mc.execute('SELECT CCODE,CCOMPANY,CNAME,CCOLOUR,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE,CPRICE_DAY FROM record WHERE CCLASS="{}"'.format(choice3))
            f = mc.fetchall()
            for i in f:
                table.add_row(i)
            print()
            print('All Car Details Table have been displayed. Car Doors, Transmission Type, Car Type and Fuel Type columns have been displayed separately.')
            print()
            print(table)
            print()
            print()
            table2 = PrettyTable(['Car Code', 'Car Comapany', 'Car Name',
                                 'Car Doors', 'Trasmission Type', 'Car Type', 'Car Fuel Type'])
            mc.execute(
                'SELECT CCODE,CCOMPANY,CNAME,CDOORS,CTRANSMISSION,CTYPE,CFUEL FROM record WHERE CCLASS="{}"'.format(choice3))
            f = mc.fetchall()
            for i in f:
                table2.add_row(i)
            print(table2)
            print()
            print('_'*162)
            time.sleep(10)
            choicevalued1()
        elif choice2 == '5':
            print()
            print()
            ccde = input(' '*64 + 'Enter Car Code to Display : ')
            print()
            print('_'*162)
            table = PrettyTable(['Car Code', 'Car Comapany', 'Car Name', 'Car Colour', 'Car Class',
                                'Price/Month', 'Model Year', 'Availability', 'Image Code', 'Price/Day'])
            mc.execute(
                'SELECT CCODE,CCOMPANY,CNAME,CCOLOUR,CCLASS,CPRICE_MONTH,CYEAR,AVAILABILITY,IMAGECODE,CPRICE_DAY FROM record WHERE CCODE="{}"'.format(ccde))
            f = mc.fetchall()
            if f == None:
                showerror(title='Error',
                          message='A Car with this Car Class does\'nt Exist')
            else:
                for i in f:
                    table.add_row(i)
                print()
                print()
                print('All Car Details Table have been displayed. Car Doors, Transmission Type, Car Type and Fuel Type columns have been displayed separately.')
                print()
                print(table)
                print()
                print()
                table2 = PrettyTable(['Car Code', 'Car Comapany', 'Car Name',
                                     'Car Doors', 'Trasmission Type', 'Car Type', 'Car Fuel Type'])
                mc.execute(
                    'SELECT CCODE,CCOMPANY,CNAME,CDOORS,CTRANSMISSION,CTYPE,CFUEL FROM record WHERE CCODE="{}"'.format(ccde))
                f = mc.fetchall()
                for i in f:
                    table2.add_row(i)
                print(table2)
                print()
                print('_'*162)
            time.sleep(10)
            choicevalued1()
        elif choice2 == '7':
            temp1 = False
            options()
        else:
            showerror(title='Error', message='Invalid Entry Detected')


def validate_all_entry_car(w1, ccode, ccompany, cname, ccolour, ctype, transmission, cdoors, cclass, cprice_month, cmodel_year, image_code, fuel_type, cprice_day):
    mc.execute('SELECT * FROM record WHERE CCODE="{}"'.format(ccode))
    f = mc.fetchone()
    if f == None:
        if len(ccode) == 6 and 'CD' in ccode:
            if transmission == 'Manual' or transmission == 'Automatic' or transmission == 'Continuously Variable (CVT)' or transmission == 'Dual-Clutch' or transmission == 'Sequential Manual' or transmission == 'Semi-Automatic':
                if cdoors in ('2 Doors', '3 Doors', '4 Doors', '5 Doors', '6 Doors'):
                    if cclass in ('SUV', 'Sedan', 'Coupe', 'HatchBack', 'Ute', 'MiniVan', 'Luxury SUV', 'Luxury Sedan', 'Luxury Coupe', 'Luxury HatchBack', 'Luxury Ute', 'Luxury MiniVan'):
                        if str(cprice_month).isdigit() and str(cprice_day).isdigit():
                            if str(cmodel_year).isdigit():
                                if './images/' in image_code:
                                    if fuel_type in ('Petrol', 'Electric', 'Liquefied Petroleum Gas (LPG)', 'Biofuel', 'Diesel'):
                                        try:
                                            mc.execute('INSERT INTO record VALUES("{}","{}","{}","{}","{}","{}","{}","{}",{},{},"Available","{}","{}",{},5)'.format(
                                                ccode, ccompany, cname, ccolour, ctype, transmission, cdoors, cclass, cprice_month, cmodel_year, image_code, fuel_type, cprice_day))
                                            mdb.commit()
                                            showinfo(
                                                title='Successful', message='Records Saved Successfully')
                                            return_w1(w1)
                                        except:
                                            showerror(
                                                title='Error', message='Records Couldn\'t be saved')
                                    else:
                                        showerror(title='Error',
                                                  message='Invalid Fuel Type')
                                else:
                                    showerror(
                                        title='Error', message='Invalid Image Code - Location Not Identified')
                            else:
                                showerror(title='Error',
                                          message='Invalid Car Model Year')
                        else:
                            showerror(title='Error',
                                      message='Invalid Car Price')
                    else:
                        showerror(title='Error', message='Invalid Car Class')
                else:
                    showerror(title='Error', message='Invalid Doors Capacity')
            else:
                showerror(title='Error', message='Invalid Transmission Type')
        else:
            showerror(title='Error',
                      message='Invalid Car Code. Refer to Instructions')
    else:
        showerror(title='Error', message='This Car Code already exists')


def enter_new_value():
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Performa')
    img = Image.open('performa.png')
    photo = ImageTk.PhotoImage(img)
    dsp = Label(w1, image=photo, borderwidth=0).place(x=0, y=0, anchor='nw')
    ccde = StringVar()
    entcde = Entry(w1, textvariable=ccde, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=175, y=108, anchor='w')
    ccom = StringVar()
    entcom = Entry(w1, textvariable=ccom, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=211, y=153, anchor='w')
    cnme = StringVar()
    entnme = Entry(w1, textvariable=cnme, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=178, y=200, anchor='w')
    clor = StringVar()
    entclr = Entry(w1, textvariable=clor, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=200, y=246, anchor='w')
    ctpe = StringVar()
    enttpe = Entry(w1, textvariable=ctpe, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=178, y=292, anchor='w')
    trns = StringVar()
    enttrs = Entry(w1, textvariable=trns, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=222, y=338, anchor='w')
    cdrs = StringVar()
    entdrs = Entry(w1, textvariable=cdrs, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=188, y=384, anchor='w')
    ccls = StringVar()
    entcls = Entry(w1, textvariable=ccls, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=188, y=430, anchor='w')
    cp_m = IntVar()
    entp_m = Entry(w1, textvariable=cp_m, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=694, y=109, anchor='w')
    cmoy = IntVar()
    entmoy = Entry(w1, textvariable=cmoy, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=663, y=155, anchor='w')
    imgc = StringVar()
    enti_c = Entry(w1, textvariable=imgc, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=659, y=201, anchor='w')
    fl_t = StringVar()
    entfty = Entry(w1, textvariable=fl_t, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=646, y=247, anchor='w')
    cp_d = IntVar()
    entp_d = Entry(w1, textvariable=cp_d, fg='black', bg='#f6f6f6', relief='flat', font=(
        'century gothic', '11'), width=30).place(x=672, y=294, anchor='w')
    but2 = Button(w1, text='(Submit)', bg='white', fg='black', relief='flat', command=lambda: validate_all_entry_car(w1, ccde.get(), ccom.get(), cnme.get(
    ), clor.get(), ctpe.get(), trns.get(), cdrs.get(), ccls.get(), cp_m.get(), cmoy.get(), imgc.get(), fl_t.get(), cp_d.get())).place(x=907, y=49, anchor='e')
    but3 = Button(w1, text='(Revert)', bg='white', fg='black', relief='flat',
                  command=lambda: return_w1(w1)).place(x=94, y=49, anchor='w')
    w1.mainloop()


def exodus(w1):
    tk = tkinter.messagebox.askquestion(
        'Close Home', 'Are you sure you want to close Voiture', icon='warning')
    if tk == 'yes':
        w1.destroy()
        showinfo('Voiture Quote','Thank You For Your Presence')
        quit()
    else:
        pass

try:
    mc.execute("USE car1")
    cover()
except:
    createall()
    cover()
