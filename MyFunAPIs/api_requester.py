# Help me maake a function that calls an api running at 

import requests
import json

def generate_new_character(race=None, character_class=None):
    """
    Generate a new character using the Fantasy Character API
    
    Args:
        race (str, optional): The race of the character
        character_class (str, optional): The class of the character
    
    Returns:
        dict: The generated character data or None if request fails
    """
    url = "http://localhost:5000/generate_character"
    
    # Only include non-None values in the request
    payload = {}
    if race:
        payload['race'] = race
    if character_class:
        payload['class'] = character_class

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error generating character: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Generate a completely random character
    print("\nRandom character:")
    print(json.dumps(generate_new_character(), indent=2))
    
    # Generate an elf mage
    print("\nElf Mage:")
    print(json.dumps(generate_new_character("elf", "Mage"), indent=2)) 