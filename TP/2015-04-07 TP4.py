#TP4

A = [4, [2, [1, [], []], []], [6, [5, [], []], [8, [7, [], []], [9, [], []]]]]

def nbNoeuds(n) :
    if n == [] :return 0
    return 1 + nbNoeuds(n[1]) + nbNoeuds(n[2])

#print(nbNoeuds(A))

def hauteur(n):
    if n == [] : return 0
    return 1+max(hauteur(n[1]), hauteur(n[2]))

#print(hauteur(A))

def affPrefixe(n):
    if n == [] : return ""
    return str(n[0]) + affPrefixe(n[1]) + affPrefixe(n[2])

#print(affPrefixe(A))

def affInfixe(n):
    if n == [] : return ""
    return affInfixe(n[1]) + str(n[0]) + affInfixe(n[2])

#print(affInfixe(A))

A2 = [[4, 1, 2, -1],#0
      [2, 3, -1, 0],#1
      [6, 4, 5, 0],#2
      [1, -1, -1, 1],#3
      [5, -1, -1, 2],#4
      [8, 6, 7, 2],#5
      [7, -1, -1, 5],#6
      [9, -1, -1, 5]#7
      ]

def affichagePrefixe(A):
    res = ""
    n = 0
    while n > -1:
        res += str(A[n][0])
        if A[n][1] == -1:
            if A[n][2] == -1:
                while (A[A[n][3]][1] == n and A[A[n][3]][2] == -1) or A[A[n][3]][2] == n:
                    n = A[n][3]
                n = A[A[n][3]][2]
            else :
                n = A[n][2]
        else :
            n = A[n][1]
    return res

print(affichagePrefixe(A2))

