def determinant_mod(matrix, mod):
    if len(matrix) == 1:
        return matrix[0][0] % mod
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    else:
        det = 0
        for i in range(len(matrix)):
            sign = (-1) ** i
            sub_det = determinant_mod([row[:i] + row[i+1:] for row in matrix[1:]], mod)
            det += sign * matrix[0][i] * sub_det
        return det % mod


def cofactor(matrix, i, j):
    sign = (-1) ** (i + j)
    minor_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    return sign * determinant_mod(minor_matrix, mod)


def adjoint_mod(matrix, mod):
    n = len(matrix)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adj[j][i] = cofactor(matrix, i, j) % mod
    return adj


def scalar_multiply(matrix, scalar, mod):
    result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = (matrix[i][j] * scalar) % mod
    return result

def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix (one row at a time):")
    for i in range(rows):
        row = list(map(int, input().split()))[:cols]
        if len(row) != cols:
            print("Invalid number of elements entered. Please try again.")
            return None
        matrix.append(row)
    return matrix


x, y = 0, 1

def gcdExtended(a, b):
    global x, y
    if (a == 0):
        x = 0
        y = 1
        return b
 
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
 
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
        return None
    else:
        res = (x % M + M) % M
        return res


a = int(input("Enter no of rows and cols in square matrix :"))
matrix = input_matrix(a,a)
mod = 26
det = determinant_mod(matrix, mod)
print("Determinant of the matrix modulo", mod, ":")
print(det)

adj = adjoint_mod(matrix, mod)
print("Original Matrix : ")
for row in matrix:
    print(row)

detInverse = modInverse(det,26)

if(detInverse!=None):
    print("Inverse Matrix : ")
    inverseMatrix = scalar_multiply(adj,detInverse,mod)
    for row in inverseMatrix:
        print(row)
