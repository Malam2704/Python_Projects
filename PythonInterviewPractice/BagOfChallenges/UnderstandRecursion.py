def subtract_recursively(num):
    if(num < 0):
        return None
    print(num)
    num -= 1
    subtract_recursively(num)

subtract_recursively(10)