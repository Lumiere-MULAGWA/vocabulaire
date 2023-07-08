from os import system, listdir, remove

from random import randint

def lecture():
    
    rep=()
    
    while rep!="0" and rep!=0:
        
        # système de choix de la fiche
        system("cls")
        print("\n\n\t\tBIENVENUE DANS LE MODE LECTURE")
        print("\n\t\tQUELLE FICHE VOULEZ-VOUS TRAVAILLER ?")
        fiches = listdir("fiches")
        print()
        for i in range(len(fiches)):
            print("\t\t" + str(i+1), "-\t", fiches[i][0:-4])
        print("\n\t\t0 -\tretour au menu")
        rep=input("\n\n\t\tRéponse : - ")
        
        try: rep = int(rep)
        except:pass
            
        # affiche la liste
        if type(rep)==int:
            if rep !=0 and (rep<=len(fiches)):
                
                
                
                # importe le contenu du fichier
                chaine = 'fiches/'+fiches[rep-1]
                with open(chaine, "r") as fic:
                    content = fic.readlines()
                    for i in range(len(content)):
                        content[i]=content[i][0:-1]
                
                # crée le dictionnaire des mots étrangers / mots français
                traductions = {}
                for i in range(int(len(content)/2)):
                    traductions[content[i*2]] = content[i*2+1]
                    
                # crée le dictionnaire des scores
                scores = {}
                for i in range(int(len(content)/2)):
                    scores[content[i*2]] = 0
                
                
                refaire_le_même_mot = False
                
                bonnes_reps = 0
                mauvaises_reps = 0
                
                nombres_de_mots_par_lignées = len(traductions)*10
                # pour la lignée de mots
                lignée = []
                
                # mode récitation
                reponse=()
                while reponse!="0":
                    
                    
                    system('cls')
                    
                    
                    # si il y a trop de réponses dans la lignée
                    if len(lignée) > nombres_de_mots_par_lignées :
                        lignée.pop(0)
                    
                    nbr_lignée_B_R = 0
                    nbr_lignée_M_R = 0
                    for i in lignée :
                        if i:
                            nbr_lignée_B_R +=1
                        elif not i:
                            nbr_lignée_M_R +=1
                    
                    
                    
                    try : pourcentage_lignée = nbr_lignée_B_R*100/(nbr_lignée_M_R+nbr_lignée_B_R)
                    except ZeroDivisionError : pourcentage_lignée = 50
                    
                    try : pourcentage = bonnes_reps*100/(mauvaises_reps+bonnes_reps)
                    except ZeroDivisionError : pourcentage = 50
                    
                    
                    # affiche l'interface
                    
                    #print(traductions)
                    #print(scores)
                    print("\n\n\t\tMODE LECTURE, 0 POUR QUITTER")
                    print("\t\tLISTE : \"", fiches[rep-1][0:-4],"\"   POURCENTAGE TOTAL =",round(pourcentage,2),"%",", POURCENTAGE RECENT =",round(pourcentage_lignée,2),"%\n")
                    
                    if refaire_le_même_mot == False:
                    
                        # une chance sur trois de faire réciter le mot que l'on connait le moins
                        if randint(1,2)==1:
                            #print("\t\tQUESTION VISEE")
                            # mot_français = mot ayant le moins de score
                            liste_scores = list(scores.items())
                            plus_petit = liste_scores[0][1]
                            mot_étranger = liste_scores[0][0]
                            place = 0
                            for rang in range(len(liste_scores)):
                                if liste_scores[rang][1] < plus_petit:
                                    plus_petit = liste_scores[rang][1]
                                    mot_étranger = liste_scores[rang][0]
                                    place = rang
                        
                        else :
                            liste_scores = list(scores.items())
                            
                            place = randint(0,len(liste_scores)-1)
                            
                            plus_petit = liste_scores[place][1]
                            mot_étranger = liste_scores[place][0]
                        
                        
                    
                    
                    #print("mot le plus faible :",mot_étranger, place)
                        
                    
                    # tuple mots étranger/français
                    mot_français = list(traductions.items())[place][1]
                    
                    #print("mot le plus faible :",mot_étranger, mot_français)
                    
                    # demande la traduction
                    print("\n\t\tDONNEZ LA TRADUCTION DE :",mot_français)
                    
                    reponse = input("\n\n\t\tRéponse : - ")
                    
                    # si la réponse est juste
                    if reponse == mot_étranger:
                        #input("\t\tBRAVO")
                        scores[mot_étranger] = scores[mot_étranger]+0.5
                        refaire_le_même_mot = False
                        bonnes_reps +=1
                        lignée.append(True)
                    
                    # si elle est fausse
                    elif reponse != mot_étranger and reponse != "0":
                        print("\t\tRATE LA TRADUCTION ETAIT :", mot_étranger)
                        input("\t\t")
                        scores[mot_étranger] = scores[mot_étranger]-1
                        refaire_le_même_mot = True
                        mauvaises_reps += 1
                        lignée.append(False)
                    
                    







