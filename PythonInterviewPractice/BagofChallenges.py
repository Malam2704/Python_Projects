def palindrome_checker(my_string):
    my_string = my_string.lower()
    new_str = ""
    for l in my_string:
        if(l.isalnum()):
            new_str += l
    my_string = new_str

    if(len(my_string) == 0):
        return True
    elif(len(my_string) == 1):
        return True
    
    for i in range(0, len(my_string)):
        if(my_string[i] != my_string[(i+1)*-1]):
            return False
        
    return True

print("Palindromes")
print(palindrome_checker("racecar"), True)
print(palindrome_checker("madam"), True)
print(palindrome_checker("level"), True)
print(palindrome_checker("noon"), True)
print(palindrome_checker("deified"), True)

print("Non Palindromes")
print(palindrome_checker("hello"), False)
print(palindrome_checker("world"), False)
print(palindrome_checker("python"), False)
print(palindrome_checker("chatGPT"), False)

print("case sensitivity")
print(palindrome_checker("Racecar"), True)  # Assuming case insensitivity
print(palindrome_checker("MadAm"), True)

print("edge cases")
print(palindrome_checker(""), True)
print(palindrome_checker("a"), True)

print("Sentences")
print(palindrome_checker("A man a plan a canal Panama"), True)
print(palindrome_checker("Was it a car or a cat I saw"), True)
print(palindrome_checker("No lemon, no melon!"), True)
print(palindrome_checker("Eva, can I see bees in a cave?"), True)

print("Numbers")
print(palindrome_checker("12321"), True)
print(palindrome_checker("123456"), False)
print(palindrome_checker("1001"), True)