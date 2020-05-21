class player:
    def __init__ (self, name, b):
        self.name = name
        self.b = b
    win = False

class space:
    def __init__ (self, spa, hit, ship):
        self.spa = spa
        self.hit = hit
        self.ship = ship


def makeboard():
    alp = ["a","b","c","d","e","f","g","h","i","j"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    board = []
    for x in range(10):
        board.append([x])
        for y in range(9):
            board[x].append(y)

    for i in range(10):
        for j in range(10):
            board[i][j] = alp[j] + num[i]
           
    for a in range(10):
        for b in range(10):
            board[a][b] = space(str(board[a][b]), False, False)
            #print(board[a][b].value, end=" ")
       # print("\n")
    
    return board


def showspace(board):
    for i in range(10):
        for j in range(10):
            print (board[i][j].spa, end=" ")
        print("\n")

def showships(board):
    for i in range(10):
        for j in range (10):
            if board[i][j].ship == True:
                print("O", end="  ")
            else:
                print("X", end="  ")
        print("\n")

def setships(board):
    #showspace(board)
    print("Select space for your ships. Type \"done\" when you are ready")
    
    x = input()
    if x == "done":
        print("Player done setting ships")
        return board
    for i in range(10):
        for j in range(10):
            if x == board[i][j].spa:
                print(board[i][j].spa)
                board[i][j].ship = True
                showships(board)
                break
    setships(board)

def game():
    player1 = player("Player 1", makeboard())
    player2 = player("Player 2", makeboard())
    
    print("Player 1: Set ships \n")
    showspace(player1.b)
    setships(player1.b)
    print("Player 1 done \n")
    #print("Press enter \n")
    #input()
    print("Player 2: Set ships \n")
    showspace(player2.b)
    setships(player2.b)
    while player1.win == False & player2.win == False:
        turn(player1, player2)
        if player2.win == True:
            print("Game Over, Player 1 wins")
            return
        turn(player2, player1)
    print("Game over, player 2  wins")
    return
    
def turn (turnp, opponentboard):
    print (turnp.name + "'s turn")
    print ("Enter space")
    inp = input()
    for x in range(10):
        for y in range(9):
            #print (board.b[x][y].spa)
            #print(inp)
            if inp == opponentboard.b[x][y].spa:
                if opponentboard.b[x][y].ship == True:
                    opponentboard.win = True
                    print(turnp.name + " wins!")
                    return
    return
    
game()