def visionner():
    
    rep=()
    
    while rep!="0" and rep!=0:
        
        # système de choix de la fiche
        system("cls")
        print("\n\n\t\tBIENVENUE DANS LA GESTION DES FICHES")
        print("\n\t\tQUELLE FICHE VOULEZ-VOUS GERER ?")
        fiches = listdir("fiches")
        print()
        for i in range(len(fiches)):
            print("\t\t" + str(i+1), "-\t", fiches[i][0:-4])
        print("\n\t\t0 -\tretour au menu")
        rep=input("\n\n\t\tRéponse : - ")
        
        try: rep = int(rep)
        except:pass
            
            # affiche la liste
        if type(rep)==int:
            if rep !=0 and (rep<=len(fiches)):
                nom_liste = fiches[rep-1]
                chaine = "fiches/"+nom_liste
                
                # récupère le contenu
                with open(chaine, "r") as fic:
                    content = fic.readlines()
                    
                    system("cls")
        
                    print("\n\n\t\tMODE VISION")
                    print("\n\t\tLISTE :", fiches[rep-1][0:-4],"\n")
                    
                    # affiche le contenus
                    for i in range(int(len(content)/2)):
                        print("\t\t",content[int(i*2)][0:-1], " - ",content[int(i*2)+1][0:-1])
                
                print("\n\t\tSUPPRIMER LA LISTE ?")
                print("\n\t\t1 - OUI")
                print("\n\t\t2 - NON")
                reponse_suppr=input("\n\n\t\tRéponse : - ")
                
                if reponse_suppr.lower()=="oui" or reponse_suppr=="1":
                    remove(chaine)
                    print("\n\t\tLA LISTE A BIEN ETE SUPPRIMEE")
                
                else: print("\n\t\tLA LISTE N'A PAS ETE SUPPRIMEE")
                
                input()



