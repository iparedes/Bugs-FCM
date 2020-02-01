from VM import *


SEARCH_RADIUS=1

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
        VM.__init__(self)

        # Add bug registers
        # SRR: Search radius. Determines the field of vision of the bug
        # SRF: Search for. Holds the type of item to search for (1:food)
        # DRS: Holds the result of the search operation. It codifies the directions where the items were found
        #       in the four lower bits WSEN
        nr=['SRR,''SRF','DRS']
        REGS+=nr

        self._srridx=REGS.index('SRR')
        self._srfidx=REGS.index('SRF')
        self._drsidx=REGS.index('DRS')

        self.set_reg('SRR',SEARCH_RADIUS)
        self.set_reg('SRF',0)
        self.set_reg('DRS',0)

        self.MyCell=cell


    def _srf(self):
        radius=self.get_reg(self._srridx)
        item_type=self.get_reg(self._srfidx)
        # Gets list of cells in the view radius
        cells_in_radius=self.MyCell.get_neighbors(radius)
        cells_with_item=[c for c in cells_in_radius if c.things[item_type]]
        pass

    def _wlkt(self):
        pass

    def _wlkw(self):
        pass

    def _wlk(self):
        pass






