

DIRS=['N','E','S','W']
ANTA={'N':'S','E':'W','S':'N','W':'E'}

class cell:

    def __init__(self):
        # In order: N, W, E, S
        self.neighbors=[]
        self.food=1


class board:

    def __init__(self,width,height):
        """
        width=x coordinate
        height=y coordinate
        :param width:
        :param height:
        :return:
        """
        self.height=height
        self.width=width
        self.b=[[cell() for x in range(width)] for y in range(height)]

        # Just for testing
        cont=0
        for r in range(0,self.height):
            for c in range(0,self.width):
                self.b[r][c].food=cont
                cont+=1

        shifts=self.von_neumann_pos(1)
        for r in range(0,self.height):
            for c in range(0,self.width):
                for n in shifts:
                    a=self.add_coords([r,c],n)
                    self.b[r][c].neighbors.append(self.get_cell(a))

    # p: [r,c]
    def get_cell(self,p):
        return self.b[p[0]][p[1]]

    # two lists [row,col]
    # ret: a coord inside the board (the edges are adjacent to the opposite)
    def add_coords(self, p1, p2):
        r= p1[0] + p2[0]
        c= p1[1] + p2[1]
        if (r<0) or (r>=self.height):
            r=r%self.height
        if (c<0) or (c>=self.width):
            c=c%self.width
        return (r,c)

    # sets the position inside the boundaries of the board
    def normalize_coord(self,p):
        r=p[0]
        c=p[1]
        if (r<0) or (r>=self.height):
            p[0]=r%self.height
        if (c<0) or (c>=self.width):
            p[1]=r%self.width


    # start: list [row,col]
    # dir: N,W,E,S
    def neighbor(self,start,dir):
        r=start[0]
        c=start[1]
        if dir=='N':
            nr=r-1
            if nr==-1:
                nr=self.height-1
            new=[nr,c]
        elif dir=='E':
            nc=c+1
            if nc==self.width:
                nc=0
            new=[r,nc]
        elif dir=='S':
            nr=r+1
            if nr==self.height:
                nr=0
            new=[nr,c]
        elif dir=='W':
            nc=nc-1
            if nc==-1:
                nc=self.width-1
            new=[r,nc]
        else:
            # wrong dir
            new=start
        return new

    # row, column
    # return coordinates of neumann neighbours with dist 1
    def neighbors(self,pos):
        r=pos[0]
        c=pos[1]
        N=[]
        for d in DIRS:
            N.append(self.neighbor([r,c],d))
        return N

    # Gives directions to cover (redundantly) all the cells in the neumann neighborhood of dist
    def von_neumann(self, dist):
        if dist==1:
            return DIRS
        else:
            N=[]
            for dir in DIRS:
                a=self.von_neumann(dist-1)
                for item in a:
                    if item!=ANTA[dir]:
                        new=list(dir)+list(item)
                        N.append(new)
            return N

    # dist: von_neumann dist
    # ret: list with shifts to get all positions in the neighborhood
    # dist=1: N,W,E,S
    def von_neumann_pos(self,dist):
        N=[]
        for dr in range(-dist,dist+1):
            if dr<=0:
                a=dr+dist
            else:
                a=dist-dr
            for dc in range(-a,a+1):
                N.append([dr,dc])
        N.remove([0,0])
        return N



B=board(3,3)
a=B.von_neumann_pos(2)
print(a)