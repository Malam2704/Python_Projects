def compress_string(old_str):
    new_str = ""
    curr_letter = old_str[0]
    occurence_counter = 0

    for i in range(0, len(old_str)):
        if(old_str[i] == curr_letter):
            occurence_counter += 1
        else:
            new_str += curr_letter
            new_str += str(occurence_counter)
            curr_letter = old_str[i]
            occurence_counter = 1
    
    new_str += curr_letter
    new_str += str(occurence_counter)
    
    return new_str

print(compress_string("aabcccccaaa"))
