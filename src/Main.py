from tkinter import *
import time

melumatlar = ("sahin", "1")
sinamahakki = 4
zaman = 0


def girisFunction():
    global sinamahakki, zaman
    if sinamahakki <= 0:
        if time.time() - zaman >= 5:
            sinamahakki = 4
        else:
            netice.config(text="wait 5 second please..")
            return False

    Name = ad.get()
    parol = sifre.get()
    print (Name, " - ", parol)
    print ("Controlling...")
    if Name == melumatlar[0] and parol == melumatlar[1]:
        print ("Credentials is correct..")
        netice.config(text="Successfully logged in..")
        ekranitemizle()
    else:
        print ("Wrong Credentials..")
        sinamahakki -= 1
        if sinamahakki == 0:
            zaman = time.time()
        netice.config(text="Wrong Credentials.. Left: %d" % sinamahakki)


def ekranitemizle():
    qarsilama.config(text="Sahin Welcome")
    username.destroy()
    ad.destroy()
    password.destroy()
    sifre.destroy()
    buton.destroy()


pencere = Tk()
pencere.title("Sahin's window")
pencere.geometry("400x400+200+150")

qarsilama = Label(pencere)
qarsilama.config(text="Welcome to my window :)")
qarsilama.pack()

username = Label(pencere)
username.config(text="User name: ")
username.pack()

ad = Entry(pencere)
ad.pack()

password = Label(pencere)
password.config(text="Password: ")
password.pack()

sifre = Entry(pencere)
sifre.pack()

buton = Button(pencere)
buton.config(text="Log in!", command=girisFunction)
buton.pack()

netice = Label(pencere)
netice.config(text="No logged in yet..")
netice.pack()

mainloop()



