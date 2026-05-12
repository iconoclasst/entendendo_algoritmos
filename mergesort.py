def merge(a, b):
    c = []
    i=0
    j=0

    while i < len(a) and j< len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c

def sort(l):
    n = len(l)
    if n <= 1:
        return l

    esq = l[:n//2]
    dir = l[n//2:]

    a = sort(esq)
    b = sort(dir)
    c = merge(a, b)

    return c


l = [21, 2, 4, 11, 8, 54, 2, 1, -15, 43, 3]

print(sort(l))
