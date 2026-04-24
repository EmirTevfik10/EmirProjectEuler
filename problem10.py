number = 3
total = 2
while number < 2000000:
    asal_mi = True
    for i in range(3, number):
        if number % i == 0:
            asal_mi = False
            break
        if i ** 2 > number:
            break
    if asal_mi:
        total += number
    number += 2
    print(number)
print(total)