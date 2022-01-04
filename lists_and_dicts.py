
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstName":"Freider", "LastName":"Escobar"}
    
    super_list = [
        {"firstName":"Freider", "LastName":"Escobar"},
        {"firstName":"Johan", "LastName":"Cueltan"},
        {"firstName":"Aaron", "LastName":"Nuñez"},
        {"firstName":"Manuel", "LastName":"Mendoza"},
        {"firstName":"Ana", "LastName":"Muñoz"},
    ]
    
    super_dict = {
        "Natural_nums":[1,2,3,4,5],
        "Integer_nums":[-1,-2,0,1,2],
        "Floating_nums":[1.1, 4.5, 6.43]
    }
    
    '''Como es un diccionario recordemos que podemos acceder tanto a la llave como al valor 
    o a ambos, en el bucle vemos que se sacan ambos valores, por eso el items(), si quisieramos sacar
    solo las llaves for key in super_dict.keys() y para el valor for value in super_dict.keys()'''
    
    for key, value in super_dict.items(): 
        print(key, "-", value)
        
    '''Las listas las recorremos normal, pero en este caso tenemos diccionarios dentro de la lista, 
    entonces sacamos el primervalor de la lista y en el print sacamos cada valor del diccionario,
    por eso i[llave] - i[valor o podriamos hacer doble bucle, pero recordemos que es mejor un codigo plano
    para mejor eficiencia.'''
    for i in super_list:
        print(i["firstName"], "-", i["LastName"])
    
if __name__ == '__main__':
    run()