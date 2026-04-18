asal_sayilar = [2]
sayi = 3
while len(asal_sayilar) < 10001:
    bs = 0
    dene = sayi
    for asal in asal_sayilar:
        while dene % asal == 0:
            dene //= asal
            bs += 1
        if bs > 1:
            break
    if bs == 1:
        print(dene)    
        asal_sayilar.append(dene) 
    sayi += 1
