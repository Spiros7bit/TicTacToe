plaisio = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

ROUNDS = 9
turn = True #when turn==True player_x play
player_x = "player1"
player_o = "player2"
rounds = 0 #counter of rounds


def enter_this(row, col, plaisio):
    if turn:
        plaisio[row][col] = "X" 
        return 

    plaisio[row][col] = "O"
#end of enter_this

def display_plaisio(plaisio):
    for row in range( len(plaisio) ):
        print("\t\t +----------------------------------------------+")
        print("\n\t\t |\t",plaisio[row][0],"\t|\t" ,plaisio[row][1],"\t|\t", plaisio[row][2], "\t|\t\t\n")

    print("\t\t +----------------------------------------------+")
#end of display_plaisio

def check_winner(plaisio):
    r, l, x, s = end_game(plaisio)

    if 3 in r:
        return False #player_o win
    elif 0 in r:
        return True #player_x win

    if 3 in l:
        return False #player_o win
    elif 0 in l:
        return True #player_x win
    
    if x == 3:
        return False #player_o win
    elif x == 0:
        return True #player_x win

    if s == 3:
        return False #player_o win
    elif s == 0:
        return True #player_x win
    
#end of check_winner

def end_game(plaisio):

    r1 = 0
    r2 = 0
    r3 = 0
    #rows
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
    #columns
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
    for i in range(3):
        if "O"in plaisio[i][i]:
            x+=1
        
        if "O" in plaisio[i][i]:
            x+=1

        if "O" in plaisio[i][i]:
            x+=1

    s = 0
    if "O" in plaisio[0][2]:
        s+=1

    if "O" in plaisio[1][1]:
        s+=1

    if "O" in plaisio[2][0]:
        s+=1

    return r_list, l_list, x, s
#end of end_game
                      














###########################main program if __name__ = "__main__":

player_o = input("Enter the name of player O: ")
player_x = input("Enter the name of player X: ")


while rounds < ROUNDS:
    if turn :
        print(player_x, " ,enter the X on a box------------------")

        row = int( input("1. Enter the row: ") )
        col = int( input("2. Enter the column: ") )
            
        while col >= 3 or row >= 3:
            row = int( input("Wrong input, enter the row again: ") )
            col = int( input("Wrong input, enter the column again: ") )

        enter_this(row, col, plaisio)

        turn = False

    else:
        print(player_o, " ,enter the O on a box------------------")

        row = int( input("1. Enter the row: ") )
        col = int( input("2. Enter the column: ") )
            
        while col >= 3 or row >= 3:
            row = int( input("Wrong input, enter the row again: ") )
            col = int( input("Wrong input, enter the column again: ") )

        enter_this(row, col, plaisio)

        turn = True
    
    rounds+=1
    display_plaisio(plaisio)


win = check_winner(plaisio)

if win == False:
    print("The winner is: ", player_o)
elif win == True:
    print("The winner is: ", player_x)
else:
    print("Draw...")


