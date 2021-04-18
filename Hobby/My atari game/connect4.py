from itertools import groupby, chain
import os,time,re

def diagonalPos(board,columns,rows):
    for diag in ([(j, i - j) for j in range(columns)] for i in range(columns + rows -1)):
        yield [board[i][j] for i, j in diag if i >= 0 and j >= 0 and i < columns and j < rows]

def diagonalNeg(board,columns,rows):
    for diag in ([(j, i - columns + j + 1) for j in range(columns)] for i in range(columns + rows - 1)):
        yield [board[i][j] for i, j in diag if i >= 0 and j >= 0 and i < columns and j < rows]

class Game:
    gameState = True; playerState = True
    def __init__(self,columns=7,rows=6,amountWin=4):
        self.columns = columns
        self.rows = rows
        self.win = amountWin
        self.board = [['-'] * rows for _ in range(columns)]
    
    def printBoard(self):
        print('  '.join(map(str, range(self.columns)))) # Print column numbers
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.columns))) # Print state of board

    def insertColour(self,column,colour):
        insertCol = self.board[column]
        i = -1 # Set index to last value of column (can be 6)
        if insertCol[0]!=('-'):
            print('Column is full please choose a different column!')
            time.sleep(1)
            Game.changePlayerState(1)
            # Return to column select but keep player the same
        else:   
            while insertCol[i]!='-':
                i-=1 # Iterates to row above '-' value        
            insertCol[i]=colour
            Game.changePlayerState(0)

    def changePlayer(self,colour):
        playerState = Game.getPlayerState()
        if colour=='Y' and playerState:
            colour='R'
        elif colour=='R' and playerState:
            colour='Y'
        else:
            colour=colour
        return colour

    def checkWin(self):
        lines = (
			self.board, # columns
			zip(*self.board), #rows
            diagonalPos(self.board, self.columns, self.rows), # positive diagonals
			diagonalNeg(self.board, self.columns, self.rows) # negative diagonals
            )
        for line in chain(*lines):
            for colour,group in groupby(line):
                if colour != '-' and len(list(group)) >= self.win:
                    os.system('clear')
                    if colour =='Y':
                        for _ in range(10):
                            print('\033[33m'+f'{colour} WON THE GAME!'+'\033[0m')
                            time.sleep(0.5)
                            os.system('clear')
                            time.sleep(0.5)
                    else:
                        for _ in range(10):
                            print('\033[91m'+f'{colour} WON THE GAME!'+'\033[0m')
                            time.sleep(0.5)
                            os.system('clear')
                            time.sleep(0.5)
                    Game.changeGameState()
        # Check diagonals
    @classmethod
    def changePlayerState(cls,value):
        if value==1:
            cls.playerState = False
        elif value==0:
            cls.playerState = True

    @classmethod
    def getPlayerState(cls):
        return cls.playerState
    @classmethod
    def changeGameState(cls):
        cls.gameState = False

colour = 'Y'
os.system('clear')
print('Welcome to connect 4!')
time.sleep(1)
game = Game()

while game.gameState:
    os.system('clear')
    game.printBoard()
    try:
        colInput = int(input('Which column would you like to insert into (Type non column value to quit)? '))
        game.insertColour(colInput,colour)
        game.checkWin()
        colour = game.changePlayer(colour)
    except:
        quitresp = input('Would you like to quit? Y/N ')
        regexp = re.compile(r'y(es)?$',flags=re.IGNORECASE)
        regexp = regexp.match(quitresp)
        if regexp:
            os.system('clear')
            exit('Quitting application')
        else:
            print('Invalid column entered!')
            time.sleep(1)
            os.system('clear')
