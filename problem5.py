def find_prime_nums(max_divide):
    """
    Returns a list of prime numbers from 2 up to max_divide.
    """
    primes = []
    for i in range(2, max_divide + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
        
def find_lcm(max_divide,primes):
    """
    Calculates the LCM of numbers from 1 to max_divide using prime factors.
    """
    nums = [i for i in range(1, max_divide + 1)]
    lcm = 1
    for prime in primes:
        while True:
            divide = 0
            for indis,value in enumerate(nums):
                if value % prime == 0:
                    divide += 1
                    value //= prime
                    nums[indis] = value
            if divide > 0:
                lcm *= prime
            else:
                break
    return lcm

def main():
    max_divide = int(input("Bir sayı giriniz:"))
    primes = find_prime_nums(max_divide)
    lcm = find_lcm(max_divide, primes)
    print(lcm)

main()