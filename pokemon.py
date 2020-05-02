# Become a Pokemon Master! Participate in Pokemon battles.
import random
import time

types = {
    'Normal': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': 1,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': .5,'Ghost': 0,'Dragon': 1,'Dark': 1,'Steel': .5,'Fairy': 1
    },

    'Fire': {
        'Normal': 1,'Fire': .5,'Water': .5,'Electric': 1,'Grass': 2,'Ice': 2, 'Fighting': 1,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 2,'Rock': .5,'Ghost': 1,'Dragon': .5,'Dark': 1,'Steel': 2,'Fairy': 1
    },

    'Water': {
        'Normal': 1,'Fire': 2,'Water': .5,'Electric': 1,'Grass': .5,'Ice': 1, 'Fighting': 1,'Poison': 1,'Ground': 2,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': 2,'Ghost': 1,'Dragon': .5,'Dark': 1,'Steel': 1,'Fairy': 1
    },

    'Electric': {
        'Normal': 1,'Fire': 1,'Water': 2,'Electric': .5,'Grass': .5,'Ice': 1, 'Fighting': 1,'Poison': 1,'Ground': 0,'Flying': 2,'Psychic': 1,'Bug': 1,'Rock': 1,'Ghost': 1,'Dragon': .5,'Dark': 1,'Steel': 1,'Fairy': 1
    },

    'Grass': {
        'Normal': 1,'Fire': .5,'Water': 2,'Electric': 1,'Grass': .5,'Ice': 1, 'Fighting': 1,'Poison': .5,'Ground': 2,'Flying': .5,'Psychic': 1,'Bug': .5,'Rock': 2,'Ghost': 1,'Dragon': .5,'Dark': 1,'Steel': .5,'Fairy': 1
    },

    'Ice': {
        'Normal': 1,'Fire': .5,'Water': .5,'Electric': 1,'Grass': 2,'Ice': .5, 'Fighting': 1,'Poison': 1,'Ground': 2,'Flying': 2,'Psychic': 1,'Bug': 1,'Rock': 1,'Ghost': 1,'Dragon': 2,'Dark': 1,'Steel': .5,'Fairy': 1
    },

    'Fighting': {
        'Normal': 2,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 2, 'Fighting': 1,'Poison': .5,'Ground': 1,'Flying': .5,'Psychic': .5,'Bug': .5,'Rock': 2,'Ghost': 0,'Dragon': 1,'Dark': 2,'Steel': 2,'Fairy': .5
    },

    'Poison': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 2,'Ice': 1, 'Fighting': 1,'Poison': .5,'Ground': .5,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': .5,'Ghost': .5,'Dragon': 1,'Dark': 1,'Steel': 0,'Fairy': 2
    },

    'Ground': {
        'Normal': 1,'Fire': 2,'Water': 1,'Electric': 2,'Grass': .5,'Ice': 1, 'Fighting': 1,'Poison': 2,'Ground': 1,'Flying': 0,'Psychic': 1,'Bug': .5,'Rock': 2,'Ghost': 1,'Dragon': 1,'Dark': 1,'Steel': 2,'Fairy': 1
    },

    'Flying': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': .5,'Grass': 2,'Ice': 1, 'Fighting': 2,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 2,'Rock': .5,'Ghost': 1,'Dragon': 1,'Dark': 1,'Steel': .5,'Fairy': 1
    },

    'Psychic': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': 2,'Poison': 2,'Ground': 1,'Flying': 1,'Psychic': .5,'Bug': 1,'Rock': 1,'Ghost': 1,'Dragon': 1,'Dark': 0,'Steel': .5,'Fairy': 1
    },

    'Bug': {
        'Normal': 1,'Fire': .5,'Water': 1,'Electric': 1,'Grass': 2,'Ice': 1, 'Fighting': .5,'Poison': .5,'Ground': 1,'Flying': .5,'Psychic': 2,'Bug': 1,'Rock': 1,'Ghost': .5,'Dragon': 1,'Dark': 2,'Steel': .5,'Fairy': .5
    },

    'Rock': {
        'Normal': 0,'Fire': 2,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 2, 'Fighting': .5,'Poison': 1,'Ground': .5,'Flying': 2,'Psychic': 1,'Bug': 2,'Rock': 1,'Ghost': 1,'Dragon': 1,'Dark': 1,'Steel': .5,'Fairy': 1
    },

    'Ghost': {
        'Normal': 0,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': 1,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 2,'Bug': 1,'Rock': 1,'Ghost': 2,'Dragon': 1,'Dark': .5,'Steel': 1,'Fairy': 1
    },

    'Dragon': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': 1,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': 1,'Ghost': 1,'Dragon': 2,'Dark': 1,'Steel': .5,'Fairy': 0
    },

    'Dark': {
        'Normal': 1,'Fire': 1,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': .5,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 2,'Bug': 1,'Rock': 1,'Ghost': 2,'Dragon': 1,'Dark': .5,'Steel': 1,'Fairy': .5
    },

    'Steel': {
        'Normal': 1,'Fire': .5,'Water': .5,'Electric': .5,'Grass': 1,'Ice': 2, 'Fighting': 1,'Poison': 1,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': 2,'Ghost': 1,'Dragon': 1,'Dark': 1,'Steel': .5,'Fairy': 2
    },

    'Fairy': {
        'Normal': 1,'Fire': .5,'Water': 1,'Electric': 1,'Grass': 1,'Ice': 1, 'Fighting': 2,'Poison': .5,'Ground': 1,'Flying': 1,'Psychic': 1,'Bug': 1,'Rock': 1,'Ghost': 1,'Dragon': 2,'Dark': 2,'Steel': .5,'Fairy': 1
    }    
}

