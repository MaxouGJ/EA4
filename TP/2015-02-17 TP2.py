#TP2

#Exercice 1 :

P = [2, 3, 4]
Q = [1, 2, 3]

def mult_poly_naif(P, Q):
    R = [0]*(len(P)+len(Q)-1)
    operations = 0
    for i in range(0, len(P)) :
        for j in range(0, len(Q)) :
            R[i+j] += P[i]*Q[j]
            operations += 2
    print("Nombre d'opérations : ",operations)
    return R;

print(mult_poly_naif(P,Q))

def mult_poly_rec(P, Q):
    R = [0]*(len(P)+len(Q)-1)
    if(len(P)==1):
        R[0] = Q[0] * P[0]
    else :
        p0 = P[0 : len(P)//2]
        p1 = P[len(P)//2 : len(P)]
        q0 = Q[0 : len(Q)//2]
        q1 = Q[len(Q)//2 : len(Q)]

        r1 = mult_poly_rec(p0, q0)
        r2 = mult_poly_rec(p1, q0)
        r3 = mult_poly_rec(p0, q1)
        r4 = mult_poly_rec(p1, q1)

        for i in range(len(r1)):
            R[i] += r1[i]
            R[i + len(P)//2] += r2[i] + r3[i]
            R[i + len(P)] += r4[i]
    return R

#print(mult_poly_rec(P,Q))

def karatsuba(P, Q):
    print()    

#Exercice 2 :

def compte(i, T):
    compte = 0
    for k in range(len(T)):
        if T[k] == i:
            compte += 1
    return compte

#Complexite  : n

def tab_occ(T):
    Tab = [0]*len(T)
    for i in range(len(T)):
        Tab[i] = compte(i, T)
    return Tab

#Complexite : len(T) * m
