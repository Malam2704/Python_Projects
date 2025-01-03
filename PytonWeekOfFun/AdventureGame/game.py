class Player():
    def __init__(self, name, health=100, attack = 5, gold = 5):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold
        self.current_item = "Basic Sword"
        self.current_armor = "Basic Armor"
        self.inventory = []

class Item():
    def __init__(self, name, attack_power, price):
        self.name = name
        self.attack_power = attack_power 
        self.price = price

class Monster():
     def __init__(self, name, health, attack, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward

def print_characters(characters):
    print("---------- Current Characters ----------")
    for character in characters:
        print(character)

def battle_function(player1, player2):
    original_player1_health = player1.health
    original_player2_health = player2.health

    print(" *** Battle Time! ***")
    while (player1.health > 0 and player2.health > 0):
        player2.health -= player1.attack
        print(f"   {player1.name} (Health: {player1.health}) attacks {player2.name} (Health: {player2.health})")
        player1.health -= player2.attack
        print(f"   {player2.name} (Health: {player2.health}) attacks {player1.name} (Health: {player1.health})")
    
    if(player1.health > 0):
        print(f"{player1.name} wins")
    elif(player2.health > 0):
        print(f"{player2.name} wins")

    if(type(player2) == Monster):
        player1.gold += player2.gold_reward

    player1.health = original_player1_health
    player2.health = original_player2_health

def main():
    playing = input("\n*********** Welcome to Treasure Quest! ***********\n\t Type 'Play' to Enter\n:")

    characters = {}
    shop_items = {"Basic Sword": Item("Basic Sword", 5, 5), 
                  "Bronze Sword": Item("Bronze Sword", 15, 15), 
                  "Silver Sword": Item("Silver Sword", 50, 50), 
                  "Gold Sword": Item("Gold Sword", 100, 100)}
    monsters = {
        "Goblin": Monster("Goblin", 25, 3, 5),
        "Orc": Monster("Orc", 75, 7, 10),
        "Troll": Monster("Troll", 150, 10, 25),
        "Golem": Monster("Golem", 500, 15, 75),
    }
    
    chosen_character = None
    
    while(chosen_character == None):
        if(playing.lower() != "play"):
            break
        
        if(len(characters) == 0):
            character_name = input("Name your character: ")
            characters[character_name] = Player(character_name)
            chosen_character = characters[character_name]
        else:
            print_characters(characters)
            creating_new_character = input("Type 'create' to make a new character or enter character name: ")
            if(creating_new_character == 'create'):
                character_name = input("Name your character: ")
                characters[character_name] = Player(character_name)
            else:
                if creating_new_character in characters:
                    print("Let us Continue " + creating_new_character + "\n")
                    chosen_character = characters[creating_new_character]
                else:
                    print("!!!!! Character not found !!!!!")
    
    while(playing.lower() == "play"):
        player_action = input("****** Player Home *****\n -- Shop\n -- Fight\n -- Inventory\n -- Exit Game (Type 'exit')\n:")

        if(player_action.lower() == 'shop'):
            print("\n  ***** Shop Items *****")
            for item in shop_items:
                print(f"\t{item}, Attack Power: {shop_items[item].attack_power}, Price: {shop_items[item].price}")
            player_shop_action = input("  What will you do?\n    Buy\n    Exit\n:" )

            if(player_shop_action.lower() == 'exit'):
                continue
            elif(player_shop_action.lower() == 'buy'):
                buying_choice = input('type in item to buy: ')
                if buying_choice in shop_items:
                    if(chosen_character.gold >= shop_items[buying_choice].price):
                        chosen_character.gold -= shop_items[buying_choice].price
                        chosen_character.inventory.append(shop_items[buying_choice])
                        print("You obtained " + buying_choice)
                    else:
                        print("You cannot afford this item")
                else:
                    print("Item does not exist")
        elif(player_action.lower() == 'fight'):
            print("\n  ***** Arena Monsters *****")
            for monster in monsters:
                print(f"\t{monster}, Health: {monsters[monster].health}, Attack Power: {monsters[monster].attack}")
            player_fight_action = input("  What will you do?\n    Fight\n    Exit\n:" )

            if(player_fight_action.lower() == 'exit'):
                continue
            elif(player_fight_action.lower() == 'fight'):
                fighting_choice = input('type in monster to fight: ')
                if fighting_choice in monsters:
                    battle_function(chosen_character, monsters[fighting_choice])
                else:
                    print("Monster does not exist")

        elif(player_action.lower() == 'inventory'):
            print("\n  ***** Inventory Items *****")
            for item in chosen_character.inventory:
                print(f"{item.name}")
            print("\n")
        if(player_action.lower() == 'exit'):
            break

main()