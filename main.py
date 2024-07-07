import random

game = {
    'r': 'Rock',
    's': 'Scissor',
    'p': 'paper'
}

player_score = 0
computer_score = 0

while True:
    i = input('Rock(r), Paper(p), Scissor(s):')
    print(i)

    if i not in ['r', 'p', 's']:
        print('Not Valid.')
        continue

    print('You Choose ' + game[i])

    choice = ['r', 'p', 's']
    choice_number = random.randint(0, 2)
    c = choice[choice_number]

    print('Computer Choose ' + game[c])

    if i == c:
        print('Tie !')

    elif i == 'r':
        if c == 'p':
            print('computer wins.')
            computer_score += 1
        else:
            print('you win.')
            player_score += 1

    elif i == 'p':
        if c == 'r':
            print('you win.')
            player_score += 1
        else:
            print('computer wins.')
            computer_score += 1

    elif i == 's':
        if c == 'r':
            print('computer wins.')
            computer_score += 1
        else:
            print('you win.')
            player_score += 1
    print("---------------------------------")

    print('Your Score is:', player_score)
    print('Computer Score is:', computer_score)

    print('-----------------------------------')
    t = input('Do You Want to Continue?[y/n]')

    if t == 'y':
        pass
    else:
        break
