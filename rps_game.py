import random
user_count=0
computer_count=0
while True:
    print('Enter your choice')
    print("1-Rock 2-Paper 3-Scissor")
    user = int(input())

    computer = random.randint(1, 3)
    computer = int(computer)

    print('user= ',user)
    print('computer = ', computer)


    if user == computer:
        print('Tie')
    elif user == 1 and computer == 2:
        print('computer is won')
        computer_count += 1
    elif user == 1 and computer == 3:
        print('user is won')
        user_count += 1
    elif user == 2 and computer == 1:
        print('user is won')
        user_count += 1
    elif user == 2 and computer == 3:
        print('computer is won')
        computer_count += 1
    elif user == 3 and computer == 1:
        print('computer is won')
        computer_count += 1

    elif user == 3 and computer == 2:
        print('user is won')
        user_count += 1

    print('Winning Count')
    print("user = "+ str(user_count) + " computer = " + str(computer_count))
    print("")

    print("Do you want to play again?")
    play = input()
    if play == 'no':
        break
