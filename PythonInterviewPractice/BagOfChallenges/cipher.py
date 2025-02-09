def caesar_cipher(cur_str, cipher):
    new_str = ""
    for i in cur_str:
        new_str += (chr(ord(i) + cipher))

    return new_str

print(caesar_cipher("abc", 2))