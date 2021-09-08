import random

roles = {0: "pierre", 1: "papier", 2: "ciseaux", 3: "lezard", 4: "spock"}
go = True

while(go is True):
    print("0. Pierre, 1. papier, 2. ciseaux, 3. lezard, 4. spock ?")
    choix = int(input("Entrer le chiffre : "))

    if isinstance(choix, int) and 0 <= choix and choix < 5:
        ordi = random.choice([ele for ele in roles.keys() if ele != choix])
        print("Votre choix :", roles[choix])
        print("L'ordi a joué", roles[ordi])

        true_table = ([
        # 0=lose, 1=win, 2=draw.

            [2,0,1,1,0], #Lizard
            [1,2,0,1,0], #Paper
            [0,1,2,0,1], #Rock
            [0,0,1,2,1], #Scissors
            [1,1,0,0,2]  #Spock
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
