def string_to_matrix(text, m):
    numerical_values = [ord(char) - ord('a') for char in text.lower() if char.isalpha()]
    remainder = len(numerical_values) % m
    if remainder != 0:
        numerical_values += [0] * (m - remainder)

    matrix = []
    for i in range(0, len(numerical_values), m):
        matrix.append(numerical_values[i:i+m])
    
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


m = 3
key = "CIPHERING"
keyMatrix = string_to_matrix(key,m)
text1 = "SAFEMESSAGE"
matrix = string_to_matrix(text1, m)


encrypted_text = ""
for row in matrix:
    encrypted_row = matrix_multiply_mod([row], keyMatrix, 26)
    encrypted_text += numerical_values_to_text(encrypted_row)
print(f"\nFor message = {text1} and key =CIPHERING and m=3 : ")
print("Encrypted text:", encrypted_text)

text2 = "HAPPYLIFE"
matrix = string_to_matrix(text2, m)


encrypted_text = ""
for row in matrix:
    encrypted_row = matrix_multiply_mod([row], keyMatrix, 26)
    encrypted_text += numerical_values_to_text(encrypted_row)
print(f"\nFor message = {text2} and key =CIPHERING and m=3 : ")
print("Encrypted text:", encrypted_text)

