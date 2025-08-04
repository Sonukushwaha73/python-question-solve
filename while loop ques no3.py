
#create a random number guessing game with python
import random   

num = random.randint(1, 10)   # random number generate karega 1 se 10 ke beech

guess = int(input("please guess your number: "))  # user se number le raha hai

if num == guess:
    print("You guessed right!")  # agar number match kare
else:
    print("You guessed wrong. The correct number was", num)  # galat guess
