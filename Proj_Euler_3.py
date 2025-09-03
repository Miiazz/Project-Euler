# Find factors

def find_factors(n):
    factor = 2
    while factor * factor <= n:
        if n % factor ==0:
            n //= factor
        else:
            factor += 1
    return n

n = 600851475143
result = find_factors(n)
print(result)
