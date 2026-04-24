def is_pythagorean(a,b,c):
    return a < b and b < c and a**2 + b**2 == c**2
    
def find_triplet(total):
    for a in range(1,total):
        for b in range(a + 1, total):
            c = total - a - b
            if c <= b:
                break
            if is_pythagorean(a, b, c):
                return a, b, c 

def main():
    a, b, c = find_triplet(1000)
    print(f"{a} x {b} x {c} = {a * b * c}")

main()
        