from tkinter import*
from random import*
from tkinter import messagebox


cases1=[ [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0]]


cases2=[ [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0],
        [0, 0, 0,0, 0, 0,0,0, 0, 0]]


selection = True
mode = True
clic = True
q = 0
z = 0
n = 1
h = 0

t0 = True
t1 = True
t2 = True
t3 = True
t4 = True
t5 = True
t6 = True
t7 = True
t8 = True
t9 = True

bouton_jouer = None
bouton_blanchir = None


def binder() : #programme qui permet d'obliger le clic sur le plateau de gauche ou droite
    
    global clic
    if clic :
        plateau1.unbind('<Button-1>') #enleve l'execution du programme core sur le plateau1
        plateau2.bind('<Button-1>', core)#configure éxécution programme core sur plateau 2
        clic = not(clic)
        
    
    else :
        plateau2.unbind('<Button-1>')#enlève l'éxécution du programme core sur le plateau2
        plateau1.bind('<Button-1>', core)#configure éxécution programme core sur plateau 2
        clic = not(clic)



def orientation(): #programme qui gère l'orientation des bateaux
    
    global z
    global q
    z = 0
    q = 0
    w=messagebox.askyesno("Orientation du bateau","Verticale ? Cliquez oui sinon Cliquez non") #message box verticale ou horizontale
    if w :
        z = 1
        q = 0
    else :
        z = 0
        q = 1

        

def erreur(): #programme qui affiche une erreur dans le canvas "message"
    
    message.configure(text='emplacement indisponible')


