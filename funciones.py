# funciones en python
def saludar():
    print("Hola, mundo")

# saludar()

def saludar_persona(nombre):
    print(f"Hola, {nombre}")

# saludar_persona("Alice")

def obtener_saludo(nombre):
    return f"Hola, {nombre}"

# print(obtener_saludo("Ana"))

def obtener_saludo_completo(nombre="fulano", apellido="de_tal"):
    return f"Hola, {nombre} {apellido}"

# print(obtener_saludo_completo("Ana", "García"))

print(obtener_saludo_completo(apellido="García", nombre="Ana"))

print(obtener_saludo_completo("Ana"))
print(obtener_saludo_completo("García"))
print(obtener_saludo_completo())