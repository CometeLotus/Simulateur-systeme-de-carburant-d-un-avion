#Projet Concepts avances de programmation#
 
##################################
#    Pierre-Emmanuel Scrève      #
#    Alexandre Mihet             #
#    L2 TD1                      #
##################################
 
 
#Importations#

import tkinter as tk
import os
import random as rd
import time

#Initialisations#

Longueur = 700
Hauteur = 700

couleur_fg = 'white'
couleur_bg = 'black'
couleur_afg = 'white'
couleur_abg = 'grey'
bouton_bd = 5
bouton_relief = 'groove'
font = ('bold', '30')
liste = ['Tank 1', 'Tank 2', 'Tank 3', 'VanT12', 'VanT23', 'Van12', 'Van13', 'Van23','Mot1', 'Mot2','Mot3', 'P11_Mot1',
 'P12_Mot1', 'P11_Mot2', 'P12_Mot2', 'P11_Mot3', 'P12_Mot3']
dico = {}
sc = 0
texte = ""

#Fonctions utiles dans tout le code#

class Fonction(object):
    def __init__(self):
        pass
    def creer_dico(self):
        """Cette fonction permet de créer le dictionnaire que nous allons utiliser tout au long du code.
        ce dictionnaire aura pour clef le nom de l'objet (Moteurs, Pompes, vannes) et la valeur de cet objet
        (plein, ouverte, fermée, etc...)"""
        global liste, dico
        for i in range(len(liste)):
            if i < 3:
                dico[liste[i]] = 'plein'
            elif i >= 3 and i < 5:
                dico[liste[i]] = 'ouverte'
            elif i >= 5 and i < 8:
                dico[liste[i]] = 'fermée'
            elif i >= 8 and i < 11:
                dico[liste[i]] = liste[i-8]
            elif i >=11:
                if i%2 != 0:
                    dico[liste[i]] = 'en marche'
                else:
                    dico[liste[i]] = "à l'arret"
        

Cla = Fonction()


#Fonctions pour les boutons#
"""Chacune de ces fonctions sera  la commande d'un bouton, ce fier au nom de cette fonction pour 
trouver de quel bouton il s'agit"""

def functVT12():
    """La fonction functVT12 va modifier l'etat de la vanne (ouvert ou fermé) et si l'un des 2 tanks est plein
    et que l'autre est vide, l'un va remplir l'autre"""
    global VanT12, dico, texte, Tank_1, Tank_2
    texte2 = ""
    if dico['VanT12'] == 'ouverte':
        dico['VanT12'] = 'fermée'
    elif dico['VanT12'] == 'fermée':
        dico['VanT12'] = 'ouverte'
        if dico["Tank 1"] == 'vide' or dico['Tank 2'] =='vide':
            if dico["Tank 1"] == 'vide' and dico['Tank 2'] =='vide':
                texte2 = "Tank 1 " + dico["Tank 1"]
                Tank_1.configure(text = texte2)
                texte2 = "Tank 2 " + dico["Tank 2"]
                Tank_2.configure(text = texte2)
            else :
                dico["Tank 1"] = 'plein' 
                dico['Tank 2'] ='plein'
                texte2 = "Tank 1 " + dico["Tank 1"]
                Tank_1.configure(text = texte2)
                texte2 = "Tank 2 " + dico["Tank 2"]
                Tank_2.configure(text = texte2)
    texte = "La vanne VT12 est " + dico['VanT12']
    VanT12.configure(text=texte)
    action()

def functVT23():
    """Idem que functVT12 sauf qu'il s'agit de la vanne entre Tank 2 et Tank 3"""
    global VanT23, dico, texte, Tank_3, Tank_2
    if dico['VanT23'] == 'ouverte':
        dico['VanT23'] = 'fermée'
    elif dico['VanT23'] == 'fermée':
        dico['VanT23'] = 'ouverte'
        if dico["Tank 3"] == 'vide' or dico['Tank 2'] =='vide':
            if dico["Tank 3"] == 'vide' and dico['Tank 2'] =='vide':
                texte2 = "Tank 3 " + dico["Tank 3"]
                Tank_3.configure(text = texte2)
                texte2 = "Tank 2 " + dico["Tank 2"]
                Tank_2.configure(text = texte2)
            else :
                dico["Tank 3"] = 'plein' 
                dico['Tank 2'] ='plein'
                texte2 = "Tank 3 " + dico["Tank 3"]
                Tank_3.configure(text = texte2)
                texte2 = "Tank 2 " + dico["Tank 2"]
                Tank_2.configure(text = texte2)
    texte = "La vanne VT23 est " + dico['VanT23']
    VanT23.configure(text=texte)
    action()

