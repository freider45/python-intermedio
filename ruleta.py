import random
import os


def election():
    options = ["Desayuno","Almuerzo","Cena","No lava"]
    names = ["Daniela","Emily","Thomas","Freider"]
    aux = 0
    dic = {}
    while(aux < 4):
        option = random.choice(options)
        name = random.choice(names)
        dic[name] = option
        options.remove(option)
        names.remove(name)
        aux = aux+1
    return dic

def run():
    os.system("cls")
    a = election()
    print(a)
    

if __name__=='__main__':
    run()