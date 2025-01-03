class Player():
    def __init__(self, name, health=100, gold = 5):
        self.name = name
        self.health = health
        self.gold = gold

def print_characters(characters):
    for character in characters:
        print(character.name)

def main():
    characters = set()
    playing = input("Welcome to Treasure Quest!\n Type Play to Enter\n")
    while(True):
        if(playing.lower() != "play"):
            break
        
        if(len(characters) == 0):
            character_name = input("Name your character: ")
            characters.add(Player(character_name))
        else:
            print("Current Characters")
            print_characters(characters)
            creating_new_character = input("type 'create' to make a new character or 'continue' to resume Player journey")

            if(creating_new_character == 'create'):
                character_name = input("Name your character: ")
                characters.add(Player(character_name))
            elif(creating_new_character == 'continue'):
                chosen_character = input("Choose a character: ")
                for character in characters:
                    if(chosen_character.lower() == character.name):
                        print("Let us Continue " + character.name)

main()