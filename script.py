# Claudio Campos Spring Final Modulo 3 
import random
import string

# Función para crear una contraseña segura
def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for i in range(10))
    return contraseña

# Función para verificar el número telefónico
def verificar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 8

# Lista de nombres de usuarios
nombres_usuarios = ["Armando Luna", "Benito Muñoz", "Eladio Alarcón", "Macarena Mora", "Rosa Martínes",
                    "Sofia Perez", "Carlos Santana", "Tomas Araya", "Axl Rosas", "Jhon Lemon"]

# Diccionario para almacenar usuarios y contraseñas
cuentas = {}

# Crear cuentas y asignar contraseñas
for nombre in nombres_usuarios:
    cuentas[nombre] = generar_contraseña()

# Solicitar números telefónicos 
numeros_telefonicos = {}
for usuario in cuentas:
    while True:
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        if verificar_telefono(telefono):
            numeros_telefonicos[usuario] = telefono
            break
        else:
            print("El número telefónico debe tener 8 dígitos numéricos. Intente de nuevo.")

# Mostrar a todos los usuarios con su contraseña y numero telefónico
for usuario, contraseña in cuentas.items():
    print(f"Usuario: {usuario}, Contraseña: {contraseña}, Teléfono: {numeros_telefonicos[usuario]}")