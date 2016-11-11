def carreCor(n) :
    return([i**2 for i in range(1,n+1)])

def carre(n) :
    l = []
    for i in range(1,n+1) :
        l.append(i*i)
    return l

def carreRec(n) :
    if(n == 1) :
        return [1]
    else :
        return carreRec(n-1) + [n*n]
        
def carCub(n) : #Revient à chercher les puissances de 6
    bons = []
    for i in range(n):
        bons = bons + [i**6]
    return bons

print("carre cor",carreCor(5))
print("carre", carre(5))
print("carre rec",carreRec(5))
print("carre cub",carCub(5))
