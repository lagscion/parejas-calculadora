def es_capicua(numero):
    """
    Determina si un número es capicúa.
    Un número capicúa se lee igual de izquierda a derecha
    que de derecha a izquierda.
    """

    numero_str = str(numero)

    return numero_str == numero_str[::-1]

def fibonacci():
    try:
        n = int(input("Ingrese la cantidad de términos: "))
        
        if n <= 0:
            print("Debe ingresar un número mayor que 0.")
            return
        
        a, b = 0, 1
        contador = 0
        
        print("Serie Fibonacci:")
        
        while contador < n:
            print(a, end=" ")
            a, b = b, a + b
            contador += 1
            
        print()  # salto de línea final
        
    except ValueError:
        print("Debe ingresar un número entero válido.")

def numero_perfecto():
    try:
        n = int(input("Ingrese un número entero positivo: "))
        
        if n <= 1:
            print("El número debe ser mayor que 1.")
            return
        
        suma = 0
        
        for i in range(1, n):
            if n % i == 0:
                suma += i
        
        if suma == n:
            print(f"{n} es un número perfecto.")
        else:
            print(f"{n} no es un número perfecto.")
            
    except ValueError:
        print("Debe ingresar un número entero válido.")