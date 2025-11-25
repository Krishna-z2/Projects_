# Rock , Paper & Scissors
import random

# Score of both computer and user

options = ['Rock', 'Paper', 'Scissor']

while True:
    user_permission = input("Wanna Play (Rock/ Paper/ Scissors) if Yes then ['Y' or 'Yes'] then ['Q' or 'Quit']: ").title()
    if user_permission in ['Y','Yes']:
        print("Let's Go!")
        break
    else:
        print("Thank You! '_' ")
        quit()

print("Rules:")
print("1. Correct Answer = +1")
print("2. Wrong Answer = 0")
print("3. Wrong Answer Other Than options = 0")

while True:
    user_score = 0
    computer_score = 0
    try:
        times = int(input("Best of (1 to 10): "))

        if(times >= 1  and  times <= 10):

            for i in range(1, times+1):
            
                random_guess = random.randrange(0,3)
                computer_guess = options[random_guess]

                user_input = input("Choose Between (Rock / Paper / Scissor) : ").title()
                
                if((user_input == 'Rock'  and  computer_guess == 'Scissor') or
                   (user_input == 'Scissor'  and  computer_guess == 'Paper') or
                   (user_input == 'Paper'  and  computer_guess == 'Rock')):
                    print("--------------------You Won!--------------------")
                    print("Computer Pick :", computer_guess+".\n")
                    user_score += 1

                elif((user_input == 'Rock'  and  computer_guess == 'Rock') or
                    (user_input == 'Paper'  and  computer_guess == 'Paper') or
                    (user_input == 'Scissor'  and  computer_guess == 'Scissor')):
                    print("--------------------Both Tied '.'--------------------")
                    print("Computer Pick :", computer_guess+".\n")
                    computer_score += 1
                    user_score += 1

                else:
                    print("--------------------You Lost!--------------------")
                    print("Computer Pick :", computer_guess+".")
                    computer_score += 1
        
            if user_score > computer_score:
                print("You Won The Game.")
                print("Score : ",user_score)
            else:
                print("You Lost The Game.")
                print("Score : ",user_score)

        else:
            print("Try Between 1 TO 10.")
            continue


    except ValueError:
        print("Invalid Input!!, Try Between 1 TO 10.")
        continue

    again = input("Wanna Play Again (Yes / No):\n").title()
    if again in ['Yes','Y']:
        continue
    else:
        print("Thank You For Playing!!")
        break
