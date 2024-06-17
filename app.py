# MATRIX 2X2
mat=[]
n=2

print("Matrix Input:")
for i in range(2):
    li=list(map(int,input().split(' ')))
    mat.append(li)

#Determinant of a 2X2 matrix
determinant=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

cofactor=[[0,0],[0,0]]

#Finding Co factor matrix
for i in range(n):
    for j in range(n):
        cofactor[i][j]=(-1)**(i+j)*(mat[(i+1)%2][(j+1)%2])

adjoint=[[0,0],[0,0]]

#Transpose cofactor = Adjoint of matrix
for i in range(n):
    for j in range(n):
        adjoint[j][i]=cofactor[i][j]

#Inverse =  Adjoint of matrix / determinant of matrix
for i in range(n):
    for j in range(n):
        adjoint[i][j]=adjoint[i][j]/determinant



print("Matrix INVERSE:")
for i in range(n):
    for j in range(n):
        print(adjoint[i][j],end=' ')
    print("",end='\n')