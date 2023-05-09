# Instructions

For this challenge, you will create a Superclass called Humanoids, followed by three subclasses called Humans, Elves and Dwarves.  All three subclasses will inherit all the base features associated with the Humanoid class, but each will contain a few additional methods that help distinguish them from one another. 

### class Humanoid:
Height: 3ft - 7ft
Weight: 60lbs - 300lbs
Hair color: white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde
Eye color: white, black, red, green, blue, brown, purple, amber
Strength: 1-18
Dexterity: 1-18
Constitution: 1-18
Intelligence: 1-18
Wisdom: 1-18
Charisma: 1-18

#### class Humans:
+2 to any attribute of the user's choice

#### class Elves:
100% Resistance to Sleep (can't be put to sleep)
Gain +2 to their Dexterity and Charisma scores

#### class Dwarves:
20% Reistance to magic
Gain +2 bonus to Strength and Constiution
-2 score to Charisma


1. Create a function called characterCreation(). This function will let the user decide if they wish to be a Human, an Elf, or a Dwarf.  No matter what race the user chooses, all three should ask the user to enter a value for height, weight, hair color, and eye color. 

2. Use the random import to create random values for each attribute.

3. If the user chooses to be a Human, let them add two points to any of their 6 attributes (but only one of those 6 attributes). 

If the user chooses to be an Elf, them they get a 100% Resistance to Sleep and add 2 points to their Dexterity and Charisma scores.

If the user chooses to be a Dwarf, tell them they get 20% resistance to magic bonus, add 2 points to their Strength and Constitution scores, and subtract 2 points from their Charisma score.

4. Print these items to the screen once they have finished making their character.