# Guess the number Game
import random
cpu = random.randint(1,100)
count = 5
while True:
    num = int(input("Guess the number.."))
    if cpu == num:
        print("Congrats you guessed the correct number..")
        break
    elif num > cpu:
        print("You guessed the larger number..")
    elif num < cpu:
        print("You guessed the smaller number..")
    else:
        print("Invalid input..")
    count -= 1
    print("Chances left..",count)
    if count == 0:
        print("You lose the game.. Number was",cpu)
        break
