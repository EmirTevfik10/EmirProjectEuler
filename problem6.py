def find_first_hundred():
    
    sum_square = ((100 * 101) / 2) ** 2
    square_sum = 0
    
    for numb in range(1,101,1):
        square_sum += numb ** 2
    
    diffirence = sum_square - square_sum
    
    return diffirence

def main():
    difference = find_first_hundred()
    print(difference)

main()    