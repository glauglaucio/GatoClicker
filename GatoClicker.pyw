import tkinter as tk
from tkinter import *
import os


#Variaveis
gatos = clique = resultado = endgame = gsegundo = leite = racao = sard = cientista = h = s = m = leiteValor = qAmanteGatos =catloverValor = racaoValor = sardValor = cientistaValor =stop = 0
AmantGatos = Qtd = cQtd = lp = rp = sp = 1


#Função Principal
def cats():
    global gsegundo, stop, sardValor, leiteValor, racaoValor, catloverValor, cientistaValor, clique

    #Produção por Segundo
    gsegundo = (leite*(1)) + (racao*(10)) + (sard*(100))
    clique = (1+cientista)*AmantGatos

    #Atualizar Valores de Produção
    label1.config(text=f"{gatos:,}\nGatos".replace(",","."))
    label5.config(text=f"Gatos por Cliques: {clique:,}".replace(",","."))
    label6.config(text=f"Gatos por Segundo: {gsegundo:,}".replace(",","."))


    #Desabilitar Botões de Upgrades
    botao2.config(state=DISABLED)
    botao3.config(state=DISABLED)
    botao4.config(state=DISABLED)
    botao5.config(state=DISABLED)
    botao6.config(state=DISABLED)


    #Obter Preços
    catloverValor = obterValor("AmantGatos")
    leiteValor = obterValor("lp")
    racaoValor = obterValor("rp")
    sardValor = obterValor("sp")
    cientistaValor = obterValor("cientista")


    #Atualização dos Preços (Caso o valor seja muito grande, ele será encurtado)
    if  catloverValor >= 1000000000000:
        botao2.config(text=f'Amante de Gatos / Click x{AmantGatos:,}\nCusto: {catloverValor:.2e}\nGanhe 2x mais gatos por clique.'.replace(",","."))
    else:
        botao2.config(text=f'Amante de Gatos / Click x{AmantGatos:,}\nCusto: {catloverValor:,}\nGanhe 2x mais gatos por clique.'.replace(",","."))

    if  leiteValor >= 1000000000000:
        botao3.config(text=f'Leite *{leite}*\nCusto: {leiteValor:.2e}\nAtraia 1 gato por segundo.'.replace(",","."))
    else:
        botao3.config(text=f'Leite *{leite}*\nCusto: {leiteValor:,}\nAtraia 1 gato por segundo.'.replace(",","."))
    
    if racaoValor >= 1000000000000:
        botao4.config(text=f'Ração *{racao}*\nCusto: {racaoValor:.2e}\nAtraia 10 gatos por segundo.'.replace(",","."))
    else:
        botao4.config(text=f'Ração *{racao}*\nCusto: {racaoValor:,}\nAtraia 10 gatos por segundo.'.replace(",","."))

    if sardValor >= 1000000000000:  
        botao5.config(text=f'Sardinha *{sard}*\nCusto: {sardValor:.2e}\nAtraia 100 gatos por segundo.'.replace(",","."))
    else:
        botao5.config(text=f'Sardinha *{sard}*\nCusto: {sardValor:,}\nAtraia 100 gatos por segundo.'.replace(",","."))
    
    if cientistaValor >=1000000000000:
        botao6.config(text=f'Cientista de Gatos *{cientista}*\nCusto: {cientistaValor:.2e}\nSeu clique valhe 1 a mais.'.replace(",","."))
    else:
        botao6.config(text=f'Cientista de Gatos *{cientista}*\nCusto: {cientistaValor:,}\nSeu clique valhe 1 a mais.'.replace(",","."))


    #Reveladores de Botões
    if gatos == 1 and stop == 0:
        stop += 1
        botaocm1.config(state=DISABLED)
        label2.destroy()
        timer()

    if cientista >= 1 and stop == 1:
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
    
    if sard >= 1 and stop == 4:
        stop += 1
        label4.destroy()
        frame6.destroy()
    


    #Faz com que os Botões dos Upgrades Compraveis sejam Clicáveis
    if endgame == 0 or endgame  == 2:
        if gatos >= catloverValor:
            botao2.config(state=NORMAL)

        if gatos >= leiteValor:
            botao3.config(state=NORMAL)

        if gatos >= racaoValor:
            botao4.config(state=NORMAL)
        
        if gatos >= sardValor:
            botao5.config(state=NORMAL)
        
        if gatos >= cientistaValor:
            botao6.config(state=NORMAL)


