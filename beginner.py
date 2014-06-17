import c4

class Beginner(c4.Player):
    def find_pot_win(self,board):
        ver = (board.data == self)
        sub = np.array([[True]*3])
    def get_next_move(self,board):
        
