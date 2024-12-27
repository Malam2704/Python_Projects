import json

def print_json_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
        for date in data:
            print(date)

def add_task():
    print("Current Dates")
    print_json_data()

    with open('data.json', 'a') as file:
        while(True):
            
            choice = input("Choose a date or type 'new' for new task: ")
            
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