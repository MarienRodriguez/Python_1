print ( "SISTEMA DE EVALUACIÓN DE ÉLITE" )

Nombre = input ("¿Cuál es tu nombre ")
Edad = int(input("Insertar su edad "))
Nota = float(input("Insertar su calificación: "))
aceptados = 0

while True:

    if Edad > 17 and Nota > 4.0: 
        print("Bienvenido a la Élite, Ingeniero.")
    elif Edad <= 17 and Nota >= 4.0:
        print("Buen promedio. Postula cuando seas mayor de edad.")
    else:
        print("Fuera de mi sistema. No cumples el perfil.")

    continuar = input("¿Evaluar a otro? (s/n): ")
    
    if continuar == 's':
     Nombre = input ("¿Cuál es tu nombre ")
     Edad = int(input("Insertar su edad"))
     Nota = float(input("Insertar su calificación: "))
    if continuar == 'n':
        print(f"Cerrando sistema de seguridad... Adiós, {Nombre}.")
    if continuar == 'n':
        break

    if Edad < 17 and Nota > 4.0:
aceptadoss = 1 * print("Buen promedio. Postula cuando seas mayor de edad.")

print("Misión finalizada. Total de ingenieros reclutados para la élite: {aceptadoss}")