def functV12():
    """"Va modifier l'etat de la vanne"""
    global Van12, dico, texte
    if dico['Van12'] == 'ouverte':
        dico['Van12'] = 'fermée'
    elif dico['Van12'] == 'fermée':
        dico['Van12'] = 'ouverte'
    texte = "La vanne V12 est " + dico['Van12']
    Van12.configure(text=texte)
    action()

def functV13():
    global Van13, dico, texte
    if dico['Van13'] == 'ouverte':
        dico['Van13'] = 'fermée'
    elif dico['Van13'] == 'fermée':
        dico['Van13'] = 'ouverte'
    texte = "La vanne V13 est " + dico['Van13']
    Van13.configure(text=texte)
    action()

def functV23():
    global Van23, dico, texte
    if dico['Van23'] == 'ouverte':
        dico['Van23'] = 'fermée'
    elif dico['Van23'] == 'fermée':
        dico['Van23'] = 'ouverte'
    texte = "La vanne V23 est " + dico['Van23']
    Van23.configure(text=texte)
    action()
    
def functP12():
    """"Va modifier l'etat de la pompe"""
    global P12_Mot1, dico, texte
    if dico['P12_Mot1'] == 'en marche':
        dico['P12_Mot1'] = "à l'arret"
        texte = "La pompe P12 du moteur 1 est " + dico['P12_Mot1']
        P12_Mot1.configure(text=texte)
    elif dico['P12_Mot1'] == "à l'arret":
        dico['P12_Mot1'] = 'en marche'
        texte = "La pompe P12 du moteur 1 est " + dico['P12_Mot1']
        P12_Mot1.configure(text=texte)
    elif dico['P12_Mot1'] == "en panne":
        dico['P12_Mot1'] = "en panne"
    action()


def functP22():
    global P12_Mot2, dico, texte
    if dico['P12_Mot2'] == 'en marche':
        dico['P12_Mot2'] = "à l'arret"
        texte = "La pompe P12 du moteur 2 est " + dico['P12_Mot2']
        P12_Mot2.configure(text=texte)
    elif dico['P12_Mot2'] == "à l'arret":
        dico['P12_Mot2'] = 'en marche'
        texte = "La pompe P12 du moteur 2 est " + dico['P12_Mot2']
        P12_Mot2.configure(text=texte)
    elif dico['P12_Mot2'] == "en panne":
        dico['P12_Mot2'] ="en panne"
    action()


def functP32():
    global P12_Mot3, dico, texte
    if dico['P12_Mot3'] == 'en marche':
        dico['P12_Mot3'] = "à l'arret"
        texte = "La pompe P12 du moteur 3 est " + dico['P12_Mot3']
        P12_Mot3.configure(text=texte)
    elif dico['P12_Mot3'] == "à l'arret":
        dico['P12_Mot3'] = 'en marche'
        texte = "La pompe P12 du moteur 3 est " + dico['P12_Mot3']
        P12_Mot3.configure(text=texte)    
    elif dico['P12_Mot3'] == "en panne":
        dico['P12_Mot3'] = "en panne"
    action()


def functank1():
    """"Va modifier l'etat du reservoir"""
    global Tank_1, dico
    dico["Tank 1"] = "vide"
    Tank_1.configure(text="Tank 1 vide")
    action()

def functank2():
    global Tank_2, dico
    dico["Tank 2"] = "vide"
    Tank_2.configure(text="Tank 2 vide")
    action()