class Moves:
    def __init__(self, name, type_, category, power, accuracy, pp, effect=None, status_effect=None):
        self.name = name
        self.type = type_
        # 'physical' or 'special' or 'status'
        self.category = category
        # Integer value
        self.power = power
        # 0 to 100
        self.accuracy = accuracy
        # Amount of power points left until move can't be used
        self.pp = pp

        # Whats printed to the user when selecting moves
        self.effect = effect
        # [effect, turns, chance]
        # Default to None
        # Requires effect to be passed with status_effect
        self.status_effect = status_effect

tackle = Moves('Tackle', 'normal', 'physical', 40, 100, 35)
leer = Moves('Leer', 'normal', 'status', 0, 100, 30, 'Lowers opponent\'s Defense.') # Add lower defence effect
cut = Moves('Cut', 'normal', 'physical', 50, 95, 30)
ember = Moves('Ember', 'fire', 'special', 40, 100, 25, 'May burn opponent.') # Add chance to burn [effect, turns, chance]
hydro_pump = Moves('Hydro Pump', 'water', 'special', 110, 80, 5)
thunderbolt = Moves('Thunderbolt', 'electric', 'special', 90, 100, 15, 'May paralyze opponent.')
swift = Moves('Swift', 'normal', 'special', 60, 100, 20)
vinewhip = Moves('Vinewhip', 'grass', 'physical', 45, 100, 25)
razor_leaf = Moves('Razor Leaf', 'grass', 'physical', 55, 95, 25)
water_gun = Moves('Water Gun', 'Water', 'special', 40, 100, 25)
rapid_spin = Moves('Rapid Spin', 'Normal', 'physical', 50, 100, 40)

