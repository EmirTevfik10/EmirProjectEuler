def tek_mi():
    sayilar = [i**2 for i in range(1,991001,1)]
    tek_kare = []
    for sayi in sayilar:
        if sayi % 2 != 0:
            tek_kare.append(sayi)
    return tek_kare

def topla(tek_kare):
    toplam = 0
    for sayi in tek_kare:
        toplam += sayi
    return toplam

def main():
    tek_kare = tek_mi()
    toplam = topla(tek_kare)
    print(toplam)

main()