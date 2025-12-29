def find_largest_prime_factor(max_value):
    """
    Finds largest prime factor of Max Value.
    """
    num = 3
    max_prime = 1
    while max_value % 2 == 0:
        max_prime = 2
        max_value //= 2
    
    while num * num <= max_value:
        while max_value % num == 0:
            max_prime = num
            max_value //= num
        num += 2
    if max_value > 1:
        max_prime = max_value
    return max_prime

def main():
    max_value = 600851475143
    max_prime = find_largest_prime_factor(max_value)
    print(max_prime)

main()