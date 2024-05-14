import json
import random


class Character:
    def __init__(self, name, dexterity, wits):
        self.name = name
        self.dexterity = dexterity
        self.wits = wits
        self.initiative = 0

    def roll_initiative(self):
        self.initiative = self.dexterity + self.wits + random.randint(1, 10)

class Combat:
    def __init__(self):
        self.characters = []

    def add_character(self, name, dexterity, wits):
        character = Character(name, dexterity, wits)
        self.characters.append(character)

    def load_characters_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for name, stats in data.items():
                self.add_character(name, stats['dexterity'], stats['wits'])

    def add_npcs(self, npcs):
        for name, stats in npcs.items():
            self.add_character(name, stats['dexterity'], stats['wits'])

    def roll_initiative_for_all(self):
        for character in self.characters:
            character.roll_initiative()

    def sort_characters_by_initiative(self):
        self.characters.sort(key=lambda x: x.initiative, reverse=True)

    def display_initiative_order(self):
        print("\nInitiative Order:")
        for character in self.characters:
            print(f"{character.name}: {character.initiative}")

    def new_combat_round(self):
        self.roll_initiative_for_all()
        self.sort_characters_by_initiative()
        self.display_initiative_order()

def main():
    combat = Combat()

    json_file = 'characters.json'
    combat.load_characters_from_json(json_file)

    npcs = {
        "NPC 1": {
            "dexterity": 4,
            "wits": 2
        },
        "NPC 2": {
            "dexterity": 3,
            "wits": 4
        }
    }

    combat.add_npcs(npcs)
    combat.new_combat_round()

if __name__ == '__main__':
    main()
