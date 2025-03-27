def maxminarray(arr):
    if(len(arr) == 0):
        return None
    if(len(arr) == 1):
        min, max = arr[0]
        return (min,max)
    
    min = arr[0]
    max = arr[0]
    for i in range(0, len(arr)):
        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]

    return min,max

print(maxminarray([1,2,3,4,5,6,7,8,9]))

# Can also use min(arr) and max(arr) functions