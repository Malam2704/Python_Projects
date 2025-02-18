import time
import json
import os

class Item():
    def __init__(self, name, attack_power, price):
        self.name = name
        self.attack_power = attack_power 
        self.price = price

class Armor():
    def __init__(self, name, health_boost, price):
        self.name = name
        self.health_boost = health_boost
        self.price = price

class Monster():
     def __init__(self, name, health, attack, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward

class Player():
    def __init__(self, name, health=100, attack = 5, gold = 5, experience = 0):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold
        self.experience = experience
        self.current_item = "Basic Sword"
        self.current_armor = "Basic Armor"
        self.inventory = []

    def __str__(self):
        return f"{self.name}\n---------------\n  Attack: {self.attack}\n  Health: {self.health}\n  Gold: {self.gold}\n  Current Item: {self.current_item}\n  Current Armor: {self.current_armor}\n  Inventory: {self.inventory}"

    def add_inventory(new_item: Item):
        self.inventory.append(new_item)

def print_characters(characters):
    print("---------- Current Characters ----------")
    for character in characters:
        print(character)

def battle_function(player1, player2):
    original_player1_health = player1.health
    original_player2_health = player2.health

    print(" *** Battle Time! ***")
    while (player1.health > 0 and player2.health > 0):
        time.sleep(1)
        player2.health -= player1.attack
        print(f"   {player1.name} (Health: {player1.health}) attacks {player2.name} (Health: {player2.health})")
        time.sleep(1)
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

def load_players_json():
    # Open and read the JSON file
    new_characters = {}
    with open('players.json', 'r') as file:
        data = json.load(file)
        print(data)

    return new_characters

def main():
    playing = input("\n*********** Welcome to Treasure Quest! ***********\n\t Type 'Play' to Enter\n:")

    characters = load_players_json()
    
    shop_items = {"Basic Sword": Item("Basic Sword", 5, 5), 
                  "Bronze Sword": Item("Bronze Sword", 15, 15), 
                  "Silver Sword": Item("Silver Sword", 50, 50), 
                  "Gold Sword": Item("Gold Sword", 100, 100),
                  "Basic Armor": Item("Basic Sword", 5, 5), 
                  "Bronze Armor": Item("Bronze Sword", 15, 15), 
                  "Silver Armor": Item("Silver Sword", 50, 50), 
                  "Gold Armor": Item("Gold Sword", 100, 100)}
    monsters = {
        "Goblin": Monster("Goblin", 25, 3, 5),
        "Orc": Monster("Orc", 75, 7, 10),
        "Troll": Monster("Troll", 150, 10, 25),
        "Golem": Monster("Golem", 500, 15, 75),
        "Hobbit": Monster("Hobbit", 40, 2, 5),
        "Bomber": Monster("Bomber", 10, 200, 30),
        "Beast Rider": Monster("Beast Rider", 200, 20, 50),
        "Blazk Dragon": Monster("Black Dragon", 1000, 50, 100),
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
        player_action = input("\n****** Player Home *****\n -- Shop\n -- Fight\n -- Inventory\n -- Player Stats\n -- Exit Game (Type 'exit')\n -- Exit and Save (Type 'save')\n:")

        if(player_action.lower() == 'shop'):
            print("\n***** Shop Items *****")
            for item in shop_items:
                if(type(shop_items[item]) == Item):
                    print(f"\t{item}, Attack Power: {shop_items[item].attack_power}, Price: {shop_items[item].price}")
                elif(type(shop_items[item]) == Armor):
                    print(f"\t{item}, Health Boost: {shop_items[item].attack_power}, Price: {shop_items[item].price}")
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
            print("\n***** Arena Monsters *****")
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
        elif(player_action.lower() == 'player stats'):
            print("\n  ***** Player Stats *****")
            print(chosen_character)
        elif(player_action.lower() == 'exit' or player_action.lower() == 'exit game'):
            break
        elif(player_action.lower() == 'save' or player_action.lower() == 'save game'):
            if os.path.isfile('./players.json') and os.access('./players.json', os.R_OK):
                # checks if file exists
                print ("File exists and is readable")

        leave = input("Type anything to leave")

main()