def max(T):
    max = T[0]
    for i in T:
        if T[i] > max : max = T[i]
    return max

def inf(T, x):
    n = 0
    for i in T:
        if x > T[i]:
            n +=1
    return n

def trie(T):
    for i in range(1, len(T)):
        if T[i] < T[i-1] :
            return False
    return True

def circulaire(T):
    cesure = 0
    for i in range(len(T)-1):
        if T[i] >= T[i+1]:
           cesure += 1
           if cesure > 1 :
               return False
    if cesure == 0 :
           return True
    else :
        if T[0] >= T[len(t)-1] :
            return True
        else :
           return False 

def circulaire2(T):
    cesure = 0
    for i in range(len(T)):
        if T[i] > T[(i+1)%len(T)]:
            cesure +=1
        return (cesure <= 1)
