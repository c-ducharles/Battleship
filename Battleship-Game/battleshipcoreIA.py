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

cIA=[]
lIA=[]
ram = 0
raml = 0
ramc = 0
oraml = 0
oramc = 0
q = 0
z = 0
n = 1
h = 0
a = 0
a = randint(1,2)

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
bouton_action = None
bouton_placerIA = None



def orientation(): #programme qui gère l'orientation des bateaux en manuel
    
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

def orientationIA(): #programme qui gère l'orientation des bateaux en automtique
    global z
    global q
    w = randint(0,1)
    if w == 1 :
        z = 1
        q = 0
    elif w == 0:
        z = 0
        q = 1

        

def erreur(): #programme qui affiche une erreur dans le canvas "message"
    
    message.configure(text='! Emplacement Indisponible !')
    message1.configure (text='RAPPEL : NE PAS COLLER')
    
    
def blockaround():  #programme qui gère le blocage des cases autour des bateaux 
    for l in range (10) : #en gros le programme cherche une case avec un bateaux et met toutes les cases autour à -10
        for c in range (10) :
            if (cases1[l][c] > 0) :
                if (l-1 > -1) and (cases1[l-1][c] == 0) : 
                    cases1[l-1][c] = -10
                    
                if (l+1 < 10) and (cases1[l+1][c] == 0) :
                    cases1[l+1][c] = -10
                    
                if (c-1 > -1) and (cases1[l][c-1] == 0 ) :
                    cases1[l][c-1] = -10
                
                if (c+1 < 10) and (cases1[l][c+1] == 0) :
                    cases1[l][c+1] = -10
                
                if (l+1 < 10) and (c+1 < 10) and(cases1[l+1][c+1] == 0) :
                    cases1[l+1][c+1] = -10
                
                if (l-1 > -1) and (c-1 > -1) and(cases1[l-1][c-1] == 0) :
                    cases1[l-1][c-1] = -10

                if (l+1 < 10) and (c-1 > -1) and(cases1[l+1][c-1] == 0) :
                    cases1[l+1][c-1] = -10
                
                if (l-1 > -1) and (c+1 < 10) and(cases1[l-1][c+1] == 0) :
                    cases1[l-1][c+1] = -10
                

                
    for l in range (10) : #il met une croix sur les cases à -10
        for c in range (10) :
            if (cases1[l][c] < -9) :
                plateau1.create_image(50*(c)+25, 50*(l)+25,image=croix)
                plateau1.pack()

def blockaroundIA(): #même programme que au dessus sauf que c'est pour le placement de l'IA
    for l in range (10) :
        for c in range (10) :
            if (cases2[l][c] > 0) :
                if (l-1 > -1) and (cases2[l-1][c] == 0) :
                    cases2[l-1][c] = -10
                    
                if (l+1 < 10) and (cases2[l+1][c] == 0) :
                    cases2[l+1][c] = -10
                    
                if (c-1 > -1) and (cases2[l][c-1] == 0 ) :
                    cases2[l][c-1] = -10
                
                if (c+1 < 10) and (cases2[l][c+1] == 0) :
                    cases2[l][c+1] = -10
                
                if (l+1 < 10) and (c+1 < 10) and(cases2[l+1][c+1] == 0) :
                    cases2[l+1][c+1] = -10
                
                if (l-1 > -1) and (c-1 > -1) and(cases2[l-1][c-1] == 0) :
                    cases2[l-1][c-1] = -10

                if (l+1 < 10) and (c-1 > -1) and(cases2[l+1][c-1] == 0) :
                    cases2[l+1][c-1] = -10
                
                if (l-1 > -1) and (c+1 < 10) and(cases2[l-1][c+1] == 0) :
                    cases2[l-1][c+1] = -10                
    
