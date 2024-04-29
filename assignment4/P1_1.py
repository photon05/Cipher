def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Ensure base is within the modulus range

    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Halve the exponent
        exponent = exponent // 2

        # Square the base
        base = (base * base) % modulus

    return result

# Example usage:
base = 7
exponent = 128
modulus = 11
result = modular_exponentiation(base, exponent, modulus)
print("Result:", result)