def functank3():
    global Tank_3, dico
    dico["Tank 3"] = "vide"
    Tank_3.configure(text="Tank 3 vide")
    action()

def functP11_Mot1():
    """"Va modifier l'etat de la pompe"""
    global P11_Mot1, dico
    dico["P11_Mot1"] = "en panne"
    P11_Mot1.configure(text="La pompe P11 du moteur 1 est en panne")
    action()

def functP11_Mot2():
    global P11_Mot2, dico
    dico["P11_Mot2"] = "en panne"
    P11_Mot2.configure(text="La pompe P11 du moteur 2 est en panne")
    action()

def functP11_Mot3():
    global P11_Mot3, dico
    dico["P11_Mot3"] = "en panne"
    P11_Mot3.configure(text="La pompe P11 du moteur 3 est en panne")
    action()

def functP12_Mot1():
    global P12_Mot1,dico
    P12_Mot1.configure(text="La pompe P12 du moteur 1 est en panne")
    dico['P12_Mot1'] = "en panne"
    action()

def functP12_Mot2():
    global P12_Mot2,dico
    P12_Mot2.configure(text="La pompe P12 du moteur 2 est en panne")
    dico['P12_Mot2'] = "en panne"
    action()

def functP12_Mot3():
    global P12_Mot3,dico
    P12_Mot3.configure(text="La pompe P12 du moteur 3 est en panne")
    dico['P12_Mot3'] = "en panne"
    action()

def action():
    """"
    La fonction action permet de vérifier que les moteurs sont bien alimentés
    """
    "global stop"
    global dico
    global Mot1, Mot2, Mot3
    if  dico["Tank 1"] == "plein":
        if dico["P11_Mot1"] == "en marche":
            Mot1.configure(text = "M1 est alimenté par Tank 1")
        elif  dico["P11_Mot1"] != "en marche" and dico["P12_Mot1"] == "en marche":
            Mot1.configure(text = "M1 est alimenté par Tank 1")

        elif dico["P11_Mot1"] != "en marche" and dico["P12_Mot1"] != "en marche" :
            if (dico["P12_Mot2"] == "en marche") and dico["Van12"] == "ouverte" and dico["Tank 2"] == "plein":
                dico["Mot1"] = "Tank 2"
                Mot1.configure(text = "M1 est alimenté par Tank 2")
            elif (dico["P12_Mot3"] == "en marche") and dico["Van13"] == "ouverte" and dico["Tank 3"] == "plein":
                dico["Mot1"] = "Tank 3"
                Mot1.configure(text = "M1 est alimenté par Tank 3")
            else:
                dico["Mot1"] = ""
                Mot1.configure(text = "M1 est alimenté par")

    elif dico["Tank 1"] != "plein":
        if (dico["P12_Mot2"] == "en marche") and dico["Van12"] == "ouverte" and dico["Tank 2"] == "plein":
            dico["Mot1"] = "Tank 2"
            Mot1.configure(text = "M1 est alimenté par Tank 2")
        elif (dico["P12_Mot3"] == "en marche") and dico["Van13"] == "ouverte" and dico["Tank 3"] == "plein":
            dico["Mot1"] = "Tank 3"
            Mot1.configure(text = "M1 est alimenté par Tank 3")
        else:
            dico["Mot1"] = ""
            Mot1.configure(text = "M1 est alimenté par")

    if  dico["Tank 2"] == "plein":
        if dico["P11_Mot2"] == "en marche":
            Mot2.configure(text = "M2 est alimenté par Tank 2")
        elif  dico["P11_Mot2"] != "en marche" and dico["P12_Mot2"] == "en marche":
            Mot2.configure(text = "M2 est alimenté par Tank 2")



        elif dico["P11_Mot2"] != "en marche" and dico["P12_Mot2"] !=  "en marche":
            if (dico["P12_Mot1"] == "en marche") and dico["Van12"] == "ouverte" and dico["Tank 1"] == "plein":
                dico["Mot2"] = "Tank 1"
                Mot2.configure(text = "M2 est alimenté par Tank 1")
            elif (dico["P12_Mot3"] == "en marche") and dico["Van23"] == "ouverte" and dico["Tank 3"] == "plein":
                dico["Mot2"] = "Tank 3"
                Mot2.configure(text = "M2 est alimenté par Tank 3")
            else:
                dico["Mot2"] = ""
                Mot2.configure(text = "M2 est alimenté par")

    elif dico["Tank 2"] != "plein":
        if (dico["P12_Mot1"] == "en marche") and dico["Van12"] == "ouverte" and dico["Tank 1"] == "plein":
            dico["Mot2"] = "Tank 1"
            Mot2.configure(text = "M2 est alimenté par Tank 1")
        elif (dico["P12_Mot3"] == "en marche") and dico["Van23"] == "ouverte" and dico["Tank 3"] == "plein":
            dico["Mot2"] = "Tank 3"
            Mot2.configure(text = "M2 est alimenté par Tank 3")
        else:
            dico["Mot2"] = ""
            Mot2.configure(text = "M2 est alimenté par")

    if  dico["Tank 3"] == "plein":
        if dico["P11_Mot3"] == "en marche":
            Mot3.configure(text = "M3 est alimenté par Tank 3")
        elif  dico["P11_Mot3"] != "en marche" and dico["P12_Mot3"] == "en marche":
            Mot3.configure(text = "M3 est alimenté par Tank 3")



        elif dico["P11_Mot3"] != "en marche" and dico["P12_Mot3"] != "en marche":
            if (dico["P12_Mot1"] == "en marche") and dico["Van13"] == "ouverte" and dico["Tank 1"] == "plein":
                dico["Mot3"] = "Tank 1"
                Mot3.configure(text = "M3 est alimenté par Tank 1")
            elif (dico["P12_Mot2"] == "en marche") and dico["Van23"] == "ouverte" and dico["Tank 2"] == "plein":
                dico["Mot3"] = "Tank 2"
                Mot3.configure(text = "M3 est alimenté par Tank 2")
            else:
                dico["Mot3"] = ""
                Mot3.configure(text = "M3 est alimenté par")
                
    elif dico["Tank 3"] != "plein":
        if (dico["P12_Mot1"] == "en marche") and dico["Van13"] == "ouverte" and dico["Tank 1"] == "plein":
            dico["Mot3"] = "Tank 1"
            Mot3.configure(text = "M3 est alimenté par Tank 1")
        elif (dico["P12_Mot2"] == "en marche") and dico["Van23"] == "ouverte" and dico["Tank 2"] == "plein":
            dico["Mot3"] = "Tank 2"
            Mot3.configure(text = "M3 est alimenté par Tank 2")
        else:
            dico["Mot3"] = ""
            Mot3.configure(text = "M3 est alimenté par")
    

