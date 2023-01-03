import tkinter as tk
from tkinter import *
import os


#Multiplicadores e Funções
gatos = endgame = gsegundo = leite = racao = sard = h = s = m = 0
AmantGatos = 1
catloverValor = 50
leiteValor = 10
racaoValor = 100
sardValor = 1000

stop = 0

def cats():
    global gsegundo, stop
    gsegundo = (leite*(1)) + (racao*(10) + sard*(100))

    label1.config(text=f"{gatos:,}\nGatos")
    label6.config(text=f"Gatos por Segundo: {gsegundo:,}")
    label5.config(text=f"Gatos por Cliques: {AmantGatos:,}")

    botao2.config(text=f'Amante de Gatos / Click x{AmantGatos}\nCusto: {catloverValor:,}\nGanhe 2x mais gatos por clique.')
    botao3.config(text=f'Leite *{leite}*\nCusto: {leiteValor:,}\nAtraia 1 gato por segundo.')
    botao4.config(text=f'Ração *{racao}*\nCusto: {racaoValor:,}\nAtraia 10 gatos por segundo.')
    botao5.config(text=f'Sardinha *{sard}*\nCusto: {sardValor:,}\nAtraia 100 gatos por segundo.')

    botao2.config(state=DISABLED)
    botao3.config(state=DISABLED)
    botao4.config(state=DISABLED)
    botao5.config(state=DISABLED)

    if gatos == 1 and stop == 0:
        stop += 1
        label2.destroy()

    if AmantGatos >= 2 and stop == 1:
        stop += 1
        frame1.destroy()
        frame2.destroy()
    
    if leite >= 1 and stop == 2:
        stop += 1
        frame4.destroy()
        frame3.destroy()

    if racao >=1 and stop == 3:
        stop += 1
        frame5.destroy()

    if endgame == 0 or endgame  == 2:
        if gatos >= catloverValor:
            botao2.config(state=NORMAL)

        if gatos >= leiteValor:
            botao3.config(state=NORMAL)

        if gatos >= racaoValor:
            botao4.config(state=NORMAL)
        
        if gatos >= sardValor:
            botao5.config(state=NORMAL)

def catclick():
    global gatos

    if endgame == 0 or endgame == 2:
        if gatos >= 8000000000 and endgame!= 2:
            finalg()
        
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
    leiteValor = int(10*(leite)**1.5+(9+leite/leite))
    cats()

def catrac():
    global racaoValor, racao, gatos
    
    racao += 1
    gatos -= racaoValor
    racaoValor = int(100*(racao)**1.4+(99+racao/racao))
    cats()

def catsard():
    global sardValor, sard, gatos

    sard += 1
    gatos -= sardValor
    sardValor = int(1000*(sard)**1.3+(999+sard/sard))
    cats()


def escolheu(escolha):
    global endgame
    if escolha == "continuar":
        endgame = 2
        cats()
        timer()
        final.destroy()
    elif escolha == "parar":
        root.destroy()
        final.destroy()

def finalg():
    global final, endgame
    endgame = 1

    final = tk.Tk()
    final.title("OS GATOS DOMINARAM O MUNDO.")
    nx = int((sw-clickerw/2)/2)
    ny = int((sh-clickerh/2)/2)
    final.geometry(f"{int(clickerw/2)}x{int(clickerh/2)}+{nx}+{ny}")
    final.iconbitmap(f"{pastaAtual}\image\png.ico")

    final.configure(takefocus=True, background="red")

    finallabel1 = tk.Label(
        final, text="A população de gatos acabou de ultrapassar...\n A POPULAÇÃO HUMANA!!!",
        font=(None,15), bg="black",fg="red"
    )
    finallabel1.pack(pady=5)

    finallabel4 = tk.Label(
    final, text=f"Humanos: 8,000,000,000.\nGatos: {gatos:,}+",
    font=(None,15), bg="black",fg="red"
    )
    finallabel4.pack(pady=5)

    finallabel2 = tk.Label(
        final, text=f"Você conseguiu fazer esta proesa em {h:02d}:{m:02d}:{s:02d}!",
        font=(None,15), bg="black",fg="red"
    )
    finallabel2.pack(pady=5)

    finallabel3 = tk.Label(
        final, text="Deseja continuar jogando?",
        font=(None,15), bg="black",fg="red"
    )
    finallabel3.pack(pady=5)

    finalframe = tk.Frame(final,bg="black",
        borderwidth=30,padx=20,pady=10
    )
    finalframe.pack(pady=10)

    continuar = tk.Button(finalframe, text="CONTINUAR",
        font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
        height=1,width=10,
        command=lambda: escolheu("continuar")
    )
    continuar.grid(column=0,row=0,sticky=tk.W,padx=30)

    parar = tk.Button(finalframe, text="PARAR",
        font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
        height=1,width=10,
        command=lambda: escolheu("parar")
    )
    parar.grid(column=1,row=0,sticky=tk.E,padx=30)


#Timer
def timer():
    global  h, m, s, gatos
    if endgame == 0 or endgame == 2:
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1

        gatos += gsegundo 

        if gatos >= 8000000000 and endgame != 2:
            finalg()

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
root.columnconfigure(0, weight=1)
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


#UI
label1 = tk.Label(
    root,fg="red",bg="black",
    font=(None,30),text=f"{gatos:,}\nGatos"
)
label1.grid(column=1, row=0, sticky=tk.N, padx=10, pady=30)

label2 = tk.Label(
    root,bg="red",fg="black",border=50,
    font=(None,20),text="CLIQUE NO GATO"
)
label2.grid(column=1,row=0,sticky=tk.N)

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
    font=(None,20),text=f"Gatos por Cliques:{AmantGatos:,}"
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
    font=(None,20),text=f"Gatos por Segundo:{gsegundo:,}"
)
label6.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

frame4 = tk.Frame(
    root,width=365,height=100,bg="black"
)
frame4.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

botao5 = tk.Button(
    root, text=f'Sardinha\nCusto: {sardValor:,}\nAtraia 100 gatos por segundo.',
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catsard,
    state=DISABLED
)
botao5.grid(column=2, row=4, sticky=tk.N, padx=5, pady=5)

frame5 = tk.Frame(
    root,width=445,height=100,bg="black"
)
frame5.grid(column=2, row=4, sticky=tk.N, padx=5, pady=5)

timer()
root.mainloop()