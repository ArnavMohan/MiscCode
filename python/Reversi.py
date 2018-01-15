from tkinter import *
import random

class ReversiSquare(Canvas):
    '''represents a square in the Reversi game'''

    def __init__(self,master,r,c):
        '''ReversiSquare(master,r,c)
        creates a new blank Reversi square at (r,c)'''
        # create and place the widget
        Canvas.__init__(self,master,width=50,height=50,bg='medium sea green')
        self.grid(row=r,column=c)
        # set the attributes
        self.position = (r,c)
        self.color = None
        # bind button click to placing a piece
        self.bind('<Button>',master.get_click)

    def get_position(self):
        '''ReversiSquare.get_position() -> (int,int)
        returns (row,column) of square'''
        return self.position

    def get_color(self):
        '''ReversiSquare.get_color() -> obj
        returns color of piece on square
        returns None if square is empty'''
        return self.color

    def make_color(self,color):
        '''ReversiSquare.make_color(color)
        changes color of piece on square to specified color'''
        self.create_oval(10,10,44,44,fill=color)
        self.color = color  # update color attribute


class ReversiTestSquare():
    '''special ReversiSquare used for move testing'''

    def __init__(self,r,c):
        '''ReversiTestSquare(r,c) -> ReversiTestSquare
        creates a new ReversiTestSquare'''
        self.position = (r,c)
        self.color = None

    def get_position(self):
        '''ReversiSquare.get_position() -> (int,int)
        returns (row,column) of square'''
        return self.position

    def get_color(self):
        '''ReversiSquare.get_color() -> obj
        returns color of piece on square
        returns None if square is empty'''
        return self.color

    def make_color(self,color):
        '''ReversiSquare.make_color(color)
        changes color of piece on square to specified color'''
        self.color = color

        
