import random


# Humanoid superclass.
class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


# Human subclass.
class Humans(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        Humanoid.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    def add_attribute_points(self, attribute, points):
        if attribute == 'strength':
            self.strength += points
        elif attribute == 'dexterity':
            self.dexterity += points
        elif attribute == 'constitution':
            self.constitution += points
        elif attribute == 'intelligence':
            self.intelligence += points
        elif attribute == 'wisdom':
            self.wisdom += points
        elif attribute == 'charisma':
            self.charisma += points


# Elf subclass.
class Elves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        Humanoid.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    def boost_dexterity_charisma(self):
        self.dexterity += 2
        self.charisma += 2


# Dwarf subclass.
class Dwarves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        Humanoid.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    def boost_strength_constitution(self):
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2


# Character creation.
def characterCreation():

    # User choosing character race.
    valid_races = ["human", "elf", "dwarf"]
    race = input("What race would you like your character to be? (Human/Elf/Dwarf): ")
    while race.lower() not in valid_races:
        race = input("You may only choose Human, Elf, or Dwarf: ")
    

    # User choosing height.
    while True:
        try:
            height = int(input("How tall do you want your character to be? (3ft to 7ft): "))
            if height < 3 or height > 7:
                print("Height must be between 3ft and 7ft.")
            else:
                break
        except ValueError:
            print("Please enter a whole number.")
    

    # User choosing weight.
    while True:
        try:
            weight = int(input("How much do you want your character to weigh? (60lbs to 300lbs): "))
            if weight < 60 or weight > 300:
                print("Weight must be between 60lbs and 300lbs.")
            else:
                break
        except ValueError:
            print("Please enter a whole number.")
    

    # User choosing hair color.
    valid_hair_colors = ['white', 'silver', 'gray', 'black', 'brown', 'green', 'blue', 'yellow', 'pink', 'red', 'blonde']
    hair_color = input("What color do you want your characters hair to be? (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ")
    while hair_color.lower() not in valid_hair_colors:
            hair_color = input("You may only choose one of the given colors: ")

    
    # User choosing eye color.
    valid_eye_colors = ['white', 'black', 'red', 'green', 'blue', 'brown', 'purple', 'amber']
    eye_color = input("What color do you want your characters eyes to be? (white, black, red, green, blue, brown, purple, amber): ")
    while eye_color.lower() not in valid_eye_colors:
            eye_color = input("You may only choose one of the given colors: ")


    # Randomly generated attributes.
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)


    # Human special attribute.
    if race.lower() == 'human':
        character = Humans(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        print("\nAs a Human, you get to add 2 points to any attribute of your choice.")
        print("Please choose which attribute you want to increase by 2 points:")
        print("[1] Strength")
        print("[2] Dexterity")
        print("[3] Constitution")
        print("[4] Intelligence")
        print("[5] Wisdom")
        print("[6] Charisma")

        choice = None
        while choice not in [1, 2, 3, 4, 5, 6]:
            try:
                choice = int(input("Enter your choice (1-6): "))
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 6.")

        if choice == 1:
            character.strength += 2
        elif choice == 2:
            character.dexterity += 2
        elif choice == 3:
            character.constitution += 2
        elif choice == 4:
            character.intelligence += 2
        elif choice == 5:
            character.wisdom += 2
        elif choice == 6:
            character.charisma += 2


    # Elf special attribute.
    elif race.lower() == 'elf':
        character = Elves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        
        print("\nAs an Elf, you get a 100% resistance to Sleep, and +2 to your Dexterity and Charisma scores.")
        character.dexterity += 2
        character.charisma += 2


    # Dwarf special attribute.
    elif race.lower() == 'dwarf':
        character = Dwarves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        
        print("\nAs a Dwarf, you get a 20% resistance to Magic, +2 to your Strength and Constitution scores, and -2 to your Charisma score.")
        character.strength += 2
        character.constitution += 2
        character.charisma -= 2


    # Outputting the created character stats.
    print("\nYour character has been created!")
    print("Here are your generated stats.")
    print(f"Race: {race}")
    print(f"Height: {character.height}lbs")
    print(f"Weight: {character.weight}ft")
    print(f"Hair color: {character.hair_color}")
    print(f"Eye color: {character.eye_color}")

    print()
    print(f"Strength: {character.strength}")
    print(f"Dexterity: {character.dexterity}")
    print(f"Constitution: {character.constitution}")
    print(f"Intelligence: {character.intelligence}")
    print(f"Wisdom: {character.wisdom}")
    print(f"Charisma: {character.charisma}")


def main():
    characterCreation()


if __name__ == "__main__":
    main()
