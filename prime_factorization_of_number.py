def prime_factorization(N):
    factors = []
    
    
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            factors.append(i)
            N //= i
    
   
    if N > 1:
        factors.append(N)
    
    return factors



N = 18
print("Input:", N)
print("Output:", prime_factorization(N))