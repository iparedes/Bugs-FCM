import numpy as np


class FCM:
    def __init__(self):
        self.Concepts={}
        self.Concepts['values'] = np.array([[]])
        self.Concepts['names']=[]
        self.Edges = np.array([[]])

    def add_concept(self,val=None):
        if val==None:
            val=np.random.rand()
        last=self.Concepts['values'].size
        if last==0:
            self.Concepts['values']=np.array([[val]])
            self.Edges=np.array([[0]])
        else:
            # Add a new column (concept) to Concepts
            self.Concepts['values']=np.append(self.Concepts['values'],[[val]],axis=1)
            # Creates a new column for the edges
            rows=self.Edges.shape[0]
            col=np.zeros([rows,1])
            # Adds the new column
            self.Edges=np.append(self.Edges,col,axis=1)
            # Creates a new row for the edges
            row=np.zeros([1,rows+1])
            self.Edges=np.append(self.Edges,row,axis=0)
        self.Concepts['names'].append("C"+str(last+1))

    def set_edge(self,i,j,val=None):
        if val==None:
            val=np.random.rand()
        try:
            self.Edges[i,j]=val
        except IndexError as e:
            print("set_edge: ",e)

    def set_concept_value(self, i, val=None):
        if val==None:
            val=np.random.rand()
        try:
            self.Concepts['values'][0][i]=val
        except IndexError as e:
            print("set_concept_value: ",e)

    def set_concept_name(self, i, name=None):
        if name==None:
            name="C"+str(i)
            # should include a test to avoid duplicated names in the concepts
        try:
            self.Concepts['names'][i]=name
        except IndexError as e:
            print("set_concept: ",e)

    def get_concept_value(self, i):
        try:
            return self.Concepts['values'][0][i]
        except IndexError as e:
            print("get_concept_value: ",e)
            return 0

    def get_concept_name(self, i):
        try:
            return self.Concepts['names'][i]
        except IndexError as e:
            print("get_concept_name: ",e)
            return 0

    def activation(self,val):
        z = 1/(1 + np.exp(-val))
        return z

    # Updates the values of the concepts according to the edges
    # Returns the index of the biggest concept
    def update_concepts_values(self):
        for i in range(0,self.Concepts['values'].size):
            col=self.Edges[:,i]
            dotprod=self.Concepts['values'].dot(col)
            oldconcept=self.get_concept_value(i)
            self.set_concept_value(i, self.activation(oldconcept + dotprod))
        return self.Concepts['values'][0].argmax()