def modifier_liste():
    
    rep = ()
    
    while rep!=0:
    
        system("cls")
        
        print("\n\n\t\tMODE MODIFIER")
        print("\n\t\tQUELLE LISTE VOULEZ-VOUS MODIFIER ?")
        
        # AFFICHE LES LISTES
        liste_fiches = listdir("fiches")
        print()
        for i in range(len(liste_fiches)):
            chaine = "\t\t" + str(i + 1) + " - \t" + liste_fiches[i][0:-4]
            print(chaine)
        print("\n\t\t0 - \tRetour au menu")
        rep = input("\n\t\tRéponse : - ")
        
        # affiche la liste demandée
        try : rep = int(rep)
        except ValueError : pass
        if rep!=0 and type(rep) == int:
            
            system("cls")
        
            print("\n\n\t\tMODE MODIFIER")
            print("\n\t\tLISTE :", liste_fiches[rep-1][0:-4],"\n")
            
            nom_fiche=liste_fiches[rep-1]
            
            # affiche la liste
            chaine = "fiches/" + liste_fiches[rep-1]
            with open(chaine, "r") as fic:
                content = fic.readlines()
                for i in range(len(content)):
                    print("\t\t\t",content[int(i)][0:-1])
                    if i%2==1 : print()
                    
            
            print("\n\t\t1 -\tMODIFIER UN MOT")
            print("\t\t2 -\tSUPPRIMER UN MOT")
            print("\t\t3 -\tAJOUTER UN MOT")
            print("\n\t\t0 -\tRETOUR")
            
            rep=input("\n\n\t\tRéponse : - ")
            
            # Si on modifie
            if rep=="1":
                
                question_remodifier="1"
                    
                while question_remodifier=="1":
                
                    system("cls")
                    print("\n\n\t\tMODE MODIFIER")
                    print("\n\t\tQUEL MOT VOULEZ-VOUS MODIFIER ?")
                    
                    # affiche la liste
                    chaine = "fiches/" + nom_fiche
                    with open(chaine, "r") as fic:
                        content = fic.readlines()
                        for i in range(len(content)):
                            print("\t\t",i+1,"\t",content[int(i)][0:-1])
                            if i%2==1 : print()
                    
                    # demande par quoi remplacer
                    rep=input("\n\n\t\tRéponse : - ")
                    print("\n\t\tPAR QUEL MOT VOULEZ-VOUS REMPLACER", content[int(rep)-1][0:-1], "?")
                    nouveau_mot=input("\n\n\t\tRéponse : - ")
                    content[int(rep)-1] = nouveau_mot+"\n"
                    
                    # écrit dans le fichier
                    with open(chaine, "w") as fic :
                        for i in content :
                            fic.write(i)
                    print("\n\t\tLE MOT A ETE REMPLACE PAR :", nouveau_mot)
                    print("\n\t\tVOULEZ VOUS ENCORE MODIFIER UN ELEMENT ?")
                    print("\n\t\t1 -\tOUI")
                    print("\t\t2 -\tNON")
                    
                    question_remodifier=input("\n\n\t\tRéponse : - ")
            
            
            # Si on supprime
            elif rep=="2":
                
                question_resupprimer="1"
                    
                while question_resupprimer=="1":
                    
                    system("cls")
                    print("\n\n\t\tMODE SUPPRIMER")
                    print("\n\t\tQUEL MOT VOULEZ-VOUS SUPPRIMER ?")
                    
                    # affiche la liste
                    chaine = "fiches/" + nom_fiche
                    with open(chaine, "r") as fic:
                        content = fic.readlines()
                        for i in range(len(content)):
                            if i%2==0 :
                                print("\t\t",int(i/2)+1,"\t",content[int(i)][0:-1])
                            elif i%2==1 :
                                print("\t\t","\t",content[int(i)][0:-1])
                                print()
                    
                    # quoi supprimer -1 , *2
                    rep=input("\n\n\t\tRéponse : - ")
                    print("\n\t\tLA SUPRESSION DE :",content[(int(rep)-1)*2][0:-1],"/",content[((int(rep)-1)*2)+1][0:-1], "A ETE REUSSI")
                    
                    # suppression
                    content.remove(content[(int(rep)-1)*2])
                    content.remove(content[(int(rep)-1)*2])
                    
                    # écrit dans le fichier
                    with open(chaine, "w") as fic :
                        for i in content :
                            fic.write(i)
                    
                    
                    # supprimmer autre chose ?
                    print("\n\t\tVOULEZ VOUS ENCORE SUPPRIMER UN ELEMENT ?")
                    print("\n\t\t1 -\tOUI")
                    print("\t\t2 -\tNON")
                    
                    question_resupprimer=input("\n\n\t\tRéponse : - ")
            
            
            # Si on ajoute
            elif rep=="3":
                
                question_reajouter="1"
                    
                while question_reajouter=="1":
                    
                    system("cls")
                    print("\n\n\t\tMODE AJOUTER")
                    print("\n\t\tQUEL MOT VOULEZ-VOUS AJOUTER ?")
                    
                    
                    
                    # mot étranger
                    print("\n\t\tENTREZ LE MOT ETRANGER :")
                    mot_étranger = input("\n\t\t\t- ")
                    
                    while len(mot_étranger)==0:
                        print("\n\t\tMOT ETRANGER NON VALIDE:")
                        print("\t\tENTREZ LE MOT ETRANGER :")
                        mot_étranger = input("\n\t\t\t- ")
                    
                    # mot français
                    print("\n\t\tENTREZ LE MOT FRANCAIS :")
                    mot_français = input("\n\t\t\t- ")
                    
                    while len(mot_français)==0:
                        print("\n\t\tMOT FRANCAIS NON VALIDE:")
                        print("\t\tENTREZ LE MOT FRANCAIS :")
                        mot_français = input("\n\t\t\t- ")
                    
                    # recuperons le contenu du fichier
                    with open(chaine, "r") as fic :
                        content = fic.readlines()
                    
                    # il reste a enregistrer
                    mot_étranger += "\n"
                    mot_français += "\n"
                    content.append(mot_étranger)
                    content.append(mot_français)
                    with open(chaine, "w") as fic :
                        for i in content :
                            fic.write(i)
                    
                    # ajouter autre chose ?
                    print("\n\t\tVOULEZ VOUS ENCORE AJOUTER UN ELEMENT ?")
                    print("\n\t\t1 -\tOUI")
                    print("\t\t2 -\tNON")
                    
                    question_reajouter=input("\n\n\t\tRéponse : - ")





