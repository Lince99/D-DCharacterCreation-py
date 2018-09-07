class Races:
	races = {
				"dragonide": {"cos": 2, "car": 2, "intimidire": 2, "storia": 2, "vel": 6, "visione": "normale", "linguaggi": ["comune", "dragonico"]},
				"eladrin": {"des": 2, "int": 2, "arcano": 2, "storia": 2, "vel": 6, "visione": "crepuscolare", "linguaggi": ["comune", "elfico"]},
				"elfo": {"des": 2, "sag": 2, "natura": 2, "percezione": 2, "vel": 7, "visione": "crepuscolare", "linguaggi": ["comune", "elfico"]},
				"halfling": {"des": 2, "car": 2, "acrobazia": 2, "manolesta": 2, "vel": 6, "visione": "normale", "linguaggi": ["comune", "blank"]},
				"mezzelfo": {"cos": 2, "car": 2, "diplomazia": 2, "intuizione": 2, "vel": 6, "visione": "crepuscolare", "linguaggi": ["comune", "elfico", "blank"]},
				"nano": {"cos": 2, "sag": 2, "dungeon": 2, "tenacia": 2, "vel": 5, "visione": "crepuscolare", "linguaggi": ["comune", "nanico"]},
				"tiefling": {"int": 2, "car": 2, "furtivita": 2, "raggirare": 2, "vel": 6, "visione": "crepuscolare", "linguaggi": ["comune", "blank"]},
				"umano": {"blank": 2, "blank": 5, "vel": 6, "visione": "crepuscolare", "linguaggi": ["comune", "blank"]}
			}

	core_skills = ["for", "cos", "des", "int", "sag", "car"]
	others = ["vel", "visione", "linguaggi"]

	def printRaces(self):
		for race, items in self.races.items():
			print("	Razza " + race)
			for item in items:
				print(item + ": " + str(items[item]))
			print("-----------------")

	def isValid(self, race):
		if(race in self.races):
			return True
		return False

	def getTraits(self, race):
		traits = {}
		for race_i, item in self.races.items():
			if(str(race_i) == race.lower()):
				for key in item:
					if(key in self.others):
						traits[key] = item[key]
				break
		return traits

	def getBonuses(self, race):
		bonuses = {}
		for race_i, item in self.races.items():
			if(str(race_i) == race.lower()):
				for key in item:
					if(key not in self.others):
						bonuses[key] = item[key]
				break
		return bonuses

	def printTraits(self, race):
		for race_i, item in self.races.items():
			if(str(race_i) == race.lower()):
				for key in item:
					if(key in self.others):
						print(key + " " + str(item[key]))
				break

	def printBonuses(self, race):
		for race_i, item in self.races.items():
			if(str(race_i) == race.lower()):
				for key in item:
					if(key not in self.others):
						print(" +" + str(item[key]) + " to " + key)
				break

