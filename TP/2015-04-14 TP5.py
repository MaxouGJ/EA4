#Exercice 1:

#1
'''
Tableau trié : 1
Liste chainée triée : k
Tableau non trié : n (select)
ABR : parcours infixe
'''

#2
A = [[4, 1, 2, 8],#0
      [2, 3, -1, 2],#1
      [6, 4, 5, 5],#2
      [1, -1, -1, 1],#3
      [5, -1, -1, 1],#4
      [8, 6, 7, 3],#5
      [7, -1, -1, 1],#6
      [9, -1, -1, 1]#7
      ]
     
def insertion(A, x):
    i = 0
    while True:
        if x < A[i][0] :
            if A[i][1] == -1:
                A[i][1] = 
