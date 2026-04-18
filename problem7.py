def is_prime(numb,prime_numbs):
    for prime in prime_numbs:
        if prime * prime > numb:
            break
        if numb % prime == 0:
            return False

    return True

def nt_prime(n):
    prime_numbs = [2]
    numb = 3

    while len(prime_numbs) < n:
        if is_prime(numb, prime_numbs):
            prime_numbs.append(numb) 
        numb += 2

    return prime_numbs[-1]

def main():
    print(nt_prime(10001))

main()