#Exercice 2
def estPermu(T):
    Tab = [False]*len(T) 
    for i in T:
        if (i <= len(T)) and (i >= 1) and (Tab[i-1] == False) :
            Tab[i-1] = True
        else :
            return False
    return True

def triPerm(T):
    Tab = [0]*len(T)
    for i in T :
        Tab[i-1] = i
    return Tab

def inverse(T):
    res = [0]*len(T)
    for i in range(len(T)):
        res[T[i]-1] = i+1
    return res

def produit(T1, T2):
    res = [0]*len(T1)
    for i in range(len(T2)):
        res[i] = T1[T2[i]-1]
    return res

#Exercice 4
def indiceMin(T)
    x = 0
    for i in range(len(T)):
        if T[i] > T[x] :
            x = i
    return x

def monotonie(T, i, j):
   return T[i] < T[j]

#3. On passe dans un autre sous tableau, k est la césure

def indiceMinLog(T, i, j):
    if i-j == 0 :
        return i
    elif T[(i+j+1)/2] < T[j]:
        return indiceMinLog(T, i, (i+j)/2)
    else :
        return indiceMinLog(T, (i+j)/2, j)
