points = [[0, 1], [0, 2],[0, 3]]

def dist(j,k):
    return ((j[0] - k[0])**2+(j[1] - k[1])**2) **0.5

try:
    u1 = dist(points[0],points[1])
    u2 = dist(points[1],points[2])
    u3 = dist(points[0],points[2])

    if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
        print("Body jsou v sobě")
    else:
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
except:
    print("Nesprávný vstup")


