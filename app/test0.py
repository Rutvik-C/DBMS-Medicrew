from tkinter import *
import tkinter.font as font
from requests import request
import json
import pyodbc
from datetime import datetime, date


def get_distance(source, destination):
    try:
        api_key = "XjVG4ySCbF98zHBv5Zvbn7p16HPeb"

        url = "https://api.distancematrix.ai/maps/api/distancematrix/json?"  # outputFormat?parameters
        parameters = "origins=%s&destinations=%s&key=%s" % (source, destination, api_key)

        response = request("GET", url + parameters)
        response = json.loads(response.text)

        dist = int(response["rows"][0]["elements"][0]["distance"]["value"])
        dist_txt = response["rows"][0]["elements"][0]["distance"]["text"]
        time_txt = response["rows"][0]["elements"][0]["duration"]["text"]

        lst = list(dist_txt)
        i = 0
        while i < len(lst):
            if lst[i] == " ":
                del lst[i]
            i += 1
        dist_txt = "".join(lst)

        lst = list(time_txt)
        i = 0
        while i < len(lst):
            if lst[i] == " ":
                del lst[i]
            i += 1
        time_txt = "".join(lst)

        return [dist_txt, time_txt, dist]

    except:
        return ["--", "--", 0]


def display(name, specialization, dist):
    str1 = ""
    str1 += name
    for _ in range(24 - len(name)):
        str1 += " "
    str1 += specialization
    for _ in range(46 - len(str1)):
        str1 += " "
    str1 += dist
    return str1


def get_error(err):
    try:
        x = err.index("xaybz_")
        y = err.index("_axbyc")

        return err[x + 6: y]
    except:
        return err


class General(object):
    def __init__(self):
        self.month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
        self.month_rev = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

        self.default = "def"
        self.elevated = "upd"
        self.user = "USER"
        self.doctor = "DOCTOR"
        self.date = [date.today().strftime("%d"), date.today().strftime("%B"), date.today().strftime("%Y")]
        self.email = ""
        self.password = ""
        self.f_name = ""
        self.l_name = ""
        self.locality = ""
        self.city = ""
        self.building = ""
        self.pin = None
        self.phone = None
        self.special = "SELECT"
        self.fee = None
        self.minor = "Y"
        self.gender = ""
        self.buffer_1 = ""
        self.buffer_2 = ""

    def reinitialiser(self):
        self.f_name = "First Name"
        self.l_name = "Last Name"
        self.locality = "Locality"
        self.city = "City"
        self.building = "Building"
        self.pin = "PIN Code"
        self.phone = ""
        self.date = [date.today().strftime("%d"), date.today().strftime("%B"), date.today().strftime("%Y")]
        self.special = "SELECT"
        self.fee = ""
        self.minor = "SELECT"
        self.gender = "SELECT"


class FontStyle(object):
    def __init__(self):
        self.tahoma_bold = font.Font(family="Tahoma", size=20, weight="bold")
        self.tahoma = font.Font(family="Tahoma", size=20)
        self.tahoma_small = font.Font(family="Tahoma", size=10)
        self.tahoma_medium = font.Font(family="Tahoma", size=15)
        self.consolas = font.Font(family="Consolas", size=30, weight="bold")
        self.consolas_medium = font.Font(family="Consolas", size=20)


class Img(object):
    def __init__(self):
        self.logo = PhotoImage(file="./Images/700.gif")
        self.small_logo = PhotoImage(file="./Images/400.gif")
        self.sq_logo = PhotoImage(file="./Images/200.gif")
        self.pers = PhotoImage(file="./Images/user.gif")
        self.doc = PhotoImage(file="./Images/doctor.gif")
        self.dash_my_details = PhotoImage(file="./Images/1.gif")
        self.dash_history = PhotoImage(file="./Images/3.gif")
        self.dash_my_appoint = PhotoImage(file="./Images/2.gif")
        self.dash_sch_meet = PhotoImage(file="./Images/sch.gif")