def placement(event) : #programme principal qui réagit à chaque clic
    
    global cases1, cases2, n, h, bouton_blanchir
    
    l = (event.y)//50     #converti les coordonnée du clic en valeur qui correspond au nombre de case        
    c = (event.x)//50                   
    if (n < 11) : # empeche de demander l'orientation du bateau si n=11 à la fin du programme 
        orientation()
    
    if (n == 1) and (cases1[l][c] < 1) : #en fonction du n, le programme place différents bateaux + vérification si la case sélectionnée est occupée donc [l][c] > 0
        if (z == 1) and (l == 9) : #vérification si la place necessaire est ok
            erreur()
        elif (q == 1) and (c == 9) : #vérification si la place necessaire est ok
            erreur()
        elif (cases1[l][c] < 0) : #verif que la case cliqué n'est pas à -10
            erreur()
        else:
            cases1[l][c] += 1 # affecte à [l][c] une valeure
            cases1[l+(1*z)][c+(1*q)] += 1 # affecte aux autres cases [l][c] qui correspond au reste des case qui composent le bateau  une valeure
            verifinterne() #vérifie que les cases sont disponibles et que les bateaux ne soient pas collés
            if (h == 0) :
                
                if (z == 1):
                    plateau1.create_image(50*c+25, 50*l+50,image=voiliervertical) #fait apparaitre l'image en vertical
                    plateau1.pack()
                else :
                    plateau1.create_image(50*c+50, 50*l+25,image=voilierhorizontal)#fait apparaitre l'image en horizontal
                    plateau1.pack() 
                n += 1
                blockaround()#programme qui vabloquer toutes las cases autour du bateau
                message.configure(text='HUMAIN placez torpilleur 1 ')
            
            else :  #en cas de détection d'une case qui est déjà occupée affiche erreur() et enlève la valeure attribuée aux cases 
                erreur()
                cases1[l][c] -= 1 #remet les cases comme à l'origine si la place n'était pas disponible
                cases1[l+(1*z)][c+(1*q)] -= 1
        
    elif (n == 2) and (cases1[l][c] < 1) : #même schéma de programme répétée autant de fois que de bateaux
        if (z == 1) and (l == 8) :
            erreur()
        elif (q == 1) and (c == 8) :
            erreur()
        elif (cases1[l][c] < 0) :
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
                blockaround()
                message.configure(text='HUMAIN placez torpilleur 2')
            else :
                erreur()
                cases1[l][c] -= 2
                cases1[l+(1*z)][c+(1*q)] -= 2
                cases1[l+(2*z)][c+(2*q)] -= 2
    
    elif (n == 3) and (cases1[l][c] < 1) :
        if (z == 1) and (l == 8) :
            erreur()
        elif (q == 1) and (c == 8) :
            erreur()
        elif (cases1[l][c] < 0) :
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
                blockaround()
                message.configure(text='HUMAIN placez sous-marin')
            else :
                erreur()
                cases1[l][c] -= 3
                cases1[l+(1*z)][c+(1*q)] -= 3
                cases1[l+(2*z)][c+(2*q)] -= 3
        
    elif (n == 4) and (cases1[l][c] < 1) :
        if (z == 1) and (l == 7) :
            erreur()
        elif (q == 1) and (c == 7) :
            erreur()
        elif (cases1[l][c] < 0) :
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
                blockaround()
                message.configure(text='HUMAIN placez porte-avion ')
            else :
                erreur()
                cases1[l][c] -= 4
                cases1[l+(1*z)][c+(1*q)] -= 4
                cases1[l+(2*z)][c+(2*q)] -= 4
                cases1[l+(3*z)][c+(3*q)] -= 4
    
    elif (n == 5) and (cases1[l][c] < 1) :
        if (z == 1) and (l == 6) :
            erreur()
        elif (q == 1) and (c == 6) :
            erreur()
        elif (cases1[l][c] < 0) :
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
                blockaround()
                message.configure(text='BLANCHISSEZ') #blanchissement demandé
                bouton_blanchir = Button(fen1, text='! BLANCHIR !', command=construction4, borderwidth=3, relief='raised') #création du bouton de blanchissement
                bouton_blanchir.pack(pady=40) #décalage sur y
                bouton_blanchir.configure(font=("Times New Roman", 20)) #police du bouton
                plateau1.unbind('<Button-1>') 
            else :
                erreur()
                cases1[l][c] -= 5
                cases1[l+(1*z)][c+(1*q)] -= 5
                cases1[l+(2*z)][c+(2*q)] -= 5
                cases1[l+(3*z)][c+(3*q)] -= 5
                cases1[l+(4*z)][c+(4*q)] -= 5

