from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("ejemplo de place")
vent.geometry("400x200")

def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r)

#valores relativos

lbl1 = Label(vent,text="Primer número", bg="yellow")
lbl1.place(relx=0.03,rely=0.04,relwidth=0.23,relheight=0.1)
txt1 = Entry(vent, bg="pink")
txt1.place(relx=0.3,rely=0.04,relwidth=0.22,relheight=0.1)

lbl2 = Label(vent,text="Segundo número", bg="yellow")
lbl2.place(relx=0.03,rely=0.17,relwidth=0.23,relheight=0.1)
txt2 = Entry(vent, bg="pink")
txt2.place(relx=0.3,rely=0.17,relwidth=0.22,relheight=0.1)
btn1=Button(vent,text="Sumar", command=fnSuma)
btn1.place(relx=0.55, rely=0.17, relwidth=0.20, relheig=0.1)

lbl3 = Label(vent,text="Resultado", bg="yellow")
lbl3.place(relx=0.03,rely=0.35,relwidth=0.23,relheight=0.1)
txt3 = Entry(vent, bg="pink")
txt3.place(relx=0.3,rely=0.35,relwidth=0.22,relheigh=0.1)


vent.mainloop()

#Valores absolutos

# vent = Tk()
# vent.title("ejemplo de place")
# vent.geometry("400x200")

# def fnSuma():
#     n1 = txt1.get()
#     n2 = txt2.get()
#     r = float(n1) + float(n2)
#     txt3.delete(0,'end')
#     txt3.insert(0,r)

# lbl1 = Label(vent,text="Primer número", bg="yellow")
# lbl1.place(x=10,y=10,width=100,height=30)
# txt1 = Entry(vent, bg="pink")
# txt1.place(x=120,y=10,width=100,height=30)

# lbl2 = Label(vent,text="Segundo número", bg="yellow")
# lbl2.place(x=10,y=50,width=100,height=30)
# txt2 = Entry(vent, bg="pink")
# txt2.place(x=120,y=50,width=100,height=30)
# btn1=Button(vent,text="Sumar", command=fnSuma)
# btn1.place(x=230, y=50, width=80, height=30)

# lbl3 = Label(vent,text="Resultado", bg="yellow")
# lbl3.place(x=10,y=120,width=100,height=30)
# txt3 = Entry(vent, bg="pink")
# txt3.place(x=120,y=120,width=100,height=30)
