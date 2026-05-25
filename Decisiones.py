year = int (input("¿En que año naciste?"))
Edad = 2026 - year
if Edad >= 18:
    print ("Acceso concedido. Estatus: Adulto responsable.")
else:
    print ("Acceso restringido. Estatus: Cadete en formación.")
print (f"Edad: {Edad} años.")
