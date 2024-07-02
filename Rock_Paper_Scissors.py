import random

choice = int(input("0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0, 2)

print("Computer Chose", computer_choice)

if choice == 0:
    if computer_choice == 0:
        print("Draw Won!")
    elif computer_choice == 1:
        print("Computer won!")
    else:
        print('Human won')
        
elif choice == 1:
    if computer_choice == 0:
        print("Human won!")
    elif computer_choice == 1:
        print("Draw")
    else:
        print("Computer Won!")

elif choice == 2:
    if computer_choice == 0:
        print("compute won!")
    elif computer_choice == 1:
        print("Human won!")
    else:
        print("Draw!")
else:
    print("enter a valid choice!")
