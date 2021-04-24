class tictactoe:
    def __init__(self):
        self.n = 3
        self.x = 0
        self.y = 0
        self.map = [[0,]*self.n for _ in range(self.n)]
        self.circleposition = []
        self.xposition = []
         
    def draw(self):
        for i in range (self.n):
            for j in range(self.n):
                print(self.map[i][j],end = "")
            print()

    def update(self):
        for i in range(self.n):
            for j in range(self.n):
                self.map[i][j] = 0
                for  pos_axis in self.circleposition:
                    if i==pos_axis[0] and j==pos_axis[1]:
                        self.map[i][j] = 1
                for  pos_axis in self.xposition:
                    if i==pos_axis[0] and j==pos_axis[1]:
                        self.map[i][j] = 2
                
    def a(self):
        while True:
            pos = list(map(int,input("player y").split() ) )
            print(pos)
            if (pos[0],pos[1]) not in self.circleposition and (pos[0],pos[1]) not in self.xposition:
                break
        
        self.circleposition.append((pos[0],pos[1]))

        
    def b(self):
        while True:
            pos = list(map(int,input("player x").split() ) )
            print(pos)
            if (pos[0],pos[1]) not in self.circleposition and (pos[0],pos[1]) not in self.xposition:
                break

        self.xposition.append((pos[0],pos[1]))
    def c(self):
        for i in range(3):
            if (i,0) in self.xposition and  (i,1) in self.xposition and (i,2) in self.xposition:
                return 1
            elif (i,0) in self.circleposition and  (i,1) in self.circleposition and (i,2) in self.circleposition:
                return 2
            else:
                pass
        for j in range(3):
            if (0,j) in self.xposition and (1,j) in self.xposition and (2,i) in self.xposition:
                return 1
            elif (0,j) in self.circleposition and (1,j)in self.circleposition and (2,j)in self.circleposition:
                return 2
            else:
                pass
        if (0,0)in self.xposition and (1,1) in self.xposition and (2,3) in self.xposition:
            return 1
        elif (0,2) in self.circleposition and (1,1) in self.circleposition and (0,2) in self.circleposition:
            return 2
        else:
            pass
        
                
                
a = tictactoe()
cnt =0
while True:
    
    a.update()
    a.b()
    a.update()
    a.draw()
    a.c()
    flag = a.c()
    if flag == 1:
        break
    elif flag == 2 :
        break
    else:
        pass
    print()
    cnt + 1
    if cnt == 9:
        break
    a.update()  
    a.a()
    a.update()
    a.draw()
    a.c()
    flag = a.c()
    if flag == 1:
        break
    elif flag == 2 :
        break
    else:
        pass
    print()
    cnt + 1
    if cnt == 9:
        break
