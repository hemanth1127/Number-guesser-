import random

def guess(x):
  random_number=random.randint(1,x)
  guess=0
  while guess !=random_number:
    guess=int(input(f"enter a number betweei 1 and {x}:"))
    if guess<random_number:
      print("too low")
    elif guess>random_number:
      print("too high")
  print(f"you have guessed the  number{random_number} congrats")



  guess(10)
