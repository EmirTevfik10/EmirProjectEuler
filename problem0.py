def tek_kareleri_üret():
    return (i*i for i in range(1,991001,2))

def main():
    toplam = sum(tek_kareleri_üret())
    print(toplam)

main()