class Pokemon:
    def __init__(self, name, type_, level, given_moveset, 
    max_health, attack_stat, defence_stat, special_attack_stat, special_defence_stat, speed):
        self.name = name
        self.type = type_
        self.level = level
        # a list is passed
        # Ex: given_moveset = [tackle, leer, cut, ember]
        self.moveset = {}
        i = 1
        for move in given_moveset:
            self.moveset.update({
                i: [move, move.pp]
            })
            i += 1
        # Ex: self.moveset = {1: [tackle, 25], 2: [leer, 40], ...}
        # self.moveset[1[0]].power ........

        self.max_health = max_health
        self.current_health = max_health
        self.attack_stat = attack_stat
        self.defence_stat = defence_stat
        self.special_attack_stat = special_attack_stat
        self.special_defence_stat = special_defence_stat
        self.speed = speed
        
        # Add to this list: {effect: numofturns}
        self.status_effects = {}
        self.knocked_out = False

    def health(self):
        # Print current_health
        print(f'{self.name} now has {self.current_health}/{self.max_health} health.')

    def lose_health(self, damage):
        self.current_health -= damage

        # Knock out if health <= 0
        # Else, print current_health
        if self.current_health <= 0:
            self.knock_out()
        else:
            self.health()

    def gain_health(self, health):
        self.current_health += health
        # Ensure current_health doesn't exceed max_health
        if self.current_health > self.max_health:
            self.current_health = self.max_health

        self.health()

    def knock_out(self):
        self.current_health = 0
        self.knocked_out = True

        print(f'{self.name} was knocked out!')

    def revive(self):
        # Revive to half max_health
        self.current_health = (self.max_health / 2)
        self.knocked_out = False

        print(f'{self.name} has been revived and now has {self.current_health}/{self.max_health} health.')

    def max_revive(self):
        # Revive to max_health
        self.current_health = self.max_health
        self.knocked_out = False

        print(f'{self.name} has been max revived and now has {self.current_health}/{self.max_health} health.')

    def attack(self, other_pokemon):
        print(f'\n{other_pokemon.name} has been targeted by {self.name}.\n')
        # Let user pick a move
        while True:
            print('Pick a move: \n')
            # moveset = {i: [move, move.pp], ...}
            for move in range(1, 5):
                # Add power and accuracy to options
                print(f'[{move}] {self.moveset[move][0].name}: {self.moveset[move][1]} PP', f': {self.moveset[move][0].effect}')

            try:
                # move is an instance of Moves class
                # Ensure user's choice is in the moveset
                while True:
                    choice = int(input())
                    if choice not in self.moveset:
                        print('Please pick a valid move: \n')
                        for move in range(1,5):
                            print(f'[{move}] {self.moveset[move][0].name}: {self.moveset[move][1]} PP', f': {self.moveset[move][0].effect}')
                        continue
                    move = self.moveset[choice][0]
                    break
            except ValueError:
                print('Please pick a valid move: \n')
                continue
            break

        print(f'{self.name} has attacked {other_pokemon.name} using {move.name}!')

        # Whether or not the move hits based on accuracy
        if random.randrange(100) > move.accuracy:
            time.sleep(1)
            print(f'{self.name} missed!')
            return

        # Calculate modifiers:
        effectiveness = types[move.type.title()][other_pokemon.type.title()]
        random_factor = random.randint(85, 100) * .01
        if random.randrange(10000) < 625:
            crit = 2
            time.sleep(1)
            print('It was a critical hit!')
        else:
            crit = 1
        modifier = effectiveness * crit * random_factor

        # Calculate base damage from levels, move power, attack stats and defence stats:
        level_calc = self.level * 2/5 + 2

        # Physical, special, or status depends of move
        # Consider status category when it is implemented
        if move.category == 'physical':
            a_d = self.attack_stat / other_pokemon.defence_stat
        elif move.category == 'special':
            a_d = self.special_attack_stat / other_pokemon.special_defence_stat
        elif move.category == 'status':
            pass

        # Power changes depending on move
        power = move.power

        # Bring base damage and modifiers together with this formula (round to whole number):
        damage = round((level_calc * power * a_d / 50 + 2) * modifier)

        # Time for attack to take place
        if effectiveness == 2:
            time.sleep(1)
            print('It was super effective!')
        elif effectiveness == .5:
            time.sleep(1)
            print('It was not very effective.')
        elif effectiveness == 0:
            time.sleep(1)
            print('It was not effective...')

        time.sleep(1)
        other_pokemon.lose_health(damage)
        time.sleep(1)

pikachu = Pokemon('Pikachu', 'electric', 1, [tackle, cut, thunderbolt, swift], 35, 55, 30, 50, 40, 90)

charmander = Pokemon('Charmander', 'fire', 1, [tackle, cut, ember, swift], 39, 52, 43, 60, 50, 65)

bulbasaur = Pokemon('Bulbasaur', 'grass', 1, [tackle, cut, vinewhip, razor_leaf], 45, 49, 59, 65, 65, 45)

squirtle = Pokemon('Squirtle', 'water', 1, [tackle, water_gun, rapid_spin, hydro_pump], 44, 48, 65, 50, 74, 43)

while True:
    pikachu.attack(squirtle)
    squirtle.attack(pikachu)