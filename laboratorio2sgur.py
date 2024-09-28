def calcular_superficie(lado1, lado2):
    
    return lado1 * lado2

if __name__ == "__main__":

    lado1_xd1 = float(input("Ingrese el lado 1 del primer rectángulo: "))
    lado2_xd1 = float(input("Ingrese el lado 2 del primer rectángulo: "))
    

    lado1_xd2 = float(input("Ingrese el lado 1 del segundo rectángulo: "))
    lado2_xd2 = float(input("Ingrese el lado 2 del segundo rectángulo: "))
    
    superficie_xd1 = calcular_superficie(lado1_xd1, lado2_xd1)
    superficie_xd2 = calcular_superficie(lado1_xd2, lado2_xd2)
    
    if superficie_xd1 > superficie_xd2:
        print(f"El primer rectángulo tiene mayor superficie: {superficie_xd1}")
    elif superficie_xd2 > superficie_xd1:
        print(f"El segundo rectángulo tiene mayor superficie: {superficie_xd2}")
    else:
        print("los 2 tienen la misma superficie.")