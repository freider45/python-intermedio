
def divisors(num):
    divisors = [worker for worker in range(1, num+1) if num % worker == 0]
    return divisors 
    

def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un números positivos"
    print(divisors(int(num)))
    print("Termino el programa")
    
    
    

if __name__=='__main__':
    run()