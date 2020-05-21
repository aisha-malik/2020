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
    alp = ["A","B","C","D","E","F","G","H","I","J"]
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
    uh=0
    x = input()
    if x.lower() == "done":
        print("Player done setting ships")
        return board
    else:
        
        for i in range(10):
            for j in range(10):
                if x.lower() == (board[i][j].spa).lower():
                    #print(board[i][j].spa)
                    board[i][j].ship = True
                    showships(board)
                    uh=1
                    break
                
    
                
    if uh == 0:
        print("Input not valid")
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

#def runthruinp(txt):
    
 #   if inp.lower() == txt.lower():
  #      return
   # else:
    #    print("Input not valid")
     #   runthruinp(inp,txt)

def runthruspace(board, txt):
    print("Enter space")
    inn = input()
    if txt =="space":
        for x in range(10):
            for y in range(9):
                #print(board.b[x][y].spa)
                if inn.lower() == ((board.b[x][y].spa)).lower():
                    return inn
                
    
        print("Input not valid")
        #print(txt)
        runthruspace(board, txt)
    else:
        print ("idk")
        
def turn (turnp, opponentboard):
    print (turnp.name + "'s turn")
    
    inp = runthruspace(opponentboard, "space")
    for x in range(10):
        for y in range(9):
            #print (board.b[x][y].spa)
            #print(inp)
            if inp == (opponentboard.b[x][y].spa).lower():
                if opponentboard.b[x][y].ship == True:
                    opponentboard.win = True
                    print(turnp.name + " wins!")
                    return
    return
    
game()




