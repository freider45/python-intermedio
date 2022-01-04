import os
import random
from typing import Type
import pyfiglet

def read():
    with open("./archivos/DATA.txt","r", encoding="utf-8") as data:
        words = [word for word in data] 
        word = random.choice(words)
    return word


def draw(pal):
    print("*"*49)
    print(pal)
    print("*"*49)
    print("\t\t=================")
    print("\t\t         |      ||") 
    print("\t\t     **  |      ||")
    print("\t\t    *   **      ||")
    print("\t\t     **  *      ||")
    print("\t\t       * * *    ||")
    print("\t\t      *  *  *   ||")
    print("\t\t     *   *   *  ||")
    print("\t\t         *      ||") 
    print("\t\t         *      ||")
    print("\t\t        *  *    ||")
    print("\t\t       *    *   ||")
    print("\t\t      *      *  ||")
    print("\t\t                ||")
    print("\t\t                ||")
    print("\t\t     =============")
    print("\n","*"*49)

def comparation(palabra,titulo):
    list = ["_"]*(len(palabra)-1)
    bandera = True
    aux = 10
    while(bandera): 
        if aux>0:
            bandera2 = True
            os.system("cls")
            draw(titulo)
            print("\n\t\t¡ADIVINA LA PALABRA!\n")
            for k in list:
                if "_" in list:
                    print(k,end=" ")
                else:
                    print("¡GANASTE! CON LA PALABRA ",palabra.upper())
                    bandera = False
                    break
            if bandera:
                if aux == 1:
                    print("\n\nTienes ",aux," vida")
                else:
                    print("\n\nTienes ",aux," vidas")
                    
                try:
                    let = input("\nDigite una letra: ") 
                    if len(let) == 0:
                        raise ValueError("\nDebe digitar una letra")
                    if let.isnumeric():
                        raise ValueError("\nSolo digite letras")
                    for i,pal in enumerate(palabra):
                        if pal!= "\n":
                            if pal == "á":
                                pal = "a"
                            elif pal == "é":
                                pal = "e"
                            elif pal == "í":
                                pal = "i"
                            elif pal == "ó":
                                pal = "o"
                            elif pal == "ú":
                                pal = "u"
                            elif pal == "Ü":
                                pal = "u"
                            if let == pal:
                                list.pop(i)
                                list.insert(i,let.upper()) 
                                bandera2 = False 
                    if bandera2:
                        aux = aux-1
                except ValueError as ve:
                    print(ve)
                    input()

        else:
            bandera = False
            print("\n¡PERDISTE! LA PALABRA ERA ",palabra.upper()) 
            input() 
        

def run():
    word = read()
    title = pyfiglet.figlet_format("HANGMAN")
    comparation(word,title)
    
if __name__=='__main__':
    run()

    
