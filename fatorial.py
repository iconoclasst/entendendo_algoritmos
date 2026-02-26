
def fatorial(x):
    if x <= 1:
        return x
    return x * fatorial(x-1)

x = int(input())
print(fatorial(x))