#Multiplicadores de preço
def obterValor(valorde):
    resultado = 0

    if valorde == "AmantGatos":
        ppAG = qAmanteGatos
        desejoTer = ppAG + cQtd

        somatoria = []
        while ppAG < desejoTer:
            ppAG += 1
            somatoria.append(int(ppAG))

        for x in somatoria:
            print(x)
            somar = int((10)**x)
            resultado = somar + resultado

    if valorde == "lp":
        pplp = lp
        desejoTer = pplp + cQtd

        somatoria = []
        while pplp < desejoTer:
            pplp += 1
            somatoria.append(int(pplp))

        for x in somatoria:
            somar = int(10*1.15**x)
            resultado = somar + resultado

    if valorde == "rp":
        pprp = rp
        desejoTer = pprp + cQtd

        somatoria = []
        while pprp < desejoTer:
            pprp += 1
            somatoria.append(int(pprp))

        for x in somatoria:
            somar = int(100*1.15**x)
            resultado = somar + resultado

    if valorde == "sp":
        ppsp = sp
        desejoTer = ppsp + cQtd

        somatoria = []
        while ppsp < desejoTer:
            ppsp += 1
            somatoria.append(int(ppsp))

        for x in somatoria:
            somar = int(1000*1.15**x)
            resultado = somar + resultado

    if valorde == "cientista":
        cp = cientista
        desejoTer = cp + cQtd   

        somatoria = []
        while cp < desejoTer:
            cp += 1
            somatoria.append(int(cp))
        for x in somatoria:
            somar = int(7*1.5**x)
            resultado = somar + resultado

    return resultado


#Funções dos Botões
def catclick():
    global gatos, clique
    
    if endgame == 0 or endgame == 2:
        if gatos >= 8000000000 and endgame!= 2:
            finalg()
        
        gatos += clique
        cats()

def catlover():
    global AmantGatos, gatos, catloverValor, qAmanteGatos

    qAmanteGatos += 1*(cQtd)
    AmantGatos *= 2*(cQtd)
    gatos -= catloverValor
    cats()

def catmilk():
    global leite, leiteValor, gatos, lp

    leite += 1*(cQtd)
    if leite != 0 and leite != 1:
        lp = leite
    else:
        lp += 0.5

    gatos -= leiteValor
    cats()

def catrac():
    global racaoValor, racao, gatos, rp
    
    racao += 1*(cQtd)
    if racao != 0 and racao != 1:
        rp = racao
    else:
        rp += 0.5

    gatos -= racaoValor
    cats()

def catsard():
    global sardValor, sard, gatos,sp

    sard += 1*(cQtd)
    if sard != 0 and sard != 1:
        sp = sard
    else:
        sp += 0.5
    
    gatos -= sardValor
    cats()

def catcience():
    global cientistaValor, cientista, gatos

    cientista += 1*(cQtd)
    gatos -= cientistaValor

    cats()
    pass


#Switchs dos Botões de escolher Quantidade
def comprarQtd(Qtd):
    global cQtd

    if Qtd == 1:
        cQtd = 1
        botaocm1.config(state=DISABLED)
        botaocm2.config(state=NORMAL)
        botaocm3.config(state=NORMAL)
        cats()

    elif Qtd == 10:
        cQtd = 10
        botaocm1.config(state=NORMAL)
        botaocm2.config(state=DISABLED)
        botaocm3.config(state=NORMAL)
        cats()

    elif Qtd == 100: 
        cQtd = 100
        botaocm1.config(state=NORMAL)
        botaocm2.config(state=NORMAL)
        botaocm3.config(state=DISABLED)
        cats()