def créer_liste():
    system("cls")
    
    print("\n\n\t\tMODE ECRITURE")
    print("\n\t\tENTREZ LE NOM DE LA LISTE")
    
    
    # verifie que le nom de la liste est valide
    caractères_interdits = ["/","\\",":","*","?","\"","<",">","|"]
    
    nom_valide = False
    
    while nom_valide == False :
        
        nom_valide = True
        
        nom_liste=input("\n\t\t\t- ")
        nom_liste_txt = nom_liste+".txt"
            
        for i in range(len(nom_liste)):
            
            if nom_liste[i] in caractères_interdits:
                print("\tLE NOM DE LA LISTE NE DOIS PAS CONTENIR : /,\,:,*,?,\",>,<,|")
                nom_valide = False
        
        if nom_liste_txt in listdir("fiches"):
            print("\tLA LISTE EST DEJA EXISTANTE")
            nom_valide = False
        
        if len(nom_liste) == 0:
            print("\tNOM DE LA LISTE INVALIDE")
            nom_valide = False
            
        if nom_valide != False : nom_valide = True
    
    
    # écriture
    mot_étranger=()
    mot_français=()
    
    mots_étrangers = []
    mots_français = []
    
    while mot_étranger!="0" and mot_français!="0":
        
        mot_étranger=()
        mot_français=()
        
        system("cls")
        print("\n\n\t\tMODE ECRITURE, 0 POUR STOPPER")
        
        # mot étranger
        print("\n\t\tENTREZ LE MOT ETRANGER :")
        mot_étranger = input("\n\t\t\t- ")
        
        while len(mot_étranger)==0:
            print("\n\t\tMOT ETRANGER NON VALIDE:")
            print("\t\tENTREZ LE MOT ETRANGER :")
            mot_étranger = input("\n\t\t\t- ")
        
        # mot français
        print("\n\t\tENTREZ LE MOT FRANCAIS :")
        mot_français = input("\n\t\t\t- ")
        
        while len(mot_français)==0:
            print("\n\t\tMOT FRANCAIS NON VALIDE:")
            print("\t\tENTREZ LE MOT FRANCAIS :")
            mot_français = input("\n\t\t\t- ")
        
        # ajoute à la liste
        if mot_étranger!="0" and mot_français!="0" :
            
            mots_étrangers.append(mot_étranger)
            mots_français.append(mot_français)
    
    
    # enregistrement
    system("cls")
    print("\n\n\t\tMODE ECRITURE, OUI POUR ENREGISTRER")
    print("\n\t\tVOULEZ-VOUS ENREGISTRER :", nom_liste,"?")
    rep=input("\n\t\t\t- ")
    
    if len(mots_étrangers) == 0:
        print("\n\t\tLA LISTE N'A PAS ETE ENREGISTREE, CAR ELLE EST VIDE")
        rep=input("\n\t\t\t")
    
    # enregistrer
    elif rep.lower()=="oui":
        
        nom_fiche = nom_liste + ".txt"
        nom_chemin = "fiches/"+nom_fiche
        
        # crée le fichier
        with open(nom_chemin, "a") as fic: pass
        
        # écriture dans le fichier
        with open(nom_chemin, "w") as fic:
            for i in range(len(mots_étrangers)):
                
                chaine_mot_étranger = mots_étrangers[i] + "\n"
                fic.write(chaine_mot_étranger)
                
                chaine_mot_français = mots_français[i] + "\n"
                fic.write(chaine_mot_français)
        
        print("\n\t\tLA LISTE A BIEN ETE ENREGISTREE")
        rep=input("\n\t\t\t")
    
    # ne pas enregistrer
    else :
        print("\n\t\tLA LISTE N'A PAS ETE ENREGISTREE")
        rep=input("\n\t\t\t")




