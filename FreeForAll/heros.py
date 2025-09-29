class Unit():
    def __init__(self, name):
        self.name = name
        

class NPC(Unit):
    def __init__(self, name, dialogue="Hello there dear traveler"):
        super().__init__(name)
        self.__dialogue = dialogue

    def say_dialogue(self):
        print(self.__dialogue)
        
class Player(Unit):
    def __init__(self, name, health, player_class):
        super().__init__(name)
        self.health = health
        self.player_class = player_class

    def say_class(self):
        print(self.player_class)

def main():
    dave = NPC("Dave")
    gazef = Player("Gazef", 100, "Warrior")

    dave.say_dialogue()
    gazef.say_class()

if __name__ == "__main__":
    main()