#Final do Jogo
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
    final, text=f"Humanos: 8,000,000,000.\nGatos: {gatos:,}+".replace(",","."),
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


#Cronômetro
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

        label1.config(text=f"{gatos:,}\nGatos".replace(",","."))
        tempo = (f"{h:02d}:{m:02d}:{s:02d}")
        label3.config(text=tempo,font=(None,20))
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
    font=(None,30),text=f"{gatos:,}\nGatos".replace(",",".")
)
label1.grid(column=1, row=0, sticky=tk.N, padx=10, pady=30)

label2 = tk.Label(
    root,bg="red",fg="black",border=50,
    font=(None,20),text="CLIQUE NO GATO"
)
label2.grid(column=1,row=0,sticky=tk.N)

label3 = tk.Label(
    root,bg="red",fg="black",border=50,width=10,height=1,
    text="Objetivo:\nAtrair\n8.000.000.000\nGatos",
    font=(None,20)
)
label3.grid(column=0,row=0,sticky=tk.N)

botaocm1 = tk.Button(
    root,text="1",width=3,
    bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    font=(None,13),
    command=lambda: comprarQtd(1)
)
botaocm1.grid(column=2,row=0,sticky=tk.SW,pady=40,padx=120)

botaocm2 = tk.Button(
    root,text="10",width=3,
    bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    font=(None,13),
    command=lambda: comprarQtd(10)
)
botaocm2.grid(column=2,row=0,sticky=tk.S,pady=40,padx=120)

botaocm3 = tk.Button(
    root,text="100",width=3,
    bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    font=(None,13),
    command=lambda: comprarQtd(100)
)
botaocm3.grid(column=2,row=0,sticky=tk.SE,pady=40,padx=120)

labelcm = tk.Label(
    root,text="Comprar",width=7,
    bg="red",fg="black",borderwidth=0.5,activebackground="#151515",
    font=(None,30)
)
labelcm.grid(column=2,row=0,sticky=tk.N,pady=15)

label4 = tk.Label(
    root,bg="red",fg="black",border=50,width=22,
    font=(None,20),text="COMPRE UPGRADES"
)
label4.grid(column=2,row=0,sticky=tk.N)

botao1 = tk.Button(
    root,background="black",foreground="black", activebackground="black",
    image=gatoimage,
    command=catclick,
    borderwidth=0, width=200
)
botao1.grid(column=1, row=1, sticky=tk.W,padx=100)

botao2 = tk.Button(
    root, text=f'Amante de Gatos\nCusto: {catloverValor}\nGanhe 2x mais gatos por clique.',
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catlover,
    state=DISABLED
)
botao2.grid(column=2, row=5, sticky=tk.S, padx=5, pady=5)

label5 = tk.Label(
    root,bg="red",fg="black",border=20, width=20,
    font=(None,20),text=f"Gatos por Cliques:{clique:,}".replace(",",".")
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
    root, text=f'Ração\nCusto: {racaoValor:,}\nAtraia 10 gatos por segundo.'.replace(",","."),
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
    root,bg="red",fg="black",border=20, width=20,
    font=(None,20),text=f"Gatos por Segundo:{gsegundo:,}".replace(",",".")
)
label6.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

frame4 = tk.Frame(
    root,width=365,height=100,bg="black"
)
frame4.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

botao5 = tk.Button(
    root, text=f'Sardinha\nCusto: {sardValor:,}\nAtraia 100 gatos por segundo.'.replace(",","."),
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

botao6 = tk.Button(
    root, text=f'Cientista de Gatos\nCusto: {cientistaValor:,}\nSeu clique valhe 1 a mais.'.replace(",","."),
    font=(None,15), bg="#151515",fg="red",borderwidth=0.5,activebackground="#151515",
    height=3,width=40,
    command=catcience,
    state=DISABLED
)
botao6.grid(column=2, row=1, sticky=tk.S, padx=5, pady=5)

frame6 = tk.Frame(
    root,width=445,height=100,bg="black"
)
frame6.grid(column=2, row=5, sticky=tk.N, padx=5, pady=5)


cats()
root.mainloop()