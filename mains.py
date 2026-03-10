import random  

user_wins= 0
computer_wins = 0
draws = 0

options= ['rock','paper','scissors','r','p','s']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower() 
    if user_input== 'q':
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #rock : 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f'You picked {user_input}')
    print('Computer picked', computer_pick + '.')

    if user_input[0] == 'r' and computer_pick == 'scissors':
        print('you won')
        user_wins += 1
        continue

    elif user_input[0] == 'p' and computer_pick == 'rock':
        print('you won')     
        user_wins += 1
        continue

    elif user_input[0] == 's' and computer_pick == 'paper':
        print('you won')     
        user_wins += 1
        continue

    elif user_input[0] == computer_pick[0]:
        print('Draw!')
        draws += 1
        continue

    else: 
        print('You lost')
        computer_wins +=1

print('You won', user_wins,'times.')
print('The computer won', computer_wins, 'times.')
print('Draws:', draws, 'times.' )
print('goodbye')