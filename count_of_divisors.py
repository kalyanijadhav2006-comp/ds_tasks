def count_divisors(N: int) -> int:
    count = 1
    i = 2
    while i * i <= N:
        exponent = 0
        while N % i == 0:
            N //= i
            exponent += 1
        if exponent > 0:
            count *= (exponent + 1)
        i += 1
    if N > 1:  
        count *= 2
    return count



N = 12
print(count_divisors(N))  