class ReversiGame(Frame):
    '''represents a game of Reversi'''

    def __init__(self,master,computerPlayer=None):
        '''ReversiGame(master,[computerPlayer])
        creates a new Reversi game
        computerPlayer is the computer player (2-player by default)'''
        # initialize the Frame
        Frame.__init__(self,master,bg='white')
        self.grid()
        # set up game data
        self.squares = {}  # dict to store the squares
        self.colors = ('black','white')  # players' colors
        # set up computer player
        if computerPlayer:
            self.computerPlayer = self.colors.index(computerPlayer)
        else:
            self.computerPlayer = -1
        # set current player to white, so that black will go first
        self.currentPlayer = 1
        # create the squares
        for row in range(8):
            for col in range(8):
                self.squares[(row,col)] = ReversiSquare(self,row,col)
        # set up starting position
        self.squares[(3,3)].make_color(self.colors[1])
        self.squares[(3,4)].make_color(self.colors[0])
        self.squares[(4,3)].make_color(self.colors[0])
        self.squares[(4,4)].make_color(self.colors[1])
        # set up scoreboard and status markers
        self.rowconfigure(8,minsize=3)  # leave a little space
        self.turnSquares = []  # to store the turn indicator squares
        self.scoreLabels = []  # to store the score labels
        # create indicator squares and score labels
        for i in range(2):  
            self.turnSquares.append(ReversiSquare(self,9,7*i))
            self.turnSquares[i].make_color(self.colors[i])
            self.scoreLabels.append(Label(self,text='2',font=('Arial',18)))
            self.scoreLabels[i].grid(row=9,column=1+5*i)
        self.update_status()

    def get_click(self,event):
        '''ReversiGame.get_click(event)
        event handler for mouse click
        Gets click data and sends to place_piece'''
        if self.currentPlayer != self.computerPlayer and \
           event.widget.get_color() == None:
            # can only place a piece in a blank square
            (row,col) = event.widget.get_position()
            self.place_piece((row,col))
                
    def place_piece(self,coords):
        '''ReversiGame.place_piece(coords)
        places the current player's piece in the given square if the
          square is empty and the move is legal
        also flips necessary pieces and goes to other player's turn'''
        (row,col) = coords
        # flip any pieces and check how many got flipped
        numFlipped = self.flip_pieces(row,col)
        if numFlipped > 0:  # the move must flip pieces
            # set the current square to the current player's color
            self.squares[coords].make_color(self.colors[self.currentPlayer])
            self.update_status()   # update the scoreboard, go to other player

    def flip_pieces(self,r,c,checkingOnly=False,board=None):
        '''ReversiGame.flip_pieces(r,c,[checkingOnly],[board]) -> int
        returns number of pieces flipped when a piece is played at (r,c)
          checkingOnly True just computes, doesn't actually flip
          checkingOnly False also flips the pieces
        board is an optional test board -- if omitted, uses the "real" board'''
        if not board:
            board = self.squares
        # get player colors
        currentcolor = self.colors[self.currentPlayer]
        othercolor = self.colors[1-self.currentPlayer]
        flipped = 0  # counts flipped pieces
        # loop over the 8 possible directions
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr==0 and dc==0:  # non-direction
                    continue
                # look at the first square in the given direction
                (row,col) = (r+dr,c+dc)
                counter = 0  # keep track of how many squares have a
                             # piece of the opposite color
                # keep looking as long as we have pieces of the opposite
                #   color and we're still on the board
                while (0 <= row < 8) and (0 <= col < 8) and \
                      board[(row,col)].get_color() == othercolor:
                    (row,col) = (row+dr,col+dc) # continue moving in this direction
                    counter += 1  # increment the count of number of stones flipped
                # the next stone must be of the current player's color
                #  (and still on the board)
                if (0 <= row < 8) and (0 <= col < 8) and \
                   board[(row,col)].get_color() == currentcolor:
                    # this direction will get flipped
                    flipped += counter  # update the overall flipped counter
                    if not checkingOnly:  # if not just checking, flip them!
                        for i in range(1,counter+1):
                            board[(r+i*dr,c+i*dc)].make_color(currentcolor)
        return flipped

    def update_status(self,playerPassed=False):
        '''Reversi.update_status([playerPassed])
        updates the scoreboard, goes to next player's turn
        checks if a player has a legal move; if not, calls itself with
          playerPassed=True
        if both players can't move, game ends.'''
        # switch player's roles and update current player
        oldPlayer = self.currentPlayer
        newPlayer = 1 - self.currentPlayer
        self.currentPlayer = newPlayer
        # update the turn indicator
        self.turnSquares[newPlayer]['highlightbackground'] = 'blue'
        self.turnSquares[oldPlayer]['highlightbackground'] = 'white'
        # compute the scores
        scores = [0,0]
        for row in range(8):
            for column in range(8):
                # get the color and add to that player's count
                color = self.squares[(row,column)].color
                if color:
                    scores[self.colors.index(color)] += 1
        # update the score displays
        for i in range(2):
            self.scoreLabels[i]['text'] = scores[i]
        # check if the current player can move
        for row in range(8):
            for column in range(8):
                if not self.squares[(row,column)].color and \
                   self.flip_pieces(row,column,True) > 0:
                    if self.currentPlayer == self.computerPlayer:
                        # computer player's turn
                        self.after(1000,self.take_computer_turn)
                    return  # a move is available, we can stop checking
        # player can't move, go to other player unless 2 passes in a row
        if not playerPassed:
            # current player must pass -- go to other player
            self.update_status(playerPassed=True)
        else: # game is over!
            # remove the turn indicator
            self.turnSquares[newPlayer]['highlightbackground'] = 'white'
            # figure out who won and display winner
            if scores[0] > scores[1]:
                endgameMessage = 'Black wins!'
            elif scores[0] < scores[1]:
                endgameMessage = 'White wins!'
            else:
                endgameMessage = "It's a tie!"
            Label(self,text=endgameMessage,font=('Arial',18)).grid(row=9,column=2,columnspan=4)

    def get_move_value(self,row,column):
        '''ReversiGame.get_move_value(row,column) -> int
        returns the move value of the current player playing at (row,column)
        looks at all of opponent's possible responses'''
        # create test board
        testBoard = {}
        for r in range(8):
            for c in range(8):
                # create a new test square with the same color as the real board
                testBoard[(r,c)] = ReversiTestSquare(r,c)
                testBoard[(r,c)].make_color(self.squares[(r,c)].get_color())
        # make computer's move on the test board
        self.flip_pieces(row,column,board=testBoard)
        testBoard[(row,column)].make_color(self.colors[self.currentPlayer])
        # switch to opponent to look at opponent's responses
        self.currentPlayer = 1 - self.currentPlayer
        bestResponseValue = 9999  # initialize best response tracking variable
        # loop through opponent's moves
        for row in range(8):
            for column in range(8):
                if not testBoard[(row,column)].color and \
                   self.flip_pieces(row,column,True,board=testBoard):
                    # make a new test board for the response
                    responseBoard = {}
                    for r in range(8):
                        for c in range(8):
                            responseBoard[(r,c)] = ReversiTestSquare(r,c)
                            responseBoard[(r,c)].make_color(testBoard[(r,c)].get_color())
                    # make human's move on the response board
                    self.flip_pieces(row,column,board=responseBoard)
                    responseBoard[(row,column)].make_color(self.colors[self.currentPlayer])
                    # get the board value
                    responseValue = self.get_board_value(responseBoard,1-self.currentPlayer)
                    # see if this is an improvement
                    if responseValue < bestResponseValue:
                        bestResponseValue = responseValue
        # return player back to computer player
        self.currentPlayer = 1 - self.currentPlayer
        # return result (use testBoard if human doesn't have a move)
        if bestResponseValue != 9999:
            return bestResponseValue
        else:
            return self.get_board_value(testBoard,self.currentPlayer)

    def get_board_value(self,board,player):
        '''ReversiGame.get_board_value(board,player) -> int
        returns the value of the board for the given player'''
        squarePointValues = [[99,-8,8,6,6,8,-8,99],
                             [-8,-24,-4,-3,-3,-4,-24,-8],
                             [8,-4,7,4,4,7,-4,8],
                             [6,-3,4,0,0,4,-3,6],
                             [6,-3,4,0,0,4,-3,6],
                             [8,-4,7,4,4,7,-4,8],
                             [-8,-24,-4,-3,-3,-4,-24,-8],
                             [99,-8,8,6,6,8,-8,99]]
        value = 0
        for row in range(8):
            for col in range(8):
                if board[(row,col)].get_color() == self.colors[player]:
                    value += squarePointValues[row][col]  # current player
                elif board[(row,col)].get_color() == self.colors[1-player]:
                    value -= squarePointValues[row][col]  # other player
        return value

    def take_computer_turn(self):
        '''ReversiGame.take_computer_turn()
        takes the computer turn in the game
        uses a minimax algorithm to select a move'''
        bestMoveValue = -9999  # initialize best move tracking variable
        for row in range(8):
            for column in range(8):
                if not self.squares[(row,column)].color:
                    if self.flip_pieces(row,column,True) > 0:
                        # get value of the move
                        moveValue = self.get_move_value(row,column)
                        # check if better or equally-good
                        if moveValue > bestMoveValue: # better
                            bestMoves = [(row,column)] # start new list
                            bestMoveValue = moveValue  # update tracking variable
                        elif moveValue == bestMoveValue: # just as good
                            bestMoves.append((row,column)) # add to list
        # pick a "best" move at random
        self.place_piece(random.choice(bestMoves))


def play_reversi(computerPlayer=None):
    '''play_reversi()
    starts a new game of Reversi'''
    root = Tk()
    root.title('Reversi')
    RG = ReversiGame(root,computerPlayer)
    RG.mainloop()
