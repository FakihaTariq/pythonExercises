secretNumber = 9
tries = 0
while tries < 3:
    guess = input('Guess: ')
    tries = tries + 1
    if int(guess) == secretNumber:
        print('You win!')
        break
    elif tries > 2:
        print('You lose!')
