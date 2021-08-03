from main import main

while True:
    answer = input('Do you want to play Tic-Tac-Toe? (YES/NO) ')
    answer = answer.upper().replace(' ', '')
    if(answer == 'YES' or answer == 'Y'):
        print('-----------------------------------------------')
        board = [' ' for space in range(10)]
        main()
    else:
        print('Alright, see you next time!')
        break