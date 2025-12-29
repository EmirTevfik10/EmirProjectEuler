def fibonacci():
    """
    4.000.000 değerini geçinceye kadar fibonacci listesi üreten ve bu listeyi döndüren fonksiyon.
    """
    sayilar = [1,2]
    while True:
        sayi = sayilar[-1] + sayilar [-2]
        if sayi > 4000000:
            break
        else:
            sayilar.append(sayi)
    return sayilar

def cift_topla(sayilar):
    """
    Veri listesindeki çift sayıları toplayıp değerini döndüren fonksiyon.
    """
    toplam = 0
    for sayi in sayilar:
        if sayi % 2 == 0:
            toplam += sayi
    return toplam

def main():
    sayilar = fibonacci()
    toplam = cift_topla(sayilar)
    print(toplam)

main()