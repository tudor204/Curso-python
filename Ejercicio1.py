# Cálculo de año de nacimiento
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
edad = int(input("¿Qué edad tienes? "))
anyo_actual = int(input("¿En qué año estamos? "))

while True:
    cumplido = input("¿Has cumplido ya los años? (si/no) ").lower()
  
    resultado = anyo_actual - edad
    resultado1 = anyo_actual - edad - 1

    if cumplido == "si":
        print(f"Naciste en: {resultado}")
        break
    elif cumplido == "no":
        print(f"Naciste en: {resultado1}")
        break
    else:
        print("Valor incorrecto. Escribe 'si' o 'no'.")
