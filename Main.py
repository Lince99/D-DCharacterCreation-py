from classes.character import Character
from classes.Races import Races

def newCharacter():
	races_list = Races()

	name = input("Character's name: ")
	while True:
		race = input("Character's race: ")
		if(races_list.isValid(race) == True):
			break
		print("The race " + race + " is not defined")
	print("The race " + race + " has the following bonuses: ")
	races_list.printBonuses(race)
	races_list.printTraits(race)

	char_class = input("Character's class: ")

	print("Please, apply these 6 numbers to the character's core skills")
	print("16  14  13  12  11  10")
	forza = int(input("Forza: "))
	cos = int(input("Costituzione: "))
	des = int(input("Destrezza: "))
	intel = int(input("Intelligenza: "))
	sag = int(input("Saggezza: "))
	car = int(input("Carisma: "))
	character = Character(forza, cos, des, intel, sag, car, race)

	return character

races = Races()
print(races.getBonuses("dragonide"))
print(races.getTraits("dragonide"))
character = newCharacter()
