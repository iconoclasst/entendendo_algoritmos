import random

def qs(a):
    if len(a) <= 1:
        return a
    
    p = random.choice(a)
    l = [i for i in a if i<p]
    m = [j for j in a if j==p]
    r = [k for k in a if k>p]

    return qs(l) + m + qs(r)

a = [7, 6, 12, 3, 11, 8, 9, 1, 4, 10, 2]

b = qs(a)

print(b)
