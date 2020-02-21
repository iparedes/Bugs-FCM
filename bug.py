from VM import *


SEARCH_RADIUS=1
STAMINA=50

# Coded in five lower bits CWSEN
CODE_DIRS={'N':1,'E':2,'S':4,'W':8,'C':16}

class Bug(VM):

    """Let's talk about the capability of finding food and moving towards it. This probably means that there are other
    instruction to move away from

    SRCF (search food). Looks for food in a radius determined by a property of the bug. The result is to code in a register
    the directions where there are food (just the direction for the first step)

    Another approach would be to have a generic function to search and moveaway or movto, that uses the value of a register to determine what
    to search for, then put the direction values on a fixed register"""


    """
    Need to find a way to allow the bug to evolve. Right now I am adding registers, instructions and logic to emulate
    a sensor. Could that somehow be packetized? Shouldnt use new registers, but the general ones...
    """


    def __init__(self,cell=None):

        # Add bug registers
        # SRR: Search radius. Determines the field of vision of the bug
        # SRF: Search for. Holds the type of item to search for (1:food)
        # DRS: Holds the result of the search operation. It codifies the directions where the items were found
        #       in the five lower bits CWSEN (C is Center)
        # NRG: The energy level of the bug. Reduced by executing instructions, increased by food
        # STM: Stamina. The number of instructions that can be executed by the bug in each cycle
        nr=['SRR','SRF','DRS','NRG','STM']
        global REGS
        REGS+=nr

        VM.__init__(self)

        self._srridx=REGS.index('SRR')
        self._srfidx=REGS.index('SRF')
        self._drsidx=REGS.index('DRS')
        self._nrgidx=REGS.index('NRG')
        self._stmdix=REGS.index('STM')

        self.set_reg('SRR',SEARCH_RADIUS)
        self.set_reg('SRF',0)
        self.set_reg('DRS',0)
        self.set_reg('STM',STAMINA)

        self.MyCell=cell

    # Executes code at pos
    def cycle(self,pos):
        self.set_reg('PC',pos)
        steps=self.get_reg(self._stmdix)
        run=1
        while steps and run:
            run=self.step()
            steps-=1


    # DRS codes directions in the five lower bits. CWSEN (C is Center)
    def _srcf(self):
        radius=self.get_reg(self._srridx)
        item_type=self.get_reg(self._srfidx)
        # Gets list of cells in the view radius
        cells_in_radius=self.MyCell.get_neighbors(radius)
        cells_with_item=[c for c in cells_in_radius if c.things[item_type]]
        dirs=[]
        for c in cells_with_item:
            if c==self.MyCell:
                dirs+=['C']
            else:
                dirs+=self.MyCell.dirs_to(c)
        dirs=list(set(dirs))
        drs=0
        for d in dirs:
            drs+=CODE_DIRS[d]
        self.set_reg('DRS',drs)

    def _wlkt(self):
        pass

    def _wlkw(self):
        pass

    def _wlk(self):
        pass






