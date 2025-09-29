import requests

user_input = input("Give me a number, I give you a character: ")
if(user_input.isdigit()):
    user_num = int(user_input)
    response = requests.get(f'https://rickandmortyapi.com/api/character/{user_num}')
elif(user_input == "all"):
    response = requests.get(f'https://rickandmortyapi.com/api/character/')

    my_data = response.json()
    for i,j in my_data.items():
        for k in j:
            print(k)

