import tkinter as tk
from tkinter import *
import os


#Gatos
gatos = h = s = m = gsegundo = leite = 0
AmantGatos = qtdbotoes = 1
catloverValor = 50
leiteValor = 100


def cats():
    label1.config(text=f"{gatos:,}\nGatos")
    botao2.config(text=f'Amante de Gatos\nCusto: {catloverValor:,}\nGanhe 2x mais gatos por clique.')
    botao2.config(state=DISABLED)

    if gatos >= catloverValor:
        botao2.config(state=NORMAL)

    if AmantGatos >= 2:
        novoBotao()

    if gatos >= leiteValor:
        botao3.config(state=NORMAL)

def catclick():
    global gatos
    gatos += AmantGatos
    cats()

def catlover():
    global AmantGatos, gatos, catloverValor

    AmantGatos *= 2
    gatos -= catloverValor
    catloverValor = int(50*(AmantGatos)**1.5)
    botao2.config(state=DISABLED)
    cats()

def catmilk():
    global leite, leiteValor, gatos, gsegundo

    leite += 1
    gatos -= leiteValor
    if leite == 1:
        leiteValor = 150
    else:
        leiteValor = int(100*(leite)**1.2)
    botao3.config(state=DISABLED)
    botao3.config(text=f'Leite\nCusto: {leiteValor}\nAtraia 1 gato por segundo.')
    gsegundo = leite
    label5.config(text=f"Gatos por Segundo:{gsegundo}")
    cats()


def novoBotao():
    global botao3, qtdbotoes, label5
    if qtdbotoes == 1 and AmantGatos >= 2:
        botao3 = tk.Button(
        root, text=f'Leite\nCusto: {leiteValor}\nAtraia 1 gato por segundo.',
        font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
        height=3,width=40,
        command=catmilk,
        state=DISABLED
        )
        botao3.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)
    if qtdbotoes == 1 and AmantGatos >= 2:
        label5 = tk.Label(
            root,bg="red",fg="black",border=20,width=20,
            font=(None,20),text=f"Gatos por Segundo:{gsegundo}"
        )
        label5.grid(column=1, row=2, sticky=tk.N, padx=5, pady=5)
        qtdbotoes += 1
    
    botao3.config(state=DISABLED)
    botao3.config(text=f'Leite\nCusto: {leiteValor}\nAtraia 1 gato por segundo.')
        


#Timer
def timer():
    global  h, m, s, gatos, gsegundo

    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1

    gatos += gsegundo 

    if gatos >= 8000000000:
        root.destroy()

    label1.config(text=f"{gatos:,}\nGatos")
    tempo = (f"{h:02d}:{m:02d}:{s:02d}")
    label3.config(text=tempo)
    label3.after(1000, timer)
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
    font=(None,20)
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

timer()
root.mainloop()