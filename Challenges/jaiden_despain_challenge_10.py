class PlayerCharacter:
    def __init__(self, health, armor_rating, attack_power):
        self.health = health
        self.armor_rating = armor_rating
        self.attack_power = attack_power

    # Attribute Setters.
    def set_health(self, health):
        self.health = health
    def set_armor_rating(self, armor_rating):
        self.armor_rating = armor_rating
    def set_attack_power(self, attack_power):
        self.attack_power = attack_power

    # Attribute Getters.
    def get_health(self):
        return self.health
    def get_armor_rating(self):
        return self.armor_rating
    def get_attack_power(self):
        return self.attack_power


def main():
    # Asking the user to enter attribute values within specific ranges.
    health = int(input("Enter your character's health (1-100): "))
    while health < 1 or health > 100:
        health = int(input("Enter a valid value: "))
    
    armor_rating = int(input("Enter your character's armor rating (1-20): "))
    while armor_rating < 1 or armor_rating > 20:
        armor_rating = int(input("Enter a valid value: "))
    
    attack_power = int(input("Enter your character's attack power (1-20): "))
    while attack_power < 1 or attack_power > 20:
        attack_power = int(input("Enter a valid value: "))
    
    # Printing out the character's attributes.
    wizard = PlayerCharacter(health, armor_rating, attack_power)
    print("\nWizard's attributes:")
    print(f"Health: {wizard.get_health()}")
    print(f"Armor Rating: {wizard.get_armor_rating()}")
    print(f"Attack Power: {wizard.get_attack_power()}")


if __name__ == "__main__":
    main()