def Simulation():
    """Permet de lancer la simulation ou au moins un reservoir se vide et des pompes qui tobment en panne"""
    "global start"
    global  dico 
    global  Tank_1, Tank_2, Tank_3
    global P11_Mot1, P11_Mot2, P11_Mot3, P12_Mot1, P12_Mot2, P12_Mot3

    "start = time.time()"
    BoutSimul.configure(state= "disabled")
    Tanks = ["Tank 1" , "Tank 2", "Tank 3"]
    Pepom = ["P11_Mot1" , "P12_Mot1", 'P11_Mot2', "P12_Mot2", "P11_Mot3", "P12_Mot3"]
    temptank = rd.choice(Tanks)
    temppepom = rd.choices(Pepom, k=3)

    dico[temptank] = "vide"
    if temptank == "Tank 1":
        Tank_1.configure(text="Tank 1 vide")
    elif temptank == "Tank 2":
        Tank_2.configure(text="Tank 2 vide")
    elif temptank == "Tank 3":
        Tank_3.configure(text="Tank 3 vide")
    

    dico[temppepom[0]] = "en panne"

    for i in range(3):
        if temppepom[i] == "P11_Mot1":
            P11_Mot1.configure(text = "La pompe P11 du moteur 1 est en panne")
            dico["P11_Mot1"] = "en panne"
        elif temppepom[i] == "P11_Mot2":
            P11_Mot2.configure(text = "La pompe P11 du moteur 2 est en panne")
            dico["P11_Mot2"] = "en panne"
        elif temppepom[i] == "P11_Mot3":
            P11_Mot3.configure(text = "La pompe P11 du moteur 3 est en panne")
            dico["P11_Mot3"] = "en panne"
        elif temppepom[i] == "P12_Mot1":
            P12_Mot1.configure(text = "La pompe P12 du moteur 1 est en panne")
            dico["P12_Mot1"] = "en panne"
        elif temppepom[i] == "P12_Mot2":
            P12_Mot2.configure(text = "La pompe P12 du moteur 2 est en panne")
            dico["P12_Mot2"] = "en panne"
        elif temppepom[i] == "P12_Mot3":
            P12_Mot3.configure(text = "La pompe P12 du moteur 3 est en panne")
            dico["P12_Mot3"] = "en panne"
    action()