def placementIA(): #programme de placement des bateaux en automatique
    global cases1, cases2, n, h, bouton_blanchir,z,q
    if (n == 6):
        orientationIA()#décide si vertical ou horizontal en aléatoire
        l = randint(0,9-1*z) #donne les cases disponibles en aléatoire
        c = randint(0,9-1*q)
        cases2[l][c] += 1
        cases2[l+(1*z)][c+(1*q)] += 1
        verifinterne()  
        if (h == 0):
            if (z == 1):
                plateau2.create_image(50*c+25, 50*l+50,image=voiliervertical)
                plateau2.pack()
            else :
                plateau2.create_image(50*c+50, 50*l+25,image=voilierhorizontal)
                plateau2.pack() 
            n += 1
            blockaroundIA()

        else :
            cases2[l][c] -= 1
            cases2[l+(1*z)][c+(1*q)] -= 1
        
        placementIA()
        
                    
    elif (n == 7) :
        orientationIA()
        l = randint(0,9-2*z)
        c = randint(0,9-2*q)
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
            blockaroundIA()   
            n += 1

        else :
            cases2[l][c] -= 2
            cases2[l+(1*z)][c+(1*q)] -= 2
            cases2[l+(2*z)][c+(2*q)] -= 2
        placementIA()
                
    elif (n == 8) :
        orientationIA()
        l = randint(0,9-3*z)
        c = randint(0,9-3*q)
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
            blockaroundIA()
        else :
            cases2[l][c] -= 3
            cases2[l+(1*z)][c+(1*q)] -= 3
            cases2[l+(2*z)][c+(2*q)] -= 3
        placementIA()
                
    elif (n == 9) :
        orientationIA()
        l = randint(0,9-4*z)
        c = randint(0,9-4*q)
        cases2[l][c] += 4
        cases2[l+(1*z)][c+(1*q)] += 4
        cases2[l+(2*z)][c+(2*q)] += 4
        cases2[l+(3*z)][c+(3*q)] += 4
        verifinterne()
        if (h == 0) :
            if (z == 1) :
                plateau2.create_image(50*c+25, 50*l+100,image=sousmarinvertical)
                plateau2.pack()
            else :
                plateau2.create_image(50*c+100, 50*l+25,image=sousmarinhorizontal)
                plateau2.pack()
            n += 1
            blockaroundIA()
        else :
            cases2[l][c] -= 4
            cases2[l+(1*z)][c+(1*q)] -= 4
            cases2[l+(2*z)][c+(2*q)] -= 4
            cases2[l+(3*z)][c+(3*q)] -= 4
        placementIA()
        
    elif (n == 10):
        orientationIA()
        définitionaléatoire()
        l = randint(0,9-5*z)
        c = randint(0,9-5*q)
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
            blockaroundIA()

        else :
            cases2[l][c] -= 5
            cases2[l+(1*z)][c+(1*q)] -= 5
            cases2[l+(2*z)][c+(2*q)] -= 5
            cases2[l+(3*z)][c+(3*q)] -= 5
            cases2[l+(4*z)][c+(4*q)] -= 5
            placementIA()
            
def tir(event) : #programme qui gère le tir en manuel
    global cases1, cases2, n, h, bouton_blanchir
    l = (event.y)//50     #converti les coordonnée du clic en valeur qui correspond au nombre de case        
    c = (event.x)//50 
    plateau1.configure(cursor='target') #change le curseur
    plateau2.configure(cursor='exchange') #change le curseur
    if (cases2[l][c] >= 1): #si case avec un bateau 
        plateau2.create_image(50*c+25, 50*l+25,image=boum) 
        plateau2.pack()
        cases2[l][c] = -1
        message1.configure(text='TOUCHE')
        message.configure(text='ORDI TIREZ SUR HUMAIN !')
        couler()
        plateau2.unbind('<Button-1>')
        construction6()

    elif (cases2[l][c] == 0) or (cases2[l][c] == -10): #si case vide
        plateau2.create_image(50*c+25, 50*l+25,image=plouf)
        plateau2.pack()
        cases2[l][c] = -1
        message1.configure(text='RATE')
        message.configure(text='ORDI TIREZ SUR HUMAIN !')
        plateau2.unbind('<Button-1>')
        construction6()
        
    else  : #affiche erreur et relance l'action si case deja cliquée 
        message.configure(text='DEJA BOMBARDEE')
        plateau2.configure(cursor='target') #change le curseur
        plateau1.configure(cursor='exchange') #change le curseur
    
    verif()
    

