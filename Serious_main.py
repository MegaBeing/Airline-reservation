import tkinter
from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import scrolledtext
import admin
import psgn_rsrv
root=Tk()

hour_string = StringVar()
min_string = StringVar()
last_value_sec = ""
last_value = ""
f = ('Times', 20)


def g(cal,fm, des, arkey, to, td, flkey, min_sb, sec_hour,avgs,np):


    date = cal.get_date().replace('/',':')
    m = min_sb.get()
    h = sec_hour.get()
    T = f"{m}:{h}"

    if des is False:
        d=admin.new(arkey, flkey.get(), fm.get(), T, to.get(), td.get(), date, avgs,np)
        if d is True:
            for x in frame.winfo_children():
                x.destroy()
            Label(frame, text='file successfully saved', fg='green').pack()
            Button(frame, text='Quit', command=lambda: quit()).pack()
        else:
            for x in frame.winfo_children():
                x.destroy()
            Label(frame, text='Wrong airplane key', fg='red').pack()
            Button(frame, text='Quit', command=lambda: quit()).pack()
    elif des is True:
        d=admin.old(arkey, flkey.get(), fm.get(), T, to.get(), td.get(), date, avgs, np)
        if d is True:
            for x in frame.winfo_children():
                x.destroy()
            Label(frame, text='file successfully saved', fg='green').pack()
            Button(frame, text='Quit', command=lambda: quit()).pack()
        else:
            for x in frame.winfo_children():
                x.destroy()
            Label(frame, text='Wrong Airplane key', fg='red').pack()
            Button(frame, text='Quit', command=lambda: quit()).pack()

def date_time(cal,min_sb,sec_hour):
    date = cal.get_date().replace('/',':')
    m = min_sb.get()
    h = sec_hour.get()
    T = f"{m}:{h}"
    label3 = Label(frame, text='Choose :')
    label3.grid(row=3, column=1, padx=40, pady=30)

    Rbutton1 = Button(frame, text='Only Flight', command=lambda: only_flight(T, date))
    Rbutton1.grid(row=4, column=0, ipadx=40, ipady=30)

    Rbutton2 = Button(frame, text='Flight with the passenger list', command=lambda: flight_psgn_lst(T, date))
    Rbutton2.grid(row=5, column=0, ipadx=40, ipady=30)

    Rbutton3 = Button(frame, text='flight with single passenger', command=lambda: flight_sng_psgn(T, date))
    Rbutton3.grid(row=6, column=0, ipadx=40, ipady=30)


