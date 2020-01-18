

# Type of register
RW=0
RO=1

class register:

    def __init__(self,val=0,type=RW):
        self.type=type
        self.value=val

    def set(self,val):
        if self.type!=RO:
            self.value=val
            
