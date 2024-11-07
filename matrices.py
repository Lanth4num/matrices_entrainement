import time
import os
import sys
import random

clear_scr = lambda: os.system('clear')
if sys.platform == "win32":
    clear_scr = lambda: os.system('cls')


clear_scr()
print("1- Apuyez sur le retour à la ligne pour commencer")
print("2- Calculez le produit de la matrice puis réapuyez sur 'Entrer'\n pour afficher la correction")
print("3- Si vous voulez quitter, vous pouvez soit appuyer sur Ctrl+C")
print("Ou bien en appuyant sur 'q' puis 'Entrer' après avoir vu la correction")
print("Bonnes révisions")

ask_icon = input("Voulez vous activer les icones ? (si votre police d'écriture vous le permet) O(ui)/n(on)")
enable_icons = True if (ask_icon == "Oui" or ask_icon == "O" or ask_icon=="oui") else False

def new_random_matrice(row:int, col:int)->list:
    lst = []
    # for each line
    for i in range(row):
        # append the column number
        lst.append([]);
        for _ in range(col):
            lst[i].append(random.randint(-6, 6))

    return lst

def print_matrice(matrice:list)->None:
    for i, row in enumerate(matrice):
        end_of_loop = (i == len(matrice)-1)
        # print opening brackets
        if enable_icons:
            print( "⎡" if i==0 else "⎣" if end_of_loop else "⎢", end="")
        else:
            print ("[")
        
        for j, col in enumerate(row):
            start_of_line = (j == 0)
            # printing matrix elements
            print(f"{col:>4}" if not start_of_line else f"{col:>3}", end="")
            
        # print closing brackets
        if enable_icons:
            print("", "⎤" if i==0 else "⎦" if i==len(matrice)-1 else "⎥")
        else:
            print("]")
    return None


def matrice_mul(matrice1, matrice2):
    res_matrice = []
    rowlen = len(matrice1)
    collen = len(matrice2[0])

    for nrow in range(rowlen):
        res_matrice.append([])
        for ncol in range(collen):
            res = 0
            for k in range(len(matrice1[nrow])):
                res += matrice1[nrow][k] * matrice2[k][ncol]
            res_matrice[nrow].append(res)

    return res_matrice


# app loop
while input() != "q":
    
    # clear screen
    clear_scr();

    # generate matrice
    row1 = random.randint(2, 4)
    col1 = random.randint(2, 4)
    row2 = col1
    col2 = random.randint(2, 4)

    first_matrice = new_random_matrice(row1, col1);
    second_matrice = new_random_matrice(row2, col2);
    
    # print matrice
    print_matrice(first_matrice)
    print("x")
    print_matrice(second_matrice)
    start = time.time()

    # calculate result
    result = matrice_mul(first_matrice, second_matrice)

    # wait to show results
    input()

    # show results
    end = time.time()
    print("=")
    print_matrice(result)
    time_taken = int(end-start)
    m_taken = int(time_taken//60)
    s_taken = int(time_taken%60)
    print(f"\n({m_taken}min {s_taken}s)")

    print("\nVoulez vous continuer (q pour quitter)? ", end="")

clear_scr()
