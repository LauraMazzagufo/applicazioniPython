import random
import sys
from os.path import exists
import tkinter as tk
from tkinter import messagebox
import turtle
import time

############################################
#    Progetto a cura di Laura Mazzagufo    #
#             Matricola: 589573            #
#      l.mazzagufo@studenti.unipi.it       #
############################################

######################################################
# stabilisco delle costanti per rappresentare celle vive e celle morte
cella_viva = "x"
cella_morta = "o"

square_width = 30  # definisce ampiezza quadrato che rappresenta la cella
spacing = 30  # essendo uguale a square_width, affianca ogni quadrato al successivo, per creare una griglia


# codice di gestione di evento per il clic sul pulsante choice1
def handle_click_choice1(event):
    window.destroy()  # chiude la finestra dopo il clic
    griglia = carica_simulazione_da_file()
    numero_passi = carico_numero_passi()
    print(numero_passi)  # stampa a riga di comando (solo per controllo)
    stampa_griglia(griglia)  # stampa a riga di comando (solo per controllo)
    disegna_griglia(griglia)
    animazione(griglia, numero_passi)
    # aggiungere chiamata a popup per chiedere del salvataggio
    salva_simulazione(griglia)


# codice di gestione di evento per il clic sul pulsante choice2
def handle_click_choice2(event):
    window.destroy()  # Chiude la finestra dopo il clic
    lato_griglia = carica_lato_griglia()
    percentuale_riempimento_griglia = carica_percentuale_riempimento_griglia()
    griglia = genera_griglia(lato_griglia, percentuale_riempimento_griglia)
    numero_passi = carico_numero_passi()
    print(numero_passi)  # stampa a riga di comando (solo per controllo)
    stampa_griglia(griglia)  # stampa a riga di comando (solo per controllo)
    disegna_griglia(griglia)
    animazione(griglia, numero_passi)
    # aggiungere chiamata a popup per chiedere del salvataggio
    salva_simulazione(griglia)


# CHOICE 1: funzione per caricare e leggere la simulazione già esistente
def carica_simulazione_da_file():
    # codice di gestione dell'evento per l'input del nome del file
    def handle_keypress(event):
        nonlocal nomefile
        nomefile = entry.get()
        window.destroy()  # Chiudi la finestra dopo l'input

    nomefile = None  # Inizializza il nome del file a None
    window_open = True  # Inizializza la finestra come aperta

    while window_open:
        # Crea una seconda finestra (task1)
        window = tk.Tk()
        label = tk.Label(window, text="Inserisci il nome del file e premi 'Invio'")
        entry = tk.Entry(window, fg="white", bg="grey", width=50)
        label.pack()
        entry.pack()

        # Associa l'evento di pressione del tasto Invio alla funzione handle_keypress
        entry.bind("<Return>", handle_keypress)

        # Attendi finché la finestra non viene chiusa
        window.mainloop()

        if nomefile is None:
            # L'utente ha cliccato su Annulla o chiuso la finestra
            window_open = False
        else:
            try:
                f = open(nomefile)
                griglia = f.read()  # assegna alla variabile griglia
                griglia = griglia.split(
                    "\n")  # suddivide la griglia in una lista, per righe (ogni volta che c'è un a capo)

                for i in range(len(griglia)):
                    griglia[i] = list(griglia[i])
                    ### inserito ciclo che scorre tutte le celle e riassegna come "cella morta" tutte quelle che non sono "cella viva", a prescindere dal simbolo utilizzato nel file sorgente/simulazione
                    for j in range(len(griglia[i])):
                        if griglia[i][j] != cella_viva:
                            griglia[i][j] = cella_morta
                window_open = False

            except Exception as e:
                # Mostra un popup di errore
                messagebox.showerror("Errore", f"Errore nella lettura del file: {e}")
    return griglia


