from tkinter import *

def vvid(numb):
    a = name.get()
    if len(a) != 0:
        if a[0] == '0':
            name.delete(a[0])
    name.insert(END, numb)

print('pislya')
def clear():
    a = name.get()
    d = len(a) - 1
    name.delete(d)

def ochistka():
    f =name.get()
    name.delete(0, len(f))
    name.insert(END,'0')

def knopiks(cifra):
    fff = str(cifra)
    return Button(root, text=fff, padx=15, pady=15, foreground='blue', background='white', activebackground='blue',
                  command=lambda: vvid(cifra))


def dura():
    tt = name.get()
    audi = eval(tt)
    name.delete(0, END)
    name.insert(0, audi)

print("calc")


def pups(opp):
    value = name.get()
    try:
        if value[-1] in '+*/':
            name.delete(len(value) - 1)
            name.insert(END, opp)
        else:
            name.insert(END, opp)
    except IndexError:
        name.insert(0,'помилка')
def close():
   root.quit()

root = Tk()
root.geometry('335x400+500+200')
root.resizable(False, False)
root.title("PELMEN'")
root["bg"] = "gray22"
pic=PhotoImage(file="b.png")
label = Label(image=pic,width=60,height=60)
label.grid(row=5,column=0)
name = Entry(root, justify=RIGHT, font=('ARIAL', 20))
name.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=10, ipady=15, sticky='wens')
name.insert(0, '0')

knopiks(1).grid(sticky='wens', row=1, column=0, padx=5, pady=5)
knopiks(2).grid(sticky='wens', row=1, column=1, padx=5, pady=5)
knopiks(3).grid(sticky='wens', row=1, column=2, padx=5, pady=5)
knopiks(4).grid(sticky='wens', row=2, column=0, padx=5, pady=5)
knopiks(5).grid(sticky='wens', row=2, column=1, padx=5, pady=5)
knopiks(6).grid(sticky='wens', row=2, column=2, padx=5, pady=5)
knopiks(7).grid(sticky='wens', row=3, column=0, padx=5, pady=5)
knopiks(8).grid(sticky='wens', row=3, column=1, padx=5, pady=5)
knopiks(9).grid(sticky='wens', row=3, column=2, padx=5, pady=5)
knopiks(0).grid(sticky='wens', row=4, column=0, padx=5, pady=5)
Button(root, text='cl', padx=10, pady=10, foreground='blue', background='white', activebackground='blue',
       command=clear).grid(sticky='wens', row=4, column=1, padx=5, pady=5)
plus = Button(root, text='+', padx=10, pady=10, foreground='blue', background='white', activebackground='blue',
              command=lambda: pups('+')).grid(sticky='wens', row=1, column=3, padx=5, pady=5)
dill = Button(root, text='/', padx=10, pady=10, foreground='blue', background='white', activebackground='blue',
              command=lambda: pups('/')).grid(sticky='wens', row=3, column=3, padx=5, pady=5)
mnozhenia = Button(root, text='*', padx=10, pady=10, foreground='blue', background='white', activebackground='blue',
                   command=lambda: pups('*')).grid(sticky='wens', row=4, column=3, padx=5, pady=5)
dora = Button(root, text='=', padx=10, pady=10, foreground='blue', background='white', activebackground='blue',
              command=dura).grid(sticky='wens', row=2, column=3, padx=5, pady=5)
cliner = Button(root, text='cl all', padx=5, pady=5, foreground='red', background='white', activebackground='blue',command=ochistka
              ).grid(sticky='wens', row=4, column=2, padx=5, pady=5)
virub = Button(root, text='Вирубить БЕЗДУШНУЮ МАШІНУ\n<---Blackhall кста', padx=5, pady=5, foreground='red', background='black', activebackground='blue',command=close
              ).grid(sticky='wens', row=5, column=1, padx=5, pady=5, columnspan=3)
root.mainloop()
