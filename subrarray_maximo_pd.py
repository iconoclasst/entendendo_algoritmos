

a = [-2, -4, 1, 5, -4]


opt = []
for i in range(len(a)):
    if i==0:
        opt.append(a[i])
    else:
        opt.append(max(a[i], a[i]+opt[i-1]))

print(max(opt))