def core(event) : #programme principal qui réagit à chaque clic
    
    global cases1, cases2, n, mode, selection, h, bouton_blanchir
    
    l = (event.y)//50     #converti les coordonnée du clic en valeur qui correspond au nombre de case        
    c = (event.x)//50                   

    if mode : #si mode est vrai alors le programme place les batteaux 
            
        if (n < 11) : # empeche de demander l'orientation du bateau si n=11 à la fin du programme 
            orientation()
        
        if (n == 1) and (cases1[l][c] == 0) : #en fonction du n, le programme place différents bateaux + vérification si la case sélectionnée est occupée donc [l][c] > 0
            if (z == 1) and (l == 9) : #vérification si la place necessaire est ok
                erreur()
            elif (q == 1) and (c == 9) : #vérification si la place necessaire est ok
                erreur()
            else:
                cases1[l][c] += 1 # affecte à [l][c] une valeure
                cases1[l+(1*z)][c+(1*q)] += 1 # affecte aux autres cases [l][c] qui correspond au reste des case qui composent le bateau  une valeure
                verifinterne()
                if (h == 0) :
                    
                    if (z == 1):
                        plateau1.create_image(50*c+25, 50*l+50,image=voiliervertical) #fait apparaitre l'image en vertical
                        plateau1.pack()
                    else :
                        plateau1.create_image(50*c+50, 50*l+25,image=voilierhorizontal)#fait apparaitre l'image en horizontal
                        plateau1.pack() 
                    n += 1
                    message.configure(text='joueur gauche placez torpilleur 1 ')
                
                else :  #en cas de détection d'une case qui est déjà occupée affiche erreur() et enlève la valeure attribuée aux cases 
                    erreur()
                    cases1[l][c] -= 1
                    cases1[l+(1*z)][c+(1*q)] -= 1
            
        elif (n == 2) and (cases1[l][c] == 0) : #même schéma de programme répétée autant de fois que de bateaux
            if (z == 1) and (l == 8) :
                erreur()
            elif (q == 1) and (c == 8) :
                erreur()
            else:
                cases1[l][c] += 2
                cases1[l+(1*z)][c+(1*q)] += 2
                cases1[l+(2*z)][c+(2*q)] += 2
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau1.create_image(50*c+25, 50*l+75,image=torpilleurvertical)
                        plateau1.pack()
                    else :
                        plateau1.create_image(50*c+75, 50*l+25,image=torpilleurhorizontal)
                        plateau1.pack()
                        
                    n += 1
                    message.configure(text='joueur gauche placez torpilleur 2')
                else :
                    erreur()
                    cases1[l][c] -= 2
                    cases1[l+(1*z)][c+(1*q)] -= 2
                    cases1[l+(2*z)][c+(2*q)] -= 2
        
        elif (n == 3) and (cases1[l][c] == 0) :
            if (z == 1) and (l == 8) :
                erreur()
            elif (q == 1) and (c == 8) :
                erreur()
            else:
                cases1[l][c] += 3
                cases1[l+(1*z)][c+(1*q)] += 3
                cases1[l+(2*z)][c+(2*q)] += 3
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau1.create_image(50*c+25, 50*l+75,image=torpilleurvertical)
                        plateau1.pack()
                    else :
                        plateau1.create_image(50*c+75, 50*l+25,image=torpilleurhorizontal)
                        plateau1.pack()
                    n += 1
                    message.configure(text='joueur gauche placez sous-marin')
                else :
                    erreur()
                    cases1[l][c] -= 3
                    cases1[l+(1*z)][c+(1*q)] -= 3
                    cases1[l+(2*z)][c+(2*q)] -= 3
            
        elif (n == 4) and (cases1[l][c] == 0) :
            if (z == 1) and (l == 7) :
                erreur()
            elif (q == 1) and (c == 7) :
                erreur()
            else:
                cases1[l][c] += 4
                cases1[l+(1*z)][c+(1*q)] += 4
                cases1[l+(2*z)][c+(2*q)] += 4
                cases1[l+(3*z)][c+(3*q)] += 4
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau1.create_image(50*c+25, 50*l+100,image=sousmarinvertical)
                        plateau1.pack()
                    else :
                        plateau1.create_image(50*c+100, 50*l+25,image=sousmarinhorizontal)
                        plateau1.pack()
                    n += 1
                    message.configure(text='joueur gauche placez porte-avion ')
                else :
                    erreur()
                    cases1[l][c] -= 4
                    cases1[l+(1*z)][c+(1*q)] -= 4
                    cases1[l+(2*z)][c+(2*q)] -= 4
                    cases1[l+(3*z)][c+(3*q)] -= 4
        
        elif (n == 5) and (cases1[l][c] == 0) :
            if (z == 1) and (l == 6) :
                erreur()
            elif (q == 1) and (c == 6) :
                erreur()
            else:
                cases1[l][c] += 5
                cases1[l+(1*z)][c+(1*q)] += 5
                cases1[l+(2*z)][c+(2*q)] += 5
                cases1[l+(3*z)][c+(3*q)] += 5
                cases1[l+(4*z)][c+(4*q)] += 5
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau1.create_image(50*c+25, 50*l+125,image=porteavionvertical)
                        plateau1.pack()
                    else :
                        plateau1.create_image(50*c+125, 50*l+25,image=porteavionhorizontal)
                        plateau1.pack()
                    n += 1
                    message.configure(text='BLANCHISSEZ') #blanchissement demandé
                    binder()
                    bouton_blanchir = Button(fen1, text='! BLANCHIR !', command=construction4, borderwidth=3, relief='raised') #clréation du couton de blanchissement
                    bouton_blanchir.pack(pady=10) #décalage sur y
                    bouton_blanchir.configure(font=("Times New Roman", 20)) #police du bouton
                    plateau2.unbind('<Button-1>') #desaffectation de commande de core en clic sur plateau 2
                else :
                    erreur()
                    cases1[l][c] -= 5
                    cases1[l+(1*z)][c+(1*q)] -= 5
                    cases1[l+(2*z)][c+(2*q)] -= 5
                    cases1[l+(3*z)][c+(3*q)] -= 5
                    cases1[l+(4*z)][c+(4*q)] -= 5
        
        elif (n == 6) and (cases2[l][c] == 0) :
            if (z == 1) and (l == 9) :
                erreur()
            elif (q == 1) and (c == 9) :
                erreur()
            else:
                cases2[l][c] += 1
                cases2[l+(1*z)][c+(1*q)] += 1
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau2.create_image(50*c+25, 50*l+50,image=voiliervertical)
                        plateau2.pack()
                    else :
                        plateau2.create_image(50*c+50, 50*l+25,image=voilierhorizontal)
                        plateau2.pack() 
                    n += 1
                    message.configure(text='joueur droit placez torpilleur 1 ')
                else :
                    erreur()
                    cases2[l][c] -= 1
                    cases2[l+(1*z)][c+(1*q)] -= 1
                    
        elif (n == 7) and (cases2[l][c] == 0) :
            if (z == 1) and (l == 8) :
                erreur()
            elif (q == 1) and (c == 8) :
                erreur()
            else:
                cases2[l][c] += 2
                cases2[l+(1*z)][c+(1*q)] += 2
                cases2[l+(2*z)][c+(2*q)] += 2
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau2.create_image(50*c+25, 50*l+75,image=torpilleurvertical)
                        plateau2.pack()
                    else :
                        plateau2.create_image(50*c+75, 50*l+25,image=torpilleurhorizontal)
                        plateau2.pack()
                        
                    n += 1
                    message.configure(text='joueur droit placez torpilleur 2')
                else :
                    erreur()
                    cases2[l][c] -= 2
                    cases2[l+(1*z)][c+(1*q)] -= 2
                    cases2[l+(2*z)][c+(2*q)] -= 2
                    
        elif (n == 8) and (cases2[l][c] == 0) :
            if (z == 1) and (l == 8) :
                erreur()
            elif (q == 1) and (c == 8) :
                erreur()
            else:
                cases2[l][c] += 3
                cases2[l+(1*z)][c+(1*q)] += 3
                cases2[l+(2*z)][c+(2*q)] += 3
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau2.create_image(50*c+25, 50*l+75,image=torpilleurvertical)
                        plateau2.pack()
                    else :
                        plateau2.create_image(50*c+75, 50*l+25,image=torpilleurhorizontal)
                        plateau2.pack()
                    n += 1
                    message.configure(text='joueur droit placez sous-marin')
                else :
                    erreur()
                    cases2[l][c] -= 3
                    cases2[l+(1*z)][c+(1*q)] -= 3
                    cases2[l+(2*z)][c+(2*q)] -= 3
                    
        elif (n == 9) and (cases2[l][c] == 0) :
            if (z == 1) and (l == 7) :
                erreur()
            elif (q == 1) and (c == 7) :
                erreur()
            else:
                cases2[l][c] += 4
                cases2[l+(1*z)][c+(1*q)] += 4
                cases2[l+(2*z)][c+(2*q)] += 4
                cases2[l+(3*z)][c+(3*q)] += 4
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau2.create_image(50*c+25, 50*l+100,image=sousmarinvertical)
                        plateau2.pack()
                    else :
                        plateau2.create_image(50*c+100, 50*l+25,image=sousmarinhorizontal)
                        plateau2.pack()
                    n += 1
                    message.configure(text='joueur droit placez porte-avion ')
                else :
                    erreur()
                    cases2[l][c] -= 4
                    cases2[l+(1*z)][c+(1*q)] -= 4
                    cases2[l+(2*z)][c+(2*q)] -= 4
                    cases2[l+(3*z)][c+(3*q)] -= 4
                    
        elif (n == 10) and (cases2[l][c] == 0) :
            if (z == 1) and (l == 6) :
                erreur()
            elif (q == 1) and (c == 6) :
                erreur()
            else:
                cases2[l][c] += 5
                cases2[l+(1*z)][c+(1*q)] += 5
                cases2[l+(2*z)][c+(2*q)] += 5
                cases2[l+(3*z)][c+(3*q)] += 5
                cases2[l+(4*z)][c+(4*q)] += 5
                verifinterne()
                if (h == 0) :
                    if (z == 1):
                        plateau2.create_image(50*c+25, 50*l+125,image=porteavionvertical)
                        plateau2.pack()
                    else :
                        plateau2.create_image(50*c+125, 50*l+25,image=porteavionhorizontal)
                        plateau2.pack()
                    n += 1      
                    message.configure(text='BLANCHISSEZ')                 
                    mode = not(mode) #passe en mode pour le tir de missiles
                    binder()
                    bouton_blanchir = Button(fen1, text='! BLANCHIR !', command=construction5, borderwidth=3, relief='raised')
                    bouton_blanchir.pack(pady=10)
                    bouton_blanchir.configure(font=("Times New Roman", 20))
                    plateau1.unbind('<Button-1>')
                else :
                    erreur()
                    cases2[l][c] -= 5
                    cases2[l+(1*z)][c+(1*q)] -= 5
                    cases2[l+(2*z)][c+(2*q)] -= 5
                    cases2[l+(3*z)][c+(3*q)] -= 5
                    cases2[l+(4*z)][c+(4*q)] -= 5
        
        
            
            
    
    else :
        if selection : #permet d'inerverser les joueurs 
            plateau2.configure(cursor='target') #change le curseur
            plateau1.configure(cursor='exchange') #change le curseur
            if (cases1[l][c] >= 1):
                plateau1.create_image(50*c+25, 50*l+25,image=boum) 
                plateau1.pack()
                cases1[l][c] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='joueur gauche TIREZ !')
                couler()

            elif (cases1[l][c] == 0) :
                plateau1.create_image(50*c+25, 50*l+25,image=plouf)
                plateau1.pack()
                cases1[l][c] = -1
                message1.configure(text='RATE')
                message.configure(text='joueur gauche TIREZ !')
                
            else  : #affiche erreur et relance l'action si case deja cliquée 
                selection = not(selection)
                message1.configure(text='! DEJA BOMBARDEE !')
                binder()
                plateau1.configure(cursor='target') #change le curseur
                plateau2.configure(cursor='exchange') #change le curseur

            selection = not(selection)
            verif()
            binder()
        
        else :
            plateau1.configure(cursor='target')
            plateau2.configure(cursor='exchange')
            if (cases2[l][c] >= 1):
                plateau2.create_image(50*c+25, 50*l+25,image=boum)
                plateau2.pack()
                cases2[l][c] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='joueur droit TIREZ !')
                couler()
            
            elif (cases2[l][c] == 0) :
                plateau2.create_image(50*c+25, 50*l+25,image=plouf)
                plateau2.pack()
                cases2[l][c] = -1
                message1.configure(text='RATE')
                message.configure(text='joueur droit TIREZ !')
                
            else  :
                selection = not(selection)
                message1.configure(text='! DEJA BOMBARDEE !')
                binder()
                plateau2.configure(cursor='target') #change le curseur
                plateau1.configure(cursor='exchange') #change le curseur
            
            selection = not(selection)
            verif()            
            binder()
    
