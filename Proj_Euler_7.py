# Prob 7
import math

def find_prime(n):
  upper_bound = int(n * (math.log(n) + math.log(math.log(n)))) +5

  while True:
    sieve = bytearray(b"\x01") * (upper_bound + 1)
    sieve[0:2] = b"\x00\x00"

    limit = math.sqrt(upper_bound)

    for p in range(2, int(limit)):
      if sieve[p]:
        start = p * p
        sieve[start:upper_bound + 1:p] = b"\x00" * (((upper_bound - start) // p) + 1)

    primes = [i for i, ok in enumerate(sieve) if ok]
    if len(primes) >= n:
      return primes[n-1]

result = find_prime(10001)
print(result)