def écriture():
    
    rep=()
    
    while rep!="0":
        
        system("cls")
        
        print("\n\n\t\tBIENVENUE L'ECRITURE")
        print("\n\t\tQUE VOULEZ-VOUS FAIRE ?")
        print("\n\n\t\t1 -\tcréer une fiche de vocabulaire")
        print("\n\t\t2 -\tmodifier une fiche deja éxistante")
        print("\n\t\t0 -\tretour au menu")

        rep=input("\n\n\t\tRéponse : - ")
        
        if rep=="1":créer_liste()
        if rep=="2":modifier_liste()




def changer_fond():
    
    
    rep=()
    
    while rep!="0":
        
        with open("variables.txt","r") as fic :
        
            content = fic.readlines()
            couleur_texte = content[0][0]
            couleur_fond = content[1][0]
        
        system("cls")
    
        print("\n\n\t\tBIENVENUE DANS LES REGLAGES - CHANGER LE FOND")
        print("\n\t\tQUELLE COULEUR ?")
        
        print("\n\n\t\t1 -\tNOIR\t\t9 -\tGRIS")
        print("\t\t2 -\tBLEU\t\t10 -\tBLEU CLAIR")
        print("\t\t3 -\tVERT\t\t11 -\tVERT CLAIR")
        print("\t\t4 -\tBLEU-GRIS\t12 -\tCYAN")
        print("\t\t5 -\tROUGE\t\t13 -\tROUGE CLAIR")
        print("\t\t6 -\tVIOLET\t\t14 -\tVIOLET CLAIR")
        print("\t\t7 -\tJAUNE\t\t15 -\tJAUNE CLAIR")
        print("\t\t8 -\tBLANC\t\t16 -\tBLANC BRILLANT")
        
        print("\n\t\t0 -\tretour aux réglages")

        rep=input("\n\n\t\tRéponse : - ")
        
        if rep=="0":break
        
        if rep=="1":color =  "0"
        elif rep=="2":color =  "1"
        elif rep=="3":color =  "2"
        elif rep=="4":color =  "3"
        elif rep=="5":color =  "4"
        elif rep=="6":color =  "5"
        elif rep=="7":color =  "6"
        elif rep=="8":color =  "7"
        elif rep=="9":color =  "8"
        elif rep=="10":color =  "9"
        elif rep=="11":color =  "A"
        elif rep=="12":color =  "B"
        elif rep=="13":color =  "C"
        elif rep=="14":color =  "D"
        elif rep=="15":color =  "E"
        elif rep=="16":color =  "F"
        
        chaine = "color "+color+str(couleur_texte)
        system(chaine)
        
        
        with open("variables.txt","w") as fic :
        
            fic.write(couleur_texte)
            fic.write("\n")
            fic.write(color)