class Interface(object):
    def __init__(self, root_win):
        self.root = root_win

        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                   'SERVER=medicrewdbms.database.windows.net;'
                                   'DATABASE=medicrewdbms;UID=medicrewdbms;'
                                   'PWD=Abcd1234')
        self.cursor = self.conn.cursor()

        # Creating Img class and FontStyle class object
        self.imag = Img()
        self.fnt = FontStyle()
        self.gen = General()

        # Initialising Frames
        self.curr_frame = Frame()
        self.frame_load = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_log_in = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sign_in_0 = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sign_in_1 = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_info = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_dashboard = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_history = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_details = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sch_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_get_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_show_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_show_his = Frame(self.root, bg="#05161D", height=768, width=1366)

        # Initialising Labels, Entry_widget
        self.entry_1 = Entry()
        self.entry_2 = Entry()
        self.entry_3 = Entry()
        self.entry_4 = Entry()
        self.entry_5 = Entry()
        self.entry_6 = Entry()
        self.entry_7 = Entry()
        self.entry_8 = Entry()
        self.entry_9 = Entry()
        self.entry_10 = Entry()
        self.entry_11 = Entry()
        self.entry_12 = Entry()

        self.label_1 = Label()
        self.b_1 = Button()

        self.list_1 = Listbox()
        self.list_2 = Listbox()
        self.list_3 = Listbox()
        self.list_4 = Listbox()

        self.var_char_1 = StringVar()
        self.var_char_2 = StringVar()
        self.var_char_3 = StringVar()
        self.var_char_4 = StringVar()
        self.var_char_5 = StringVar()
        self.var_char_6 = StringVar()
        self.var_char_7 = StringVar()
        self.var_char_8 = StringVar()

        # Errors
        self.err_1 = False
        self.err_2 = False
        self.err_3 = False
        self.err_4 = False

    def launch_load(self):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing main menu frame
        self.frame_load = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_load.pack()
        self.curr_frame = self.frame_load

        # Creating interactions
        Label(self.frame_load, image=self.imag.logo, height=200, width=695).place(x=320, y=100)

        Button(self.frame_load, height=2, width=15, text="LOG IN", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_log_in(self.gen.default)).place(x=212, y=397)
        Button(self.frame_load, height=2, width=15, text="SIGN IN", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=self.launch_sign_in_0).place(x=890, y=397)

    def launch_log_in(self, _type):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing login frame
        self.frame_log_in = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_log_in.pack()
        self.curr_frame = self.frame_log_in

        # Creating interactions
        Label(self.frame_log_in, image=self.imag.small_logo, height=110, width=390).place(x=500, y=50)
        Label(self.frame_log_in, text="E-Mail ID", height=2, width=15, font=self.fnt.tahoma_bold,
              bg="#05161D", fg="#819EA6").place(x=325, y=310)
        Label(self.frame_log_in, text="Password", height=2, width=15, font=self.fnt.tahoma_bold,
              bg="#05161D", fg="#819EA6").place(x=325, y=400)
        Label(self.frame_log_in, text="LOG IN", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#3AD5D9").place(x=570, y=150)

        self.entry_1 = Entry(self.frame_log_in, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_2 = Entry(self.frame_log_in, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000", show="●")
        if _type == self.gen.elevated:
            self.entry_1.insert(0, self.gen.email)

        Button(self.frame_log_in, height=1, width=10, text="LOG IN", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=self.bridge_log_dash).place(x=590, y=550)
        Button(self.frame_log_in, height=2, width=24, text="Don't have an account?\nSIGN UP",
               font=self.fnt.tahoma_small,
               bg="#05161D", fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=self.launch_sign_in_0).place(x=590, y=625)

        if self.err_1:
            Label(self.frame_log_in, text="E-mail ID not registered!", height=2, width=20, anchor=W,
                  font=self.fnt.tahoma_medium, bg="#05161D", fg="#B40000").place(x=1020, y=315)
        if self.err_2:
            Label(self.frame_log_in, text="Incorrect Password!", height=2, width=16, anchor=W,
                  font=self.fnt.tahoma_medium, bg="#05161D", fg="#B40000").place(x=1020, y=405)

        self.entry_1.place(x=550, y=327)
        self.entry_2.place(x=550, y=417)

    def launch_sign_in_0(self):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing sign in frame
        self.frame_sign_in_0 = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sign_in_0.pack()
        self.curr_frame = self.frame_sign_in_0

        # Creating interactions
        Label(self.frame_sign_in_0, image=self.imag.small_logo, height=110, width=390).place(x=500, y=50)
        Label(self.frame_sign_in_0, text="SIGN IN", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#3AD5D9").place(x=570, y=150)
        Label(self.frame_sign_in_0, text="Who are you?", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#3AD5D9").place(x=575, y=200)

        Button(self.frame_sign_in_0, height=125, width=125, image=self.imag.pers, font=self.fnt.tahoma_bold,
               bg="#05161D", fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_sign_in_1(self.gen.user, self.gen.default)).place(x=500, y=300)
        Button(self.frame_sign_in_0, height=125, width=125, image=self.imag.doc, font=self.fnt.tahoma_bold,
               bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_sign_in_1(self.gen.doctor, self.gen.default)).place(x=750, y=300)
        Button(self.frame_sign_in_0, height=1, width=10, text="BACK", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=self.launch_load).place(x=600, y=550)

    def launch_sign_in_1(self, person, _type):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing sign in frame
        self.frame_sign_in_1 = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sign_in_1.pack()
        self.curr_frame = self.frame_sign_in_1

        # Creating interactions
        Label(self.frame_sign_in_1, image=self.imag.small_logo, height=110, width=390).place(x=500, y=50)
        Label(self.frame_sign_in_1, text=person, height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#3AD5D9").place(x=570, y=200)
        Label(self.frame_sign_in_1, text="SIGN IN", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#3AD5D9").place(x=570, y=150)
        Label(self.frame_sign_in_1, text="E-mail ID", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#819EA6").place(x=325, y=270)
        Label(self.frame_sign_in_1, text="Password", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#819EA6").place(x=325, y=340)
        Label(self.frame_sign_in_1, text="Confirm\nPassword", height=2, width=15, font=self.fnt.tahoma,
              bg="#05161D", fg="#819EA6").place(x=325, y=420)

        self.entry_1 = Entry(self.frame_sign_in_1, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_2 = Entry(self.frame_sign_in_1, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000", show="●")
        self.entry_3 = Entry(self.frame_sign_in_1, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000", show="●")
        if _type == self.gen.elevated:
            self.entry_1.insert(0, self.gen.email)

        Button(self.frame_sign_in_1, height=1, width=10, text="BACK", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=self.launch_sign_in_0).place(x=500, y=550)
        Button(self.frame_sign_in_1, height=1, width=10, text="SIGN IN", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.bridge_s1_myinfo(person)).place(x=700, y=550)

        if self.err_1:
            Label(self.frame_sign_in_1, text="Invalid E-mail ID!", height=2, width=15,
                  font=self.fnt.tahoma_medium,
                  anchor=W, bg="#05161D", fg="#B40000").place(x=1025, y=275)
        if self.err_2:
            Label(self.frame_sign_in_1, text="Passwords did not match!", height=2, width=22,
                  font=self.fnt.tahoma_medium, anchor=W, bg="#05161D", fg="#B40000").place(x=1025, y=350)
        if self.err_3:
            Label(self.frame_sign_in_1, text="Password criteria not met!", height=2, width=22,
                  font=self.fnt.tahoma_medium, anchor=W, bg="#05161D", fg="#B40000").place(x=1025, y=350)
        if self.err_4:
            Label(self.frame_sign_in_1, text="E-Mail ID already registered!", height=2, width=24,
                  font=self.fnt.tahoma_medium, anchor=W, bg="#05161D", fg="#B40000").place(x=1025, y=275)

        self.entry_1.place(x=550, y=287)
        self.entry_2.place(x=550, y=357)
        self.entry_3.place(x=550, y=435)

    def launch_my_info_0(self, person, _type, _id):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_my_info = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_info.pack()
        self.curr_frame = self.frame_my_info

        if _type == self.gen.default:
            self.gen.reinitialiser()

        Label(self.frame_my_info, image=self.imag.sq_logo, height=77, width=195).place(x=25, y=25)
        Label(self.frame_my_info, text="MY INFORMATION\n" + person, height=2, width=15,
              font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=570, y=25)
        Label(self.frame_my_info, text="NAME", height=2, width=15, font=self.fnt.tahoma,
              anchor=W, bg="#05161D", fg="#819EA6").place(x=325, y=125)
        Label(self.frame_my_info, text="ADDRESS", height=2, width=15, font=self.fnt.tahoma,
              anchor=W, bg="#05161D", fg="#819EA6").place(x=325, y=200)
        Label(self.frame_my_info, text="PHONE NUMBER", height=2, width=15, font=self.fnt.tahoma,
              anchor=W, bg="#05161D", fg="#819EA6").place(x=325, y=325)
        Label(self.frame_my_info, text="DATE OF BIRTH", height=2, width=15, font=self.fnt.tahoma,
              anchor=W, bg="#05161D", fg="#819EA6").place(x=325, y=400)
        Label(self.frame_my_info, text="GENDER", height=2, width=15, font=self.fnt.tahoma,
              anchor=W, bg="#05161D", fg="#819EA6").place(x=325, y=475)

        self.entry_1 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_2 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_3 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_4 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_5 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_6 = Entry(self.frame_my_info, width=14, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_7 = Entry(self.frame_my_info, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")

        self.var_char_1.set(self.gen.gender)
        self.var_char_4.set(self.gen.date[0])
        self.var_char_5.set(self.gen.date[1])
        self.var_char_6.set(self.gen.date[2])
        self.list_1 = OptionMenu(self.frame_my_info, self.var_char_1, "MALE", "FEMALE")
        self.list_1.config(font=self.fnt.tahoma_medium, width=37, height=1, bg="#819EA6", fg="#000000")
        self.list_2 = OptionMenu(self.frame_my_info, self.var_char_5, *self.gen.month.keys())
        self.list_2.config(font=self.fnt.tahoma_medium, width=8, height=1, bg="#819EA6", fg="#000000")

        Spinbox(self.frame_my_info, width=8, from_=1, to=31, textvariable=self.var_char_4,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=560, y=415)
        Spinbox(self.frame_my_info, width=8, from_=1940, to=int(datetime.now().year), textvariable=self.var_char_6,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=870, y=415)

        if person == self.gen.user:
            if _type == self.gen.default:
                Button(self.frame_my_info, height=1, width=10, text="CONFIRM", font=self.fnt.tahoma_bold, bg="#05161D",
                       fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                       command=lambda: self.bridge_myinfo_dash(person)).place(x=590, y=610)
            else:
                Button(self.frame_my_info, height=1, width=10, text="CONFIRM", font=self.fnt.tahoma_bold, bg="#05161D",
                       fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                       command=lambda: self.bridge_upd_myinfo_dash(person, _id)).place(x=590, y=610)

        else:  # Doctor
            Button(self.frame_my_info, height=1, width=10, text="NEXT", font=self.fnt.tahoma_bold, bg="#05161D",
                   fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                   command=lambda: self.launch_my_info_1(person, _type, _id)).place(x=590, y=610)

        self.entry_1.place(x=560, y=140)  # f name
        self.entry_2.place(x=800, y=140)  # l name
        self.entry_3.place(x=560, y=215)  # address
        self.entry_4.place(x=800, y=215)  # address
        self.entry_5.place(x=560, y=265)  # address
        self.entry_6.place(x=800, y=265)  # address
        self.entry_7.place(x=560, y=340)

        self.entry_1.insert(0, self.gen.f_name)
        self.entry_2.insert(0, self.gen.l_name)
        self.entry_3.insert(0, self.gen.building)
        self.entry_4.insert(0, self.gen.locality)
        self.entry_5.insert(0, self.gen.city)
        self.entry_6.insert(0, self.gen.pin)
        self.entry_7.insert(0, self.gen.phone)

        self.list_1.place(x=560, y=490)
        self.list_2.place(x=720, y=415)

    def launch_my_info_1(self, person, _type, _id):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_my_info = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_info.pack()
        self.curr_frame = self.frame_my_info

        Label(self.frame_my_info, image=self.imag.sq_logo, height=77, width=195).place(x=25, y=25)
        Label(self.frame_my_info, text="MY INFORMATION\n" + person, height=2, width=15,
              font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=570, y=25)
        Label(self.frame_my_info, text="SPECIALIZATION", height=2, width=15,
              anchor=W, font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=325, y=200)
        Label(self.frame_my_info, text="ALLOW MINORS", height=2, width=15,
              anchor=W, font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=325, y=275)
        Label(self.frame_my_info, text="FEE", height=2, width=15,
              anchor=W, font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=325, y=350)

        self.entry_8 = Entry(self.frame_my_info, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_9 = Entry(self.frame_my_info, width=30, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")

        self.var_char_2.set(self.gen.minor)
        self.var_char_3.set(self.gen.special)
        self.list_1 = OptionMenu(self.frame_my_info, self.var_char_2, "YES", "NO")
        self.list_1.config(font=self.fnt.tahoma_medium, width=37, height=1, bg="#819EA6", fg="#000000")
        self.list_2 = OptionMenu(self.frame_my_info, self.var_char_3, *('Audiologist', 'Cardiologist', 'Cardiothoracic',
                                                                        'Dentist', 'ENT specialist', 'Endocrinologist',
                                                                        'General Practicioner', 'Gynaecologist',
                                                                        'Homeopath', 'Neurologist', 'Oncologist',
                                                                        'Orthopaedic', 'Paediatrician', 'Psychiatrist',
                                                                        'Pulmonologist', 'Radiologist', 'Veterinarian'))
        self.list_2.config(font=self.fnt.tahoma_medium, width=37, height=1, bg="#819EA6", fg="#000000")

        if _type == self.gen.default:
            Button(self.frame_my_info, height=1, width=10, text="CONFIRM", font=self.fnt.tahoma_bold, bg="#05161D",
                   fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                   command=lambda: self.bridge_myinfo_dash(person)).place(x=590, y=610)
        else:
            Button(self.frame_my_info, height=1, width=10, text="CONFIRM", font=self.fnt.tahoma_bold, bg="#05161D",
                   fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                   command=lambda: self.bridge_upd_myinfo_dash(person, _id)).place(x=590, y=610)

        self.entry_8.place(x=560, y=365)

        self.entry_8.insert(0, self.gen.fee)

        self.list_1.place(x=560, y=290)
        self.list_2.place(x=560, y=215)

    def launch_dashboard(self, person, _id):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_dashboard = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_dashboard.pack()
        self.curr_frame = self.frame_dashboard

        # Loading data of user
        query = "SELECT * FROM %s_table WHERE %s_id = %i" % (person, person, _id)
        res = self.execute_query_read_s(query)
        if res is None:
            self.launch_load()

        else:
            # Creating interactions
            Label(self.frame_dashboard, image=self.imag.sq_logo, height=77, width=195).place(x=25, y=25)
            if person == self.gen.user:
                Label(self.frame_dashboard, text="Hello, " + res[2], height=2, width=30, anchor=W,
                      font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=35, y=105)
            else:
                Label(self.frame_dashboard, text="Hello, Dr. " + res[2], height=2, width=30, anchor=W,
                      font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=35, y=105)

            if person == self.gen.user:
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_sch_meet,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.launch_schedule_appointment(person, self.gen.default, _id, True)).place(
                    x=115, y=250)
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_my_appoint,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.launch_my_appointments(person, _id)).place(
                    x=425, y=250)
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_history,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.launch_appointment_history(person, _id)).place(x=735, y=250)
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_my_details,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.bridge_change_details(person, _id)).place(x=1045, y=250)
            else:
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_my_appoint,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.launch_my_appointments(person, _id)).place(x=270, y=250)
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_history,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.launch_appointment_history(person, _id)).place(x=580, y=250)
                Button(self.frame_dashboard, height=280, width=210, image=self.imag.dash_my_details,
                       font=self.fnt.tahoma_bold, cursor='hand2',
                       command=lambda: self.bridge_change_details(person, _id)).place(x=890, y=250)

            Button(self.frame_dashboard, height=1, width=10, text="SIGN OUT", font=self.fnt.tahoma_bold, bg="#05161D",
                   fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                   command=self.launch_load).place(x=1150, y=25)

    def launch_schedule_appointment(self, person, _type, _id, calc):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_sch_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_sch_app.pack()
        self.curr_frame = self.frame_sch_app

        self.gen.buffer_2 = [person, _id]

        # Creating interactions
        Button(self.frame_sch_app, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)

        Button(self.frame_sch_app, height=3, width=20, text="SEARCH!", font=self.fnt.tahoma_medium, bg="#819EA6",
               fg="#000000", activebackground="#05161D", activeforeground="#819EA6", cursor='hand2',
               command=lambda: self.bridge_schedule_schedule(_id)).place(x=1060, y=125)

        Label(self.frame_sch_app, text="SEARCH A DOCTOR!", height=2, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=25)
        Label(self.frame_sch_app, text="Name", height=1, width=23,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=25, y=245)
        Label(self.frame_sch_app, text="Specialization", height=1, width=21,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=550, y=245)
        if self.var_char_1.get() == "Distance" or self.var_char_1.get() == "Fee":
            Label(self.frame_sch_app, text=self.var_char_1.get(), height=1, width=14,
                  font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=1030, y=245)
        else:
            Label(self.frame_sch_app, text="-- --", height=1, width=14,
                  font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=1030, y=245)
        Label(self.frame_sch_app, text="Name", height=1, width=8, anchor=W,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=100, y=175)

        self.list_1 = Listbox(self.frame_sch_app, font=self.fnt.consolas, height=8, width=60, cursor="hand2",
                              selectmode=SINGLE, borderwidth=0, highlightthickness=0, bg="#05161D", fg="#3AD5D9",
                              exportselection=0)
        self.list_1.bind('<<ListboxSelect>>', self.launch_schedule_appointment_1)

        if _type == self.gen.default:
            self.var_char_1.set("Sort by")
            self.var_char_2.set("Specialization")
            self.var_char_3.set("Filter by")

        self.list_2 = OptionMenu(self.frame_sch_app, self.var_char_1, "Name", "Fee", "Distance")
        self.list_2.config(font=self.fnt.tahoma_medium, width=23, height=1, bg="#819EA6", fg="#000000")
        self.list_3 = OptionMenu(self.frame_sch_app, self.var_char_2,
                                 *('Any', 'Audiologist', 'Cardiologist', 'Cardiothoracic',
                                   'Dentist', 'ENT specialist', 'Endocrinologist',
                                   'General Practicioner', 'Gynaecologist',
                                   'Homeopath', 'Neurologist', 'Oncologist',
                                   'Orthopaedic', 'Paediatrician', 'Psychiatrist',
                                   'Pulmonologist', 'Radiologist', 'Veterinarian'))
        self.list_3.config(font=self.fnt.tahoma_medium, width=23, height=1, bg="#819EA6", fg="#000000")
        self.list_4 = OptionMenu(self.frame_sch_app, self.var_char_3, "Any", "My locality")
        self.list_4.config(font=self.fnt.tahoma_medium, width=23, height=1, bg="#819EA6", fg="#000000")

        self.entry_1 = Entry(self.frame_sch_app, width=27, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_1.insert(END, "First Name (optional)")
        self.entry_2 = Entry(self.frame_sch_app, width=27, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
        self.entry_2.insert(END, "Last Name (optional)")

        if _type != self.gen.default:
            # if self.gen.buffer_1 is not None and len(self.gen.buffer_1) > 0:
            if calc:
                t = self.execute_query_read_s(
                    "SELECT building, locality, city, pincode, DATEDIFF(year, dob, GETDATE()) FROM user_table WHERE user_id = %d" % _id)
                cli_add = t[0] + " " + t[1] + " " + t[2] + " " + str(t[3])
                to_show = []
                cli_age = int(t[4])

                for doc in self.gen.buffer_1:
                    doc = list(doc)
                    if doc[14] == "YES" or (doc[14] == "NO" and cli_age >= 18):
                        if self.var_char_3.get() == "My locality" and self.var_char_1.get() == "Distance":
                            dest_add = doc[7] + " " + doc[8] + " " + doc[9] + " " + str(doc[10])
                            t = get_distance(cli_add, dest_add)
                            doc.extend(t)
                        elif self.var_char_1.get() == "Fee":
                            doc.extend(["", "₹ " + str(doc[13]), doc[13]])
                        else:
                            doc.extend(["--", "--", 0])

                        to_show.append(doc)

                self.gen.buffer_1 = to_show
                self.gen.buffer_1.sort(key=lambda x: x[-1])

            if self.gen.buffer_1 is not None and len(self.gen.buffer_1) > 0:
                for doc in self.gen.buffer_1:
                    self.list_1.insert(END, display("Dr." + doc[2] + " " + doc[3], doc[12], doc[15] + " " + doc[16]))

                self.list_1.place(x=25, y=300)

            else:
                Label(self.frame_sch_app, text="Oops! No ones here...", height=2, width=25,
                      font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=400)

        self.list_2.place(x=423, y=125)
        self.list_3.place(x=100, y=125)
        self.list_4.place(x=745, y=125)

        self.entry_1.place(x=200, y=175)
        self.entry_2.place(x=633, y=175)

    def launch_schedule_appointment_1(self, _type):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_get_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_get_app.pack()
        self.curr_frame = self.frame_get_app

        person, _id = self.gen.buffer_2[0], self.gen.buffer_2[1]
        doc = self.gen.buffer_1[self.list_1.curselection()[0]]

        local_buff, buffered = [], False
        if doc[15] in ("--", ""):
            t = self.execute_query_read_s(
                "SELECT building, locality, city, pincode FROM user_table WHERE user_id = %d" % int(_id))
            cli_add = t[0] + " " + t[1] + " " + t[2] + " " + str(t[3])
            dest_add = doc[7] + " " + doc[8] + " " + doc[9] + " " + str(doc[10])
            t = get_distance(cli_add, dest_add)
            if doc[15] == "" and len(doc[16]) > 1:
                buffered = True
                local_buff = [doc[15], doc[16]]
            doc[15], doc[16] = t[0], t[1]

        # Interactions
        Button(self.frame_get_app, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)

        Label(self.frame_get_app, text="BOOK AN APPOINTMENT", height=1, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=500, y=25)
        Label(self.frame_get_app, text="NAME\t\tDr. " + doc[2] + " " + doc[3], height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=75)
        Label(self.frame_get_app, text="SPECIALIZATION\t" + doc[12], height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=115)
        Label(self.frame_get_app, text="ADDRESS\t\t%s %s" % (doc[7], doc[8]),
              height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D",
              fg="#3AD5D9").place(x=400, y=160)
        Label(self.frame_get_app, text="%s %s (Dist: %s, Time: %s)" % (doc[9], doc[10], doc[15], doc[16]),
              height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D",
              fg="#3AD5D9").place(x=640, y=195)
        Label(self.frame_get_app, text="PHONE NUMBER\t" + str(doc[11]), height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=240)
        Label(self.frame_get_app, text="E-MAIL\t\t" + doc[1], height=1, width=55,
              font=self.fnt.consolas_medium,
              anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=290)
        Label(self.frame_get_app, text="CHECK-UP FEE\tRs " + str(doc[13]), height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=330)
        Label(self.frame_get_app, text="GENDER\t\t" + doc[4], height=1, width=55,
              font=self.fnt.consolas_medium,
              anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=370)
        Label(self.frame_get_app, text="MINORS ALLOWED\t" + str(doc[14]), height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=410)
        Label(self.frame_get_app, text="Set Date and Time", height=1, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=500, y=460)
        Label(self.frame_get_app, text="hrs", height=1, width=8, anchor=W,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=805, y=520)
        Label(self.frame_get_app, text="min", height=1, width=8, anchor=W,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=950, y=520)
        if _type == self.gen.elevated:
            Label(self.frame_get_app, text="Appointment not available!", height=2, width=30, anchor=W,
                  font=self.fnt.tahoma, bg="#05161D", fg="#B40000").place(x=1025, y=500)

        if buffered:
            doc[15], doc[16] = local_buff

        self.var_char_6.set(date.today().strftime("%d"))
        self.var_char_7.set(date.today().strftime("%B"))
        self.var_char_8.set(date.today().strftime("%Y"))

        self.list_2 = OptionMenu(self.frame_get_app, self.var_char_7, *self.gen.month.keys())
        self.list_2.config(font=self.fnt.tahoma_medium, width=8, height=1, bg="#819EA6", fg="#000000")
        self.list_2.place(x=453, y=519)

        Spinbox(self.frame_get_app, width=5, from_=1, to=31, textvariable=self.var_char_6,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=350, y=520)
        Spinbox(self.frame_get_app, width=5, from_=1940, to=int(datetime.now().year), textvariable=self.var_char_8,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=590, y=520)

        self.b_1.place(x=350, y=520)
        Button(self.frame_get_app, height=1, width=20, text="BACK", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_schedule_appointment(self.gen.user, self.gen.elevated, _id, False)).place(
            x=300, y=600)
        Button(self.frame_get_app, height=1, width=20, text="GET APPOINTMENT", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.terminal_schedule_appointment(_id, doc)).place(x=700, y=600)

        Spinbox(self.frame_get_app, width=5, from_=10, to=24, textvariable=self.var_char_4,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=710, y=520)
        Spinbox(self.frame_get_app, width=5,
                values=("00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"),
                textvariable=self.var_char_5,
                bg="#819EA6", fg="#000000", font=self.fnt.tahoma).place(x=850, y=520)

    def launch_my_appointments(self, person, _id):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_my_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_my_app.pack()
        self.curr_frame = self.frame_my_app

        self.gen.buffer_2 = [person, _id]

        # Creating interactions
        Label(self.frame_my_app, text="Your Upcoming Appointments", height=2, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=25)
        Label(self.frame_my_app, text="Name", height=1, width=23,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=175, y=165)
        Label(self.frame_my_app, text="Date / Time", height=1, width=22,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=697, y=165)

        Button(self.frame_my_app, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)

        self.list_1 = Listbox(self.frame_my_app, font=self.fnt.consolas, height=10, width=48, cursor="hand2",
                              selectmode=SINGLE, borderwidth=0, highlightthickness=0, bg="#05161D", fg="#3AD5D9",
                              exportselection=0)
        self.list_1.bind('<<ListboxSelect>>', self.launch_my_appointment_1)

        query = "SELECT * FROM appoints JOIN user_table ON appoints.user_id = user_table.user_id JOIN doctor_table ON appoints.doctor_id = doctor_table.doctor_id WHERE user_table.user_id = %d AND appointment_status = 'Scheduled' ORDER BY appoints.appointment_date, appoints.appointment_time" % _id
        if person == self.gen.doctor:
            query = "SELECT COUNT(user_id) FROM appoints WHERE doctor_id = %d AND appointment_status = 'Scheduled' AND appointment_date IN (SELECT CONVERT(VARCHAR(10), GETDATE(), 120))" % _id
            resp0 = self.execute_query_read_s(query)
            query = "SELECT COUNT(user_id) FROM appoints WHERE doctor_id = %d AND appointment_status = 'Scheduled'" % _id
            resp1 = self.execute_query_read_s(query)
            Label(self.frame_my_app, text="Today's Appointments: " + str(resp0[0]) + "\t\t      Total Appointments: " + str(resp1[0]), height=1, width=60,
                  anchor=W, font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=175, y=125)

            query = "SELECT * FROM appoints JOIN user_table ON appoints.user_id = user_table.user_id JOIN doctor_table ON appoints.doctor_id = doctor_table.doctor_id WHERE doctor_table.doctor_id = %d AND appointment_status = 'Scheduled' ORDER BY appoints.appointment_date, appoints.appointment_time" % _id

        self.gen.buffer_1 = self.execute_query_read_m(query)

        if self.gen.buffer_1 is not None and len(self.gen.buffer_1) > 0:
            for ent in self.gen.buffer_1:
                if person == self.gen.user:
                    self.list_1.insert(END, "Dr." + display(ent[20] + " " + ent[21], str(ent[2]) + " " + str(ent[3]), ""))
                else:
                    self.list_1.insert(END, display(ent[8] + " " + ent[9], str(ent[2]) + " " + str(ent[3]), ""))

            self.list_1.place(x=175, y=220)
        else:
            Label(self.frame_my_app, text="No Upcoming Appointments!", height=2, width=25,
                  font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=400)

    def launch_my_appointment_1(self, _type):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_show_app = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_show_app.pack()
        self.curr_frame = self.frame_show_app

        person, _id = self.gen.buffer_2[0], self.gen.buffer_2[1]
        info = self.gen.buffer_1[self.list_1.curselection()[0]]

        cli_add = info[13] + " " + info[14] + " " + info[15] + " " + str(info[16])
        dest_add = info[25] + " " + info[26] + " " + info[27] + " " + str(info[28])
        t = get_distance(cli_add, dest_add)

        # Interactions
        Label(self.frame_show_app, text="Appointment Details", height=2, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=500, y=25)

        if person == self.gen.user:
            Label(self.frame_show_app, text="NAME\t\tDr. " + info[20] + " " + info[21], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=175)
            Label(self.frame_show_app, text="SPECIALIZATION\t" + info[30], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=215)
            Label(self.frame_show_app, text="ADDRESS\t\t%s %s" % (info[25], info[26]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400,
                                                                                                                 y=260)
            Label(self.frame_show_app, text="%s %s (Dist: %s, Time: %s)" % (info[27], info[28], t[0], t[1]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=640,
                                                                                                                 y=295)
            Label(self.frame_show_app, text="PHONE NUMBER\t" + str(info[29]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=340)
            Label(self.frame_show_app, text="E-MAIL\t\t" + info[19], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=390)
            Label(self.frame_show_app, text="GENDER\t\t" + info[22], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=430)
            Label(self.frame_show_app, text="DATE / TIME\t" + str(info[2]) + " " + str(info[3]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=470)

        else:
            Label(self.frame_show_app, text="NAME\t\t" + info[8] + " " + info[9], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=175)
            Label(self.frame_show_app, text="PHONE NUMBER\t" + str(info[17]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=225)
            Label(self.frame_show_app, text="E-MAIL\t\t" + info[7], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=275)
            Label(self.frame_show_app, text="GENDER\t\t" + info[10], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=325)
            Label(self.frame_show_app, text="DATE / TIME\t" + str(info[2]) + " " + str(info[3]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=375)
            Label(self.frame_show_app, text="FEE CHARGED", height=1, width=15,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=300, y=510)
            Label(self.frame_show_app, text="₹", height=1, width=4,
                  font=self.fnt.consolas, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=500, y=500)
            Label(self.frame_show_app, text="Appointment Done?", height=1, width=25, anchor=W,
                  font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=300, y=470)

            self.entry_1 = Entry(self.frame_show_app, width=15, font=self.fnt.tahoma, bg="#819EA6", fg="#000000")
            self.entry_1.place(x=540, y=510)

            Button(self.frame_show_app, height=1, width=12, text="DONE", font=self.fnt.tahoma_bold,
                   bg="#05161D", fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
                   command=lambda: self.terminal_my_appointment(person, _id, info, 0)).place(x=835, y=500)

        Button(self.frame_show_app, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)
        Button(self.frame_show_app, height=1, width=20, text="BACK", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_my_appointments(person, _id)).place(x=300, y=600)
        Button(self.frame_show_app, height=1, width=20, text="CANCEL APPOINTMENT", font=self.fnt.tahoma_bold,
               bg="#05161D", fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.terminal_my_appointment(person, _id, info, 1)).place(x=700, y=600)

    def launch_appointment_history(self, person, _id):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_history = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_history.pack()
        self.curr_frame = self.frame_history

        self.gen.buffer_2 = [person, _id]

        # Creating interactions
        Label(self.frame_history, text="Your Previous Appointments", height=2, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=25)
        Label(self.frame_history, text="Name", height=1, width=23,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=175, y=145)
        Label(self.frame_history, text="Date / Time", height=1, width=22,
              font=self.fnt.consolas, bg="#819EA6", fg="#05161D").place(x=697, y=145)

        Button(self.frame_history, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)

        self.list_1 = Listbox(self.frame_history, font=self.fnt.consolas, height=10, width=48, cursor="hand2",
                              selectmode=SINGLE, borderwidth=0, highlightthickness=0, bg="#05161D", fg="#3AD5D9",
                              exportselection=0)
        self.list_1.bind('<<ListboxSelect>>', self.launch_appointment_history_1)

        query = "SELECT * FROM appoints JOIN user_table ON appoints.user_id = user_table.user_id JOIN doctor_table ON appoints.doctor_id = doctor_table.doctor_id WHERE user_table.user_id = %d AND appointment_status = 'Complete' ORDER BY appoints.appointment_date, appoints.appointment_time" % _id
        if person == self.gen.doctor:
            query = "SELECT * FROM appoints JOIN user_table ON appoints.user_id = user_table.user_id JOIN doctor_table ON appoints.doctor_id = doctor_table.doctor_id WHERE doctor_table.doctor_id = %d AND appointment_status = 'Complete' ORDER BY appoints.appointment_date, appoints.appointment_time" % _id

        self.gen.buffer_1 = self.execute_query_read_m(query)

        if self.gen.buffer_1 is not None and len(self.gen.buffer_1) > 0:
            for ent in self.gen.buffer_1:
                if person == self.gen.user:
                    self.list_1.insert(END, "Dr." + display(ent[20] + " " + ent[21], str(ent[2]) + " " + str(ent[3]), ""))
                else:
                    self.list_1.insert(END, display(ent[8] + " " + ent[9], str(ent[2]) + " " + str(ent[3]), ""))

            self.list_1.place(x=175, y=200)
        else:
            Label(self.frame_history, text="No Previous Appointments!", height=2, width=25,
                  font=self.fnt.tahoma, bg="#05161D", fg="#3AD5D9").place(x=500, y=400)

    def launch_appointment_history_1(self, _type):
        # Unpacking previous frame
        self.curr_frame.pack_forget()

        # Packing home page frame
        self.frame_show_his = Frame(self.root, bg="#05161D", height=768, width=1366)
        self.frame_show_his.pack()
        self.curr_frame = self.frame_show_his

        person, _id = self.gen.buffer_2[0], self.gen.buffer_2[1]
        info = self.gen.buffer_1[self.list_1.curselection()[0]]

        # Interactions
        Label(self.frame_show_his, text="Appointment Details", height=2, width=25,
              font=self.fnt.tahoma, bg="#05161D", fg="#819EA6").place(x=500, y=25)
        Label(self.frame_show_his, text="DATE / TIME\t" + str(info[2]) + " " + str(info[3]), height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=440)
        Label(self.frame_show_his, text="FEE CHARGED\t₹" + str(info[4]), height=1, width=55,
              font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=490)
        if person == self.gen.user:
            Label(self.frame_show_his, text="NAME\t\tDr. " + info[20] + " " + info[21], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=125)
            Label(self.frame_show_his, text="SPECIALIZATION\t" + info[30], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=165)
            Label(self.frame_show_his, text="ADDRESS\t\t%s %s" % (info[25], info[26]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400,
                                                                                                                 y=210)
            Label(self.frame_show_his, text="%s %s" % (info[27], info[28]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=640,
                                                                                                                 y=245)
            Label(self.frame_show_his, text="PHONE NUMBER\t" + str(info[29]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=290)
            Label(self.frame_show_his, text="E-MAIL\t\t" + info[19], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=340)
            Label(self.frame_show_his, text="GENDER\t\t" + info[22], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=390)
        else:
            Label(self.frame_show_his, text="NAME\t\t" + info[8] + " " + info[9], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=165)
            Label(self.frame_show_his, text="ADDRESS\t\t%s %s" % (info[13], info[14]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400,
                                                                                                                 y=210)
            Label(self.frame_show_his, text="%s %s" % (info[15], info[16]),
                  height=1, width=70, font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=640,
                                                                                                                 y=245)
            Label(self.frame_show_his, text="PHONE NUMBER\t" + str(info[17]), height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=290)
            Label(self.frame_show_his, text="E-MAIL\t\t" + info[7], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=340)
            Label(self.frame_show_his, text="GENDER\t\t" + info[10], height=1, width=55,
                  font=self.fnt.consolas_medium, anchor=W, bg="#05161D", fg="#3AD5D9").place(x=400, y=390)

        Button(self.frame_show_his, height=77, width=195, image=self.imag.sq_logo,
               cursor='hand2', borderwidth=0, highlightthickness=0,
               command=lambda: self.launch_dashboard(person, _id)).place(x=26, y=26)
        Button(self.frame_show_his, height=1, width=20, text="BACK", font=self.fnt.tahoma_bold, bg="#05161D",
               fg="#819EA6", activebackground="#819EA6", activeforeground="#05161D", cursor='hand2',
               command=lambda: self.launch_appointment_history(person, _id)).place(x=500, y=600)

    def bridge_log_dash(self):
        # Reset Error
        self.err_1, self.err_2, self.err_3 = False, False, False

        # Collecting data
        self.gen.email = self.entry_1.get()
        password = self.entry_2.get()

        # self.launch_dashboard(self.gen.user, 18)
        # Querying DB
        query = "SELECT password FROM user_login_credentials WHERE email_id = '%s'" % self.gen.email
        resp1 = self.execute_query_read_s(query)
        query = "SELECT password FROM doctor_login_credentials WHERE email_id = '%s'" % self.gen.email
        resp2 = self.execute_query_read_s(query)
        person = None

        if resp1 is not None:
            person = self.gen.user
        elif resp2 is not None:
            person = self.gen.doctor
            resp1 = resp2

        if person is not None:
            if password == resp1[0]:
                query = "SELECT %s_id FROM %s_table WHERE email_id = '%s'" % (person, person, self.gen.email)
                resp = self.execute_query_read_s(query)
                self.launch_dashboard(person, resp[0])
            else:
                self.err_2 = True
                self.launch_log_in(self.gen.elevated)

        else:
            self.err_1 = True
            self.launch_log_in(self.gen.default)

    def bridge_s1_myinfo(self, person):
        # Reset Error
        self.err_1, self.err_2, self.err_3, self.err_4 = False, False, False, False

        # Collect data
        self.gen.email = self.entry_1.get()
        self.gen.password = self.entry_2.get()
        conf_pass = self.entry_3.get()

        # Checking and inserting in DB
        if self.gen.password == conf_pass:
            query = "INSERT INTO %s_login_credentials VALUES ('%s', '%s')" % (person, self.gen.email, self.gen.password)
            resp = self.execute_query_write(query)
            if resp is True:
                self.launch_my_info_0(person, self.gen.default, 0)
            else:
                if resp == "dlc_email" or resp == "ulc_email":
                    self.err_1 = True
                    self.launch_sign_in_1(person, self.gen.default)
                elif resp == "dlc_password" or resp == "ulc_password":
                    self.err_3 = True
                    self.entry_1.insert(0, self.gen.email)
                    self.launch_sign_in_1(person, self.gen.elevated)
                elif resp == "dlc_pk" or resp == "ulc_pk":
                    self.err_4 = True
                    self.launch_sign_in_1(person, self.gen.default)
                else:
                    self.launch_sign_in_1(person, self.gen.default)

        else:
            self.err_2 = True
            self.launch_sign_in_1(person, self.gen.elevated)

    def bridge_myinfo_dash(self, person):
        # Reset Error
        self.err_1, self.err_2, self.err_3, self.err_4 = False, False, False, False

        # Collect data
        self.gen.f_name = self.entry_1.get()
        self.gen.l_name = self.entry_2.get()
        self.gen.building = self.entry_3.get()
        self.gen.locality = self.entry_4.get()
        self.gen.city = self.entry_5.get()
        self.gen.pin = int(self.entry_6.get())
        self.gen.date = str(self.var_char_6.get()) + "-" + str(self.gen.month[str(self.var_char_5.get())]) + "-" + str(self.var_char_4.get())
        self.gen.phone = int(self.entry_7.get())
        self.gen.gender = self.var_char_1.get()

        # Validate / Insert in DB
        if person == self.gen.user:
            query = "INSERT INTO user_table VALUES ('%s', '%s', '%s', '%s', '%s', datediff(year, '%s', getdate()), '%s', '%s', '%s', %i, %i)" % (self.gen.email, self.gen.f_name, self.gen.l_name, self.gen.gender, self.gen.date, self.gen.date, self.gen.building, self.gen.locality, self.gen.city, self.gen.pin, self.gen.phone)
            resp = self.execute_query_write(query)
            if resp is True:
                query = "SELECT user_id FROM user_table WHERE email_id = '%s'" % self.gen.email
                res = self.execute_query_read_s(query)
                if res is not None:
                    sys_id = res[0]
                    self.launch_dashboard(person, sys_id)
                    self.gen.date = "SELECT"
                else:  # CRASH
                    self.launch_load()

            else:
                self.launch_my_info_0(person, self.gen.default, 0)

        else:
            self.gen.minor = self.var_char_2.get()
            self.gen.special = self.var_char_3.get()
            self.gen.fee = int(self.entry_8.get())

            query = "INSERT INTO doctor_table VALUES ('%s', '%s', '%s', '%s', '%s', datediff(year, '%s', getdate()), '%s', '%s', '%s', %i, %i, '%s', %i, '%s')" % (
                     self.gen.email, self.gen.f_name, self.gen.l_name, self.gen.gender, self.gen.date, self.gen.date,
                     self.gen.building, self.gen.locality, self.gen.city, self.gen.pin, self.gen.phone, self.gen.special,
                     self.gen.fee, self.gen.minor)

            resp = self.execute_query_write(query)
            if resp is True:
                query = "SELECT doctor_id FROM doctor_table WHERE email_id = '%s'" % self.gen.email
                res = self.execute_query_read_s(query)
                if res is not False:
                    sys_id = res[0]
                    self.launch_dashboard(person, sys_id)
                    self.gen.date = "SELECT"

            else:
                self.launch_my_info_0(person, self.gen.default, 0)

    def bridge_change_details(self, person, _id):
        # extract information...
        query = "SELECT * FROM %s_table WHERE %s_id = %i" % (person, person, _id)
        res = self.execute_query_read_s(query)
        if res is None:
            self.launch_dashboard(person, _id)

        temp = str(res[5]).split("-")
        self.gen.f_name = res[2]
        self.gen.l_name = res[3]
        self.gen.gender = res[4]
        self.gen.date = [temp[2], self.gen.month_rev[int(temp[1])], temp[0]]
        self.gen.building = res[7]
        self.gen.locality = res[8]
        self.gen.city = res[9]
        self.gen.pin = int(res[10])
        self.gen.phone = int(res[11])
        if person == self.gen.doctor:
            self.gen.special = res[12]
            self.gen.fee = res[13]
            self.gen.minor = res[14]

        self.launch_my_info_0(person, self.gen.elevated, _id)

    def bridge_schedule_schedule(self, _id):
        # Cook query simultaneously
        temp1, temp2, temp3, temp4, temp5 = "first_name", None, None, None, None

        if self.var_char_1.get() not in ("Sort by", "Name", "Distance"):
            temp1 = self.var_char_1.get()

        if self.var_char_2.get() not in ("Any", "Specialization"):
            temp2 = self.var_char_2.get()

        if self.var_char_3.get() not in ("Any", "Filter by"):
            temp3 = self.var_char_3.get()

        if self.entry_1.get() not in ("First Name (optional)", ):
            temp4 = self.entry_1.get()

        if self.entry_2.get() not in ("Last Name (optional)", ):
            temp5 = self.entry_2.get()

        query = "SELECT * FROM doctor_table "
        if temp2 is not None or temp3 is not None or temp4 is not None or temp5 is not None:
            query += "WHERE "
        if temp2 is not None:
            query += "specialization LIKE '%s' " % temp2
        if temp3 is not None:
            if temp2 is not None:
                query += "AND "
            query += "pincode BETWEEN (SELECT pincode FROM user_table WHERE user_id = %d) - 20 AND (SELECT pincode FROM user_table WHERE user_id = %d) + 20 " % (_id, _id)
        if temp4 is not None:
            if temp3 is not None or temp2 is not None:
                query += "AND "
            query += "first_name LIKE '%s' " % temp4
        if temp5 is not None:
            if temp4 is not None or temp3 is not None or temp2 is not None:
                query += "AND "
            query += "last_name LIKE '%s' " % temp5
        query += "ORDER BY %s" % temp1.lower()

        self.gen.buffer_1 = self.execute_query_read_m(query)

        self.launch_schedule_appointment(self.gen.user, self.gen.elevated, _id, True)

    def bridge_upd_myinfo_dash(self, person, _id):
        # Collect data
        self.gen.f_name = self.entry_1.get()
        self.gen.l_name = self.entry_2.get()
        self.gen.building = self.entry_3.get()
        self.gen.locality = self.entry_4.get()
        self.gen.city = self.entry_5.get()
        self.gen.pin = int(self.entry_6.get())
        self.gen.date = str(self.var_char_6.get()) + "-" + str(self.gen.month[str(self.var_char_5.get())]) + "-" + str(self.var_char_4.get())
        self.gen.phone = int(self.entry_7.get())
        self.gen.gender = self.var_char_1.get()

        # Default user query
        query = "UPDATE %s_table SET first_name = '%s', last_name = '%s', gender = '%s', dob = '%s', building = '%s', locality = '%s', city = '%s', pincode = %d, phone = %d WHERE %s_id = %d" % (
            person, self.gen.f_name, self.gen.l_name, self.gen.gender, self.gen.date, self.gen.building,
            self.gen.locality,
            self.gen.city, self.gen.pin, self.gen.phone, person, _id)

        if person == self.gen.doctor:
            # Additional data
            self.gen.minor = self.var_char_2.get()
            self.gen.special = self.var_char_3.get()
            self.gen.fee = int(self.entry_8.get())

            query = "UPDATE %s_table SET first_name = '%s', last_name = '%s', gender = '%s', dob = '%s', building = '%s', locality = '%s', city = '%s', pincode = %d, phone = %d, specialization = '%s', fee = %d, minor_allowance = '%s' WHERE %s_id = %d" % (
                     person, self.gen.f_name, self.gen.l_name, self.gen.gender, self.gen.date, self.gen.building,
                     self.gen.locality, self.gen.city, self.gen.pin, self.gen.phone, self.gen.special, self.gen.fee,
                     self.gen.minor, person, _id)

        self.execute_query_write(query)
        self.launch_dashboard(person, _id)

    def terminal_schedule_appointment(self, _id, doc):
        _date = str(self.var_char_8.get()) + "-" + str(self.gen.month[str(self.var_char_7.get())]) + "-" + str(self.var_char_6.get())
        time = str(self.var_char_4.get()) + ":" + str(self.var_char_5.get()) + ":00"
        query = "INSERT INTO appoints VALUES (%d, %d, '%s', '%s', 0, 'Scheduled')" % (_id, doc[0], _date, time)
        resp = self.execute_query_write(query)
        if resp is True:
            self.launch_dashboard(self.gen.user, _id)

        else:
            self.launch_schedule_appointment_1(self.gen.elevated)

    def terminal_my_appointment(self, person, _id, info, op):
        query = ""
        if op == 0:
            query = "UPDATE appoints SET appointment_status = 'Complete', fee_charged = %d WHERE user_id = %d AND doctor_id = %d AND appointment_date = '%s' AND appointment_time = '%s'" % (int(self.entry_1.get()), info[0], info[1], str(info[2]), str(info[3]))
        elif op == 1:
            query = "UPDATE appoints SET appointment_status = 'Cancelled' WHERE user_id = %d AND doctor_id = %d AND appointment_date = '%s' AND appointment_time = '%s'" % (info[0], info[1], str(info[2]), str(info[3]))
        resp = self.execute_query_write(query)
        if resp is True:
            self.launch_dashboard(person, _id)
        else:
            self.launch_my_appointment_1(0)

    def execute_query_write(self, query):
        try:
            self.cursor.execute(query)
            self.cursor.execute("COMMIT")
            return True

        except Exception as e:
            return get_error(str(e))

    def execute_query_read_s(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()

        except:
            return None

    def execute_query_read_m(self, query):
        try:
            self.cursor.execute(query)
            return list(self.cursor.fetchall())

        except:
            return None


def main():
    # Initialising window essentials
    root_win = Tk()
    root_win.title("Medicrew")
    root_win.geometry("1366x768+0+0")
    root_win.wm_iconbitmap("./Images/icon.ico")

    # Creating Object
    use = Interface(root_win)
    use.launch_load()
    
    # Running mainloop
    root_win.mainloop()


if __name__ == "__main__":
    main()
