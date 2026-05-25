Edad = int(input("Insertar su edad: "))
Nota = float(input("Insertar su calificación: "))

if Edad > 17 and Nota > 4.0: 
    print("Bienvenido a la Élite, Ingeniero.")
elif Edad <= 17 and Nota >= 4.0:
    print("Buen promedio. Postula cuando seas mayor de edad.")
else:
    print("Fuera de mi sistema. No cumples el perfil.")