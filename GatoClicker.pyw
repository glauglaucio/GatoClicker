import tkinter as tk
from tkinter import *
import os


#Gatos
gatos = 0
AmantGatos = 1
catloverValor = 100

def cats():
    if gatos >= 8000000000:
        root.destroy()
    else:
        label1.config(text=f"{gatos:,}\nGatos")

    botao2.config(text=f'Amante de Gatos\nCusto: {catloverValor:,}\nGanhe 2x mais gatos por clique.')
    if gatos >= catloverValor:
        botao2.config(state=NORMAL)

def catclick():
    global gatos
    gatos += AmantGatos
    cats()

def catlover():
    global AmantGatos
    global catloverValor
    global gatos

    AmantGatos *= 2
    gatos -= catloverValor
    catloverValor = int(100*(AmantGatos)**1.5)
    botao2.config(state=DISABLED)
    cats()


#Prelúdio
pastaAtual = os.path.dirname(__file__)

root = tk.Tk()
root.title("GatoClicker")
root.iconbitmap(f"{pastaAtual}\image\png.ico")
root.configure(background="black")
root.columnconfigure(0, weight=10)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

gatoimage = PhotoImage(file=f"{pastaAtual}\image\gato1.png")


#ScreenSize
clickerw = 1000
clickerh = 800

sw = (root.winfo_screenwidth())
sh = (root.winfo_screenheight())

x = int((sw-clickerw)/2)
y = int((sh-clickerh)/2)

root.geometry(f"{clickerw}x{clickerh}+{x}+{y}")
root.maxsize(clickerw, clickerh)
root.resizable(False,True)


#HUD
label2 = tk.Label(
    root,bg="red",fg="black",border=50,
    font=(None,20),text="CLIQUE NO GATO"
)
label2.grid(column=1,row=0,sticky=tk.N,columnspan=1)

label3 = tk.Label(
    root,bg="red",fg="black",border=50,
    font=(None,20),text="Tempo:"
)
label3.grid(column=0,row=0,sticky=tk.N)

label4 = tk.Label(
    root,bg="red",fg="black",border=50,width=22,
    font=(None,20),text="COMPRE UPGRADES"
)
label4.grid(column=2,row=0,sticky=tk.N)

label1 = tk.Label(
    root,fg="red",bg="black",
    font=(None,20),text=f"{gatos}\nGatos"
)
label1.grid(column=0, row=1, sticky=tk.N, padx=10, pady=100)

botao1 = tk.Button(
    root,background="black",foreground="black", activebackground="black",
    image=gatoimage,
    command=catclick,
    borderwidth=0
)
botao1.grid(column=1, row=1, sticky=tk.W,padx=100)

botao2 = tk.Button(
    root, text=f'Amante de Gatos\nCusto: {catloverValor}\nGanhe 2x mais gatos por clique.',
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catlover,
    state=DISABLED
)
botao2.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)


root.mainloop()