def string_to_matrix(text, m):
    numerical_values = [ord(char) - ord('a') for char in text.lower() if char.isalpha()]
    remainder = len(numerical_values) % m
    if remainder != 0:
        numerical_values += [0] * (m - remainder)

    matrix = []
    for i in range(0, len(numerical_values), m):
        matrix.append(numerical_values[i:i+m])
    
    return matrix


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


def matrix_multiply_mod(matrix1, matrix2, mod):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= mod
    return result

def numerical_values_to_text(matrix):
    text = ""
    for row in matrix:
        for value in row:
            text += chr((value % 26) + ord('A'))
    return text


m = int(input("Enter the number of rows and cols in square matrix : "))

print("Key Matrix input")
keyMatrix = input_matrix(m,m)
text = input("Enter the plain text : ")
matrix = string_to_matrix(text, m)

encrypted_text = ""
for row in matrix:
    encrypted_row = matrix_multiply_mod([row], keyMatrix, 26)
    encrypted_text += numerical_values_to_text(encrypted_row)

print("Encrypted text:", encrypted_text)


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
    else:
        res = (x % M + M) % M
        return res


mod = 26
det = determinant_mod(keyMatrix, mod)
adj = adjoint_mod(keyMatrix, mod)
detInverse = modInverse(det,26)
inverseMatrix = scalar_multiply(adj,detInverse,mod)

matrix = string_to_matrix(encrypted_text, m)

decrypted_text = ""
for row in matrix:
    decrypted_row = matrix_multiply_mod([row],inverseMatrix, 26)
    decrypted_text += numerical_values_to_text(decrypted_row)

print("Decrypted text:", decrypted_text)

