import random

number_of_guesses = int(3)
guesses_left = number_of_guesses
guessed = False

print("Welcome to the guessing game!")
print("You have 3 guesses to guess what number I am thinking of ...")

answer = random.randint(1, 10)

while guesses_left > 0 and guessed == False:
  print("")
  guess = int(input("Guesses remaining - " + str(guesses_left) + ": "))

  if guess == answer:
    print("Good guess, you are correct!")
    guessed = True
    continue
  elif guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too low")

  guesses_left -= 1

  if guesses_left == 0:
    print("Better luck next time!")
    print("The answer was " + str(answer))
