def getdata(filename):
    file = open(filename, "r")
    data = file.read().splitlines()
    planes = []
    for i in data:
        coordinates = i.split(":")[0].split(",")
        coordinates = [float(c) for c in coordinates]
        name = i.split(":")[1].strip()
        planes.append([coordinates, name])
    return planes

def distance(plane1, plane2):
    x1, y1 = plane1[0] 
    x2, y2 = plane2[0]
    xdistance = abs(x1-x2)
    ydistance = abs(y1-y2)
    return ((xdistance**2)+(ydistance**2))**0.5

print("Pozice letadel:")
try:
    planes = getdata("./Zadání/Uloha5/CZE/0006_in.txt")
except:
    print("Nespravny vstup")
    exit()

planeslength = len(planes)

distances = []

for i in range(planeslength):
    for j in range(i+1, planeslength):
        distances.append(distance(planes[i], planes[j]))

mindistance = min(distances)
planenames = []

for i in range(planeslength):
    for j in range(i+1, planeslength):
        if distance(planes[i], planes[j]) == mindistance:
            planenames.append(f"{planes[i][1]} - {planes[j][1]}")
        
print(f"Vzdalenost nejblizsich letadel: {mindistance}")
print(f"Nalezenych dvojic:{len(planenames)}")
for i in planenames:
    print(i)