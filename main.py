from VM import *
from bug import *
from cell import *
from world import *
import tools

tools.init_tools()


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
#
# exit()

# stream=FileStream("test.asm")
# #stream = antlr4.InputStream("LD R1,{200}\nST R1,1")
# C=Analyzer(stream)
# C.Walk()
#
# M=VM()
# M.load(C.Context['program'])
# M.show_architecture()
# M.set_mem(200,999)
# M.step()
# M.show_architecture()
# M.step()
# M.show_architecture()
# M.step()
# M.show_architecture()
# M.show_memory()
# a=M.get_reg('PC')

#b=Bug()


# v=VM()
# v.set_mem(30,1)
# v.set_mem(50,1)
# cs=v.get_reg('CS')
# s=v.find_blocks()

# v=VM()
# v.Memory[1]=64
# w=v.generate()
#
# print(v.show_architecture())
# print(w.show_architecture())
# print(v.show_memory())
# print(w.show_memory())
#
# exit()
#
#
#
# B=board(10,10)
# B.b[4][5].sow()
# B.b[8][5].sow()
#
# C=B.b[4][4]
#
# b=Bug(cell=C)
# pos_test=b.load_file("test.asm")
# pos_eat=b.load_file("eat.asm")

# stream=FileStream("test.asm")
# #stream = antlr4.InputStream("ADD R1,R2\n")
# analyzer=Analyzer(stream)
# analyzer.Walk()
# pos_test=b._compile(analyzer.Context['program'])



# #b.cycle(pos)
# b.run(pos_test)
# #b.set_mem(20,10)
# go=1
# while (go):
#     go=b.step()
#     B.display()
#     print('---------------------')
#     #input("")
#     print(b.show_architecture())


W=World()
prog="test2.asm"
W.spawn_bug(prog)
for b in W.Bugs:
    b.step()

while (1):
    W.step()
    W.Board.display()
    input("")
    print('---------------------')


