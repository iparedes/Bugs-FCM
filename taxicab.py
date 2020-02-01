

class TCPos:

    def __init__(self,f,c):
        # rows and columns
        self.f=f
        self.c=c


    # Returns taxicab distance to other position
    def dist(self,pos):
        return abs(self.f-pos.f)+abs(self.c-pos.c)

    # Returns a list with the directions that may be followed to reach another position
    # If the list is [0] means that destination is same as origin
    #   1
    #  402
    #   3
    def dir_to(self,pos):
        vectf=pos.f-self.f
        vectc=pos.c-self.c
        ret=[]

        if vectf<0:
            ret.append(1)
        elif vectf>0:
            ret.append(3)
        if vectc<0:
            ret.append(4)
        elif vectc>0:
            ret.append(2)

        if not len(ret):
            ret.append(0)

        return ret

    # Moves the position towards the specified direction
    def mov_to(self,dir):
        if dir==1:
            self.f-=1
        elif dir==2:
            self.c+=1
        elif dir==3:
            self.f+=1
        elif dir==4:
            self.c-=1


    def print(self):
        print('('+str(self.f)+','+str(self.c)+')')

    def __add__(self, other):
        return TCPos(self.f + other.f, self.c + other.c)

    def __str__(self):
        return "("+str(self.f)+","+str(self.c)+")"



# a=taxicabPos(2,2)
# b=taxicabPos(2,4)
#
# dir=a.dir_to(b)
# print(dir)
