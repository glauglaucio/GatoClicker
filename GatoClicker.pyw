import tkinter as tk
from tkinter import *
import os


#Multiplicadores e Funções
gatos = gsegundo = leite = racao = h = s = m = 0
AmantGatos = 1
catloverValor = 50
leiteValor = 100
racaoValor = 1000

stop = 0

def cats():
    global gsegundo, stop
    gsegundo = (leite*(1)) + (racao*(10))

    label1.config(text=f"{gatos:,}\nGatos")
    label6.config(text=f"Gatos por Segundo: {gsegundo}")
    label5.config(text=f"Gatos por Cliques: {AmantGatos}")

    botao2.config(text=f'Amante de Gatos\nCusto: {catloverValor:,}\nGanhe 2x mais gatos por clique.')
    botao3.config(text=f'Leite\nCusto: {leiteValor:,}\nAtraia 1 gato por segundo.')
    botao4.config(text=f'Ração\nCusto: {racaoValor:,}\nAtraia 10 gatos por segundo.')

    botao2.config(state=DISABLED)
    botao3.config(state=DISABLED)
    botao4.config(state=DISABLED)

    if AmantGatos >= 2 and stop == 0:
        stop += 1
        frame1.destroy()
        frame2.destroy()
    
    if leite >= 1 and stop == 1:
        stop += 1
        frame4.destroy()
        frame3.destroy()

    if gatos >= catloverValor:
        botao2.config(state=NORMAL)

    if gatos >= leiteValor:
        botao3.config(state=NORMAL)

    if gatos >= racaoValor:
        botao4.config(state=NORMAL)

def catclick():
    global gatos
    gatos += AmantGatos
    cats()

def catlover():
    global AmantGatos, gatos, catloverValor

    AmantGatos *= 2
    gatos -= catloverValor
    catloverValor = int(50*(AmantGatos)**1.3)
    cats()

def catmilk():
    global leite, leiteValor, gatos

    leite += 1
    gatos -= leiteValor
    if leite == 1:
        leiteValor = 150
    else:
        leiteValor = int(100*(leite)**1.1)
    cats()

def catrac():
    global racaoValor, racao, gatos
    
    racao += 1
    gatos -= racaoValor
    if racao == 1:
        racaoValor = 1500
    else:
        racaoValor = int(1000*(racao)**1.2)
    cats()


#Timer
def timer():
    global  h, m, s, gatos

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
botao2.grid(column=2, row=1, sticky=tk.S, padx=5, pady=5)

label5 = tk.Label(
    root,bg="red",fg="black",border=20,width=20,
    font=(None,20),text=f"Gatos por Cliques:{AmantGatos}"
)
label5.grid(column=1, row=2, sticky=tk.N, padx=5, pady=5)

frame1 = tk.Frame(
    root,width=365,height=100,bg="black"
)
frame1.grid(column=1, row=2, sticky=tk.N, padx=5, pady=5)

botao3 = tk.Button(
    root, text=f'Leite\nCusto: {leiteValor}\nAtraia 1 gato por segundo.',
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catmilk,
    state=DISABLED
)
botao3.grid(column=2, row=2, sticky=tk.N, padx=5, pady=5)

frame2 = tk.Frame(
    root,width=445,height=100,bg="black"
)
frame2.grid(column=2, row=2, sticky=tk.N, padx=5, pady=5)

botao4 = tk.Button(
    root, text=f'Ração\nCusto: {racaoValor:,}\nAtraia 10 gatos por segundo.',
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catrac,
    state=DISABLED
)
botao4.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)

frame3 = tk.Frame(
    root,width=445,height=100,bg="black"
)
frame3.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)

label6 = tk.Label(
    root,bg="red",fg="black",border=20,width=20,
    font=(None,20),text=f"Gatos por Segundo:{gsegundo}"
)
label6.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

frame4 = tk.Frame(
    root,width=365,height=100,bg="black"
)
frame4.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

timer()
root.mainloop()