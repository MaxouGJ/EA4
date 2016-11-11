T1 = [1, 4, 5, 6, 8, 9]
T2 = [2, 4, 6, 7, 9, 10]

def unionRec(E,F):
    if len(E) == 0 : return F[:]
    if len(F) == 0 : return E[:]
    if E[0] == F[0] : return [E[0]] +  unionRec(E[1:], F[1:])
    if E[0] < F[0] : return  [E[0]] +  unionRec(E[1:], F)
    else : return [F[0]] +  unionRec(E, F[1:])

print(unionRec(T1, T2))

def interRec(E, F):
    if len(E) == 0 : return []
    if len(F) == 0 : return []
    if E[0] == F[0] : return [E[0]] +  interRec(E[1:], F[1:])
    if E[0] < F[0] : return  interRec(E[1:], F)
    else : return interRec(E, F[1:])

print(interRec(T1, T2))

def difRec(E,F):
    if len(E) == 0 : return []
    if len(F) == 0 : return []
    if E[0] == F[0] : return difRec(E[1:], F[1:])
    if E[0] < F[0] : return  [E[0]] +  difRec(E[1:], F)
    else : return difRec(E, F[1:])

print(difRec(T1, T2))

def difSymRec(E,F) :
    if len(E) == 0 : return F[:]
    if len(F) == 0 : return E[:]
    if E[0] == F[0] : return difSymRec(E[1:], F[1:])
    if E[0] < F[0] : return  [E[0]] +  difSymRec(E[1:], F)
    else : return [F[0]] +  difSymRec(E, F[1:])

print(difSymRec(T1, T2))

def inversions(T):
    if len(T)<2 : return (T,0)
    gauche, inv_gauche = inversions(T[:len(T)//2])
    droite, inv_droite = inversions(T[len(T)//2:])
    liste,nb = fusion(gauche, droite)
    return liste, nb + inv_gauche +inv_droite

def fusion(gauche, droite):
    if len(gauche)==0 : return (droite,0)
    if len(droite)==0 : return (gauche,0)
    if gauche[0] < droite[0] :
        liste, nb = fusion(gauche[1:], droite)
        return [gauche[0]] + liste, nb
    else :
        liste, nb = fusion(gauche, droite[1:])
        return [droite[0]] + liste, nb +len(gauche)
