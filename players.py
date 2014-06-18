"""These classes extend the base Player class in c4.py """

import c4
import random
import numpy as np
import copy

class Human(c4.Player):
    """gets user input"""
    name = "Human"
    strategy = "User controlled player"
    def get_next_move(self,board):
        move = int(raw_input("Column: "))
        if not board.data[0,move] is None:
            print("Column filled, choose another")
            move = self.get_next_move(board)
        return move

class Novice(c4.Player):
    """Makes random moves"""
    name = "Novice"
    strategy = "Make a random move"
    def get_next_move(self,board):
        return random.choice([i for i in range(board.shape[1]) if board.data[0,i] == None])
        
class Beginner(c4.Player):
    name = "Beginner"
    strategy = "1. Win if possible\n2. Block opponent wins\n3. Make a random move"
    def get_next_move(self,board):
        if board.p1 is self:
            opp = board.p2
        else:
            opp = board.p1
        test = copy.deepcopy(board)
        for i in range(board.shape[1]):
            test.make_move(i,self)
            if test.check_for_win(self):
                return i
            test = copy.deepcopy(board)
        for i in range(board.shape[1]):
            test.make_move(i,opp)
            print(test)
            if test.check_for_win(opp):
                return i
            test = copy.deepcopy(board)
        return random.choice([i for i in range(board.shape[1]) if board.data[0,i] == None])
