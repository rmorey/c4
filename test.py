import c4
import players

p1 = players.Beginner()
p2 = players.Beginner()
g = c4.Game(p1,p2)

g.play_game()
