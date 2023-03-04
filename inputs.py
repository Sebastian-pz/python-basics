# Método input en python
name = input('Inserte su nombre: ')
print(f"Hola {name}")
age = input('Inserte su edad: ')

# Se necesita parsear
age = int(age)

# Se hace un ternario
print("Es mayor de edad." if age >= 18 else "No es mayor de edad.")
