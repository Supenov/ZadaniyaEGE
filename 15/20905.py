p = set(range(17, 59))
q = set(range(29, 81))
a = set(range(29, 59))

def f(x):
    P = x in p
    Q = x in q
    A = x in a

    return P <= ((Q and (not A)) <= (not P))

for x in range(0, 100):
    if not f(x):
        a.add(x)

print(max(a)-min(a))