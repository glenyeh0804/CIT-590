import copy

flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def make_squarelotron(list):
    """Return a squarelotron based on the 'flat' list."""
    squarelotron = []
    tentative_list = []
    for i in list:
        tentative_list.append(i)
        if i % 5 == 0:
            squarelotron.append(tentative_list)
            tentative_list = []
    return squarelotron

def make_list(squarelotron):
    """Return a flat list based on the squarelotron"""
    list = squarelotron[0] + squarelotron[1] + squarelotron[2] + squarelotron[3] + squarelotron[4]
    return list

def upside_down_flip(squarelotron, ring):
    """Return a new squarelotron that is flipped upside-down"""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'outer':
        new_squarelotron[4], new_squarelotron[0] = new_squarelotron[0], new_squarelotron[4]
        new_squarelotron[1][0], new_squarelotron[3][0] = new_squarelotron[3][0], new_squarelotron[1][0]
        new_squarelotron[1][4], new_squarelotron[3][4] = new_squarelotron[3][4], new_squarelotron[1][4]
    if ring == 'inner':
        for i in range(1, 4):
            new_squarelotron[1][i], new_squarelotron[3][i] = new_squarelotron[3][i], new_squarelotron[1][i]
    return new_squarelotron

def left_right_flip(squarelotron, ring):
    """Return a new squarelotron that is flipped left-right"""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'outer':
        for i in range(0, 5):
            new_squarelotron[i][0], new_squarelotron[i][4] = new_squarelotron[i][4], new_squarelotron[i][0]
        new_squarelotron[0][1], new_squarelotron[0][3] = new_squarelotron[0][3], new_squarelotron[0][1]
        new_squarelotron[4][1], new_squarelotron[4][3] = new_squarelotron[4][3], new_squarelotron[4][1]
    if ring == 'inner':
        for i in range(1, 4):
            new_squarelotron[i][1], new_squarelotron[i][3] = new_squarelotron[i][3], new_squarelotron[i][1]
    return new_squarelotron

def inverse_diagonal_flip(squarelotron, ring):
    """Return a new squarelotron that is flipped inverse diagonal"""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'outer':
        for i in range(0, 4):
            new_squarelotron[0][i], new_squarelotron[4 - i][4] = new_squarelotron[4 - i][4], new_squarelotron[0][i]
        for i in range(1, 4):
            new_squarelotron[i][0], new_squarelotron[4][4 - i] = new_squarelotron[4][4 - i], new_squarelotron[i][0]
    if ring == 'inner':
        new_squarelotron[1][2], new_squarelotron[2][3] = new_squarelotron[2][3], new_squarelotron[1][2]
        new_squarelotron[1][1], new_squarelotron[3][3] = new_squarelotron[3][3], new_squarelotron[1][1]
        new_squarelotron[2][1], new_squarelotron[3][2] = new_squarelotron[3][2], new_squarelotron[2][1]
    return new_squarelotron

def main_diagonal_flip(squarelotron, ring):
    """Return a new squarelotron that is flipped main diagonal"""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'outer':
        for i in range(1, 5):
            new_squarelotron[0][i], new_squarelotron[i][0] = new_squarelotron[i][0], new_squarelotron[0][i]
        for i in range(1, 4):
            new_squarelotron[i][4], new_squarelotron[4][i] = new_squarelotron[4][i], new_squarelotron[i][4]
    if ring == 'inner':
        new_squarelotron[1][2], new_squarelotron[2][1] = new_squarelotron[2][1], new_squarelotron[1][2]
        new_squarelotron[1][3], new_squarelotron[3][1] = new_squarelotron[3][1], new_squarelotron[1][3]
        new_squarelotron[2][3], new_squarelotron[3][2] = new_squarelotron[3][2], new_squarelotron[2][3]
    return new_squarelotron

def print_map(squarelotron):
    """Print the squarelotron"""
    count = 0
    for i in squarelotron:
        print('|', end='')
        for k in squarelotron[count]:
            if k < 10:
                print(k, ' |', end='')
            else:
                print(k, '|', end='')
        count += 1
        print('\n')

def flip_selection():
    """Return user's selection for the flip type"""
    selection = input('\nWhich flips do you want to perform?\n''Respond \'U\' for Upside-Down flip, '
                      '\'L\' for Left-Right flip,\n'
                      '\'M\' for Main Diagonal flip, '
                      '\'I\' for Inverse Diagonal flip.').upper().replace('\'', '')
    if selection in 'ULMI':
        return selection
    else:
        print('\nPlease fill in the correct command!')
        return flip_selection()

def ring_selection():
    """Return user's selection for the ring type"""
    ring = input('\nWhich ring do you want to perform?\n''Respond \'outer\' for outer ring, '
                 '\'inner\' for inner ring.').lower().replace('\'', '')
    if (ring == 'outer') or (ring == 'inner'):
        return ring
    else:
        print('\nPlease fill in the correct command!')
        return ring_selection()

def user_decision():
    """Return user's decision for continuing or ending the current game"""
    decision = input('Do you want to do more flips?\n''Respond \'Y for Yes, \'N\' for No.').upper().replace('\'', '')
    if (decision == 'Y') or (decision == 'YES'):
        return True
    elif (decision == 'N') or (decision == 'NO'):
        return False
    else:
        print('\nPlease fill in the correct command!\n')
        return user_decision()

def end_or_restart():
    """Return user's decision for restarting the game or ending the program"""
    end_decision = input('\nDo you want to start a new game?\n''Respond \'Y\' for Yes, '
                         '\'N\' for ending this game.').upper().replace('\'', '')
    if (end_decision == 'Y') or (end_decision == 'YES'):
        print('\nNew game starts! Initiated the squarelotron.\n')
        return True
    elif (end_decision == 'N') or (end_decision == 'NO'):
        print('\nThank you for playing this game.')
        return False
    else:
        print('\nPlease fill in the correct command!')
        return end_or_restart()

def flip_decision(new_squarelotron, selection, ring):
    """Return the updated squarelotron based on user's selections of flip and ring"""
    if selection == 'U':
        return upside_down_flip(new_squarelotron, ring)
    elif selection == 'L':
        return left_right_flip(new_squarelotron, ring)
    elif selection == 'M':
        return main_diagonal_flip(new_squarelotron, ring)
    elif selection == 'I':
        return inverse_diagonal_flip(new_squarelotron, ring)
    else:
        return False

def flip_exection(squarelotron):
    """Consolidate flips & selections functions to keep the game running or end the program"""
    new_squarelotron = copy.deepcopy(squarelotron)
    key = True
    while key:
        selection = flip_selection()
        ring = ring_selection()
        new_squarelotron = flip_decision(new_squarelotron, selection, ring)
        print_map(new_squarelotron)
        key = user_decision()
    if end_or_restart():
        print_map(squarelotron)
        flip_exection(squarelotron)
    else:
        return False

def main():
    """Initialize the game and execute the main function"""
    squarelotron = make_squarelotron(flat_list)
    print_map(squarelotron)
    flip_exection(squarelotron)

if __name__ == "__main__":
    main()
