prime_numbs = [2]
numb = 3

while len(prime_numbs) < 10001:
    isPrime = True
    
    for prime in prime_numbs:
        if prime * prime > numb:
            break
        if numb % prime == 0:
            isPrime = False
            break

    if isPrime:    
        prime_numbs.append(numb) 
    
    numb += 2
print(prime_numbs[-1])