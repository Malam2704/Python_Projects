class Player():
    def __init__(self, name, health=100, gold = 5):
        self.name = name
        self.health = health
        self.gold = gold
        self.current_item = "Basic Sword"
        self.current_armor = "Basic Armor"
        self.inventory = []

class Item():
    def __init__(self, name, attack_power, price):
        self.name = name
        self.attack_power = attack_power
        self.price = price

def print_characters(characters):
    print("\n----------Current Characters----------")
    for character in characters:
        print(character.name)
    print('\n')

def main():
    playing = input("\n*********** Welcome to Treasure Quest! ***********\n\t Type 'Play' to Enter\n")

    characters = {}
    shop_items = {"Basic Sword": Item("Basic Sword", 5, 5), 
                  "Bronze Sword": Item("Bronze Sword", 15, 15), 
                  "Silver Sword": Item("Silver Sword", 50, 50), 
                  "Gold Sword": Item("Gold Sword", 100, 100)}
    
    chosen_character = None
    
    while(chosen_character == None):
        if(playing.lower() != "play"):
            break
        
        if(len(characters) == 0):
            character_name = input("Name your character: ")
            characters[character_name] = Player(character_name)
        else:
            
            print_characters(characters)
            
            creating_new_character = input("type 'create' to make a new character or 'continue' to resume Player journey: ")

            if(creating_new_character == 'create'):
                character_name = input("Name your character: ")
                characters[character_name] = Player(character_name)
            elif(creating_new_character == 'continue'):
                chosen_character = input("Choose a character: ")
                if chosen_character in characters:
                    print("Let us Continue " + chosen_character + "\n")
                    chosen_character = characters[chosen_character]
    
    while(True):
        player_action = input("****** Player Home *****\n -- Shop\n -- Fight\n -- Exit Game (Type 'exit')\n")

        if(player_action.lower() == 'shop'):
            print("\n ***** Shop Items *****")
            for item in shop_items:
                print(f"\t{item}, Attack Power: {shop_items[item].attack_power}, Price: {shop_items[item].price}")
            player_shop_action = input("What will you do?\n Buy\n Exit: " )

            if(player_shop_action.lower() == 'exit'):
                continue
            elif(player_shop_action.lower() == 'buy'):
                buying_choice = input('type in item to buy: ')
                if buying_choice in shop_items:
                    if(chosen_character.gold > shop_items[buying_choice].price):
                        print("You obtained " + buying_choice)
                        chosen_character.gold -= shop_items[buying_choice].price
                        chosen_character.inventory.append(shop_items[buying_choice])
                    else:
                        print("You cannot afford this item")
        elif(player_action.lower() == 'inventory'):
            print("\n ***** Shop Items *****")
            for item in chosen_character.inventory:
                print(item)
        if(player_action.lower() == 'exit'):
            break

main()