# CHOICE 2: funzione per inserire e leggere la lunghezza del lato della griglia
def carica_lato_griglia():
    # codice di gestione dell'evento per l'input del nome del file
    def handle_keypress(event):
        nonlocal lato_griglia
        lato_griglia = entry.get()
        window.destroy()  # Chiudi la finestra dopo l'input

    lato_griglia = None  # Inizializza il nome del file a None
    window_open = True  # Inizializza la finestra come aperta

    while window_open:
        # Crea un'altra finestra (task1)
        window = tk.Tk()
        label = tk.Label(window, text="Inserisci il lato della griglia e premi 'Invio'")
        entry = tk.Entry(window, fg="white", bg="grey", width=50)
        label.pack()
        entry.pack()

        # Associa l'evento di pressione del tasto Invio alla funzione handle_keypress
        entry.bind("<Return>", handle_keypress)

        # Attendi finché la finestra non viene chiusa
        window.mainloop()

        if lato_griglia is None:
            # L'utente ha cliccato su Annulla o chiuso la finestra
            window_open = False
        else:
            if not lato_griglia.isdigit() or not int(
                    lato_griglia) > 0:  # condizioni: che t sia una stringa formata solo da cifre numeriche (isdigit) e che sia maggiore di 0
                messagebox.showerror("Errore", f"Inserisci un numero intero positivo.")
            else:
                window_open = False
    return int(lato_griglia)


# CHOICE 2: funzione per inserire e leggere il coefficiente di riempimento della griglia
def carica_percentuale_riempimento_griglia():
    # codice di gestione dell'evento per l'input del nome del file
    def handle_keypress(event):
        nonlocal percentuale_riempimento_griglia
        percentuale_riempimento_griglia = entry.get()
        window.destroy()  # Chiudi la finestra dopo l'input

    percentuale_riempimento_griglia = None  # Inizializza il nome del file a None
    window_open = True  # Inizializza la finestra come aperta

    while window_open:
        # Crea una seconda finestra (task1)
        window = tk.Tk()
        label = tk.Label(window, text="Inserisci la percentuale di riempimento della griglia e premi 'Invio'")
        entry = tk.Entry(window, fg="white", bg="grey", width=50)
        label.pack()
        entry.pack()

        # Associa l'evento di pressione del tasto Invio alla funzione handle_keypress
        entry.bind("<Return>", handle_keypress)

        # Attendi finché la finestra non viene chiusa
        window.mainloop()

        if percentuale_riempimento_griglia is None:
            # L'utente ha cliccato su Annulla o chiuso la finestra
            window_open = False
        else:
            try:
                # converte in float: se ci riesce verifica che sia tra 0 e 1, se non ci riesce va in eccezione
                t = float(percentuale_riempimento_griglia)
                if t <= 0 or t >= 1:
                    messagebox.showerror("Errore", f"Inserisci un numero decimale tra 0 e 1.")
                else:
                    window_open = False
            except Exception as e:
                # Mostra un popup di errore
                messagebox.showerror("Errore", f"Inserisci un numero decimale tra 0 e 1.")
    return float(percentuale_riempimento_griglia)


# CHOICE 2: funzione che genera la griglia in base ai parametri inseriti
def genera_griglia(l, sigma):
    griglia = list(
        ' ' * (l * l))  # creo una lista di spazi vuoti lunga quanto il numero complessivo di celle della griglia (l*l)
    num_vive = round(
        sigma * l * l)  # calcolo quante sono le celle vive. Uso round perché decido che sia arrotondato (non può essere un numero decimale, deve essere un numero intero)
    # CICLO per sistemare le celle vive nella griglia
    for i in range(num_vive):  # si ripete per un numero pari al numero delle celle vive
        p = random.randint(0,
                           l * l - 1)  # variabile p = posizione a caso tra 0 e numero massimo di celle (-1 perché l'indice parte da 0)
        while griglia[p] == cella_viva:  # Condizione: se c'è già una cella viva
            p = random.randint(0, l * l - 1)  # p viene riassegnato casualmente un'altra volta
        griglia[p] = cella_viva  # assegno la posizione a una cella viva
    griglia2 = ""  # creo una seconda stringa vuota --> sarà identica alla prima ma con le righe (inserisco gli \n nel posto giusto)
    for i in range(len(griglia)):
        if i != 0 and i % l == 0:  # verifica se l'indice i è diverso da zero e se i è un multiplo intero della lunghezza del lato l
            griglia2 += "\n"  # se la condizione è rispettata, inserisce un'interruzione di riga
        griglia2 += griglia[i]  # aggiunge la riga corrente della griglia originale alla stringa griglia2
    griglia2 = griglia2.split(
        "\n")  # suddivide la stringa griglia2 ottenuta in una lista di stringhe utilizzando \n come delimitatore
    for i in range(len(griglia2)):  # si itera per ciascuna riga
        griglia2[i] = list(griglia2[i])  # conversione in lista
    return griglia2


