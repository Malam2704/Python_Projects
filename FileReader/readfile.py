with open("FileReader/example.txt", "r") as file:
    for line in file:
        print(line.strip(), len(line))