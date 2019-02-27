from .Races import Races

class Character:
	""" Character class, with abilities, defenses, core skills, Hit points etc etc"""
	races = Races()

	core_skills = {"for": 0, "cos": 0, "des": 0, "int": 0, "sag": 0, "car": 0}
	#TODO For modifiers greater than 6, it's needed a function that will calculate the modifier given the core skill

	life = {"pf": 0, "impulsi": 0, "val_impulsi": 0}

	defenses = {"temp": 0, "rif": 0, "vol": 0, "ca": 0}

	abilities_list = ["acrobazia", "arcano", "atletica", "bassifondi", "diplomazia", "dungeon", "furtivita", "guarire", "intimidire", "intuizione", "manolesta", "natura", "percezione", "raggirare", "religione", "storia", "tenacia"]
	abilities = {"for": {"atletica": 0}, "cos": {"tenacia": 0}, "des": {"acrobazia": 0, "furtivita": 0, "manolesta": 0}, "int": {"arcano": 0, "religione": 0, "storia": 0}, "sag": {"dungeon": 0, "guarire": 0, "intuizione": 0, "natura": 0, "percezione": 0}, "car": {"bassifondi": 0, "diplomazia": 0, "intimidire": 0, "raggirare": 0}}

	others = {"vel": 0, "visione": "none", "linguaggi": []}
	level = 10
	talent_bonuses = {}


#	core_skills_list = ["for", "cos", "des", "int", "sag", "car"]
#	life_list = ["pf", "impulsi", "val_impulsi"]
#	defenses_list = ["temp", "rif", "vol", "ca"]
#	others_list = ["vel", "visione", "linguaggi"]
#^^ Didn't want to delete these lists right now, because they might come in hand later on :p

	def __init__(self, forz, cos, des, intel, sag, car, race="blank", character_class="blank"):
		self.core_skills["for"] = forz
		self.core_skills["cos"] = cos
		self.core_skills["des"] = des
		self.core_skills["int"] = intel
		self.core_skills["sag"] = sag
		self.core_skills["car"] = car

		#This section adds racial bonuses to core skills and abilities + defining speed, vision and known languages
		#Just in case an invalid race has been chosen
		while(self.races.isValid(race) == False):
			race = input("Error: " + race + " is invalid. Please, insert a valid race: ")

		#traverse the races dictionary
		for race_i, item in self.races.races.items():
			#if the chosen race has been found
			if(race_i == race):
				#look into the chosen race dictionary
				for key in item:
					#If key is a core skill
					if(key in self.core_skills):
						self.core_skills[key] += item[key]
					#if key is anything else but an ability
					if(key in self.others):
						self.others[key] = item[key]
				break

		self.updateAbilities(race)

	def calculateModifier(self, skill):
		i = -5
		for val in range(1, int(self.core_skills[skill]/2)+1):
			i = i + 1
#		print("Skill and val: " + skill + " " + str(self.core_skills[skill]) + " --> " + str(i))
		return i

	def updateAbilities(self, race="none"):
		if(race != "none"):
			#Separate for loop to iterate and place the bonuses for the abilities
			for skill, ability in self.abilities.items():
				for key in ability:
					#now find the chosen race dictionary
					for race_i, item in self.races.races.items():
						if(race_i == race):
							#Look for bonuses to give to the abilities
							for x in item:
								if(x in self.abilities_list):
									#if the current key in ability is worthy of a bonus
									if(x == key):
										#then add the bonus from item[key]
										self.abilities[skill][key] += item[x]
				self.abilities[skill][key] = self.abilities[skill][key] + self.calculateModifier(skill) + int(self.level / 2)
		else:
			for skill, ability in self.abilities.items():
				for key in ability:
					self.abilities[skill][key] = self.abilities[skill][key] + self.modifiers[self.core_skills[skill]] + int(self.level / 2)


	#TODO Add a class to handle the game classes


	def printStats(self):
		print("\nPunteggi delle caratteristiche")
		print("-----------------------------------")
		for i in self.core_skills:
			print(i + ": " + str(self.core_skills[i]))
		print("\nDifese")
		print("-----------------------------------")
		for i in self.defenses:
			print(i + ": " + str(self.defenses[i]))

		print("\nPF e Impulsi")
		print("-----------------------------------")
		for i in self.life:
			print(i + ": " + str(self.life[i]))

		print("\nAbilita'")
		print("-----------------------------------")
		for skill, abil  in self.abilities.items():
			for item in abil:
				print(item + ": 	" + str(self.abilities[skill][item]))