# CHOICE 1/2: funzione per inserire e leggere il numero di passi richiesti
def carico_numero_passi():
    # codice di gestione dell'evento per l'input del nome del file
    def handle_keypress(event):
        nonlocal numero_passi
        numero_passi = entry.get()
        window.destroy()  # Chiudi la finestra dopo l'input

    numero_passi = None  # Inizializza il nome del file a None
    window_open = True  # Inizializza la finestra come aperta

    while window_open:
        # Crea un'altra finestra (task1)
        window = tk.Tk()
        label = tk.Label(window, text="Inserisci il numero di passi e premi 'Invio'")
        entry = tk.Entry(window, fg="white", bg="grey", width=50)
        label.pack()
        entry.pack()

        # Associa l'evento di pressione del tasto Invio alla funzione handle_keypress
        entry.bind("<Return>", handle_keypress)

        # Attendi finché la finestra non viene chiusa
        window.mainloop()

        if numero_passi is None:
            # L'utente ha cliccato su Annulla o chiuso la finestra
            window_open = False
        else:
            if not numero_passi.isdigit() or not int(
                    numero_passi) > 0:  # condizioni: che t sia una stringa formata solo da cifre numeriche (isdigit) e che sia maggiore di 0
                messagebox.showerror("Errore", f"Inserisci un numero intero positivo.")
            else:
                window_open = False
    return int(numero_passi)


# CHOICE 1/2: funzione che usa modulo turtle per disegnare la griglia
def disegna_griglia(griglia):
    turtle.reset()  # cancella la tela e fa tornare il puntatore al punto di partenza
    turtle.speed(0)  # velocità massima
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            if griglia[i][j] == cella_viva:  # se la cella è viva disegna un quadrato pieno
                filled_square(square_width)  # chiama la funzione per disegnare quadrato pieno (cella viva)
            else:  # se la cella è morta disegna un quadrato vuoto
                turtle.pendown()
                for _ in range(4):
                    turtle.forward(square_width)
                    turtle.right(90)
                turtle.penup()
            turtle.forward(spacing)
        # Riposiziono il puntatore per iniziare una nuova riga:
        turtle.backward(spacing * len(griglia))  # riporto la tartaruga all'inizio della riga
        turtle.right(90)  # giro la tartaruga verso il basso
        turtle.forward(spacing)  # e la sposto di una lunghezza pari a quella del lato del quadrato
        turtle.left(90)  # giro di nuovo la tartaruga nella posizione giusta per cominciare una nuova riga


# funzione per disegnare la cella viva (quadrato pieno)
def filled_square(width):
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


# CHOICE 1/2: funzione per passare da una generazione all'altra per il numero di passi stabilito
def animazione(griglia, numero_passi):
    for i in range(numero_passi):  # ripeto tante volte quanto numero_passi
        time.sleep(1)  # mette in pausa il programma per un secondo
        print("passo", i + 1)  # questo serve solo a riga di comando
        griglia_successiva = modifica_griglia(griglia)
        stampa_griglia(griglia_successiva)  # questo serve solo a riga di comando
        disegna_griglia(griglia_successiva)
        griglia = griglia_successiva  # sovrascrive la griglia corrente
    return griglia


# funzione per modificare la griglia da una generazione all'altra
def modifica_griglia(griglia):
    # creo una variabile per memorizzare la nuova griglia, che rappresenta la generazione successiva
    griglia_successiva = []
    # ciclo per scorrere ogni cella della griglia corrente
    for i in range(len(griglia)):
        # crea una nuova riga che verrà utilizzata per creare la nuova griglia e inizializzata con tutte celle morte
        nuova_riga = [cella_morta] * len(
            griglia[0])  # il numero di celle morte deve essere uguale al numero di colonne della griglia originale
        for j in range(len(griglia[0])):
            num_adiacenti_vive = get_num_adiacenti_vive(griglia, i, j)
            # applico le condizioni del gioco della vita
            if griglia[i][j] == cella_viva:
                # in caso di cella viva:
                # if num_adiacenti_vive<2 or num_adiacenti_vive>3: # condizione 1 e condizione 3 delle istruzioni del gioco
                # morta (non faccio nulla perchè le celle sono già inizializzate tutte morte)
                if num_adiacenti_vive in (2, 3):  # condizione 2 delle istruzioni del gioco della vita
                    nuova_riga[j] = cella_viva
            else:
                # in caso di cella morta
                if num_adiacenti_vive == 3:  # condizione 4 delle istruzioni del gioco
                    nuova_riga[j] = cella_viva  # dentro la nuova riga, la cella di indice j diventa una cella viva
        griglia_successiva.append(nuova_riga)
    return griglia_successiva


