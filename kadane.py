x = [12, 5, -1, 31, -61, 59, 26, -53, 58, 97, -93, -23, 84, -15, 6]
ctt = 0
soma = 0

for i in x:
    ctt = max(i, ctt+i)
    soma = max(ctt, soma)

print(soma)
