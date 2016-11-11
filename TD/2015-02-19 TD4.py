def TriABullesOptimise(T):
    n = len(T)
    for i in range(n-1, 0, -1):
        check = True
        for j in range (0, i):
            if (T[j] > T[j+1]):
                T[j], T[j+1] = T[j+1], T[j]
                check = False
            if check:
                break
        return T
