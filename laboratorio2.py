def calcular_promedio(a, b, c):

    promedio = (a + b + c) / 3
    return promedio
numero1 = int(input("ingrese un entero"))

numero2 = int(input("ingrese otro valor"))

numero3 = int(input("ingrese el tercer valor"))

resultado = calcular_promedio(numero1, numero2, numero3)
print(f"el promedio de los 3 es: {resultado}")