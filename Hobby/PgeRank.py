import numpy as np

def dot(A,B):
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]
    return C
        
def matrixpow(A,n):
    if n == 1:
        return A
    elif n == 0:
        return np.ones(np.shape(A))
    else:
        return dot(A,matrixpow(A,n-1))
    
"""
#      1 2 3 4 5 6 7 8 9 10
a1 =  [0,1,1,0,0,0,0,0,0,0]
a2 =  [1,0,0,1,0,0,0,0,0,0]
a3 =  [1,0,0,1,0,0,0,0,0,0]
a4 =  [0,1,1,0,1,1,1,0,0,0]
a5 =  [0,0,0,1,0,0,0,1,0,0]
a6 =  [0,0,0,1,0,0,0,1,0,0]
a7 =  [0,0,0,1,0,0,0,1,0,0]
a8 =  [0,0,0,0,1,1,1,0,1,1]
a9 =  [0,0,0,0,0,0,0,1,0,0]
a10 = [0,0,0,0,0,0,0,1,0,0]
"""

#      0 1 2 3 4 5
a0 =  [0,0,1,1,1,0]
a1 =  [0,0,0,1,0,1]
a2 =  [1,0,0,0,0,0]
a3 =  [1,1,0,0,0,0]
a4 =  [1,0,0,0,0,0]
a5 =  [0,1,0,0,0,0]

# A = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10] # need for clustering example 
A =  [a0,a1,a2,a3,a4,a5]    # DB hackathon virus and the network 
#A = [[0,0,.5,.5],[1,0,0,.5],[0,.5,0,0],[0,.5,.5,0]]     test (youtube video)

A_T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] # transpose of A

for row in range(len(A)):
    for i in range(len(A[row])):
        A[row][i] = A[row][i]/sum(A_T[row])

R0 = [[1/len(A)] for _ in range(len(A))]
delta = .1E-5
n0 = 5


def Ri(R0, n):
    return dot(matrixpow(A,n),R0)
       
while True:
    brk = False
    eigenvector1 = Ri(R0,n0)
    eigenvector0 = Ri(R0,n0-1)
    for i in range(len(eigenvector1)):
        if abs(eigenvector1[i][0] - eigenvector0[i][0]) < delta:
            brk = True
        else:
            n0 += 1
            break
    if brk:
        break