def verifinterne(): #programme de vérification pour qu'aucuns bateaux ne s'empilent
    
    global h
    global n
    h = 0
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] > 1) and n==1 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] > 2) and n==2 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] > 3) and n==3 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] > 4) and n==4 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] > 5) and n==5 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] > 1) and n==6 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] > 2) and n==7 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] > 3) and n==8 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] > 4) and n==9 :
                h = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] > 5) and n==10 :
                h = 1

def verif(): #programme de vérification de fin de jeu par un joueur 
    
    global mode
    verif1 = True
    verif2 = True
    i = 1
    j = 1
    for i in range (10) : #verifie si il reste une case avec une valeur >= 1 qui veut dire qu'il reste un bateau ou un bout de bateau
        for j in range (10) :
            if (cases1[i][j] >= 1) :
                verif1 = False
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] >= 1) :
                verif2 = False
    
    if verif1 : #affiche le gagnant
        message.configure(text='joueur droit a GAGNE !')
        message1.configure(text='FIN',font=("Times New Roman", 16))
        mode = not(mode)
        messagebox.showinfo("FIN DU GAME", "Selectionner REJOUER ou QUITTER")

        
    if verif2 : #affiche le gagnant
        message.configure(text='joueur gauche a GAGNE !')
        message1.configure(text='! FIN !',font=("Times New Roman", 16))
        mode = not(mode)
        messagebox.showinfo("FIN DU GAME", "Selectionner REJOUER ou QUITTER")
        

