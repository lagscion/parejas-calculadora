# Funciones hechas por Santi .T

# Números primos en un rango
def primos_en_rango():
    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))

    print("Números primos en el rango:")

    for num in range(inicio, fin + 1):
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break

            if es_primo:
                print(num, end = " - ")
                
#______________________________________________________

# Verificar si un número es primo

def verificar_primo():
    n = int(input("Ingrese un número: "))

    if n <= 1:
        print("No es primo")
        return

    for i in range(2, n):
        if n % i == 0:
            print("No es primo")
            return

    print("Es primo")

#_________________________________________________________

# Operación factorial

def factorial():
    n = int(input("Ingrese un número: "))
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    print("El factorial es:", resultado)

#_________________________________________________________

# Máximo común divisor

def mcd():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    while b != 0:
        temp = b
        b = a % b
        a = temp

    print("El MCD es:", a)

#__________________________________________________________