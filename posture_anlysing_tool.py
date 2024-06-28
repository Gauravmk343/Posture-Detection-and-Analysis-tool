from audioop import lin2alaw
from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import random
from tkinter.ttk import *
import datetime
import time
import os


def filecreate():
    t = open("C:/Users/user/OneDrive/Desktop/DIY Project/data/dateandtime.txt", "a")
    t.write("\n" + datetime)
    t.close()
    lenth1 = len(options)
    for x in range(1, lenth1):
        options[x] = options[x].replace(":", "-")
        f = open(
            "C:/Users/user/OneDrive/Desktop/DIY Project/data/Data11/"
            + options[x]
            + ".txt",
            "a",
        )
        f.close()
    root.destroy()
    os.startfile("C:/Users/user/OneDrive/Desktop/DIY Project/posture_anylysing_tool.py")


def filedelete():
    with open(
        "C:/Users/user/OneDrive/Desktop/DIY Project/data/dateandtime.txt", "r"
    ) as f:
        lines = f.readlines()
    with open(
        "C:/Users/user/OneDrive/Desktop/DIY Project/data/dateandtime.txt", "w"
    ) as f:
        for line in lines:
            if line.strip("\n") != clicked.get():
                f.write(line)
    root.destroy()
    os.startfile("C:/Users/user/OneDrive/Desktop/DIY Project/posture_anylysing_tool.py")


def Convertint(string):
    li = list(string.split(","))
    li = li[0 : len(li) - 1]
    for num in range(len(li)):
        li[num] = int(li[num])
    li = np.array(li)
    return li


def update():
    x = datetime.datetime.now().time()
    mylbe.config(text=x)


def clock():
    hour = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    mylbe.config(text=hour + ":" + min + ":" + sec)
    mylbe.after(1000, clock)


# --------------------------------
root = Tk()
root.title(" Posture Anlysing Tool")
root.iconbitmap("C:/Users/user/OneDrive/Desktop/DIY Project/data/icondiy.ico")
root.geometry("650x300")
# root.configure(background="green")
# --------------------------------
def show():
    label.config(text=clicked.get())


# Dropdown menu options
t = open(
    "C:/Users/user/OneDrive/Desktop/DIY Project/data/dateandtime.txt", "rt"
)  # print(t.readline())
lst = []
for x in t:
    lst.append(x[0 : len(x) - 1])
t.close()
options = []
for a in range(0, len(lst)):
    options.append(lst[len(lst) - a - 1])
# options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# datatype of menu text
clicked = StringVar()
# initial menu text
tim = datetime.datetime.now().strftime("%H:%M:%S")
clicked.set(tim)
# Create Dropdown menu
Label(root, text="Choose your date and time", font=("Comic Sans MS", 12)).place(
    relx=0.2, rely=0.23
)
drop = OptionMenu(root, clicked, *options)
drop.place(relx=0.4, rely=0.235, width=200)
# Create button, it will change label text
buttn = Button(root, text="confirm", command=show).place(relx=0.4, rely=0.34)
# Create Label
label = Label(root, text=" ")
label.place(relx=0.4, rely=0.42)
# ---------------------------------
date = datetime.date.today()
x = str(date.year)
y = str(date.month)
z = str(date.day)
Label(root, text=z + "-" + y + "-" + x, font=("Comic Sans MS", 14)).place(
    relx=0.78, rely=0.02
)

mylbe = Label(root, text=tim, font=("Comic Sans MS", 14))
mylbe.place(relx=0.19, rely=0.02)
clock()
Label(root, text="current time:", font=("Comic Sans MS", 14)).place(
    relx=0.007, rely=0.02
)
Label(root, text="today date:", font=("Comic Sans MS", 14)).place(relx=0.6, rely=0.02)
Label(root, text=tim, font=("Comic Sans MS", 14)).place(relx=0.5, rely=0.12)
Label(root, text="Started at :", font=("Comic Sans MS", 14)).place(relx=0.3, rely=0.12)
datetime = z + "-" + y + "-" + x + " at " + str(tim)