def couler(): #verifie si un bateau vient de couler
    
    touchercouler0 = 0
    touchercouler1 = 0
    touchercouler2 = 0
    touchercouler3 = 0
    touchercouler4 = 0
    touchercouler5 = 0
    touchercouler6 = 0
    touchercouler7 = 0
    touchercouler8 = 0
    touchercouler9 = 0
    global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9
    i = 1
    j = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] == 1) :
                touchercouler0 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] == 1) :
                touchercouler1 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] == 2) :
                touchercouler2 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] == 2) :
                touchercouler3 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] == 3) :
                touchercouler4 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] == 3) :
                touchercouler5 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] == 4) :
                touchercouler6 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] == 4) :
                touchercouler7 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases1[i][j] == 5) :
                touchercouler8 = 1
    for i in range (10) :
        for j in range (10) :
            if (cases2[i][j] == 5) :
                touchercouler9 = 1
    if touchercouler0 == 0 and t0: #empeche de dire deux fois q'un même bateau à couler
        message1.configure(text='TOUCHE COULE')
        t0 = False
    if touchercouler1 == 0 and t1 :
        message1.configure(text='TOUCHE COULE')
        t1 = False
    if touchercouler2 == 0 and t2 :
        message1.configure(text='TOUCHE COULE')
        t2 = False
    if touchercouler3 == 0 and t3 :
        message1.configure(text='TOUCHE COULE')
        t3 = False
    if touchercouler4 == 0 and t4 :
        message1.configure(text='TOUCHE COULE')
        t4 = False
    if touchercouler5 == 0 and t5 :
        message1.configure(text='TOUCHE COULE')
        t5 = False
    if touchercouler6 == 0 and t6 :
        message1.configure(text='TOUCHE COULE')
        t6 = False
    if touchercouler7 == 0 and t7 :
        message1.configure(text='TOUCHE COULE')
        t7 = False
    if touchercouler8 == 0 and t8 :
        message1.configure(text='TOUCHE COULE')
        t8 = False
    if touchercouler9 == 0 and t9 :
        message1.configure(text='TOUCHE COULE')
        t9 = False

