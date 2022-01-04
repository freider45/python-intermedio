
from data import DATA

def listado(list):
    for worker in list:
        print(worker)

def run():

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    '''en a lista va a guardar el nombre de la llave "name", recorriendo la lista DATA que contiene los
    diccionarios que contienen llaves y valor, solo si el valor de la llave "language" es igual a python'''
    
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    '''se va a guardar los nombres de la llave "name" que estan dentro del diccionario y a la vez estos 
    estan dentro de la lista DATA, recorremos y si el valor de la llave "organization" es igual a platzi
    '''
    
    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA))
    '''se va a guardar los trabajadores mayores a 18 años, para ello usamos filter, la cual recibe una funcion y
    el iterable que es una lista (DATA), en donde a la vez va envuelta en list. en lambda pasamos worker, de worker 
    en la llave "age" que sean ayores a 18
    '''
    
    adults = list(map(lambda worker: worker["name"] , adults))
    '''de filter sacamos todos los trabajadores mayores a 18, por ende nos traera el listado de esos 
    trabajadores en su respectivo diccionario, entonces ahora usamos map para traer de la lista adults, ya no
    de DATA, los nombres de los trabajaores por eso la llave "name"
    '''
    prueba = list(map(lambda worker: worker["age"] > 18, DATA))
    print("Hola")
    listado(prueba)
    
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] > 70}, DATA))
    '''Aquí vamos a crear un nuevo diccionario, en donde tenemos a map que recibe una funcion lambda y un iterable,
    tenemos el iterable que es la lista DATA y la funcion lambda que tiene cosas nuevas. lo que pasa en lambda es
    que recibimos a worker y a cada worker que es un diccionario de la lista DATA le sumamos un nuevo diccionario,
    en donde | nos sirve para sumar diccionarios, colocamos dentro de llaves el diccionario nuevo, en donde vemos 
    que la llave es "old" y el valor va a ser true o false dependiendo de la comparacion de la llave "es" es mayor a 70
    '''
    
    #all_python_devs con filter y map
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2))
    
    #all_python_workers con filter y map
    all_python_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_python_workers2 = list(map(lambda worker: worker["name"], all_python_workers2))
    
    #lista adults con list comprenhensions
    adults2 = [worker["name"] for worker in DATA if worker["age"] > 18]
    #lista de old people con list comprenhensions
    old_people2 = [{**worker, **{'adults': worker['age'] > 50}} for worker in DATA]
    
    print("\nNombre de trabajadores que dominan python")
    listado(all_python_devs)
   
    print("\nNombre de trabajadores de platzi")
    listado(all_platzi_workers)
    
    print("\nNombre de trabajadores mayores a 18")
    listado(adults)
    
    print("\nNombre de trabajadores mayores a 70")
    listado(old_people)
        
    print("\nNombre de trabajadores que dominan python, ahora con filter y map")
    listado(all_python_devs2)
        
    print("\nNombre de trabajadores que trabajan en platzi, ahora con filter y map")
    listado(all_python_workers2)
    
    print("\nNombre de trabajadores adultos, list comprenhensions")
    listado(adults2)
    
    print("\nNombre de trabajadores mayores a 50, con list comprenhensions")
    listado(old_people2)

if __name__=='__main__':
    run()