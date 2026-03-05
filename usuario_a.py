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
