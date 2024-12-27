import json

def add_task():
    with open('data.json', 'w') as file:
        while(True):
            print(file)
            choice = input("Choose a date or add a new one: ")
            
            if(choice == "exit"):
                break
            elif(choice == "new"):
                user_dict = dict()
                user_date = input("Enter your date: ")
                user_data = input("Enter List of Tasks you need to do: ")
                user_dict[user_date] = user_data
                json.dump(user_dict, file)


def main():
    while(True):
        user_answer = input("What would you like to do?\n add - User can add a new item to their list\n exit - Leaves the application\n")

        if(user_answer == "exit"):
            break
        elif(user_answer == "add"):
            add_task()

main()