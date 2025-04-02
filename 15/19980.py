p = set(range(52, 106))
q = set(range(0, 54))
mi = float('inf')
ma = float('-inf')
def f(x):
    P = x not in p
    Q = x not in q

    return ( (P) and (Q)) <= (x**2 > 303601)

for x in range(0, 1000*4 + 1):
    x = x/4
    if not f(x):
        mi = min(mi, x)
        ma = max(ma, x)
print(ma-mi)