def Flight_info(arkey,avgs,des,np):
    global last_value, last_value_sec, min_string, hour_string
    for x in frame.winfo_children():
        x.destroy()

    my_canvas = Canvas(frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # add a scrollbar
    my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # create another frame inside the canvas
    second_frame = Frame(my_canvas)
    # add that new frame to a window in canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    root.geometry('700x700')

    label1 = ttk.Label(second_frame, text='From:')
    label1.grid(row=0, column=0, padx=40, pady=30)
    fm = ttk.Entry(second_frame)
    fm.grid(row=0, column=1, padx=40, pady=30)

    label2 = ttk.Label(second_frame, text='Time of Departure:')
    label2.grid(row=1, column=0, padx=40, pady=30)
    min_sb = Spinbox(second_frame, from_=0, to=23, wrap=True, textvariable=hour_string, width=2, state="readonly", font=f,
                     justify=CENTER)
    sec_hour = Spinbox(second_frame, from_=0, to=59, wrap=True, textvariable=min_string, font=f, width=2, justify=CENTER)

    sec = Spinbox(second_frame, from_=0, to=59, wrap=True, textvariable=sec_hour, width=2, font=f, justify=CENTER)

    min_sb.grid(row=2, column=1, padx=40, pady=30)
    sec_hour.grid(row=2, column=2, padx=40, pady=30)
    sec.grid(row=2, column=3, padx=40, pady=30)


    if last_value == "59" and min_string.get() == "0":
        hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
        last_value = min_string.get()

    if last_value_sec == "59" and sec_hour.get() == "0":
        min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
    if last_value == "59":
        hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
        last_value_sec = sec_hour.get()

    label3 = ttk.Label(second_frame, text='To:')
    label3.grid(row=3, column=0, padx=40, pady=30)
    to = ttk.Entry(second_frame)
    to.grid(row=3, column=1, padx=40, pady=30)

    label4 = ttk.Label(second_frame, text='Total Distance:')
    label4.grid(row=4, column=0, padx=40, pady=30)
    td = ttk.Entry(second_frame)
    td.grid(row=4, column=1, padx=40, pady=30)

    label5=ttk.Label(second_frame, text='Date:')
    label5.grid(row=5, column=0, padx=40, pady=30)
    cal = Calendar(second_frame, selectmode="day", year=2021, month=2, day=3)
    cal.grid(row=5, column=1, padx=40, pady=30)

    label6 = ttk.Label(second_frame, text='Flight key:')
    label6.grid(row=6, column=0, padx=40, pady=30)
    flkey = ttk.Entry(second_frame)
    flkey.grid(row=6, column=1, padx=40, pady=30)

    submitb=Button(second_frame, text='Submit', command=lambda: g(cal,fm, des, arkey, to, td, flkey, hour_string, min_string, avgs, np))
    submitb.grid(row=7,column=0,padx=40,pady=30)

def flight_type(a, b, c, d, e, f, g, h):
    admin.flight_type(a, b, c, d, e, f, g, h)
    for k in frame.winfo_children():
        k.destroy()
    ttk.Label(frame, text='Info successfully saved', foreground='green').grid(row=0, column=0, padx=40, pady=30)
    ttk.Label(frame, text='Do you want to create a flight too?').grid(row=1, column=1, padx=40, pady=30)
    ttk.Button(frame, text='Yes', command=lambda: Flight_info(g,c,False,b)).grid(row=2, column=0, padx=40, pady=30)
    ttk.Button(frame, text='No',command=lambda: quit()).grid(row=2, column=1, padx=40, pady=30)


def input_other(a):
    for k in frame.winfo_children():
        k.destroy()
    root.geometry('700x800')
    label2 = ttk.Label(frame, text="Model:")
    label2.grid(row=0, column=0, padx=40, pady=30)
    entry2 = ttk.Entry(frame)
    entry2.grid(row=0, column=1, padx=40, pady=30)

    label3 = ttk.Label(frame, text="Passenger Capacity:")
    label3.grid(row=1, column=0, padx=40, pady=30)
    entry3 = ttk.Entry(frame)
    entry3.grid(row=1, column=1, padx=40, pady=30)

    label4 = ttk.Label(frame, text="Cruising Speed:")
    label4.grid(row=2, column=0, padx=40, pady=30)
    entry4 = ttk.Entry(frame)
    entry4.grid(row=2, column=1, padx=40, pady=30)

    label5 = ttk.Label(frame, text="Maximum Cruising Speed:")
    label5.grid(row=3, column=0, padx=40, pady=30)
    entry5 = ttk.Entry(frame)
    entry5.grid(row=3, column=1, padx=40, pady=30)

    label6 = ttk.Label(frame, text="Take off speed:")
    label6.grid(row=4, column=0, padx=40, pady=30)
    entry6 = ttk.Entry(frame)
    entry6.grid(row=4, column=1, padx=40, pady=30)

    label7 = ttk.Label(frame, text="Fuel Capacity:")
    label7.grid(row=5, column=0, padx=40, pady=30)
    entry7 = ttk.Entry(frame)
    entry7.grid(row=5, column=1, pady=30, padx=40)

    label8 = ttk.Label(frame, text="Fuel Type:")
    label8.grid(row=6, column=0, padx=40, pady=30)
    entry8 = ttk.Entry(frame)
    entry8.grid(row=6, column=1, padx=40, pady=30)

    Litre = ttk.Label(frame, text='Litre')
    Litre.grid(row=5, column=2, pady=30, padx=40)

    label9 = ttk.Label(frame, text="")
    label9.grid(row=7, column=0, padx=40, pady=30)
    button9 = ttk.Button(frame, text='Submit',command=lambda: flight_type(entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry7.get(),entry8.get(), a, entry6.get()))
    button9.grid(row=7, column=1, padx=40, pady=30)


def check_key(a, d):
    b = admin.check_flight_type(a)
    if b==1:
        for k in frame.winfo_children():
            k.destroy()

        if d is False:
            ttk.Label(frame, text='Key already exists', foreground='red').grid(row=1, column=0, padx=40, pady=30)
            ttk.Button(frame, text='Back', command=Addn_flight).grid(row=0, column=0, padx=40, pady=30)

        if d is True:
            ttk.Label(frame, text='Valid key', foreground='green').grid(row=1, column=0, padx=40, pady=30)
            ttk.Button(frame, text='Next', command=lambda: Flight_info(a, lambda: admin.Check_flight_avgs(a), True)).grid(row=0, column=0, padx=40, pady=30)


    elif b==0:
        for k in frame.winfo_children():
            k.destroy()

        if d is False:
            ttk.Label(frame, text='Valid Key', foreground='green').grid(row=0, column=0, padx=40, pady=40)
            ttk.Button(frame, text='Next', command=lambda: input_other(a)).grid(row=1, column=0, padx=40, pady=30)

        if d is True:
            ttk.Label(frame, text='Key not found', foreground='red').grid(row=0, column=0, padx=40, pady=40)
            ttk.Button(frame, text='Back', command=Addo_flight).grid(row=1, column=0, padx=40, pady=30)


def Addn_flight():
    for k in frame.winfo_children():
        k.destroy()
    root.geometry('700x500')
    label1 = ttk.Label(frame, text="Airplane key:")
    label1.grid(row=0, column=0, padx=40, pady=30)
    entry1 = ttk.Entry(frame)
    entry1.grid(row=0, column=1, padx=40, pady=30)

    Subut = ttk.Button(frame, text='Check', command=lambda: check_key(entry1.get(), False))
    Subut.grid(row=1, column=0, padx=40, pady=30)


def Addo_flight():
    for k in frame.winfo_children():
        k.destroy()
    label1 = ttk.Label(frame, text='Airplane key')
    label1.grid(row=0, column=0, padx=40, pady=30)
    entry1 = ttk.Entry(frame)
    entry1.grid(row=0, column=1, padx=40, pady=30)

    submitb = ttk.Button(frame, text='Submit', command=lambda: check_key(entry1.get(), True))
    submitb.grid(row=1, column=0, padx=40, pady=30)


def fladd():
    for k in frame.winfo_children():
        k.destroy()
    root.geometry('550x300')

    Button(frame, text='Add new flight', command=Addn_flight, bg='#81D2C7', ).pack(side=LEFT, expand=True, fill=BOTH)
    Button(frame, text='Use old flight', command=Addo_flight, bg='#9BC6CC', ).pack(side=RIGHT, expand=True, fill=BOTH)


def only_flight(b1,b2='nothing',c1='nothing'):

    if b2=='nothing':
        d=admin.via_key(b1,False)               #
        if type(d)==list:
            y=0
            for x in frame.winfo_children():
                x.destroy()
            my_canvas = Canvas(frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # add a scrollbar
            my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            # create another frame inside the canvas
            second_frame = Frame(my_canvas)
            # add that new frame to a window in canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
            root.geometry('700x700')
            for x in range(0,len(d)-1):



                Label(second_frame, text='Airplane key:'+d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Date:'+ d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                y+=1
                Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                y+=1
                Label(second_frame, text= d[x][12]).grid(row=y, column=0, padx=40, pady=30)

        else:
            Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
    elif b2!='nothing':
        if c1=='nothing':
            for x in frame.winfo_children():
                x.destroy()
            d=admin.via_time(b1,b2,False)

            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(0, len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
            else:
                Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        elif c1 is True:
            for x in frame.winfo_children():
                x.destroy()
            d=admin.via_dec(b1,b2,False)
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(0, len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
            else:
                Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        else:
            d=admin.via_dpc(b1,b2,False)
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(0, len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
            else:
                Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)


def flight_psgn_lst(b1,b2='nothing',c2='nothing'):
    for x in frame.winfo_children():
        x.destroy()
    d=admin.via_key(b1,True,'all')
    if b2 == 'nothing':
        if type(d)==list:
            y=0
            my_canvas = Canvas(frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # add a scrollbar
            my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            # create another frame inside the canvas
            second_frame = Frame(my_canvas)
            # add that new frame to a window in canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
            root.geometry('700x700')
            for x in range(len(d)-1):
                Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                y+=1
                if d[-1]==True:
                    scroll=Scrollbar(second_frame)
                    scroll.pack(side=RIGHT,fill=y)
                    listbox=Listbox(second_frame, yscrollcommand=scroll.set)
                    for z in range(13,len(d[x])):
                        listbox.insert(END,d[x][z])

                    listbox.grid(row=y, column=0, pady=30, padx=40)
                    scroll.config(command=listbox.yview)
                    y+=1
                else:
                    y+=1
                    Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)


        else:
            Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
    if b2!='nothing':
        if c2=='nothing':
            d=admin.via_time(b1, b2, True, 'all')
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        elif c2 is True:
            d=admin.via_dec(b1, b2, True, 'all')
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        else:
            d=admin.via_dpc(b1, b2, True, 'all')
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)


def flight_sng_psgn(b1,b2='nothing',c2='nothing'):
    for x in frame.winfo_children():
        x.destroy()
    Label(frame, text='Passenger Key:').pack(side=LEFT)

    entry1=Entry(frame)
    entry1.pack(side=LEFT)
    d=admin.via_key(b1,True,)
    if b2 == 'nothing':
        d=admin.via_key(b1,True,'key',entry1.get())
        if type(d) == list:

            my_canvas = Canvas(frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # add a scrollbar
            my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            # create another frame inside the canvas
            second_frame = Frame(my_canvas)
            # add that new frame to a window in canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
            root.geometry('700x700')
            y = 0
            for x in range(len(d) - 1):
                Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                y += 1
                Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                y+=1
                if d[-1] == True:
                    scroll = Scrollbar(second_frame)
                    scroll.pack(side=RIGHT, fill=y)
                    listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                    for z in range(13, len(d[x])):
                        listbox.insert(END, d[x][z])

                    listbox.grid(row=y, column=0, pady=30, padx=40)
                    scroll.config(command=listbox.yview)
                    y += 1
                else:
                    y += 1
                    Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)

        else:
            Label(frame,text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
    if b2 != 'nothing':
        if c2 == 'nothing':
            d = admin.via_time(b1, b2, True, 'key', entry1.get())
            if type(d) == list:
                y=0
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        elif c2 is True:
            d = admin.via_dec(b1, b2, True, 'key',entry1.get())
            if type(d) == list:
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                y = 0

                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)
        else:
            d = admin.via_dpc(b1, b2, True, 'key',entry1.get())
            if type(d) == list:
                my_canvas = Canvas(frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                # add a scrollbar
                my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # configure the canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                # create another frame inside the canvas
                second_frame = Frame(my_canvas)
                # add that new frame to a window in canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
                root.geometry('700x700')
                y=0
                for x in range(len(d) - 1):
                    Label(second_frame, text='Airplane key:' + d[x][0]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Flight key:' + d[x][1]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='From:' + d[x][2]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Departure Time:' + d[x][3]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='To:' + d[x][4]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='ETA:' + d[x][5]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Total Distance:' + d[x][6]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Date:' + d[x][7]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Estimated Travel Time:' + d[x][8]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Available:' + d[x][9]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text='Seats Occupied:' + d[x][10]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][11]).grid(row=y, column=0, padx=40, pady=30)
                    y += 1
                    Label(second_frame, text=d[x][12]).grid(row=y, column=0, padx=40, pady=30)
                    y+=1
                    if d[-1] == True:
                        scroll = Scrollbar(second_frame)
                        scroll.pack(side=RIGHT, fill=y)
                        listbox = Listbox(second_frame, yscrollcommand=scroll.set)
                        for z in range(13, len(d[x])):
                            listbox.insert(END, d[x][z])

                        listbox.grid(row=y, column=0, pady=30, padx=40)
                        scroll.config(command=listbox.yview)
                        y += 1
                    else:
                        y += 1
                        Label(second_frame, text='passenger not found').grid(row=y, column=0, padx=40, pady=30)
            else:
                Label(frame, text='No such flight found').grid(row=0, column=0, pady=40, padx=30)

def key_act(entry1):
    for x in frame.winfo_children():
        x.destroy()

    label2 = Label(frame, text='Choose :')
    label2.grid(row=1, column=1, padx=40, pady=30)

    Rbutton1 = Button(frame, text='Only Flight', command=lambda: only_flight(entry1))
    Rbutton1.grid(row=2, column=0, ipadx=40, ipady=30)

    Rbutton2 = Button(frame, text='Flight with the passenger list', command=lambda: flight_psgn_lst(entry1))
    Rbutton2.grid(row=3, column=0, ipadx=40, ipady=30)

    Rbutton3 = Button(frame, text='flight with single passenger', command=lambda: flight_sng_psgn(entry1))
    Rbutton3.grid(row=4, column=0, ipadx=40, ipady=30)


def via_key():
    for x in frame.winfo_children():
        x.destroy()
    back_button = Button(frame, text='Back', command=archive)
    back_button.grid(row=0, column=0)

    label1 = Label(frame, text='Key')
    label1.grid(row=1, column=0, padx=40, pady=30)
    entry1 = Entry(frame)
    entry1.grid(row=1, column=1, padx=40, pady=30)

    Button(frame, text='Submit',command=lambda : key_act(entry1.get())).grid(row=2, column=0, padx=40, pady=30)



def dec_act(cal,a):
    for x in frame.winfo_children():
        x.destroy()
    date = cal.get_date().replace('/',':')

    label2 = Label(frame, text='Choose :')
    label2.grid(row=1, column=0, padx=40, pady=30)

    Rbutton1 = Button(frame, text='Only Flight', command=lambda: only_flight(a, date, True))
    Rbutton1.grid(row=2, column=0, ipadx=40, ipady=30)

    Rbutton2 = Button(frame, text='Flight with the passenger list',
                      command=lambda: flight_psgn_lst(a, date, True))
    Rbutton2.grid(row=3, column=0, ipadx=40, ipady=30)

    Rbutton3 = Button(frame, text='flight with single passenger',
                      command=lambda: flight_sng_psgn(a, date, True))
    Rbutton3.grid(row=4, column=0, ipadx=40, ipady=30)


def via_dec():
    for x in frame.winfo_children():
        x.destroy()

    root.geometry('700x700')
    back_button = Button(frame, text='Back', command=archive)
    back_button.grid(row=0, column=0)

    label1 = Label(frame, text='Destination City:')
    label1.grid(row=1, column=0, padx=40, pady=30)
    entry1 = Entry(frame)
    entry1.grid(row=1, column=1, padx=40, pady=30)

    label5 = ttk.Label(frame, text='Date ')
    label5.grid(row=2, column=0, padx=40, pady=30)

    cal = Calendar(frame, selectmode="day", year=2021, month=2, day=3)
    cal.grid(row=3,column=0,padx=40,pady=30)

    Button(frame, text='Submit', command=lambda: dep_act(cal, entry1.get())).grid(row=5,column=0,padx=40,pady=30)



def dep_act(cal,a):
    for x in frame.winfo_children():
        x.destroy()
    date=cal.get_date().replace('/',':')
    label2 = Label(frame, text='Choose :')
    label2.grid(row=4, column=0, padx=40, pady=30)

    Rbutton1 = Button(frame, text='Only Flight', command=lambda: only_flight(a, date, False))
    Rbutton1.grid(row=3, column=0, ipadx=40, ipady=30)

    Rbutton2 = Button(frame, text='Flight with the passenger list',
                      command=lambda: flight_psgn_lst(a, date, False))
    Rbutton2.grid(row=4, column=0, ipadx=40, ipady=30)

    Rbutton3 = Button(frame, text='flight with single passenger',
                      command=lambda: flight_sng_psgn(a, date, False))
    Rbutton3.grid(row=5, column=0, ipadx=40, ipady=30)


def via_dep():
    for x in frame.winfo_children():
        x.destroy()
    back_button = Button(frame, text='Back', command=archive)
    back_button.grid(row=0, column=0)

    label1 = Label(frame, text='Departure City:')
    label1.grid(row=1, column=0, padx=40, pady=30)
    entry1 = Entry(frame)
    entry1.grid(row=1, column=1, padx=40, pady=30)

    label5 = ttk.Label(frame, text='Date ')
    label5.grid(row=2, column=0, padx=40, pady=30)

    cal = Calendar(frame, selectmode="day", year=2021, month=2, day=3)
    cal.grid(row=3, column=0,padx=40, pady=30)

    Button(frame, text='Submit',command=lambda: dep_act(cal,entry1.get())).grid(row=4, column=0, padx=40, pady=30)


def via_time():
    for x in frame.winfo_children():
        x.destroy()
    global last_value,last_value_sec,min_string,hour_string
    for x in frame.winfo_children():
        x.destroy()
    back_button = Button(frame, text='Back', command=archive)
    back_button.grid(row=0, column=0)

    Label(frame, text='Date:').grid(row=1, column=0, padx=40, pady=30)

    cal = Calendar(frame, selectmode="day", year=2021, month=2, day=3)
    cal.grid(row=1, column=1, padx=40, pady=30)

    min_sb = Spinbox(frame, from_=0, to=23, wrap=True, textvariable=hour_string, width=2, state="readonly", font=f,justify=CENTER)
    sec_hour = Spinbox(frame, from_=0, to=59, wrap=True, textvariable=min_string, font=f, width=2, justify=CENTER)

    sec = Spinbox(frame, from_=0, to=59, wrap=True, textvariable=sec_hour, width=2, font=f, justify=CENTER)

    min_sb.grid(row=2, column=0, padx=40, pady=30)
    sec_hour.grid(row=2, column=1, padx=40, pady=30)
    sec.grid(row=2, column=2, padx=40, pady=30)

    actionBtn = Button(frame, text="Submit", command=lambda: date_time(cal, min_sb, sec_hour))
    actionBtn.grid(row=3, column=1, pady=30, padx=40)

    if last_value == "59" and min_string.get() == "0":
        hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
        last_value = min_string.get()

    if last_value_sec == "59" and sec_hour.get() == "0":
        min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
    if last_value == "59":
        hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
        last_value_sec = sec_hour.get()


def archive():
    for x in frame.winfo_children():
        x.destroy()
    ttk.Label(frame, text='Search through', font=('Arial', 25)).pack()

    Button(frame, text='Key', bg='#2F4858', fg='white',command=via_key).pack(expand=True, side=RIGHT, fill=BOTH)
    Button(frame, text='Destination and date', bg='#33658A', fg='white', command=via_dec).pack(expand=True, side=TOP, fill=BOTH)
    Button(frame, text='Departure city and date', bg='#F6AE2D',fg='#2F4858', command=via_dep).pack(expand=True, side=BOTTOM, fill=BOTH)
    Button(frame, text='Time of flight and date', bg='#F26419', fg='#1B2D2A', command=via_time).pack(expand=True, side=LEFT, fill=BOTH)


def login_me(Lge,Pwse):
    if Lge.get() == 'root' and Pwse.get() == 'password':
        for k in frame.winfo_children():
            k.destroy()
        root.geometry('550x300')
        Button(frame, text='Add', command=fladd, bg='#81D2C7').pack(side=LEFT, expand=True, fill=BOTH)
        Button(frame, text='Archive', command=archive, bg='#9BC6CC').pack(side=RIGHT, expand=True, fill=BOTH)

    else:

        Label(frame, text='Invalid id or Password', foreground='red').grid(row=3, column=0, padx=40, pady=30)
def admin_panel():

    for k in frame.winfo_children():
        k.destroy()


    Lg = ttk.Label(frame, text='ID:')
    Lg.grid(row=1, column=0, padx=40, pady=30)

    Lge = ttk.Entry(frame)
    Lge.grid(row=1, column=1, padx=40, pady=30)

    pws = StringVar()
    pws.set('Password:')
    Pws = Label(frame, textvariable=pws)
    Pws.grid(row=2, column=0, padx=40, pady=30)

    Pwse = ttk.Entry(frame)
    Pwse.grid(row=2, column=1, padx=40, pady=30)

    L = ttk.Button(frame, text='Login', command=lambda:login_me(Lge, Pwse))
    L.grid(row=3, column=1, padx=40, pady=30)





#Admin panel ends right here

"""-------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""

#passenger panel starts right here


def ck(e1,e2,gender,file):
    for x in frame.winfo_children():
        x.destroy()
    f=open(file,'r')
    u=f.readlines()
    flkey=u[1].strip('\n')
    if gender.get()==1:
        gval='male'
    elif gender.get()==2:
        gval='female'
    psgn_key=psgn_rsrv.Booking(e1,e2,gval,flkey)
    Label(frame, text='Please note your passenger key', font=('Arial',25)).pack()
    Label(frame, text=f'{psgn_key}').pack()
    Button(frame, text='Continue',command=log_in)


def bk(file):
    for x in frame.winfo_children():
        x.destroy()
    back=Button(frame, text='Back', command=via_psc)
    l1=Label(frame, text='Name')
    e1=Entry(frame)
    l2 = Label(frame, text='age')
    e2 = Entry(frame)
    l3 = Label(frame, text='gender')
    gender=IntVar()
    c1 = Radiobutton(frame, text='M', variable=gender, value=1)
    c2 = Radiobutton(frame, text='F', variable=gender, value=2)

    back.grid(row=0, column=0, padx=40, pady=30)
    l1.grid(row=1, column=0, padx=40, pady=30)
    e1.grid(row=1, column=1, padx=40, pady=30)
    l2.grid(row=2, column=0, padx=40, pady=30)
    e2.grid(row=2, column=1, padx=40, pady=30)
    l3.grid(row=3, column=0, padx=40, pady=30)
    c1.grid(row=3, column=1, padx=40, pady=30)
    c2.grid(row=3, column=2, padx=40, pady=30)

    Submit=Button(frame, text='Submit', command=lambda: ck(e1.get(),e2.get(),gender,file))
    Submit.grid(row=4, column=0,pady=40,padx=30)


def pron(cal,entry1,entry2):
    date=cal.get_date().replace('/',':')
    d=psgn_rsrv.via_ev(date,entry1.get(),entry2.get())

    if type(d)==list:
        for x in range(len(d)):
            f=open(d[x],'r')
            u=f.readlines()
            u[2]=u[2].strip('\n')
            u[3] = u[3].strip('\n')
            u[4] = u[4].strip('\n')
            u[5] = u[5].strip('\n')
            for k in frame.winfo_children():
                k.destroy()

            Label(frame, text=f"{u[2]} ({u[3]})  -  {u[4]} ({u[5]})").grid(row=x, column=0, padx=40, pady=30)
            Button(frame,text='Book',command=lambda: bk(d[x])).grid(row=x, column=1, padx=40, pady=30)
    if type(d)==bool:
        for k in frame.winfo_children():
            k.destroy()
        Label(frame, text='No flight found', fg='red').pack()
        Button(frame, text='Try again', command=book_fl).pack()

def via_psc():
    for x in frame.winfo_children():
        x.destroy()

    root.geometry('700x700')
    back_button = Button(frame, text='Back', command=psgn_login)
    back_button.grid(row=0, column=0)

    label1 = Label(frame, text='From:')
    label1.grid(row=1, column=0, padx=40, pady=30)
    entry1 = Entry(frame)
    entry1.grid(row=1, column=1, padx=40, pady=30)

    label2 = Label(frame, text='To:')
    label2.grid(row=2, column=0, padx=40, pady=30)
    entry2 = Entry(frame)
    entry2.grid(row=2, column=1, padx=40, pady=30)

    label5 = ttk.Label(frame, text='Date:')
    label5.grid(row=3, column=0, padx=40, pady=30)

    cal = Calendar(frame, selectmode="day", year=2021, month=2, day=3)
    cal.grid(row=4,column=0,padx=40,pady=30)

    Button(frame, text='Submit', command=lambda: pron(cal,entry1,entry2)).grid(row=5,column=0,padx=40,pady=30)



def book_fl():
    for x in frame.winfo_children():
        x.destroy()
    ttk.Label(frame, text='Search through', font=('Arial', 25)).pack()

    Button(frame, text='Destination and date', bg='#33658A', fg='white', command=via_psc).pack(expand=True, side=TOP, fill=BOTH)

def view_tk(p):
    for x in frame.winfo_children():
        x.destroy()
    my_canvas = Canvas(frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # add a scrollbar
    my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # create another frame inside the canvas
    second_frame = Frame(my_canvas)
    # add that new frame to a window in canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    root.geometry('700x700')
    Button(second_frame, text='Back',command=my_fl).grid(row=0, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Passenger key: {p[0]}').grid(row=1, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Name: {p[1]}').grid(row=2, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Age: {p[2]}').grid(row=3, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Gender: {p[3]}').grid(row=4, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Flight key: {p[4]}').grid(row=5, column=0, padx=40, pady=30)
    Label(second_frame, text=f'From: {p[5]}').grid(row=6, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Time of Departure: {p[6]}').grid(row=7, column=0, padx=40, pady=30)
    Label(second_frame, text=f'To: {p[7]}').grid(row=8, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Time of Arrival: {p[8]}').grid(row=9, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Total Distance: {p[9]}').grid(row=10, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Date: {p[10]}').grid(row=11, column=0, padx=40, pady=30)
    Label(second_frame, text=f'Travelling Time: {p[11]}').grid(row=12, column=0, padx=40, pady=30)

def my_fl():
    for x in frame.winfo_children():
        x.destroy()
    if len(psgn_rsrv.psgn_tkt)==0:
        Label(frame, text='Book a ticket first',font=('Arial',45)).pack(side=BOTTOM)
    else:
        my_canvas = Canvas(frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # add a scrollbar
        my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # create another frame inside the canvas
        second_frame = Frame(my_canvas)
        # add that new frame to a window in canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        root.geometry('700x700')
        d=psgn_rsrv.ticket_print()
        for x in range(len(d)):
            Label(second_frame,text=f'passenger key: {d[x][0]}').grid(row=x, column=0, padx=30, pady=40)
            Button(second_frame,text='View ticket',command=lambda: view_tk(d[x])).grid(row=x, column=1, pady=40, padx=30)



def Select(Lge, Pwse):
    if Lge.get() == 'root' and Pwse.get() == 'password':
        for k in frame.winfo_children():
            k.destroy()
        root.geometry('550x300')
        Button(frame, text='Book Flight', command=book_fl, bg='#81D2C7').pack(side=LEFT, expand=True, fill=BOTH)
        Button(frame, text='My Flights', command=my_fl, bg='#9BC6CC').pack(side=RIGHT, expand=True, fill=BOTH)

    else:

        Label(frame, text='Invalid id or Password', foreground='red').grid(row=3, column=0, padx=40, pady=30)


def psgn_login():
    for k in frame.winfo_children():
        k.destroy()

    Lg = ttk.Label(frame, text='ID:')
    Lg.grid(row=0, column=0, padx=40, pady=30)

    Lge = ttk.Entry(frame)
    Lge.grid(row=0, column=1, padx=40, pady=30)

    pws = StringVar()
    pws.set('Password:')
    Pws = Label(frame, textvariable=pws)
    Pws.grid(row=1, column=0, padx=40, pady=30)

    Pwse = ttk.Entry(frame)
    Pwse.grid(row=1, column=1, padx=40, pady=30)

    L = ttk.Button(frame, text='Login', command=lambda: Select(Lge, Pwse))
    L.grid(row=2, column=1, padx=40, pady=30)

def log_in():
    for k in frame.winfo_children():
        k.destroy()
    Button(frame, text='Login', command=psgn_login, bg='#9BC6CC').pack(side=RIGHT, expand=True, fill=BOTH)




root.geometry('500x400')
root.title('Announce me/Admin_panel')
frame = Frame(root)
frame.pack(side='top', expand=True, fill='both')

Label(frame, text='Sign in as:',font=('Arial',25)).pack()

Button(frame, text='Admin', command=admin_panel, bg='#81D2C7').pack(side=LEFT, expand=True, fill=BOTH)
Button(frame, text='Passenger', command=log_in, bg='#9BC6CC').pack(side=RIGHT, expand=True, fill=BOTH)


root.mainloop()
