from random import randint

def getNumber(max: int):
    return randint(0, max)

def solve(number: int, correct: int):
    return number == correct


def play(max= 10, hints=False):
    solution = getNumber(max)
    try_solve(solution, hints)

def try_solve(solution, hints):
    solved = False
    while (solved == False):
      user_number = input('Adivina el número: ')
      if (solve(int(user_number), solution)):
          solved = True
          print('Lo encontraste')
      else: get_hint(solution, int(user_number)) if hints else print('Te equivocaste, intenta otra vez.')

def get_hint(solution, user_number):
  hint = 'mayor' if solution > user_number else 'menor'
  print(f"No, ese no es, el número que buscas es {hint}")

def main():
    play(5, True)
main()
