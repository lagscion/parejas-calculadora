import usuario_a
import usuario_b


def mostrar_menu():
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Serie Fibonacci")
    print("2. Número Capicúa")
    print("3. Número Perfecto")
    print("4. Números Primos en un Rango")
    print("5. Verificar si un Número es Primo")
    print("6. Factorial")
    print("7. Máximo Común Divisor (MCD)")
    print("8. Salir")
    print("==================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            usuario_a.fibonacci()

        elif opcion == "2":
            numero = int(input("Ingrese un número: "))
            if usuario_a.es_capicua(numero):
                print("El número es capicúa.")
            else:
                print("El número NO es capicúa.")

        elif opcion == "3":
            usuario_a.numero_perfecto()

        elif opcion == "4":
            usuario_b.primos_en_rango()

        elif opcion == "5":
            usuario_b.verificar_primo()

        elif opcion == "6":
            usuario_b.factorial()

        elif opcion == "7":
            usuario_b.mcd()

        if opcion == "8":
            break

if __name__ == "__main__":
    main()