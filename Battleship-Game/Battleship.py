from tkinter import *
import os, sys, subprocess

def regle(): #lance les regles
    global bouton_quit_regles
    background_label = Label(Battleship, image=regles)#creation du background
    background_label.place(x=0, y=0, relwidth=1, relheight=1)#placement du background
    bouton_quit_regles = Button(Battleship,width=15,bg="white" ,height= 1, text='Retour menu', command=quit_regles, borderwidth=4, relief='raised')
    bouton_quit_regles.pack(side=TOP, pady=30)
    bouton_quit_regles.configure(font=("Times New Roman", 25))
    
def quit_regles():
    global bouton_quit_regles
    bouton_quit_regles.destroy()
    construction()

def jeu():
    global bouton_1vsordi, bouton_1vs1,bouton_classique ,bouton_difficile
    bouton_1vs1 = Button(Battleship,width=15,bg="white" ,height= 2, text='1 VS 1', command=jeu1vs1, borderwidth=9, relief='raised')
    bouton_1vs1.pack(side=LEFT, padx=190, anchor=S, pady=250)
    bouton_1vs1.configure(font=("Times New Roman", 30))
    bouton_1vsordi = Button(Battleship,width=15,bg="white" ,height= 2, text='1 VS ORDI', command=jeuIA, borderwidth=9, relief='raised')
    bouton_1vsordi.pack(side=LEFT, padx=0, anchor=S, pady=250)
    bouton_1vsordi.configure(font=("Times New Roman", 30))
    bouton_classique.destroy()
    bouton_difficile.destroy()

def jeu1vs1(): #lance le jeu
    global bouton_1vsordi, bouton_1vs1,bouton_classique ,bouton_difficile
    bouton_1vsordi.destroy()
    bouton_1vs1.destroy()
    bouton_classique = Button(Battleship,width=15,bg="white" ,height= 2, text='CLASSIQUE', command=classique, borderwidth=9, relief='raised')
    bouton_classique.pack(side=LEFT, padx=225, anchor=S, pady=250)
    bouton_classique.configure(font=("Times New Roman", 25))
    bouton_difficile = Button(Battleship,width=15,bg="white" ,height= 2, text='DIFFICLE', command=difficile, borderwidth=9, relief='raised')
    bouton_difficile.pack(side=LEFT, padx=0, anchor=S, pady=250)
    bouton_difficile.configure(font=("Times New Roman", 25))

def classique(): #lance le jeu
    if sys.platform == "win32":
            os.startfile('battleshipcoreclassique.bat')
    else:
        subprocess.call(["/Applications/Python 3.7/Python Launcher.app", "battleshipcoreclassique.py"])

def difficile(): #lance le jeu
    if sys.platform == "win32":
            os.startfile('battleshipcoredifficile.bat')
    else:
        subprocess.call(["/Applications/Python 3.7/Python Launcher.app", "battleshipcoredifficile.py"])

def jeuIA(): #lance le jeu
    if sys.platform == "win32":
            os.startfile('battlsehipcoreIA.bat')
    else:
        subprocess.call(["/Applications/Python 3.7/Python Launcher.app", "battleshipcoreIA.py"])
        
def construction():
    background_label = Label(Battleship, image=bg1)#creation du background
    background_label.place(x=0, y=0, relwidth=1, relheight=1)#placement du background
    bouton_quitter = Button(Battleship,bg="white" ,width=18 ,height= 2, text='Quitter', command=Battleship.destroy,borderwidth=5)#création du bouton quitter
    bouton_quitter.place(x=808, y=580)#placement du bouton
    bouton_quitter.configure(font=("Times New Roman", 20,))
    bouton_regle = Button(Battleship,width=18,bg="white" , height= 2, text='Régles',command=regle,borderwidth=5)#création du bouton régle
    bouton_regle.place(x=492, y=580)#placement du bouton
    bouton_regle.configure(font=("Times New Roman", 20, ))
    bouton_jouer = Button(Battleship,width=18,bg="white" ,height= 2, text='Jouer',relief='raised' , command=jeu, borderwidth=5)#création du bouton jouer
    bouton_jouer.place(x=176, y=580)#placement du bouton
    bouton_jouer.configure(font=("Times New Roman", 20))

Battleship = Tk() #création fenétre
Battleship.title("Battleship") #titre fenetre
Battleship.geometry("1280x720+200+150") #taille fenetre
bg1 = PhotoImage(file='bg1.png') #définition de l'image du background
regles = PhotoImage(file='regles.png') #contient l'image avec les règles

construction()
Battleship.mainloop()
