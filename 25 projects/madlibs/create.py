from random import randint

def createMadlibs(text: str, diff: int):
  madlib = text.split(' ')
  deleted_words = {}
  for i in range(diff):
    position =  randint(0, len(madlib))
    deleted_words[madlib[position]] = position
    madlib[position] = f'___{position}___'
  return [' '.join(madlib), deleted_words]

def solve(madlib: list):
  print(madlib[0])
  text: str = madlib[0].split(' ')
  words: object = madlib[1]

  health = 3

  while (health > 0 and len(words) > 0):
    data_input = input('¿Cuál es la palabra y posición que quiere llenar? ')
    word, pos = data_input.split(' ')[0], int(data_input.split(' ')[1])
    if (word in words and words[word] == pos):
      text[pos] = word
      del words[word]
      print(f"Correcto! Has encontrado una palabra")
    else:
      health = health -1
      print(f"Incorrecto! Te quedan {health} vidas ten cuidado")

  if (health == 0):
    return print('Haz fallado, intenta otra vez')
  else:
    print('Bien hecho, ¡Lo lograste!')
    return print(' '.join(text))
