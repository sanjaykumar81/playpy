import random

choice = input("predict whether it will even or odd: Enter your choice: ")

output = random.randrange(1, 6)

if choice.upper() == "EVEN" and output % 2 == 0:
    print(f"Hurray!! you were right. Choice : {choice} , output: {output}")

elif choice.upper() == "ODD" and output % 2 != 0:
    print(f"Hurray!! you were right. Choice : {choice} , output: {output}")
else:
    print(f"Sorry your prediction was wrong. Choice : {choice} , output: {output}")