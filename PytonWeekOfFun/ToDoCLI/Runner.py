import csv

def print_csv_data():
    with open('data.csv', 'r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines[0],lines[1])

def add_task():
    with open('data.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        field = ["name","age","country"]
        while(True):
            
            choice = input("Here are your tasks, type 'new' for new task, or exit to leave: ")
            
            if(choice == "exit"):
                break
            elif(choice == "new"):
                user_date = input("Enter the date for your task: ")
                user_tasks = input("Enter your tasks you will complete: ")
                writer.writerow([user_date,user_tasks])


def main():
    while(True):
        print("Current Dates")
        print_csv_data()
        user_answer = input("What would you like to do?\n add - User can add a new item to their list\n exit - Leaves the application\n")

        if(user_answer == "exit"):
            break
        elif(user_answer == "add"):
            add_task()

main()