def is_prime(n):
    if n <= 1:                    # Conditional branching
        return False  
    i = 2                         # Basic block 
    
    while i * i <= n:             # Conditional branching
        if n % i == 0:            # Conditional branching
            return False  
        i += 1                    # Basic block 

    return True           
