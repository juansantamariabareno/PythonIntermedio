def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    # Vamos a controlar esto para evitar que ingrese cosas que no son números
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == "__main__":
    run()