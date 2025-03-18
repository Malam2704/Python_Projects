from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample data - you can expand these
RACES = {
    'human': {
        'lifespan': 80,
        'traits': ['adaptable', 'ambitious', 'versatile'],
        'bonus': 'All stats +1'
    },
    'elf': {
        'lifespan': 700,
        'traits': ['graceful', 'magical_affinity', 'keen_senses'],
        'bonus': 'Magic +3, Agility +2'
    },
    'undead': {
        'lifespan': 'eternal',
        'traits': ['undying', 'cold_resistance', 'fearsome'],
        'bonus': 'Cannot die from natural causes, Weak to holy magic'
    },
    'dragon': {
        'lifespan': 1000,
        'traits': ['flying', 'breath_weapon', 'ancient_wisdom'],
        'bonus': 'Strength +5, Natural Armor'
    }
}

CLASSES = ['Warrior', 'Mage', 'Rogue', 'Cleric', 'Dragonknight', 'Necromancer']

@app.route('/')
def hello_world():
    return jsonify(message="Welcome to the Fantasy Character API!")

@app.route('/races', methods=['GET'])
def get_races():
    return jsonify(available_races=list(RACES.keys()))

@app.route('/race/<race_name>', methods=['GET'])
def get_race_info(race_name):
    if race_name.lower() in RACES:
        return jsonify(RACES[race_name.lower()])
    return jsonify(error="Race not found"), 404

@app.route('/generate_character', methods=['POST'])
def generate_character():
    data = request.get_json()
    requested_race = data.get('race', random.choice(list(RACES.keys())))
    requested_class = data.get('class', random.choice(CLASSES))
    
    if requested_race.lower() not in RACES:
        return jsonify(error="Invalid race"), 400
    
    character = {
        'race': requested_race,
        'class': requested_class,
        'level': 1,
        'traits': RACES[requested_race.lower()]['traits'],
        'power_level': random.randint(1, 100),
        'destiny': generate_destiny(requested_race, requested_class)
    }
    
    return jsonify(character)

def generate_destiny(race, character_class):
    destinies = [
        f"The Last {race} {character_class} of the Ancient Kingdom",
        f"Prophecied Savior of the {race} Realms",
        f"Dark Lord's Chosen {character_class}",
        f"Guardian of the Forgotten {race} Magic",
        f"Wandering {race} {character_class} of Legend"
    ]
    return random.choice(destinies)

if __name__ == '__main__':
    app.run(debug=True)