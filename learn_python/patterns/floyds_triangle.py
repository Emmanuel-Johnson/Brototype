n = 1
for i in range(5):
    for j in range(5):
        if j <= i:
            print(format(n, "<2d"), end = " ")
            n += 1
    print()