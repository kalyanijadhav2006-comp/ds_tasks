def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(N, M):
    return (N * M) // gcd(N, M)


N, M = 4, 6
print(lcm(N, M))  