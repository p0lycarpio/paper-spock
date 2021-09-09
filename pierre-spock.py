import random

roles = {0: "pierre", 1: "papier", 2: "ciseaux", 3: "lezard", 4: "spock"}

while(1):
    print("0. Pierre, 1. papier, 2. ciseaux, 3. lezard, 4. spock ?")
    
    try:
        choix = int(input("Entrer le chiffre : "))
    except:
        print('Votre valeur n\'est pas un entier\n')
    else:
        if 0 <= choix and choix < 5:
            ordi = random.choice([ele for ele in roles.keys() if ele != choix])
            print("Votre choix :", roles[choix])
            print("L'ordi a joué", roles[ordi])

            true_table = ([
            # 0=lose, 1=win, 2=draw.

                [2,0,1,1,0], #Rock
                [1,2,0,0,1], #Paper          
                [0,1,2,1,0], #Scissors
                [0,1,0,2,1], #Lizard
                [1,0,1,0,2] #Spock
            ])


            process = true_table[choix][ordi]

            if process == 0:
                print(" > Vous avez perdu\n")
            elif process == 1:
                print(" > Vous avez gagné\n")
            else:
                print(" > Égalité\n")
        else:
            print(f"{choix} n'est pas un objet existant du jeu.\n")
