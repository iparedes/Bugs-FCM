from analyzer import *
from VM import *



# from FCM import *
#
#
# F=FCM()
# F.add_concept()
# F.add_concept()
# F.add_concept()
# F.add_concept()
# F.set_edge(0,1)
# F.set_edge(0,2)
# F.set_edge(1,2)
# F.set_edge(2,3)
# F.set_edge(3,0)
# F.set_edge(3,1)
# print(F.Concepts['names'])
# print(F.Concepts['values'])
# print(F.Edges)
# F.update_concepts_values()
# print(F.Concepts['values'])


stream = antlr4.InputStream("LD R1,{200}\nST R1,1")
C=Analyzer(stream)
C.Walk()

M=VM()
M.load(C.Context['program'])
M.show_architecture()
M.set_mem(200,999)
M.step()
M.show_architecture()
M.step()
M.show_architecture()
# a=M.get_reg('PC')

pass