def changer_texte():
    
    
        
    
    rep=()
    
    while rep!="0":
        
        
        with open("variables.txt","r") as fic :
        
            content = fic.readlines()
            couleur_texte = content[0][0]
            couleur_fond = content[1][0]
            
        system("cls")
    
        print("\n\n\t\tBIENVENUE DANS LES REGLAGES - CHANGER LE TEXTE")
        print("\n\t\tQUELLE COULEUR ?")
        
        print("\n\n\t\t1 -\tNOIR\t\t9 -\tGRIS")
        print("\t\t2 -\tBLEU\t\t10 -\tBLEU CLAIR")
        print("\t\t3 -\tVERT\t\t11 -\tVERT CLAIR")
        print("\t\t4 -\tBLEU-GRIS\t12 -\tCYAN")
        print("\t\t5 -\tROUGE\t\t13 -\tROUGE CLAIR")
        print("\t\t6 -\tVIOLET\t\t14 -\tVIOLET CLAIR")
        print("\t\t7 -\tJAUNE\t\t15 -\tJAUNE CLAIR")
        print("\t\t8 -\tBLANC\t\t16 -\tBLANC BRILLANT")
        
        print("\n\t\t0 -\tretour aux réglages")

        rep=input("\n\n\t\tRéponse : - ")
        
        if rep=="0":break
        
        if rep=="1":color =  "0"
        elif rep=="2":color =  "1"
        elif rep=="3":color =  "2"
        elif rep=="4":color =  "3"
        elif rep=="5":color =  "4"
        elif rep=="6":color =  "5"
        elif rep=="7":color =  "6"
        elif rep=="8":color =  "7"
        elif rep=="9":color =  "8"
        elif rep=="10":color =  "9"
        elif rep=="11":color =  "A"
        elif rep=="12":color =  "B"
        elif rep=="13":color =  "C"
        elif rep=="14":color =  "D"
        elif rep=="15":color =  "E"
        elif rep=="16":color =  "F"
        
        chaine = "color "+str(couleur_fond)+color
        system(chaine)
        
        
        with open("variables.txt","w") as fic :
        
            fic.write(color)
            fic.write("\n")
            fic.write(couleur_fond)





def réglages():
    
    rep=()
    
    while rep!="0":
        
        system("cls")
        
        print("\n\n\t\tBIENVENUE DANS LES REGLAGES")
        print("\n\t\tQUE VOULEZ-VOUS FAIRE ?")
        print("\n\n\t\t1 -\tmodifier la couleur du texte")
        print("\n\t\t2 -\tmodifier la couleur du fond")
        print("\n\t\t0 -\tretour au menu")

        rep=input("\n\n\t\tRéponse : - ")

        
        if rep=="1": changer_texte()    
        elif rep=="2": changer_fond()


# actualise les couleurs
with open("variables.txt","r") as fic :
        
    content = fic.readlines()
    couleur_texte = content[0][0]
    couleur_fond = content[1][0]
    chaine = "color "+couleur_fond+couleur_texte
    system(chaine)


rep = str()

# boucle principale
while rep!="0":
    
    system("cls")
    
    print("\n\n\t\tBIENVENUE SUR LE REVISEUR DE VOCABULAIRE")
    print("\n\t\tQUE VOULEZ-VOUS FAIRE ?")
    print("\n\n\t\t1 -\tfaire réciter du vocaulaire")
    print("\n\t\t2 -\técrire / modifier du vocabulaire")
    print("\n\t\t3 -\tgérer les listes")
    print("\n\t\t4 -\tréglages")
    print("\n\t\t0 -\tquitter")

    rep=input("\n\n\t\tRéponse : - ")
    
    if rep=="4": réglages()
    
    elif rep=="2" : écriture()
    
    elif rep=="3" : visionner()
    
    elif rep=="1" : lecture()
