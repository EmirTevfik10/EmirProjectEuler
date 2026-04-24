def pythagoraen_triplet(a,b,c):
    if (a < b and b < c) and (a**2 + b**2 == c**2):
        return True
    
def find_specific_numbs(numb):
    first_list = []
    last_list = []
    a = 1
    b = 2 
    c = numb - 3
    while c > b:
        first_list.append([a,b,c])
        b += 1
        c -= 1
    for a,b,c in first_list:
        while b > a and c > b:
            last_list.append([a,b,c])
            a += 1
            c -= 1
    for a,b,c in last_list:
        if pythagoraen_triplet(a,b,c):
            return a,b,c
def main():
    a,b,c = find_specific_numbs(1000)
    print(a * b * c)

main()
        