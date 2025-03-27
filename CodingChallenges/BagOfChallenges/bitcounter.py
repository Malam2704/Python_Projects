# def bit_counter(num):
    

# bit_counter(5)

# Make a bit counter, so a number like 5 in decimal will be 101 in binary
# So if I have a number like 72, I'm thinking which exponene tof 2 is 
"""
added up to 72 or closest which is 64, or 2 ^ 6. Which mean 1000000.
Giving us 8 left, which can be subtracted by 2 ^ 3 or 1000
"""
def return_binary(exponent):
    bini = "1"
    for i in range(0, exponent):
        bini += "0"

    return int(bini)

def binary_counter(number):
    binary_number = 0
    start_exponent = 0
    while(number > 0):
        while(2**(start_exponent+1) <= number):
            start_exponent += 1

        binary_number += return_binary(start_exponent)
        number -= 2**start_exponent
        start_exponent = 0

    return binary_number


print(binary_counter(72))
        
    