Button(root, text="add data", command=filecreate).place(relx=0.45, rely=0.68)
Button(root, text="delete data", command=filedelete).place(relx=0.75, rely=0.68)


def rootdes():
    import datetime
    import matplotlib.pyplot as plt
    import numpy as np

    root.destroy()

    def restart():
        root1.destroy()
        os.startfile(
            "C:/Users/user/OneDrive/Desktop/DIY Project/posture_anylysing_tool.py"
        )

    def clock():
        hour = time.strftime("%H")
        min = time.strftime("%M")
        sec = time.strftime("%S")
        mylbe.config(text=hour + ":" + min + ":" + sec)
        mylbe.after(1000, clock)

    def intotime(x):
        lst = []
        for a in range(x):
            lst.append(time.strftime("%H:%M:%S", time.gmtime(a)))
        return lst

    x = "18-2-2022 at 12-15-31"
    t = clicked.get()
    t = t.replace(":", "-")
    fil = open("C:/Users/user/OneDrive/Desktop/DIY Project/data/data11/" + t + ".txt")
    l1 = fil.readlines()
    fil.close()

    def graph1():
        btn1.config(state=DISABLED)
        btn6.config(state=DISABLED)
        yaxis = Convertint(l1[0])
        x = np.array(intotime(len(yaxis)))
        print(x)
        print(yaxis)
        plt.plot(x, yaxis, marker="o")
        plt.plot(x, (yaxis * 0) + 787, linestyle="--")
        plt.show()
        btn6.config(state="normal")
        btn1.config(state="normal")

    def graph2():
        btn1.config(state=DISABLED)
        btn6.config(state=DISABLED)
        yaxis = Convertint(l1[1])
        x = np.array(intotime(len(yaxis)))
        print(x)
        print(yaxis)
        plt.plot(x, yaxis, marker="o")
        plt.plot(x, (yaxis * 0) + 782, linestyle="--")
        plt.show()
        btn6.config(state="normal")
        btn1.config(state="normal")

    def graph3():
        btn1.config(state=DISABLED)
        btn6.config(state=DISABLED)
        yaxis = Convertint(l1[2])
        x = np.array(intotime(len(yaxis)))
        print(x)
        print(yaxis)
        plt.plot(x, yaxis, marker="o")
        plt.plot(x, (yaxis * 0) + 785, linestyle="--")
        plt.show()
        btn6.config(state="normal")
        btn1.config(state="normal")

    def graph4():
        btn1.config(state=DISABLED)
        btn6.config(state=DISABLED)
        y1 = Convertint(l1[0])
        y2 = Convertint(l1[1])
        y3 = Convertint(l1[2])
        yaxis = []
        for x in range(0, len(y1)):
            num = (((y1[x] ** 2) + (y2[x] ** 2) + (y3[x] ** 2)) / 3) ** 0.5
            yaxis.append(num)
        x = np.array(intotime(len(yaxis)))
        print(x)
        print(yaxis)
        plt.plot(x, yaxis, marker="o")
        plt.show()
        btn6.config(state="normal")
        btn1.config(state="normal")

    def allfourgraph():
        btn1.config(state=DISABLED)
        btn2.config(state=DISABLED)
        btn3.config(state=DISABLED)
        btn4.config(state=DISABLED)
        btn5.config(state=DISABLED)
        btn6.config(state=DISABLED)
        y1 = Convertint(l1[0])
        y2 = Convertint(l1[1])
        y3 = Convertint(l1[2])
        yaxis = []
        for x in range(0, len(y1)):
            num = (((y1[x] ** 2) + (y2[x] ** 2) + (y3[x] ** 2)) / 3) ** 0.5
            yaxis.append(num)
        x = np.array(intotime(len(yaxis)))
        fig, axes = plt.subplots(2, 2)
        axes[0, 0].plot(x, y1)
        axes[0, 0].set_title("sensor1")
        axes[0, 0].xaxis.set_visible(False)
        axes[0, 1].plot(x, y2)
        axes[0, 1].set_title("sensor2")
        axes[0, 1].xaxis.set_visible(False)
        axes[1, 0].plot(x, y3)
        axes[1, 0].set_title("sensor3")
        axes[1, 0].xaxis.set_visible(False)
        axes[1, 1].plot(x, yaxis)
        axes[1, 1].set_title("RMS value")
        plt.xticks([])
        plt.show()

        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn1.config(state="normal")

    def piegraph():
        btn2.config(state=DISABLED)
        btn3.config(state=DISABLED)
        btn4.config(state=DISABLED)
        btn5.config(state=DISABLED)
        btn6.config(state=DISABLED)
        btn1.config(state=DISABLED)
        y = Convertint(l1[3])
        mylabels = ["good", "2 good", "3 good", "4 good"]
        plt.pie(y, labels=mylabels)
        plt.show()
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")

    root1 = Tk()
    root1.title(" Posture Anlysing Tool")
    root1.iconbitmap("C:/Users/user/OneDrive/Desktop/DIY Project/data/icondiy.ico")
    root1.geometry("600x500")
    # --------------------------------------------
    date = datetime.date.today()
    x = str(date.year)
    y = str(date.month)
    z = str(date.day)
    Label(root1, text=z + "-" + y + "-" + x, font=("Comic Sans MS", 14)).place(
        relx=0.57, rely=0.12
    )

    mylbe = Label(root1, text=tim, font=("Comic Sans MS", 14))
    mylbe.place(relx=0.28, rely=0.02)
    clock()
    Label(root1, text="current time:", font=("Comic Sans MS", 14)).place(
        relx=0.01, rely=0.02
    )
    Label(root1, text="today date:", font=("Comic Sans MS", 14)).place(
        relx=0.35, rely=0.12
    )
    Label(root1, text=tim, font=("Comic Sans MS", 14)).place(relx=0.8, rely=0.02)
    Label(root1, text="login at :", font=("Comic Sans MS", 14)).place(
        relx=0.63, rely=0.02
    )

    # ------------------------------------------------------
    Label(
        root1,
        text="Click down below to see you record in pie chart form",
        font=("Comic Sans MS", 17),
    ).place(relx=0.004, rely=0.25)
    btn1 = Button(root1, text=" PIE CHART", state="enable", command=piegraph)
    btn1.place(relx=0.43, rely=0.32)
    # -----------------------------------
    Label(
        root1,
        text="Click down below to see you record in graph form",
        font=("Comic Sans MS", 17),
    ).place(relx=0.004, rely=0.38)
    Label(root1, text="sensor1 reading", font=("Comic Sans MS", 14)).place(
        relx=0.1, rely=0.45
    )
    Label(root1, text="sensor2 reading", font=("Comic Sans MS", 14)).place(
        relx=0.1, rely=0.55
    )
    Label(root1, text="sensor3 reading", font=("Comic Sans MS", 14)).place(
        relx=0.5, rely=0.45
    )
    Label(root1, text="average reading", font=("Comic Sans MS", 14)).place(
        relx=0.5, rely=0.55
    )
    btn2 = Button(root1, text=" sensor1", command=graph1)
    btn2.place(relx=0.13, rely=0.5)
    btn3 = Button(root1, text=" sensor2", command=graph2)
    btn3.place(relx=0.13, rely=0.61)
    btn4 = Button(root1, text=" sensor3", command=graph3)
    btn4.place(relx=0.53, rely=0.5)
    btn5 = Button(root1, text=" average", command=graph4)
    btn5.place(relx=0.53, rely=0.61)
    # -----------------------------
    Label(
        root1,
        text="Click down below to see you record in graph form",
        font=("Comic Sans MS", 17),
    ).place(relx=0.004, rely=0.71)
    btn6 = Button(root1, text=" all in one", command=allfourgraph)
    btn6.place(relx=0.5, rely=0.8)

    Button(root1, text="Restart", command=restart).place(relx=0.5, rely=0.9)
    root1.mainloop()


Button(root, text="click here to see your record", command=rootdes).place(
    relx=0.4, rely=0.8
)
root.mainloop()
t = clicked.get()
t = t.replace(":", "-")
print(t)
root.mainloop()
"""
print(tim)
print(t1)
x = t1[0:2]
print(x)
print(options)
"""
