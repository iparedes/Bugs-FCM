from cell import *
from bug import *


class World:

    # dim: board dimensions (rows, columns)
    def __init__(self,dim=(10,10)):
        # Board
        # Bugs
        self.Board=Board(dim[0],dim[1])
        self.Bugs=[]


    def add_bug(self,B):
        self.Bugs.append(B)

    # progs is a filename
    # Creates the bug and adds it to the world in a random cell
    def spawn_bug(self,prog):
        c=self.Board.get_rand_cell()
        B=Bug(c)
        B.load_file(prog)
        self.Bugs.append(B)

    # Executes a step on each bug
    def step(self):
        for b in self.Bugs:
            r=b.step()


    def go(self):
        while(1):
            self.step()