def tableau_bord():
    '''Création du tableau de bord'''
    global frame_main, dico, BoutSimul

    frame_main = tk.Frame(racine, bg=couleur_bg)

    tk.Label(
        frame_main, text="Tableau de bord", bg=couleur_bg, fg=couleur_fg,
        font=('Yu Gothic', '40', 'underline'), relief='flat', pady=80
    ).grid(row=0, column=0, columnspan= 5)

    tk.Button(
        frame_main, command = functVT12,
        text="VT12", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=0, sticky = 'n', columnspan = 3, padx= 60)

    tk.Button(
        frame_main, command=functVT23,
        text="VT23", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=2, sticky = 'n', columnspan = 2)

    tk.Button(
        frame_main, command=functP12,
        text="P12", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=0, padx= 30, pady= 30 )

    tk.Button(
        frame_main, command=functP22,
        text="P22", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=1, columnspan = 2, padx= 30, pady= 30)
    
    tk.Button(
        frame_main, command=functP32,
        text="P32", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=3, columnspan = 2, padx= 30, pady= 30)

    tk.Button(
        frame_main, command=functV12,
        text="V12", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=0, padx= 30)
    
    tk.Button(
        frame_main, command=functV13,
        text="V13", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=1, columnspan = 2, padx= 30)
    
    tk.Button(
        frame_main, command=functV23,
        text="V23", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=3, columnspan = 2, padx= 30)
    
    tk.Button(
        frame_main, command=placevidange,
        text="Vidange", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=('bold', 20), bd=bouton_bd, relief=bouton_relief
    ).grid(row=4, column=0, sticky = 'n',  pady= 20)

    tk.Button(
        frame_main, command=placepanne,
        text="Panne P", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=('bold', 20), bd=bouton_bd, relief=bouton_relief
    ).grid(row=4, column=1, sticky = 'n', columnspan = 2, pady= 20)

    BoutSimul = tk.Button(
        frame_main, command=Simulation,
        text="Simulation", bg=couleur_bg, fg="#F73910",
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=('bold', 20), bd=bouton_bd, relief=bouton_relief,
    )
    BoutSimul.grid(row=4, column=3, sticky = 'n', columnspan = 2, pady= 20)

    frame_main.grid(row=0, column=0)
    
#Creation de l'interface graphique#

