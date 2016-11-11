from random import randint

#Exercice 1
def randomPermutation(n) :
    l = [i+1 for i in range(n)]
    for i in range(n):
        r = randint(i, n-1)
        if i != r :
            l[i], l[r] = l[r], l[i]
    return l

#Exercice 2

t = randomPermutation(100)

def tri_selection(t):
    res = []
    c = 0
    while len(t) != 0:
        min = t[0]
        for i in range(len(t)):
            if min > t[i]:
                min = t[i]
            c += 1
        res.append(min)
        t.remove(min)
    return c, t

#print(tri_selection(t))

def tri_insertion(t):
    c = 0
    for i in range(len(t)):
        for j in range(i, 0, -1):
            c += 1
            if t[j] < t[j-1]:
                t[j], t[j-1] = t[j-1], t[j]
            else :
                break
    return c, t

#t = randomPermutation(1000)
#print(tri_insertion(t))

def tri_bulles(t):
    i = len(t)-1
    while i != 0:
        k = 0
        for j in range(0, i):
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
                k = j
        i = k
    return t

#print(tri_bulles(t))

def fusion(t1, t2):
    if len(t1) == 0:
        return t2
    elif len(t2) == 0:
        return t1
    elif t1[0] < t2[0]:
        return [t1[0]] + fusion(t1[1:], t2)
    else :
        return [t2[0]] + fusion(t1, t2[1:])

def tri_fusion(t, debut, fin):
    if fin - debut < 2:
        return t[debut:fin]
    else :
        milieu = (debut+fin)//2
        gauche = tri_fusion(t, debut, milieu)
        droite = tri_fusion(t, milieu, fin)

    return fusion(gauche, droite)

#print(tri_fusion(t, 0, len(t)-1))

def tri_rapide(t, debut, fin):
    if fin-debut < 2 : return
    indice_pivot  = partition(t, debut, fin)
    tri_rapide(t, debut, indice_pivot)
    tri_rapide(t, indice_pivot+1, fin)

def partition(t, debut, fin):
    if fin-debut == 2 and t[debut]<t[debut+1] : return debut+1
    pivot, gauche, droite = t[debut], debut+1, fin-1
    while gauche < droite:
        while gauche < fin and t[gauche] < pivot :
            gauche += 1
        while t[droite] > pivot :
            droite -= 1
        if gauche < droite :
            t[gauche], t[droite] = t[droite], t[gauche]
    t[debut], t[droite] = t[droite], pivot
    return droite

#tri_rapide(t, 0, len(t))
#print(t)

#Exercice 3

def pertubation(n, m) :
    l = [i+1 for i in range(n)]
    for i in range(m):
        r = randint(i, n-1)
        s = randint(i, n-1)
        if s != r :
            l[s], l[r] = l[r], l[s]
    return l

#print(pertubation(100, 100))
