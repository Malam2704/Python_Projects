class Player():
    def __init__(self, name, health=100, gold = 5):
        self.name = name
        self.health = health
        self.gold = gold
        self.current_item = "Basic Sword"
        self.current_armor = "Basic Armor"

def print_characters(characters):
    print("\n----------Current Characters----------")
    for character in characters:
        print(character.name)
    print('\n')

def main():
    characters = set()
    playing = input("Welcome to Treasure Quest!\n Type 'Play' to Enter\n")
    chosen_character = None
    
    while(chosen_character == None):
        if(playing.lower() != "play"):
            break
        
        if(len(characters) == 0):
            character_name = input("Name your character: ")
            characters.add(Player(character_name))
        else:
            
            print_characters(characters)
            
            creating_new_character = input("type 'create' to make a new character or 'continue' to resume Player journey: ")

            if(creating_new_character == 'create'):
                character_name = input("Name your character: ")
                characters.add(Player(character_name))
            elif(creating_new_character == 'continue'):
                chosen_character = input("Choose a character: ")
                for character in characters:
                    if(chosen_character.lower() == (character.name).lower()):
                        print("Let us Continue " + character.name)
    
    while(True):


main()