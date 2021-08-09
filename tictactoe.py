'''
Author: Spyros Tsioupros

'''

def enter_this(row, col, plaisio):
    #this function enter the inputs on the boxes (X or O)

    if turn:
        plaisio[row][col] = "X" 
        return 

    plaisio[row][col] = "O"
#end of enter_this


def display_plaisio(plaisio):
    #this function display the game status

    for row in range( len(plaisio) ):
        print("\t\t +----------------------------------------------+")
        print("\n\t\t |\t",plaisio[row][0],"\t|\t" ,plaisio[row][1],"\t|\t", plaisio[row][2], "\t|\t\t\n")

    print("\t\t +----------------------------------------------+")
#end of display_plaisio


def check_winner(plaisio):
    #this function check if there are 3 "O" on every list from the end_game function and return the right result

    r, l, x, s = end_game(plaisio)

    if 3 in r:
        return 0 #player_o win
    elif 0 in r:
        return 1 #player_x win

    if 3 in l:
        return 0 #player_o win
    elif 0 in l:
        return 1 #player_x win
    
    if x == 3:
        return 0 #player_o win
    elif x == 0:
        return 1 #player_x win

    if s == 3:
        return 0 #player_o win
    elif s == 0:
        return 1 #player_x win
    
#end of check_winner


def end_game(plaisio):
    #store the "O" from every row, comlum on lists and the diagonals "O" on variables and return them

    r1 = 0
    r2 = 0
    r3 = 0
    #store the number of "O" from every row on a list
    for i in range(3):
        if "O" in plaisio[0][i]: #0 row
            r1 += 1
    for i in range(3):
        if "O" in plaisio[1][i]: #1 row
            r2 += 1
    for i in range(3):
        if "O" in plaisio[2][i]: #2 row
            r3 += 1
    r_list = [r1, r2, r3]

    l1 = 0
    l2 = 0
    l3 = 0        
    #store the number of "O" from every comlumn on a list
    for i in range(3):
        if "O" in plaisio[i][0]: #0 column
            l1 += 1
    for i in range(3):
        if "O" in plaisio[i][1]: #1 column
            l2 += 1
    for i in range(3):
        if "O" in plaisio[i][2]: #2 column
            l3 += 1
    l_list = [l1, l2, l3]

    x = 0
    #store the number of "O" from diagonla on a variable
    for i in range(3):
        if "O" in plaisio[i][i]:
            x+=1

    #store the number of "O" from oposite diagonal on a variable
    s = 0
    if "O" in plaisio[0][2]:
        s+=1
    if "O" in plaisio[1][1]:
        s+=1
    if "O" in plaisio[2][0]:
        s+=1

    return r_list, l_list, x, s
#end of end_game


#--------------------------------main 
if __name__ == "__main__":
    
    #attributes
    plaisio = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

    ROUNDS = 9
    turn = True #when turn==True player_x play
    rounds = 0 #counter of rounds


    #players enter their names
    player_o = input("Enter the name of player O: ")
    player_x = input("Enter the name of player X: ")

    #there are 9 turns
    while rounds < ROUNDS:
        if turn: #playerX turn
            print("\n",player_x, " ,enter the X on a box------------------")

            row = int( input("1. Enter the row (0-2): ") )
            col = int( input("2. Enter the column (0-2): ") )
                
            while (col >= 3 or row >= 3) or plaisio[row][col] != "":
                row = int( input("Wrong input, enter the row again (0-2): ") )
                col = int( input("Wrong input, enter the column again (0-2): ") )

            enter_this(row, col, plaisio) #put the X on this box

            turn = False

        else: #playerO turn
            print("\n",player_o, " ,enter the O on a box------------------")

            row = int( input("1. Enter the row (0-2): ") )
            col = int( input("2. Enter the column (0-2): ") )
                
            while (col >= 3 or row >= 3) or plaisio[row][col] != "":
                row = int( input("Wrong input, enter the row again (0-2): ") )
                col = int( input("Wrong input, enter the column again (0-2): ") )

            enter_this(row, col, plaisio) #put the O on this box

            turn = True
        
        rounds+=1
        display_plaisio(plaisio)

    win = 3 #initial draw
    win = check_winner(plaisio) 

    print("\n-----------------------")
    if win == 0:
        print("The winner is: ", player_o)
    elif win == 1:
        print("The winner is: ", player_x)
    else:
        print("Draw...")


