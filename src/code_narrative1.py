import random

class Story:
    def __init__(self):
        self.secret = random.choice(["ancient artifact", "hidden treasure", "mystical gem"])
        self.narrative = {
            "ancient artifact": [
                "In a forgotten temple, deep within the jungle, lies an ancient artifact.",
                "Legends say it holds the power to control time.",
                "Many have tried to find it, but none have returned.",
                "You must navigate through treacherous paths and avoid deadly traps."
            ],
            "hidden treasure": [
                "On a deserted island, buried under the sands, lies a hidden treasure.",
                "Pirates once fought over it, leaving behind a map with cryptic clues.",
                "The treasure is said to bring immense wealth to its finder.",
                "Beware of the ghostly pirates that guard the treasure."
            ],
            "mystical gem": [
                "In the heart of a mystical forest, guarded by magical creatures, lies a mystical gem.",
                "The gem glows with an otherworldly light, said to grant wishes.",
                "Only those pure of heart can find it.",
                "You must earn the trust of the forest creatures to proceed."
            ]
        }
        self.characters = {
            "ancient artifact": ["Old Sage", "Temple Guardian"],
            "hidden treasure": ["Pirate Ghost", "Island Hermit"],
            "mystical gem": ["Forest Elf", "Mystic Wizard"]
        }
        self.locations = ["Jungle", "Temple", "Island", "Forest"]
        self.current_narrative_index = 0

    def start_story(self):
        print("Welcome to the journey of discovery!")
        print("You are about to embark on an adventure to find a hidden secret.")
        self.provide_narrative()

    def provide_narrative(self):
        if self.current_narrative_index < len(self.narrative[self.secret]):
            print(f"Chapter {self.current_narrative_index + 1}: {self.narrative[self.secret][self.current_narrative_index]}")
            self.current_narrative_index += 1
        else:
            print("The story has reached its climax. Make your guess!")

    def interact_with_character(self):
        character = random.choice(self.characters[self.secret])
        print(f"You encounter {character}. They have a clue for you.")
        if character == "Old Sage":
            print("Old Sage: 'The artifact is hidden where time stands still.'")
        elif character == "Temple Guardian":
            print("Temple Guardian: 'Only the worthy can pass.'")
        elif character == "Pirate Ghost":
            print("Pirate Ghost: 'The treasure is buried deep under the sands.'")
        elif character == "Island Hermit":
            print("Island Hermit: 'Follow the map and beware of the ghosts.'")
        elif character == "Forest Elf":
            print("Forest Elf: 'The gem is protected by the ancient magic.'")
        elif character == "Mystic Wizard":
            print("Mystic Wizard: 'Only the pure of heart can find the gem.'")

    def explore_location(self):
        location = random.choice(self.locations)
        print(f"You explore the {location}.")
        if location == "Jungle":
            print("You find a hidden path leading deeper into the jungle.")
        elif location == "Temple":
            print("You discover ancient writings on the temple walls.")
        elif location == "Island":
            print("You find a piece of the pirate's map.")
        elif location == "Forest":
            print("You encounter magical creatures guarding the path.")

    def check_guess(self, guess):
        if guess.lower() == self.secret:
            print("Congratulations! You've discovered the hidden secret!")
            return True
        else:
            print("That's not correct. The story continues...")
            self.provide_narrative()
            return False

def main():
    story = Story()
    story.start_story()
    discovered = False
    while not discovered:
        action = input("Do you want to (1) make a guess, (2) interact with a character, or (3) explore a location? ")
        if action == "1":
            guess = input("What do you think the hidden secret is? ")
            discovered = story.check_guess(guess)
        elif action == "2":
            story.interact_with_character()
        elif action == "3":
            story.explore_location()
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()