def construction(): #programme de création du quadrillage et du background du quadrillage

    plateau1.create_image(250,250,image=bgingamecan1)
    
    plateau2.create_image(260,265,image=bgingamecan2)
    
    for i in range(0,10): #création quadrillage plateau 1
        plateau1.create_line(0+50*i,0,0+50*i,502, fil='white' ,width=3)
        plateau1.create_line(0,0+50*i,502,0+50*i, fil='white' ,width=3)

                
    for j in range(0,10): #création quadrillage plateau 2
        plateau2.create_line(0+50*j,0,0+50*j,502, fil='white' ,width=3)
        plateau2.create_line(0,0+50*j,502,0+50*j, fil='white' ,width=3)
    
def construction2(): #programme qui sert à commencer la partie, enleve le bouton destroy, change curseur et lien avec le clic, et affiche message 
    bouton_jouer.destroy()
    plateau1.bind('<Button-1>', core)
    plateau1.configure(cursor='target')
    message.configure(text='joueur droit TIREZ !')

def construction3(): #sert à relancer le jeu, rappel le jeu et detruit l'ancien
    global cases1, cases2,n, z, h, q, t0, t1, t2, t3,t4, t5, t6, t7, t8, t9, bouton_action, bouton_blanchir, selection, mode, clic
    for i in range(10): 
        for j in range(10):
            cases1[i][j]=0
    
    for i in range(10): 
        for j in range(10):
            cases2[i][j]=0
    construction()
    
    selection = True
    mode = True
    clic = True
    
    q = 0
    z = 0
    n = 1
    h = 0

    t0 = True
    t1 = True
    t2 = True
    t3 = True
    t4 = True
    t5 = True
    t6 = True
    t7 = True
    t8 = True
    t9 = True

    plateau1.bind('<Button-1>', core)
    plateau1.configure(cursor='boat')
    message.configure(text='joueur gauche placez voilier !')
    message1.configure(text="Et c'est reparti pour un tour !")
    bouton_blanchir.destroy()
    
