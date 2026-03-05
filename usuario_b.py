# Funciones hechas por Santi .T
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

primos_en_rango()
#______________________________________________________