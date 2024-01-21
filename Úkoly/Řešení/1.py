import os

case = 0

path ="Úkoly/Zadání/uloha1/CZE/"
files = os.listdir(path)
files.sort()

def check_near_edge(point,size):
    c = 0
    for coord in point:
        if coord<20 or coord>size-20:
            c += 1
    return c == 1

def distances_to_edges(point,size):
    return [point[0],point[1],size-point[0],size-point[1]]

for filename in files:
    if "_in" in filename:
        case = 0
        inp = open(path+filename, "r").read().split("\n")[:-1]
        if len(inp) != 3: 
            print("Nesprávný vstup")
            continue
        side, a, b = inp
        side = int(side)

        temp_a = []
        invalid__inp = False
        for num in a.split(" "):
            try: 
                temp_a.append(int(num))
            except:
                print("Nesprávný vstup")
                invalid__inp = True
        if invalid__inp:
            continue
        a = temp_a

        temp_b = []
        invalid__inp = False
        for num in b.split(" "):
            try: 
                temp_b.append(int(num))
            except:
                print("Nesprávný vstup")
                invalid__inp = True
        if invalid__inp:
            continue
        b = temp_b

        if not check_near_edge(a,side):
            print("Nesprávný vstup")
            continue

        if not check_near_edge(b,side):
            print("Nesprávný vstup")
            continue

        c = [abs(a-b) for a,b in zip(a,b)]

        if not side in c:
            #pipes:
            pipes =  0
            for i in range(3):
                pipes += abs(a[i] - b[i]) 
            
            #hoses:
            hoses = 0

            axis = 0
            for i in range(3):
                if a[i] not in [0,side] and b[i] not in [0, side]:
                    axis = i

            hoses = (sum([c[i] for i in  range(3) if i != axis])**2 + c[axis]**2)**0.5
            print(f"Pipes: {pipes}, Hoses: {hoses}")

        else:
            a = [i for i in a if (i != side) and (i != 0)]
            b = [i for i in b if (i != side) and (i != 0)]

            a_distaces = distances_to_edges(a,side)
            b_distaces = distances_to_edges(b,side)
            pipe_distaces = []
            hose_distaces = []
            for i in range(4):
                a_dist = a_distaces[i]
                b_dist = b_distaces[i]

                dist_between_points = [abs(a[i]-b[i]) for i in range(2)]
                if i%2 == 0:
                    pipe_distaces.append(a_dist + b_dist + side + dist_between_points[1])
                    hose_distaces.append(((a_dist+b_dist+side)**2+(dist_between_points[1])**2)**0.5)
                else:
                    pipe_distaces.append(a_dist + b_dist + side + dist_between_points[0])
                    hose_distaces.append(((a_dist+b_dist+side)**2+(dist_between_points[0])**2)**0.5)

            pipes = min(pipe_distaces)
            hoses = min(hose_distaces)

            print(f"Pipes: {pipes}, Hoses: {hoses}")