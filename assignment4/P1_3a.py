def modular_exponentiation(base, exponent, modulus):
    result = 1
    base %= modulus  # Ensure base is within the modulus range

    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Halve the exponent
        exponent //= 2

        # Square the base
        base = (base * base) % modulus

    return result

# Given values
base = 27
exponent = 33
modulus = 55

# Convert the exponent to binary
binary_exponent = bin(exponent)[2:]  # Convert to binary string and remove '0b' prefix
result = 1

# Perform repeated squaring
for bit in binary_exponent:
    result = (result * result) % modulus  # Square the result
    if bit == '1':
        result = (result * base) % modulus  # Multiply by base if bit is 1

print("Result of 7^128 mod 11 using repeated squaring:", result)

