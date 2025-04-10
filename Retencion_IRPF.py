#obtener datos de entrada
sueldo =float(input("Sueldo "))
situacion = input("Situación 1-2-3 ")
hijos = int(input("Número de hijos "))

#obtener exención 
exencion = 0
if situacion == "1":
    if hijos <= 0:
        exencion = 0
    elif hijos == 1:
        exencion = 15947
    else:
        exencion = 17100

if situacion == "2":
    if hijos <= 0:
        exencion = 15546
    elif hijos == 1:
        exencion = 16481
    else:
        exencion = 17634

if situacion == "3":
    if hijos <= 0:
        exencion = 14000
    elif hijos == 1:
        exencion = 14516
    else:
        exencion = 15063

sueldo_a_retener = sueldo - exencion

#obtener retencion
porcentaje = 0
if sueldo_a_retener <= 12450:
    porcentaje = 19
elif sueldo_a_retener <= 20200:
    porcentaje = 24
elif sueldo_a_retener <= 35200:
    porcentaje = 30
elif sueldo_a_retener <= 60000:
    porcentaje  = 37
elif sueldo_a_retener <= 300000:
    porcentaje = 45
else: 
    porcentaje = 47

monto_anual = sueldo_a_retener * porcentaje /100
monto_mensual = monto_anual / 12 

#mostrar resultados
print(f"Sueldo anual: \t {sueldo}")
print("Situación: \t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Porcentaje: \t", porcentaje)
print("Total anual: \t", monto_anual)
print()
print(f"Monto mensual: \t {monto_mensual:.2f}")

