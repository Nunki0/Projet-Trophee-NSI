from tkinter import *
from tkinter import ttk


def Réglages():
    zones = ["Afrique","Asie","Europe"]
    modes = ["Pays","Capitales"]
    
    global fenetre
    fenetre = Tk()
    fenetre.title("Réglages")
    

    mainframe = ttk.Frame(fenetre, padding="3 3 12 12")     #initialisation
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    #de
    fenetre.columnconfigure(0, weight=1)                    #la
    fenetre.rowconfigure(0, weight=1)                       #grille

    ttk.Button(mainframe, text="Ok", command=fenetre.quit).grid(column=3, row=3, sticky=W)

    liste_zones = ttk.Combobox(mainframe, values=zones) #liste déroulante des zones géographiques supportées
    liste_zones.current(2)
    liste_zones.grid(column=3, row=1, sticky=E)

    liste_modes = ttk.Combobox(mainframe, values=modes) #liste déroulante des modes de jeu supportés
    liste_modes.current(0)
    liste_modes.grid(column=3, row=2, sticky=E)

    fenetre.bind("<Return>", fenetre.quit)

    fenetre.mainloop()
    return liste_zones.get()
