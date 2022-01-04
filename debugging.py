
def divisors(num):
    
    try:
        if num < 0:
            raise ValueError("Ingrese solo numeros positivos")
        divisors = [worker for worker in range(1, num+1) if num % worker == 0]
        # for i in range(1, num +1 ):
        #     if(num % i == 0):
        #         divisors.append(i)
        return divisors 
    except ValueError as ve:
        print(ve)
        return str(num) + " no es un numero positivo"
    

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino el programa")
    except ValueError as ve:
        print("Ingrese solo numeros")
    
    

if __name__=='__main__':
    run()