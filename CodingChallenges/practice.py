def reverse_string(my_string):
    new_str = ""
    for i in range(len(my_string)-1, -1, -1):
        print(my_string[i])
reverse_string("Taco Cat")

def find_target_in_array(target_num, my_array):
    return my_array.index(target_num)
print(find_target_in_array(5, [1,2,3,4,5,6]))

def calculate_factorial(my_number):
    sum = 1
    for i in range(my_number, 0, -1):
        sum *= i
    return sum
print(calculate_factorial(5))