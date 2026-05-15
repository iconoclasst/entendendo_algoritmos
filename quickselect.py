import random

def quick_select(a, k):
    
    p = random.choice(a)
    l = [i for i in a if i<p]
    m = [j for j in a if j==p]
    r = [k for k in a if k>p]

    if k <= len(l):
        return quick_select(l, k)
    elif k > len(l) + len(m):
        return quick_select(r, k - len(l) - len(m))
    else:
        return p



a = [7, 6, 12, 3, 11, 8, 9, 1, 4, 10, 2]

b = quick_select(a, 5)

print(b)