def tirIA() : #programme qui gère le tir en automatique
    global cases1, cases2, bouton_action, lIA, cIA, ram, raml, ramc, oraml, oramc
    définitionaléatoire()
    l = choice(lIA)
    c = choice(cIA)
    plateau2.configure(cursor='target') #change le curseur
    plateau1.configure(cursor='exchange') #change le curseur
    if (ram == 1):
        if (raml != 9):    
            raml = raml + 1
            if (cases1[raml][ramc] >= 1):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=boum) 
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                couler()
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                
                
                

            elif (cases1[raml][ramc] == 0) or (cases1[raml][ramc] == -10):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=plouf)
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='RATE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                ram = 2
                raml = oraml
            else  : #affiche erreur et relance l'action si case deja cliquée 
                ram = 2
                raml = oraml
                tirIA()
        else:
            ram = 2
            raml = oraml
            tirIA()
        
    elif (ram == 2):
        if (raml != 0):
            raml = raml - 1
            if (cases1[raml][ramc] >= 1):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=boum) 
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                couler()
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                
                
                

            elif (cases1[raml][ramc] == 0) or (cases1[raml][ramc] == -10):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=plouf)
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='RATE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                ram = 3
                raml = oraml
                
            else  : #affiche erreur et relance l'action si case deja cliquée 
                ram = 3
                raml = oraml
                tirIA()
        else :
            ram = 3
            raml = oraml
            tirIA()
        
    elif (ram == 3):
        if (ramc != 9):
            ramc = ramc + 1
            if (cases1[raml][ramc] >= 1):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=boum) 
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                couler()
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                
                
                

            elif (cases1[raml][ramc] == 0) or (cases1[raml][ramc] == -10):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=plouf)
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='RATE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                ramc = oramc
                ram = 4
                
            else  : #affiche erreur et relance l'action si case deja cliquée 
                ram = 4
                tirIA()
        else :
            ram = 4
            ramc = oramc
            tirIA()
    elif (ram == 4):
        if (ramc != 0):
            ramc = ramc - 1
            if (cases1[raml][ramc] >= 1):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=boum) 
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='TOUCHE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                couler()
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                
                
                

            elif (cases1[raml][ramc] == 0) or (cases1[raml][ramc] == -10):
                plateau1.create_image(50*ramc+25, 50*raml+25,image=plouf)
                plateau1.pack()
                cases1[raml][ramc] = -1
                message1.configure(text='RATE')
                message.configure(text='HUMAIN TIREZ SUR ORDI !')
                bouton_action.destroy()
                plateau2.bind('<Button-1>', tir)
                
            else  : #affiche erreur et relance l'action si case deja cliquée 
                ram = 1
                tirIA()
        else:
            ram = 1
            ramc = oramc
            tirIA()
    
    elif (cases1[l][c] >= 1)and ram==0:
        plateau1.create_image(50*c+25, 50*l+25,image=boum) 
        plateau1.pack()
        cases1[l][c] = -1
        message1.configure(text='TOUCHE')
        message.configure(text='HUMAIN TIREZ SUR ORDI !')
        couler()
        bouton_action.destroy()
        plateau2.bind('<Button-1>', tir)
        ram = 1
        raml = l
        ramc = c
        oraml = l
        oramc = c
    elif (cases1[l][c] == 0) or (cases1[l][c] == -10):
        plateau1.create_image(50*c+25, 50*l+25,image=plouf)
        plateau1.pack()
        cases1[l][c] = -1
        message1.configure(text='RATE')
        message.configure(text='HUMAIN TIREZ SUR ORDI !')
        bouton_action.destroy()
        plateau2.bind('<Button-1>', tir)
        
    else  : #affiche erreur et relance l'action si case deja cliquée 
        tirIA()
    
    verif()
    
def définitionaléatoire():#décide dès le début si le quadrillage sera pair ou impair
    global lIA, cIA, a
    
    if a == 1 :
        b = randint(1,2)
        if b==1:
            lIA = [0,2,4,6,8]
            cIA = [1,3,5,7,9]
        else :
            lIA = [1,3,5,7,9]
            cIA = [0,2,4,6,8]
    else:
        b = randint(1,2)
        if b==1:
            lIA = [0,2,4,6,8]
            cIA = [0,2,4,6,8]
        else :
            lIA = [1,3,5,7,9]
            cIA = [1,3,5,7,9]
        

