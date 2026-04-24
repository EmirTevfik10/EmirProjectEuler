def is_prime(n):
    for i in range(3,n):
        if i ** 2 > n:
            break
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    return sum(n for n in range(3,limit,2) if is_prime(n)) + 2

print(sum_of_primes(2000000))