print("SISTEMA DE EVALUACIÓN DE ÉLITE")

# 1. El contador nace AFUERA del bucle
aceptados = 0 

while True:
    # 2. Los datos se piden ADENTRO para que cambien en cada vuelta
    Nombre = input("\n¿Cuál es tu nombre? ")
    Edad = int(input("Insertar su edad: "))
    Nota = float(input("Insertar su calificación: "))

    if Edad > 17 and Nota > 4.0: 
        print(f"Bienvenido a la Élite, Ingeniero {Nombre}.")
        # 3. Sumamos 1 al contador solo si es aceptado
        aceptados = aceptados + 1 
    elif Edad <= 17 and Nota >= 4.0:
        print("Buen promedio. Postula cuando seas mayor de edad.")
    else:
        print("Fuera de mi sistema. No cumples el perfil.")

    continuar = input("¿Evaluar a otro? (s/n): ")
    if continuar == 'n':
        break

# 4. El reporte final va AFUERA del bucle, al final de todo
print(f"\nMisión finalizada. Total de ingenieros reclutados: {aceptados}")
print(f"Cerrando sistema... Adiós, {Nombre}.")