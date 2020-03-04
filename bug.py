from VM import *
from analyzer import *
from Brain import *
import cell
import random


SEARCH_RADIUS=1
STAMINA=50

# Coded in five lower bits CWSEN
CODE_DIRS={'N':1,'E':2,'S':4,'W':8,'C':16}

# The bug has a Fuzzy Cognitive Map to determine what actions to activate
# Some concepts are inputs (sensors). These are only origin of edges, and are related to a register in the VM.
#   These are equivalent to senses in the bug, every time that the FCM is activated, the values of the
#   concept are updated according to the value in the register
# Other concepts, that terminate edges, may be associated to a piece of code that is executed if the concept
#   is activated


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


    def __init__(self,cell,brand=1):

        # Add bug registers
        # SRR: Search radius. Determines the field of vision of the bug
        # SRF: Search for. Holds the brand of the item to search for (0:food, >1 bug)
        # DRS: Holds the result of the search operation. It codifies the directions where the items were found
        #       in the five lower bits CWSEN (C is Center)
        # NRG: The energy level of the bug. Reduced by executing instructions, increased by food
        # STM: Stamina. The number of instructions that can be executed by the bug in each cycle
        nr=['SRR','SRF','DRS','NRG','STM']
        global REGS
        REGS+=nr

        super().__init__()

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
        self.MyCell.bug_in(self)
        self.Brain=None
        self.Running=0 # If 0 is not running a program and can activate the brain
        if brand > 1:
            self.set_brand(brand)

    # loads a file with one or more subprograms in the bug
    def load_file(self,file):
        logger.info(file)
        stream=FileStream(file)
        #stream = antlr4.InputStream("ADD R1,R2\n")
        analyzer=Analyzer(stream)
        analyzer.Walk()
        # todo: Get it here - this contains info to:1-compila and load program in memory 2-build the FCM
        # At this point, analyzer.Context['program'] is a list of dictionaries, each of one representing a program
        # and containing metadata and the sequence of pseudocode
        # {'MemPointer','prog_type','prog_name','Sequence','reg'}
        self.Programs=analyzer.Context['program']
        for p in self.Programs:
            # Compile into memory and add the start address as metadata
            prog=self._compile(p['Sequence'])
            pos=self._load(prog)
            # Add a new key with the start address of the program
            p['pos']=pos
        self.Brain=Brain(self.Programs)
        #self.Programs=self._compile(analyzer.Context['program'])

    # # files is a list of filenames to load
    # def load_files(self,files):
    #     for f in files:
    #         p=self.load_file(f)
    #         if p<0:
    #             logger.error("Unable to load "+f)


    def step(self):
        if self.Running:
            self.Running=super().step()
        else:
            self.Running=1
            self.activate()
            self.Running=super().step()


    # In the future this function will select what program to activate based on the FCM
    # by now, we just activate the first program in memory
    def activate(self):
        #prog=list(self.PAT)[0]
        #self.run(prog)

        # todo: need to finish this
        # 1-Execute sensors code
        for s in self.Brain.sensors:
            self.run(s['pos'])
            self.execute_til_end()
            reg=s['reg']
            val=self.get_reg(reg)
            idx=s['idx']
            self.Brain.set_concept_value(idx,val)
        # 2-Update concepts
        self.Brain.update_concepts_values()
        # 3-Select winner and return memory pos to execute
        winner=self.Brain.max_actor()
        pos=self.Brain.actors[winner]['pos']
        self.run(pos)
        # after this, in the next step, the winner code will be executed
        # The code is executed until it ends, when it ends, the bug can activate again

    def cycle(self,pos,steps=0):
        steps=self.get_reg(self._stmdix)
        super().cycle(pos,steps)


    def _decode_dirs(self,dirs):
        d=[]
        for x in CODE_DIRS:
            if dirs & CODE_DIRS[x]:
                d.append(x)
        return d


    # Searches for the item coded in SRF (food or other bugs=
    # DRS codes directions in the five lower bits. CWSEN (C is Center)
    def _srcf(self):
        logger.info("")
        radius=self.get_reg(self._srridx)
        item_type=self.get_reg(self._srfidx)
        # Gets list of cells in the view radius
        cells_in_radius=self.MyCell.get_neighbors(radius)

        if item_type==0: # search food
            cells_with_item=[c for c in cells_in_radius if c.has_food()]
        else: # search bugs according to type/brand
            cells_with_item=[]
            for c in cells_in_radius:
                for t in c.things:
                    if t.get_brand()==item_type:
                        cells_with_item.append(c)
                        break

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


    # dir is ['N','S','E','W','C']
    def __move_to(self,dir):
        dir_code=cell.DIRS.index(dir)
        new_cell=self.MyCell.neighbors[dir_code]
        self.MyCell.bug_out(self)
        self.MyCell=new_cell
        self.MyCell.bug_in(self)


    # Walks towards a direction in DRS
    # DRS sets the directions to get to something that has been searched for
    # There is room for different heuristics to select the direction in the case there are multiple
    def _wlkt(self):
        dirs=self.get_reg(self._drsidx)
        # decodes the dirs
        d=self._decode_dirs(dirs)
        if d:
            dir=d[0]
            if dir != 'C':
                self.__move_to(dir)
            else:
                pass
        else:
            dir=random.choice(['N','E','S','W'])
            self.__move_to(dir)

    # Walks away from DRS
    def _wlkw(self):
        dirs=self.get_reg(self._drsidx)
        cdirs=[]
        for d in CODE_DIRS.keys():
            if not d in dirs:
                cdirs.append(d)
        if d:
            dir=d[0]
            if dir != 'C':
                self.__move_to(dir)
            else:
                dir=random.choice(['N','E','S','W'])
                self.__move_to(dir)
        else:
            dir=random.choice(['N','E','S','W'])
            self.__move_to(dir)




    def _wlk(self):
        pass

    def _eat(self):
        f=self.MyCell.harvest()
        # Need to add all the energy shebang





