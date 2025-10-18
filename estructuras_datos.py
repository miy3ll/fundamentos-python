# estructuras de datos en python
# enteros
number = 10
# print(type(number)) # <class 'int'>

# flotantes
pi = 3.14
# print(type(number)) # <class 'float'>

# cadenas de texto
greeting = "Hola, mundo"
# print(type(greeting)) # <class 'str'>

# booleanos
is_active = True
# print(type(is_active)) # <class 'bool'>

# listas
fruits = [
    "manzana", 
    "banana", 
    "cereza"
    ]
# print(fruits)
# agregar un elemento a la lista
fruits.append("naranja")

# print(fruits)

# print(fruits[1:])
# print(fruits[-1])

fruits[1] = "kiwi"
# print(fruits)

# tuplas
nombres = (
            "Alice", 
            "Bob", 
            "Charlie",
            "Diana",
            )
# print(nombres[-1])

# nombres[0] = "Eve"  # Esto generará un error porque las tuplas son inmutables

# diccionarios
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Wonderland",
    "comida_favorita": ["tarta", "té"],
    "profesion": "adventurer"
}
# print(persona["nombre"])
# print(persona["edad"])

# persona["profesion"] = "adventurer"
# print(persona)

