for m in range(2, 11):
    for n in range(1, m):
        print("%d+%d=%2d" % (n, m - n, m), end=" ")
    print(" ")
