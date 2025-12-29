def fibonacci(max_value):
    """
    4.000.000 değerini geçinceye kadar fibonacci listesi üreten ve bu listeyi döndüren fonksiyon.
    """
    numbers = [1,2]
    while True:
        next_number = numbers[-1] + numbers[-2]
        if next_number > max_value:
            break
        else:
            numbers.append(next_number)
    return numbers

def sum_even_numbers(numbers):
    """
    Veri listesindeki çift sayıları toplayıp değerini döndüren fonksiyon.
    """
    return sum(num for num in numbers if num % 2 == 0)

def main():
    max_value = 4000000
    numbers = fibonacci(max_value)
    total = sum_even_numbers(numbers)
    print(total)

main()