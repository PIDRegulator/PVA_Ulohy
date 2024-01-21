points = [[0.1, 0], [0.2, 0], [0.3, 0]]
input()

def dist(a,b):
    return ((a[0] - b[0])**2+(a[1] - b[1])**2) **0.5
def dist(b,c):
    return ((b[0] - c[0])**2+(b[1] - c[1])**2) **0.5
def dist(a,c):
    return ((a[0] - c[0])**2+(a[1] - c[1])**2) **0.5

u1 = dist(points[0],points[1])
u2 = dist(points[1],points[2])
u3 = dist(points[0],points[2])

set

if u1 >= u2 and u1>= u3:
    middle = 2
    middlepoint = "C"
elif u2 >= u1 and u2>=u3:
    middle = 0
    middlepoint = "A"
else:
    middle = 1
    middlepoint="B"

if middle == 0:
    if u1 + u3 == u2:
        print("Body jsou v přímce a bod uprostřed je: " + middlepoint)
    else:
        print("body nejsou v přímce")
elif middle == 1:
    if u1 + u2 == u3:
        print("Body jsou v přímce a bod uprostřed je: " + middlepoint)
    else:
        print("body nejsou v přímce")
else:
    if u2 + u3 == u1:
        print("Body jsou v přímce a bod uprostřed je: " + middlepoint)
    else:
        print("body nejsou v přímce")



