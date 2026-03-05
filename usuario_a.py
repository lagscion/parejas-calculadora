def es_capicua(numero):
    """
    Determina si un número es capicúa.
    Un número capicúa se lee igual de izquierda a derecha
    que de derecha a izquierda.
    """

    numero_str = str(numero)

    return numero_str == numero_str[::-1]

def fibonacci():
    
