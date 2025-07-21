"cap1 is capacity of jug1 & cap2 is capacity of jug2"
def initialize(cap1,cap2,target):
    visit=set()
    path=[]
    "x is amt of water in jug 1 & y is amt of water in jug2"
    def search(x,y):
        if(x,y) in visit:
            return False
        visit.add((x,y))
        path.append((x,y))
        if(x==target or y==target):
            return True
        if search(3,y):
            return True
        if search(x,4):
            return True
        if search(0,y):
            return True
        if search(x,0):
            return True
        if search(max(0,x-(4-y)),min(4,x+y)):
            return True
        if search(min(3,x+y),max(y-(3-x),0)):
            return True
       
        
        path.pop()
        return False
    search(0,0)
    return path

solution=initialize(3,4,2)
if solution:
    print("solution:")
    for step in solution:
        print(step)
else:
    print("no solution")