def construction4(): #programme qui fait la transition entre le blanchissement et le bouton commencer 
    global bouton_blanchir
    bouton_blanchir.destroy()
    construction()
    plateau2.bind('<Button-1>', core)
    message.configure(text='joueur droit placez voilier')

def construction5(): #programme qui blanchis un plateau et qui reconstruit une grille
    global bouton_blanchir, bouton_jouer
    bouton_blanchir.destroy()
    construction()
    message.configure(text='configuration terminée')
    message1.configure(text='COMMENCEZ')
    bouton_jouer = Button(fen1, text='! COMMENCER !', command=construction2, borderwidth=3, relief='raised')
    bouton_jouer.pack(pady=10)
    bouton_jouer.configure(font=("Times New Roman", 20))



    
fen1 = Tk() #création fenetre 
fen1.title('Plateau de jeu') #titre fenetre
fen1.geometry("1500x700+200+150") #taille fenetre
bgingame = PhotoImage(file='bgingamenormal.png') #définition de l'image du background
background_label = Label(fen1, image=bgingame) #creation du background
background_label.place(x=0, y=0, relwidth=1, relheight=1) #placement du background
plateau1 = Canvas(fen1,bg='white', height=500, width=500, cursor='boat') #création canvas 1
plateau1.pack(side=LEFT, padx = 25) #place canvas1
plateau2 = Canvas(fen1,bg='white', height=500, width=500, cursor='boat') #création canvas2
plateau2.pack(side=RIGHT,padx = 25) #place canvas2
messageboxcanvas = Canvas(fen1,bg='black') #création canvas qui contient les messages
messageboxcanvas.pack(side=TOP) #placement messagebox
quitbox = Canvas(fen1) #création canvas des boutons 
quitbox.pack(side=BOTTOM) #placement canvas des bouton


#définition de toutes les images
bgingamecan1=PhotoImage(file="bgingamecan1.png")
bgingamecan2=PhotoImage(file="bgingamecan2.png")
voilierhorizontal=PhotoImage(file="voilierhorizontal.png")
torpilleurhorizontal=PhotoImage(file="torpilleurhorizontal.png")
sousmarinhorizontal=PhotoImage(file="sous-marinhorizontal.png")
porteavionhorizontal=PhotoImage(file="porte-avionhorizontal.png")
voiliervertical=PhotoImage(file="voiliervertical.png")
torpilleurvertical=PhotoImage(file="torpilleurvertical.png")
sousmarinvertical=PhotoImage(file="sous-marinvertical.png")
porteavionvertical=PhotoImage(file="porte-avionvertical.png")
boum=PhotoImage(file="boum.png")
plouf=PhotoImage(file="plouf.png")

#défnition de message dans le canvas
message=Label(messageboxcanvas,width=30, text='joueur gauche placez voilier ', bg="black")
message.pack(fill=X)
message.configure(font=("Times New Roman", 16), foreground='white')
#défnition de message dans le canvas
message1=Label(messageboxcanvas, text='', bg="black")
message1.pack(fill=X)
message1.configure(font=("Times New Roman", 14), foreground='white')
#création des boutons, design et placement
bouton_quitter = Button(quitbox, text='Quitter ',width=15, command=fen1.destroy, borderwidth=3, relief='raised')
bouton_quitter.pack(side=LEFT, fill=X)
bouton_quitter.configure(font=("Times New Roman", 16))
bouton_rejouer = Button(quitbox, text='Rejouer',width=15, command=construction3, borderwidth=3, relief='raised')
bouton_rejouer.pack(side= RIGHT, fill=X)
bouton_rejouer.configure(font=("Times New Roman", 16))

construction()


plateau1.bind('<Button-1>', core)




fen1.mainloop()
