def bit_counter(num):
    total = 1
    counter = 0
    while num <= 2^counter :
        print(counter, total)
        total *= 2
        counter += 1

bit_counter(5)


    