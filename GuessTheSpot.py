
    from random import shuffle

    # initiate the list
    myList = [' ', 'O', ' ']

    # shuffle the list
    def shuffle_list(mylist):
        shuffle(myList)
        return myList

    def player_guess():
        guess = ''
        while guess not in ['0', '1', '2']:
            guess = input('Pick up the correct spot from 0 to 2 :')
        return int(guess)

    def guess_play(mylist, guess):
        if mylist[guess] == 'O':

            print('Correct !!!')
        else:
            print('Wrong one ')

    mixedup_list = shuffle_list(myList)
    guess = player_guess()
    guess_play(mixedup_list, guess)
