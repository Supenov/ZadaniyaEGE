data = []

for s in open('C:/Users/User/Desktop/ZadaniyaEGE/27/27-7a.txt'):
    x, y = [float(d) for d in s.split()]
    data.append([x, y])

from math import dist

clusters = []

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 3]
        cl = cl + sosed
        for p1 in sosed:
            data.remove(p1)
    clusters.append(cl)

def centroid(cl):
    m = []
    for p in cl:
        s = 0
        for p1 in cl:
            s += dist(p, p1)
        m.append([s, p])
    return min(m)[1]

cen = [centroid(cl) for cl in clusters]
#print(cen)

px = sum(x for x, y in cen) / len(cen)
py = sum(y for x, y in cen) / len(cen)

print(int(px*10000), int(py*10000))