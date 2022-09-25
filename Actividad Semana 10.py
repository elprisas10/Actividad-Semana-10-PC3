#Integrante: Jonathan Elias Gamez Larin
from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox

def Cajero():
    value= float(input1.get())
    text = float(input2.get())
    hold = value * text
    value = int(Rad.get())
    text = "El precio es de: $"

    if value == 1:
      hold1 = hold * 0.2
      fin = hold - hold1
      x = " Tiene un descuento del 20% por pagar con tarjeta"

    elif value == 2:
      fin = hold
      x = " No hay descuento por pagar en efectivo"
    fin_f = str(fin)
    messagebox.showinfo(title="Cantidad para pagar", message=str(text)+fin_f+str(x))


ventana1= Tk()
ventana1.geometry("800x400")

Rad = IntVar()

labl2=Label(ventana1,bg = "light green", text="El Precio de su producto.")
input2=Entry(ventana1)
labl1=Label(ventana1, bg = "light green",text="Cantidades De su producto.")
input1=Entry(ventana1)

rdb1 = Radiobutton(ventana1, bg = "light blue",text="Pagar con tarjeta", value=1, variable=Rad)
rdb2 = Radiobutton(ventana1, bg = "light blue",text="Pagar en efectivo", value=2, variable=Rad)

btn1 = Button(ventana1,text="Calcular",command = Cajero)

labl3=Label(ventana1,bg = "red", text="Escoja como desea pagar:")

ventana1.configure(bg='#55C1FF')
ventana1.title("Cajero De Super Mercado :)")
labl1.pack()
input1.pack()
labl2.pack()
input2.pack()
btn1.pack()
labl3.pack()
rdb1.pack()
rdb2.pack()


ventana1.mainloop()