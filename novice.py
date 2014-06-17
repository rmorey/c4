import c4
import random

class Novice(c4.Player):
    """Makes random moves"""
    def get_next_move(self,board):
        cols = [i for i in range(board.shape[1]) if board.data[0,i] == None]
        move = random.choice(cols)
        return move
