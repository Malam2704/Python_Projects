def removeduplicates(arr):
    unique = set()
    for i in arr:
        if i not in unique:
            unique.add(i)

    # Unpacks a set into a list, or just list(unique)
    return [*unique]

print(removeduplicates([1,2,3,4,5,6,7,7,8,9,9,9]))