def etat_sys():
    '''Création de l'interface de l'etat du système'''
    global frame_titre, Tank_1, Tank_2, Tank_3, Mot1, Mot2, Mot3
    global P11_Mot1, P12_Mot1, P11_Mot2, P12_Mot2, P11_Mot3, P12_Mot3
    global VanT12, VanT23, Van12, Van13, Van23
    frame_titre = tk.Frame(racine, bg=couleur_bg)
    frame_reserv = tk.LabelFrame(frame_titre, text = 'Réservoirs:', bg=couleur_bg, fg = couleur_fg, font= font)
    frame_mot = tk.LabelFrame(frame_titre, text = 'Moteurs:', bg=couleur_bg, fg = couleur_fg, font= font)
    frames_pompes = tk.LabelFrame(frame_titre, text = 'Pompes:', bg=couleur_bg, fg = couleur_fg, font= font)
    frame_vannes = tk.LabelFrame(frame_titre, text = 'Vannes:', bg=couleur_bg, fg = couleur_fg, font= font)


    tk.Label(
        frame_titre, text="État du système", bg=couleur_bg, fg=couleur_fg,
        font=('Yu Gothic', '30', 'underline'), relief='flat', pady=40
    ).grid(row=0, column=0, columnspan= 2)

    Tank_1 = tk.Label(
        frame_reserv, text =("Tank 1 plein"), bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Tank_1.grid(row=1, column=0)


    Tank_2 = tk.Label(
        frame_reserv, text ='Tank 2 plein', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Tank_2.grid(row=2, column=0)

    Tank_3 = tk.Label(
        frame_reserv, text ='Tank 3 plein', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Tank_3.grid(row=3, column=0)

    Mot1 = tk.Label(
        frame_mot, text ='M1 est alimenté par Tank 1', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Mot1.grid(row=1, column=0)

    Mot2 = tk.Label(
        frame_mot, text ='M2 est alimenté par Tank 2', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Mot2.grid(row=2, column=0)

    Mot3 = tk.Label(
        frame_mot, text ='M3 est alimenté par Tank 3', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Mot3.grid(row=3, column=0)

    P11_Mot1 = tk.Label(
        frames_pompes, text ='La pompe P11 du moteur 1 est en marche', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P11_Mot1.grid(row=1, column=0)

    P12_Mot1 = tk.Label(
        frames_pompes, text ="La pompe P12 du moteur 1 est à l'arret", bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P12_Mot1.grid(row=2, column=0)

    P11_Mot2 = tk.Label(
        frames_pompes, text ='La pompe P11 du moteur 2 est en marche', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P11_Mot2.grid(row=3, column=0)

    P12_Mot2=tk.Label(
        frames_pompes, text ="La pompe P12 du moteur 2 est à l'arret", bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P12_Mot2.grid(row=4, column=0)

    P11_Mot3 = tk.Label(
        frames_pompes, text ="La pompe P11 du moteur 3 est en marche", bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P11_Mot3.grid(row=5, column=0)

    P12_Mot3 = tk.Label(
        frames_pompes, text ="La pompe P12 du moteur 3 est à l'arret", bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    P12_Mot3.grid(row=6, column=0)

    VanT12 = tk.Label(
        frame_vannes, text ='La vanne VT12 est ouverte', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    VanT12.grid(row=1, column=0)
    
    VanT23 = tk.Label(
        frame_vannes, text ="La vanne VT23 est ouverte", bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    VanT23.grid(row=2, column=0)

    Van12 = tk.Label(
        frame_vannes, text ='La vanne V12 est fermée', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Van12.grid(row=3, column=0)

    Van13 = tk.Label(
        frame_vannes, text ='La vanne V13 est fermée', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Van13.grid(row=4, column=0)

    Van23 = tk.Label(
        frame_vannes, text ='La vanne V23 est fermée', bg = couleur_bg, fg = couleur_fg,
        font=('Yu Gothic', '15'), relief='flat'
    )
    Van23.grid(row=5, column=0)


    frame_titre.grid(row=0, column=1)
    frame_reserv.grid(row = 1, column= 0)
    frame_mot.grid(row = 1, column = 1)
    frames_pompes.grid(row = 2, column=0,padx = 10)
    frame_vannes.grid(row = 2, column = 1, pady = 20)



def vidange():
    '''Création du menu vidange'''
    global frame_vidange
    frame_vidange = tk.LabelFrame(racine, text="Vidange des moteurs", bg=couleur_bg, fg=couleur_fg, font=font)

    tk.Button(
        frame_vidange, command=functank1,
        text="Tank 1", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=0)

    tk.Button(
        frame_vidange, command=functank2,
        text="Tank 2", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=0)

    tk.Button(
        frame_vidange, command=functank3,
        text="Tank 3", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=0)

    tk.Button(
        frame_vidange, command=reprendrevidange,
        text="Retour", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=4, column=0,padx=100)

    frame_vidange.tkraise()



def placevidange():
    "Place le menu pour vidanger"
    frame_vidange.grid(row=0, column=0)
    action()

def reprendrevidange():
    '''Quitte le menu vidange'''
    frame_vidange.grid_forget()
    action()

def panne():
    '''Création du menu vidange'''
    global frame_panne
    frame_panne = tk.LabelFrame(racine, text="Panne des pompes", bg=couleur_bg, fg=couleur_fg, font=font)

    tk.Button(
        frame_panne, command=functP11_Mot1,
        text="Pompe 11 Moteur 1", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=0)

    tk.Button(
        frame_panne, command=functP12_Mot1,
        text="Pompe 12 Moteur 1", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=0)

    tk.Button(
        frame_panne, command=functP11_Mot2,
        text="Pompe 11 Moteur 2", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=0)

    tk.Button(
        frame_panne, command=functP12_Mot2,
        text="Pompe 12 Moteur 2", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=4, column=0)

    tk.Button(
        frame_panne, command=functP11_Mot3,
        text="Pompe 11 Moteur 3", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=5, column=0)

    tk.Button(
        frame_panne, command=functP12_Mot3,
        text="Pompe 12 Moteur 3", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=6, column=0)

    tk.Button(
        frame_panne, command=reprendrepanne,
        text="Retour", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=7, column=0,)

    frame_panne.tkraise()

def placepanne():
    "Place le menu des pannes"
    frame_panne.grid(row=0, column=0)
    action()

def reprendrepanne():
    '''Quitte le menu panne'''
    frame_panne.grid_forget()
    action()


#Appel des fonctions#

racine = tk.Tk()
racine.title("Projet Avion")


Canevas = tk.Canvas(racine, width=Longueur, height=Hauteur, bg=couleur_bg, bd=0, cursor = "gobbler")
Canevas.grid(row=0, column=0)
Canevas_2 = tk.Canvas(racine, width=Longueur, height=Hauteur, bg=couleur_bg, bd=0)
Canevas_2.grid(row=0, column=1)


Cla.creer_dico()
tableau_bord()
etat_sys()
vidange()
panne()                                         

"""if dico["Mot1"] != "" and dico["Mot2"] != "" and dico["Mot3"] != "": 
        stop = time.time()"""

racine.mainloop()

def fichierscore():
    """
    Fonction génératrice de fichier de score
    """
    i = 1 #Variable du compteur et utile pour la numération des position des scores
    if os.path.isfile("score.txt") == False:
        fichierscore = open("score.txt","x")
        fichierscore.write("#############Top 10 des Scores#############" + "\n")
        while i < 11:
            fichierscore.write(str(i) + ": Score: 0" + "\n")
            i += 1
        fichierscore.close()
    
def ecriscore():
    """
    Fonction qui a pour but d'écrire le score dans un document .txt et de l'organiser.
    """
    global sc

    preced = 0 #variable qui va sauvegarder la valeur du score précédent à la position
    current = 0 #Inibiteur pour empécher d'avoir que le score qu'on vient d'avoir
    fichierscore()  #Pour lancer la fonction génératrice de fichier de score 
    fichieroriginal = open("score.txt","r") #Texte de score original
    
    ligne = fichieroriginal.readline()
    
    ecrirescore = open("score.txt","w")
    ecrirescore.write("#############Top 10 des Scores#############" + "\n")
    
    
    for ligne in fichieroriginal:
        mots = ligne.split()
        if int(mots[2]) < sc:
            #La ligne que on vérifie a un score inférieur à celui qu'on viens d'avoir
            if current == 0 :
                preced = mots[2]
                mots[2] = sc
                ecrirescore.write(mots[0] + " " + mots[1] + " " + str(mots[2]) + "\n")
                current = 1
            elif current == 1 :
                ecrirescore.write(mots[0] + " " + mots[1] + " " + str(preced) + "\n")
                preced = mots[2]
        elif int(mots[2]) == sc or int(mots[2]) > sc:
            ecrirescore.write(mots[0] + " " + mots[1] + " " + str(mots[2]) + "\n")
    fichieroriginal.close()
    ecrirescore.close()


"""print("Temps de la simulation", round(start - stop))"""