# funzione per conoscere il numero di celle adiacenti vive per ogni cella della griglia
def get_num_adiacenti_vive(griglia, i, j):
    lista_adiacenti = []
    # calcola lista adiacenti
    if i > 0:  # se la cella NON è nella prima riga --> ha celle adiacenti sopra
        lista_adiacenti.append((i - 1,
                                j))  # alla lista di celle adiacenti bisogna aggiungere la coppia di coordinate i-1 (riga sopra) e j (stessa colonna)
        if j > 0:  # se la colonna non è la prima
            lista_adiacenti.append((i - 1,
                                    j - 1))  # bisogna aggiungere anche la cella della riga superiore (i-1) e della colonna immediatamente a sinistra (j-1)
            lista_adiacenti.append((i,
                                    j - 1))  # bisogna aggiungere anche la cella della stessa riga (i) e della colonna immediatamente a sinistra (j-1)
        if j < len(griglia[0]) - 1:  # se la colonna non è l'ultima
            lista_adiacenti.append((i - 1,
                                    j + 1))  # si aggiunge anche la cella della riga superiore (i-1) e della colonna immediatamete a destra (j+1)
            lista_adiacenti.append((i,
                                    j + 1))  # si aggiunge anche la cella della stessa riga(i) e della colonna immediatamete a destra (j+1)
    else:  # se la riga è la prima
        if j > 0:  # se la colonna non è la prima
            lista_adiacenti.append((i,
                                    j - 1))  # bisogna aggiungere anche la cella della stessa riga (i) e della colonna immediatamente a sinistra (j-1)
        if j < len(griglia[0]) - 1:  # se la colonna non è l'ultima
            lista_adiacenti.append((i,
                                    j + 1))  # bisogna aggiungere anche la cella della stessa riga (i) e della colonna immediatamente a destra (j+1)
    if i < len(griglia) - 1:  # se la cella NON è nell'ultima riga
        lista_adiacenti.append(
            (i + 1, j))  # aggiungo alla lista anche la cella della riga sotto (i+1) nella stessa colonna
        if j > 0:  # se la colonna non è la prima
            lista_adiacenti.append((i + 1,
                                    j - 1))  # bisogna aggiungere anche la cella della riga inferiore (i+1) e della colonna immediatamente a sinistra (j-1)
        if j < len(griglia[0]) - 1:  # se la colonna non è l'ultima
            lista_adiacenti.append((i + 1,
                                    j + 1))  # bisogna aggiungere anche la cella della riga inferiore (i+1) e della colonna immediatamente a destra (j+1)
    # inizializzo il numero delle celle vive a 0
    num_vive = 0
    for adiacente in lista_adiacenti:  # ciclo che per ogni elemento della lista_adiacenti
        adiacente_i = adiacente[0]  # nuova variabile per indicare la coordinata i della cella adiacente
        adiacente_j = adiacente[1]  # nuova variabile per indicare la coordinata j della cella adiacente
        if griglia[adiacente_i][adiacente_j] == cella_viva:  # verifica se la cella adiacente nella griglia è viva
            num_vive += 1
    return num_vive


# funzione per stampare la griglia a riga di comando (solo per controllo)
def stampa_griglia(griglia):
    print()
    for riga in griglia:
        for c in riga:
            print(c, end="")  # end="" evita che stampi ulteriori spazi oltre a quelli presenti nella simulazione
        print()
    print()


