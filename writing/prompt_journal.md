## 1. Prompts Used
First Copilot prompt:

"Your goal is to generate python code that creates discovery. The program should be designed so that the user will go on a journey/discover to look for a hidden secret."

Second Copilot prompt:

"Your goal is to generate python code that creates discovery. The discovery should focus on storytelling elements and should have a clear narrative. The program should be designed so that the user will go on a journey/discover to look for a hidden secret."

Third and final Copilot prompt:

Note: Same one used for the Claude sonnet, which is the second LLM used.

"Your goal is to generate python code that creates discovery. There should be detailed descriptions and background stories. Introduce characters that the user can interact with, lastly add a map or some sort of locations that the user can interact with. The program should be designed so that the user will go on a journey/discover to look for a hidden secret."

## 2. Prompting Strategy
First Copilot output:
```python
import random

class Journey:
    def __init__(self):
        self.secret = random.choice(["treasure", "magic stone", "ancient scroll"])
        self.clues = {
            "treasure": ["It's shiny and valuable.", "Pirates often seek it.", "You might find it in a chest."],
            "magic stone": ["It has mystical powers.", "Wizards use it.", "It's often found in enchanted places."],
            "ancient scroll": ["It contains old knowledge.", "Scholars seek it.", "You might find it in a library."]
        }
        self.current_clue_index = 0

    def start_journey(self):
        print("Welcome to the journey of discovery!")
        print("You need to find a hidden secret.")
        self.provide_clue()

    def provide_clue(self):
        if self.current_clue_index < len(self.clues[self.secret]):
            print(f"Clue {self.current_clue_index + 1}: {self.clues[self.secret][self.current_clue_index]}")
            self.current_clue_index += 1
        else:
            print("No more clues available. Make your guess!")

    def check_guess(self, guess):
        if guess.lower() == self.secret:
            print("Congratulations! You've found the hidden secret!")
            return True
        else:
            print("That's not correct. Keep trying!")
            self.provide_clue()
            return False

def main():
    journey = Journey()
    journey.start_journey()
    found = False
    while not found:
        guess = input("What's your guess? ")
        found = journey.check_guess(guess)

if __name__ == "__main__":
    main()
```
Second output:
```python
import random

class Story:
    def __init__(self):
        self.secret = random.choice(["ancient artifact", "hidden treasure", "mystical gem"])
        self.narrative = {
            "ancient artifact": [
                "In a forgotten temple, deep within the jungle, lies an ancient artifact.",
                "Legends say it holds the power to control time.",
                "Many have tried to find it, but none have returned."
            ],
            "hidden treasure": [
                "On a deserted island, buried under the sands, lies a hidden treasure.",
                "Pirates once fought over it, leaving behind a map with cryptic clues.",
                "The treasure is said to bring immense wealth to its finder."
            ],
            "mystical gem": [
                "In the heart of a mystical forest, guarded by magical creatures, lies a mystical gem.",
                "The gem glows with an otherworldly light, said to grant wishes.",
                "Only those pure of heart can find it."
            ]
        }
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
        guess = input("What do you think the hidden secret is? ")
        discovered = story.check_guess(guess)

if __name__ == "__main__":
    main()
```
Third Copilot output:
```python
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
```

I started with a simple zero-shot prompt, and the output code was very basic and barely had any storytelling or narrative at all. The second prompt was a few-shot but very open-ended to incorporate more of the narrative and storytelling elements. The third prompt was a few-shot which had clear instructions on what to include. The output captured narrative and storytelling elements much better.

## 3. Output Evaluation

For each generated code output, consider:
- Narrative Structure: How does the organization reflect the theme? Is there a clear flow that resembles a narrative?
- Commentary and Documentation: How do Copilot’s comments contribute to the narrative? Do they add meaning to the code?
- Design Choices: Evaluate how Copilot's naming conventions, variable usage, and logic choices enhance or detract from the narrative.

### Copilot

The first output was very basic. There was a sense of narrative with the user guessing different clues to find the treasure, however, the user only got three clues. After that, there were no clues. The user was then left to figure out the secret without any clues which was very hard. There is a flow of narrative but it is not detailed at all. The design choices are logical and easy to follow. I did not get any comments.

The second output had more story and narrative to it while still following the same logic as in the previous output. The user only had three guesses again which made it very hard to guess the secret. The narrative and storytelling of this code was much better. In the beginning, you are on a deserted island and you have a quest to find the hidden secret. As you guess, the program gives more detail and context to the story. There is a clear structure that reflects the theme of a discovery. This output also has added narrative and storytelling elements. No comments from this run either. The naming of the definitions makes it easy to follow along and make additions to the code if needed.

The third output had great detail and good storytelling. The user is still on a quest and decides on whether to take a guess, talk to a character, or explore a location. The talk to a character and discover a location are clues but with a narrative and storytelling focus. The code is longer than before but very easy to follow, no comments on this run either.

### Other Single LLM

I used Claude sonnet. The model produces a very detailed program, graphically in the terminal but also with the functionality of the program. The program has characters you can interact with, inventory, and different directions to move in. The code has a clear narrative however it is hard to follow because clues and interactions only stay in the terminal for one second. The code generated by Copilot is simpler and more fun to interact with. The code is hard to follow and compared to Copilot harder to make changes due to its complexity.

## 4. Reflection

The quality of the code improved as I updated my prompts. In the beginning, it was very simple but more complicated and narrative-focused as the prompts improved. The Copilot suggestions were helpful and very accurate compared to the more general improvements suggested by Claude sonnet. The suggestions from Copilot gave me the impression that they wanted to improve the user experience while the Claude sonnet suggestions were not as accurate.