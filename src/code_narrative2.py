import random
import time
import os

class Character:
    def __init__(self, name, description, dialogue):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.has_interacted = False
        self.quest_item = None

class Location:
    def __init__(self, name, description, connections=None):
        self.name = name
        self.description = description
        self.connections = connections if connections else {}
        self.characters = []
        self.items = []

class Game:
    def __init__(self):
        self.current_location = None
        self.inventory = []
        self.game_map = {}
        self.characters = {}
        self.game_complete = False
        self.artifacts_found = 0
        self.setup_game()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def setup_game(self):
        # Create locations
        self.create_locations()
        # Create characters
        self.create_characters()
        # Set starting location
        self.current_location = self.game_map["village_square"]
        
    def create_locations(self):
        # Initialize locations
        self.game_map = {
            "village_square": Location("Village Square", 
                "A bustling square with ancient stone buildings and a mysterious fountain at its center."),
            "ancient_library": Location("Ancient Library",
                "Towering bookshelves filled with dusty tomes and scrolls. Magic seems to linger in the air."),
            "mystic_grove": Location("Mystic Grove",
                "A serene forest clearing where ethereal lights dance between the trees."),
            "forgotten_ruins": Location("Forgotten Ruins",
                "Crumbling stone structures covered in mysterious glyphs and symbols."),
            "crystal_cave": Location("Crystal Cave",
                "A spectacular cave system filled with glowing crystals of various colors.")
        }
        
        # Set connections between locations
        self.game_map["village_square"].connections = {
            "north": "ancient_library",
            "east": "mystic_grove"
        }
        self.game_map["ancient_library"].connections = {
            "south": "village_square",
            "east": "forgotten_ruins"
        }
        self.game_map["mystic_grove"].connections = {
            "west": "village_square",
            "north": "forgotten_ruins",
            "east": "crystal_cave"
        }
        self.game_map["forgotten_ruins"].connections = {
            "west": "ancient_library",
            "south": "mystic_grove"
        }
        self.game_map["crystal_cave"].connections = {
            "west": "mystic_grove"
        }

    def create_characters(self):
        # Create and place characters
        elder_sage = Character("Elder Sage", 
            "A wise old woman with silver hair and knowing eyes.",
            {"greeting": "Welcome, seeker. The artifacts of Eldara hold great power...",
             "quest": "Find the three sacred artifacts: the Crystal of Truth, the Scroll of Wisdom, and the Medallion of Balance.",
             "hint": "The library holds more than just books, young one."})
        
        mysterious_scholar = Character("Mysterious Scholar",
            "A cloaked figure surrounded by floating books.",
            {"greeting": "Ah, another searching for knowledge...",
             "hint": "The grove whispers secrets to those who listen carefully."})
        
        forest_spirit = Character("Forest Spirit",
            "A ethereal being composed of swirling leaves and light.",
            {"greeting": "Nature holds many secrets...",
             "hint": "The crystals in the cave respond to ancient magic."})

        # Place characters in locations
        self.game_map["village_square"].characters.append(elder_sage)
        self.game_map["ancient_library"].characters.append(mysterious_scholar)
        self.game_map["mystic_grove"].characters.append(forest_spirit)

    def display_location(self):
        self.clear_screen()
        print(f"\n=== {self.current_location.name} ===")
        print(self.current_location.description)
        
        # Show available directions
        print("\nPossible directions:", end=" ")
        for direction in self.current_location.connections.keys():
            print(direction, end=" ")
        
        # Show characters present
        if self.current_location.characters:
            print("\n\nCharacters present:")
            for character in self.current_location.characters:
                print(f"- {character.name}")

    def talk_to_character(self, character_name):
        for character in self.current_location.characters:
            if character.name.lower() == character_name.lower():
                print(f"\n{character.name}: {character.dialogue['greeting']}")
                if not character.has_interacted:
                    if 'quest' in character.dialogue:
                        print(f"\n{character.name}: {character.dialogue['quest']}")
                    character.has_interacted = True
                if 'hint' in character.dialogue:
                    print(f"\n{character.name}: {character.dialogue['hint']}")
                return
        print("\nThere's no one here by that name.")

    def move(self, direction):
        if direction in self.current_location.connections:
            new_location = self.game_map[self.current_location.connections[direction]]
            self.current_location = new_location
            return True
        else:
            print("\nYou cannot go that way.")
            return False

    def search_location(self):
        chance = random.random()
        if chance < 0.3 and self.artifacts_found < 3:  # 30% chance to find an artifact
            artifact_names = ["Crystal of Truth", "Scroll of Wisdom", "Medallion of Balance"]
            if artifact_names[self.artifacts_found] not in self.inventory:
                print(f"\nYou found the {artifact_names[self.artifacts_found]}!")
                self.inventory.append(artifact_names[self.artifacts_found])
                self.artifacts_found += 1
                if self.artifacts_found == 3:
                    self.game_complete = True
                    return True
        else:
            print("\nYou search the area but find nothing of interest...")
        return False

    def play(self):
        print("\nWelcome to The Lost Artifacts of Eldara!")
        print("\nYou are a seeker of ancient mysteries, drawn to the legendary land of Eldara.")
        print("Your quest: to find the three sacred artifacts that hold the key to ancient wisdom.")
        
        while not self.game_complete:
            self.display_location()
            print("\nCommands: move [direction], talk [character], search, inventory, quit")
            command = input("\nWhat would you like to do? ").lower().split()
            
            if not command:
                continue
                
            if command[0] == "quit":
                break
            elif command[0] == "move" and len(command) > 1:
                self.move(command[1])
            elif command[0] == "talk" and len(command) > 1:
                self.talk_to_character(" ".join(command[1:]))
            elif command[0] == "search":
                if self.search_location() and self.game_complete:
                    print("\nCongratulations! You have found all three artifacts!")
                    print("The secrets of Eldara have been revealed to you!")
                    break
            elif command[0] == "inventory":
                if self.inventory:
                    print("\nYour inventory:")
                    for item in self.inventory:
                        print(f"- {item}")
                else:
                    print("\nYour inventory is empty.")
            else:
                print("\nInvalid command. Try again.")
            
            time.sleep(1)

if __name__ == "__main__":
    game = Game()
    game.play()
