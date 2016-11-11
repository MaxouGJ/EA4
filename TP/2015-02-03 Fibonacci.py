k1, k2, k3 = 0, 0, 0

def fibo_1(n) :
    global k1
    k1 += 1
    if n < 0 :
        return 0 
    if n < 2 :
        return 1
    fibo_1(n-1)+fibo_1(n-2)
    return fibo_1(n-1)+fibo_1(n-2)

def fibo_2(n) :
    global k2
    if n < 0 : return 0
    liste = [1, 1]
    for i in range(1, n):
        k2 += 1
        liste.append(liste[i - 1] + liste[i])
    return liste[n]

def fibo_3(n) :
    global k3
    if n < 0 : return 0
    previous, last = 1, 1
    for i in range(1, n) :
        k3 += 1
        previous, last = last, previous+last
    return last

