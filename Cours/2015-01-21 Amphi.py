def addition(nb1, nb2) :
    #entiers représentés par des tableaux de chiffres décimaux
    res = []
    retenue = 0
    for(chiffre1, chiffre2) in zip(nb1, nb2) :
        tmp = chiffre1+chiffre2+retenue
        retenue = tmp/10
        res.append(tmp%10)
    return res+[retenue]

def multiplicaion(nb1, nb2) :
    res = nb1[:]
    for i in range(1, valeur(nb2)) :
        res = addition(res, nb1)
    return res

def multiplicationParUnChiffre(nb1, chiffre2) :
    res = []
    retenue = 0
    for chiffre1 in nb1 :
        tmp = chiffre1 * chiffre2 + retenue
        retenue = tmp/10
        res.append(tmp%10)
    return res + [retenue]

def multiplicationRusse(nb1, nb2) :
    #cette fois les entiers sont vraiment des entiers
    res = 0
    while nb2 != 0 :
        if nb2%2 == 1 : res += nb1
        nb1 *= 2    #ou : nb1 << 1
        nb2 /= 2    #ou : nb2 >> 1
    return res

def puissance(nb1, nb2) :
    res = 1
    for i in range(nb2) :
        res *= nb1
    return res

def puissanceRec(nb1, nb2) :
    if nb2 == 0 : return 1
    tmp = puissanceRec(nb1, nb2/2)
    carre = tmp * tmp
    if nb2%2 == 0 : return carre
    else : return nb1 * carre
