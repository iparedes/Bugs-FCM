from FCM import *


class Brain(FCM):

    # programs is a list of dictionaries {'MemPointer','prog_type','prog_name','Sequence','reg','pos'}
    def __init__(self,programs):
        super().__init__()

        # A sensor is a concept with no inputs, only outputs, whose value depends on the content of a register
        # sensors are initialized with the register value on each activation
        # sensors is a list of dictionaries
        # {
        # 'idx':index of the concept in the FCM
        # 'name':name,
        # 'reg':register for value activation,
        # 'pos':start memory address for the program
        # 'program':compiled program}
        self.sensors=[]
        # actors is a dictionary whose keys are concept indexes and value a dictionary with this structure:
        # {'name':name,'pos':p['pos'],'prog':p['Sequence']}
        self.actors={}

        for p in programs:
            if p['prog_type']=='SENSOR':
                name=p['prog_name']
                idx=self.add_concept(0,name)
                self.sensors.append({'idx':idx,'name':name,'reg':p['reg'],'pos':p['pos'],'prog':p['Sequence']})
            else:
                # ACTOR
                name=p['prog_name']
                idx=self.add_concept(0,name)
                #self.actors.append({'idx':idx,'name':name,'pos':p['pos'],'prog':p['Sequence']})
                self.actors[idx]={'name':name,'pos':p['pos'],'prog':p['Sequence']}


        # sensor concepts receive its value from a register in activation
        # they do not have connection between them
        # we generate an additional concept (C) for each sensor (S) in a way that
        # each S only has an output connecting to one C
        # each C is connected to the rest of the As and Actors
        intermediate_idx=[]
        for s in self.sensors:
            intermediate_idx.append(self.add_concept())

        # Now set the edges
        # first the link between sensors and the intermediate concepts
        sens_idx=[s['idx'] for s in self.sensors]
        for (i,j) in zip(sens_idx,intermediate_idx):
            self.set_edge(i,j)
        # then the edges among all the intermediate concepts
        for (i,j) in zip(intermediate_idx,intermediate_idx):
            if i!=j:
                self.set_edge(i,j)
        # and the edges between each intermediate concept and the actors
        #acts_idx=[s['idx'] for s in self.actors]
        acts_idx=self.actors.keys()
        for (i,j) in zip(intermediate_idx,acts_idx):
            self.set_edge(i,j)

    def max_actor(self):
        acts_idx=self.actors.keys()
        max=0
        i=-1
        for index in acts_idx:
            val=self.get_concept_value(index)
            if val>max:
                max=val
                i=index
        return i


    def cadena(self):
        s=super().cadena()
        return s

