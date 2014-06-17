import c4

class Human(c4.Player):
    """gets user input"""
    def get_next_move(self,board):
        move = int(raw_input("Column: "))
        if not board.data[0,move] is None:
            print("Column filled, choose another")
            move = self.get_next_move(board)
        return move
