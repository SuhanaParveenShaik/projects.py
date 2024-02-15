import random
target = random. randint(1, 100)

while True:
    userchoice = input("guess the target:")
    if(userchoice == "Q"):
        break

    userchoice = int (userchoice)
    if(userchoice == target):
        print("success : correct guess!!")
        break
    elif(userchoice < target):
        print("your guess is too small. try guessing a larger number")
    else:
        print("your guess is too big. try guessing smaller number")

print("------game over-------")
