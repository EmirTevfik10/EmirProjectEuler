def three_digit_number():
    polindrom = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            sonuc = i * j
            if str(sonuc) == str(sonuc)[::-1] and sonuc > polindrom: 
                polindrom = sonuc
    return polindrom
def main():
    max_polindrom = three_digit_number()
    print(max_polindrom)
main()