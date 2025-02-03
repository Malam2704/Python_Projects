def fibonacci(num):
    if(num <= 0):
        return 0

    arr = [0, 1]
    for i in range(2, num):
        arr.append(arr[i-1] + arr[i-2])

    return arr

def fibonacci_recursive(num):
    if num <= 0:
        return None
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

# Okay so we start wiht a number like 5, then we have two starters 1 and 0
# then we start to make the third num 

    
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci_recursive(8))