############### SALVATAGGIO ##############
# funzione per salvare l'ultima generazione
def salva_simulazione(griglia_successiva):
    # crea una finestra (task1)
    window = tk.Tk()
    # crea un widget della classe Label
    greeting = tk.Label(
        text="Vuoi salvare l'ultima generazione?",
        # colore del testo rosso
        foreground="red",
        # altezza e larghezza in «text units »
        width=50,
        height=10
    )
    # crea un widget della classe Button
    salva = tk.Button(
        text="Salva \nla simulazione",
        # altezza e larghezza in «text units »
        width=30,
        height=5,
        bg="grey",
        fg="white",
    )
    # crea un altro widget della classe Button
    esci = tk.Button(
        text="Esci \nsenza salvare",
        # altezza e larghezza in «text units »
        width=30,
        height=5,
        bg="grey",
        fg="white",
    )
    # inserisce il widget nella finestra
    # pack() fa il resize della finestra fino a includere esattamente i widget in ordine
    greeting.pack()
    salva.pack()
    esci.pack()

    # gestore di evento clic sul pulsante choice1
    salva.bind("<Button-1>", lambda event: handle_click_salvanome(event, griglia_successiva, window))

    # gestore di evento clic sul pulsante choice2
    esci.bind("<Button-1>", handle_click_esci)

    # attiva meccanismo di ascolto degli eventi esterni (task 4) e attiva la finestra (viene visualizzata)
    window.mainloop()


# codice di gestione di evento per il clic sul pulsante Esci
def handle_click_esci(event):
    # Chiude tutte le finestre della GUI
    event.widget.master.destroy()
    # Termina il programma
    sys.exit(0)


# codice di gestione di evento per il clic sul pulsante Salva
def handle_click_salvanome(event, griglia, w):
    # codice di gestione dell'evento per l'input del nome del file
    def handle_keypress(event):
        nonlocal nome_file
        nome_file = entry.get()

        # Salva la griglia in formato .txt con il nome immesso in input
        salva_su_file(griglia, nome_file)
        # Chiude tutte le finestre della GUI
        event.widget.master.destroy()
        # Termina il programma
        sys.exit(0)
        window.destroy()  # Chiudi la finestra dopo l'input

    w.destroy()  # chiude la finestra
    nome_file = None  # Inizializza il nome del file a None

    # Crea un'altra finestra (task1)
    window = tk.Tk()
    label = tk.Label(window, text="Inserisci il nome del file (.txt) e premi 'Invio'")
    entry = tk.Entry(window, fg="white", bg="grey", width=50)
    label.pack()
    entry.pack()

    # Associa l'evento di pressione del tasto Invio alla funzione handle_keypress
    entry.bind("<Return>", handle_keypress)

    # Attendi finché la finestra non viene chiusa
    window.mainloop()


def salva_su_file(griglia, nomefile):
    s = "" #  inizializza stringa vuota 
    f = open(nomefile, "w") #  apre nomefile in modalità scrittura
    for riga in griglia: #  cicla ogni riga della griglia
        r = "".join(riga) #  la riga è convertita in stringa unendo tutti i caratteri senza spazi
        s += r + "\n" #  la stringa ottenuta è concatenata ad s e a un'interruzione riga
    f.write(s[:-1]) #  toglie l'ultima interruzione di riga
    f.close()


############## INIZIO DEL GIOCO #################

# crea una finestra (task1)
window = tk.Tk()
# crea un widget della classe Label
greeting = tk.Label(
    text="Progetto 'LIFE' - dicembre 2023"
         "\n\nSeleziona un'opzione:",
    # colore del testo rosso
    foreground="red",
    # altezza e larghezza in «text units »
    width=50,
    height=10
)
# crea un widget della classe Button
choice1 = tk.Button(
    text="Clicca qui \nper caricare una simulazione da file.",
    # altezza e larghezza in «text units »
    width=30,
    height=5,
    bg="grey",
    fg="white",
)
# crea un altro widget della classe Button
choice2 = tk.Button(
    text="Clicca qui \nper creare una nuova simulazione.",
    # altezza e larghezza in «text units »
    width=30,
    height=5,
    bg="grey",
    fg="white",
)
# inserisce il widget nella finestra
# pack() fa il resize della finestra fino a includere esattamente i widget in ordine
greeting.pack()
choice1.pack()
choice2.pack()

# gestore di evento clic sul pulsante choice1
choice1.bind("<Button-1>", handle_click_choice1)

# gestore di evento clic sul pulsante choice2
choice2.bind("<Button-1>", handle_click_choice2)

# attiva meccanismo di ascolto degli eventi esterni (task 4) e attiva la finestra (viene visualizzata)
window.mainloop()
