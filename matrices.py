import math as math
import os as os
import sys
import random as random

clear_scr = lambda: os.system('clear')
if sys.platform == "win32":
    clear_scr = lambda: os.system('cls')


clear_scr()
print("1- Apuyez sur le retour à la ligne pour commencer")
print("2- Calculez le produit de la matrice puis réapuyez sur 'Entrer'\n pour afficher la correction")
print("3- Si vous voulez quitter, vous pouvez soit appuyer sur Ctrl+C")
print("Ou bien en appuyant sur 'q' puis 'Entrer' après avoir vu la correction")
print("Bonnes révisions")

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
    for row in matrice:
        print( "|", end="")
        for col in row:
            print(f"{col}\t", end="")
        print("|")
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

    # calculate result
    result = matrice_mul(first_matrice, second_matrice)

    # wait to show results
    input()

    # show results
    print("=")
    print_matrice(result)

clear_scr()
