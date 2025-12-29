def prime_numbers_generate(max_value):
    """
    Generate prime numbers.
    """
    prime_numbers = [2]
    for num in range(3,max_value,2):
        print(prime_numbers[-1])
        for i in range(2,num):
            if num % i == 0:
                break
            prime_numbers.append(num)
    return prime_numbers

def find_largest_prime_factor(max_value,prime_numbers):
    """
    Finds largest prime factor of Max Value.
    """
    max_prime = 2
    for prime in prime_numbers:
        if max_value % prime:
            max_prime = prime
    return max_prime

def main():
    max_value = 600851475143
    prime_numbers = prime_numbers_generate(max_value)
    max_prime = find_largest_prime_factor(max_value,prime_numbers)
    print(max_prime)

main()