def verifinterne(): #programme de vérification pour qu'aucuns bateaux ne s'empilent ou se collent
    
    global h
    global n
    h = 0
    
    for i in range (10) : #vérifie que les bateaux ne se menntent pas sur les cases à -10
        for j in range (10) :
            if (cases1[i][j] > -10) and (cases1[i][j] < -4):
                h = 1
            if (cases2[i][j] > -10) and (cases2[i][j] < -4):
                h = 1
    for i in range (10) : #vérifie en fonction du n, que la case ne contienne pas deux bateaux 
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
        message.configure(text='ORDINATEUR A GAGNE !')
        message1.configure(text='! FIN !',font=("Times New Roman", 16))
        messagebox.showinfo("FIN DU GAME", "Selectionner REJOUER ou QUITTER")
        plateau2.unbind('<Button-1>')

        
    if verif2 : #affiche le gagnant
        message.configure(text='HUMAIN A GAGNER !')
        message1.configure(text='! FIN !',font=("Times New Roman", 16))
        messagebox.showinfo("FIN DU GAME", "Selectionner REJOUER ou QUITTER")
        plateau2.unbind('<Button-1>')

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
    
    global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, ram
    i = 1
    j = 1
    for i in range (10) : #vérifie que il ne reste plus un bateau 
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
        ram = 0
        t0 = False
    if touchercouler1 == 0 and t1 :
        message1.configure(text='TOUCHE COULE')
        
        t1 = False
    if touchercouler2 == 0 and t2 :
        message1.configure(text='TOUCHE COULE')
        ram = 0
        t2 = False
    if touchercouler3 == 0 and t3 :
        message1.configure(text='TOUCHE COULE')
        t3 = False
        
    if touchercouler4 == 0 and t4 :
        message1.configure(text='TOUCHE COULE')
        t4 = False
        ram = 0
    if touchercouler5 == 0 and t5 :
        message1.configure(text='TOUCHE COULE')
        t5 = False
    if touchercouler6 == 0 and t6 :
        message1.configure(text='TOUCHE COULE')
        t6 = False
        ram = 0
    if touchercouler7 == 0 and t7 :
        message1.configure(text='TOUCHE COULE')
        t7 = False
    if touchercouler8 == 0 and t8 :
        message1.configure(text='TOUCHE COULE')
        t8 = False
        ram = 0
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
    construction()
    plateau2.bind('<Button-1>', tir)
    plateau2.configure(cursor='target')
    plateau1.configure(cursor='exchange') 
    message.configure(text='HUMAIN TIREZ SUR ORDI !')

def construction3(): #sert à relancer le jeu
    global cases1, cases2,n, z, h, q, t0, t1, t2, t3,t4, t5, t6, t7, t8, t9, bouton_action, bouton_blanchir, bouton_placerIA, ram, raml, ramc, oraml, oramc, a
    for i in range(10): 
        for j in range(10):
            cases1[i][j]=0
    
    for i in range(10): 
        for j in range(10):
            cases2[i][j]=0
    construction()
    ram = 0
    raml = 0
    ramc = 0
    oraml = 0
    oramc = 0
    q = 0
    z = 0
    n = 1
    h = 0
    a = 0
    a = randint(1,2)

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
    
    plateau1.bind('<Button-1>', placement)
    plateau1.configure(cursor='boat')
    
    message.configure(text='HUMAIN placez voilier !')
    message1.configure(text="Et c'est reparti pour un tour !")
    bouton_blanchir.destroy()
    bouton_placerIA.destroy()
    bouton_action.destroy()
    
def construction4(): #programme qui fait la transition entre le blanchissement et le bouton commencer 
    global bouton_blanchir, bouton_placerIA
    bouton_blanchir.destroy()
    message.configure(text='ORDINATEUR PLACEZ LES BATEAUX !')
    message1.configure(text="Faites jouer l'ordinateur !")
    construction()
    bouton_placerIA = Button(fen1, text='! PLACER IA !', command=construction5, borderwidth=3, relief='raised')
    bouton_placerIA.pack(pady=40)
    bouton_placerIA.configure(font=("Times New Roman", 20))

def construction5():
    global bouton_jouer, bouton_placerIA
    bouton_placerIA.destroy()
    message.configure(text='TOUS LES BATEAUX ONT ETE PLACE')
    message1.configure(text="COMMENCEZ !")
    placementIA()
    construction()
    bouton_jouer = Button(fen1, text='! COMMENCER !', command=construction2, borderwidth=3, relief='raised')
    bouton_jouer.pack(pady=40)
    bouton_jouer.configure(font=("Times New Roman", 20))
    for i in range(0,10): 
        for j in range(0,10):
            plateau2.create_image(25+50*i, 25+50*j,image=interrogation)

def construction6(): #programme qui blanchis un plateau et qui reconstruit une grille
    global bouton_action
    bouton_action = Button(fen1, text='! ACTION ORDI !', command=tirIA, borderwidth=3, relief='raised')
    bouton_action.pack(pady=40)
    bouton_action.configure(font=("Times New Roman", 20))

    
fen1 = Tk() #création fenetre 
fen1.title('Plateau de jeu') #titre fenetre
fen1.geometry("1500x700+200+150") #taille fenetre
bgingame = PhotoImage(file='bgingame.png') #définition de l'image du background
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
interrogation=PhotoImage(file="interrogation.png")
croix=PhotoImage(file="croix.png")

#défnition de message dans le canvas
message=Label(messageboxcanvas,width=30, text='HUMAIN placez voilier !', bg="black")
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


plateau1.bind('<Button-1>', placement)




fen1.mainloop()
