def rotate_array(arr, steps):
    new_arr = []
    for i in range(0,len(arr)):
        if( i+ steps < len(arr)):
            new_arr.append(arr[i+steps])

    j = 0
    while(True):
        if(j == steps):
            break
        else:
            new_arr.append(arr[j])
            j+=1
            
    return new_arr

print(rotate_array([1,2,3,4,5,6], 2))