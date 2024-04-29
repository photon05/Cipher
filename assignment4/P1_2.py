def baby_step_giant_step(alpha, beta, p):
    # Step 1: Compute the bound
    m = int(p**0.5) + 1
    
    # Step 2: Compute the baby steps
    baby_steps = {}
    power = 1
    for j in range(m):
        baby_steps[power] = j
        power = (power * alpha) % p
    
    # Step 3: Compute alpha^(-m)
    alpha_inv_m = pow(alpha, p-1-m, p)
    
    # Step 4: Compute the giant steps and check for a match
    gamma = beta
    for i in range(m):
        if gamma in baby_steps:
            return i * m + baby_steps[gamma]
        gamma = (gamma * alpha_inv_m) % p
    
    return None  # If no solution is found

# Given data
p = 809
alpha = 89
beta = 618

# Compute the discrete logarithm
log_alpha_beta = baby_step_giant_step(alpha, beta, p)
print("log_alpha_beta:", log_alpha_beta)
