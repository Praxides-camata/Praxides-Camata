#Ejercicio 1
# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")


#Ejercicio 2
def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series[:n]

# Solicitar al usuario ingresar el valor de 'n'
n = int(input("Ingrese el valor de 'n' para la serie de Fibonacci: "))

# Generar los primeros 'n' números de la serie de Fibonacci
fibonacci_series = fibonacci(n)

# Mostrar la serie de Fibonacci resultante
print(f"Los primeros {n} números de la serie de Fibonacci son:")
print(fibonacci_series)
 
 #Ejercicio 3
def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()

    # Eliminar signos de puntuación
    caracteres_puntuacion = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for caracter in cadena:
        if caracter in caracteres_puntuacion:
            cadena = cadena.replace(caracter, "")

    # Verificar si la cadena es un palíndromo
    return cadena == cadena[::-1]

# Solicitar al usuario ingresar una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto para verificar si es un palíndromo: ")

# Verificar si la cadena es un palíndromo
if es_palindromo(cadena_ingresada):
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")


#Ejercicio 4
    # Solicitar al usuario ingresar una lista de números separados por espacio
numeros_ingresados = input("Ingrese una lista de números separados por espacio: ")

# Convertir la entrada del usuario a una lista de números
lista_numeros = [float(numero) for numero in numeros_ingresados.split()]

# Verificar si la lista está vacía
if not lista_numeros:
    print("La lista está vacía. Por favor, ingrese al menos un número.")
else:
    # Encontrar el número más grande y el número más pequeño
    numero_mas_grande = max(lista_numeros)
    numero_mas_pequeno = min(lista_numeros)

    # Mostrar los resultados
    print(f"El número más grande de la lista es: {numero_mas_grande}")
    print(f"El número más pequeño de la lista es: {numero_mas_pequeno}")


#Ejercicio 5
    import math

# Solicitar al usuario ingresar el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área y el perímetro del círculo
area_circulo = math.pi * radio**2
perimetro_circulo = 2 * math.pi * radio

# Mostrar los resultados
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro_circulo:.2f}")

#Ejercicio 6
# Solicitar al usuario ingresar tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Determinar el número mayor
numero_mayor = max(numero1, numero2, numero3)

# Mostrar el resultado
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es: {numero_mayor}")






