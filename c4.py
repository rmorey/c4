"""Connect Four"""

import numpy as np

class Player:
    """Base class for c4 player"""
    def __init__(self):
        self.name = "Player"
    def __str__(self): 
        return self.name
    def get_next_move(self,board):
        return 1

class Game:
    """Game class"""
    def __init__(self, p1, p2):
        self.board = Board()
        if not (isinstance(p1,Player) and isinstance(p2,Player)):
            print("Invalid Player object")
        self.moves = []
        self.state = "pregame"
        self.p1 = p1
        self.p2 = p2
        self.board.p1 = p1
        self.board.p2 = p2
        p1.name = "p1"
        p2.name = "p2"
        self.turn = p1
        self.winner = None
        self.gameover = False
    def play_game(self):
        self.state = "midgame"
        while not self.gameover:
            self.play_next_move()
    def play_next_move(self):
        move = self.turn.get_next_move(self.board)
        self.moves.append(move)
        self.board.make_move(move,self.turn)
        print(self.board)
        win = self.board.check_for_win(self.turn)
        if win:
            self.winner = self.turn
            print(self.winner + " wins")
            self.gameover = True
        else:    
            if self.turn is self.p1:
                self.turn = self.p2
            else:
                self.turn = self.p1

class Board:
    """holds game state data"""
    def __init__(self, x=7, y=6):
        self.data = np.empty((y,x),object)
        self.shape = (y,x)
    def __str__(self):
        strings = str(np.array([str(i) for i in self.data.flatten()]).reshape(self.shape[0],self.shape[1]))
        return strings
    def make_move(self,c,p):
        for r in range(self.shape[0]-1,-1,-1):
            if not self.data[r,c]:
                self.data[r,c] = p
                return r
        return -1
    def check_for_win(self,p):
        wins = []
        trues = np.array([[True]*4])
        spots = (self.data == p)
        h = find_subarray(spots,trues)
        for w in h:
            wins.append(w + (w[0],w[1]+3))
        trues = trues.transpose()
        v = find_subarray(spots,trues)
        for w in v:
            wins.append(w + (w[0]+3,w[1]))
        trues = np.identity(4,dtype=bool)
        d1 = find_subarray(spots,trues)
        for w in d1:
            wins.append(w + (w[0]+3,w[1]+3))
        trues = np.fliplr(trues)
        d2 = find_subarray(spots,trues)
        for w in d2:
            wins.append(w + (w[0]-3,w[1]-3))
        return wins

def find_subarray(a,sub):
    """Finds all occurencces of array sub in a"""
    if a.shape[0] < sub.shape[0] or a.shape[1] < sub.shape[1]:
        return False
    result = []
    for r in range(a.shape[0]-sub.shape[0]+1):
        for c in range(a.shape[1]-sub.shape[1]+1):
            if (a[r:r+sub.shape[0],c:c+sub.shape[1]] == sub).all():
                result.append((r,c))
    return result
        
