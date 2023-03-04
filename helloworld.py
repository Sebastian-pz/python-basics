print("Hello world without greeting function")

def saludar():
  print("Hello world in function")
saludar()


def saludarEspecifico(nombre: str):
  """This is a function, it is used for greet someone

  Args:
      nombre (string): A name
  """
  print("Hello, " + nombre)
  return "Hello, " + nombre


saludarEspecifico("Sebastian")
