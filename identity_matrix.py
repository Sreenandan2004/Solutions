matrix=[]
n=int(input("Enter the size of the identity matrix: "))

for i in range(n):
    row=[0]*n
    row[i]=1
    matrix.append(row)

def check_identity(matrix,n):
    for i in range(n):
        if matrix[i][i]!=1 or sum(matrix[i])!=1:
            return False
    
    return True

if check_identity(matrix,n):
    print("The matrix is an identity matrix.")
else:
    print("The matrix is not an identity matrix.")
