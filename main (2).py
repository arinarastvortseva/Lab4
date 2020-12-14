class Pokemon:

    def __init__(self, name, hp, EVs, speed):
        # сохраняем переменные в качесве атрибутов
        self.name = name
        self.hp = hp
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.speed = speed
        self.level = 1

    def move(self):
        # Покемон начинает движение
        print('Pokemon ' + self.name + ' GO ')

    def fight(self, Pokemon2):
        # Даём возможность для сражения двум покемонам

        # Печатается информация о бое
        print("---------POKEMON BATTLE--------")
        print(self.name)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("SPEED/", self.speed)
        print("\nVs")
        print("\n",Pokemon2.name)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("SPEED/", Pokemon2.speed)


class Water(Pokemon):
    # Создали класс водных покемонов

    def __init__(self, name, hp, EVs, speed, w_skills):
        super().__init__(name, hp, EVs, speed)
        self.w_skills = w_skills
        self.w_skills = 100

    def damage(self):
        self.w_skills -= 5
        print (self.w_skills)

class Fire(Pokemon):
    # Создали класс огненных покемонов

    def __init__(self, name, hp, EVs, speed, f_skills):
        super().__init__(name, hp, EVs, speed)
        self.f_skills = f_skills
        self.f_skills = 85

    def assault(self):
        if self.attack > 4:
            print (self.name +' ATTACK')

    def damage(self):
        f_skills += 2
        print(self.f_skills)

class Grass(Pokemon):
    # Создали класс травянных покемонов

    def __init__(self, name, hp, EVs, speed, grss_skills):
        super().__init__(name, hp, EVs, speed)
        self.grss_skills = grss_skills
        self.grss_skills = 76

    def protection(self):
        if self.defense < 4:
            self.grss_skills += 9
        print(self.grss_skills)

    def damage(self):
        self.grss_skills -= 14
        print (self.grss_skills)

class Human:

    def __init__(self, name, gender, age, occupation):
        # cохраняем переменные в качестве атрибутов
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return '{} {}'.format(self.name, self.age)

    def move(self):
        print(self.name + ' Run')

class Evil(Human):

    def __init__(self, name, gender, age, occupation, team):
        super().__init__(name, gender, age, occupation)
        self.team = team

    def  __str__(self):
        return '{} {}'.format(self.name, self.team)



# Создаём покемонов

pok_1 = Fire ('Charizard', 5, {'ATTACK': 5, 'DEFENSE': 5}, 6, 100)
pok_2 = Water ('Blastoise', 5, {'ATTACK': 5, 'DEFENSE': 6}, 5, 60)
pok_3 = Grass('Venusaur', 5, {'ATTACK': 5, 'DEFENSE': 5}, 5, 54)

pok_4 = Fire ('Charmander', 3, {'ATTACK': 4, 'DEFENSE': 3}, 4, 98)
pok_5 = Water ('Squirtle', 3, {'ATTACK': 3, 'DEFENSE': 4}, 3, 77)
pok_6 = Grass ('Bulbasaur', 3, {'ATTACK': 3, 'DEFENSE': 3}, 3, 69)

pok_7 = Fire ('Charmeleon', 4, {'ATTACK': 4, 'DEFENSE': 4}, 5, 67)
pok_8 = Water ('Wartortle', 4,{'ATTACK': 4, 'DEFENSE': 5}, 4, 56)
pok_9 = Grass ('Ivysaur', 4,{'ATTACK': 4, 'DEFENSE': 4}, 4, 76)


# Создаём людей

hum_1 = Human ('Ash Ketchum', 'male', 10, 'pokemon trainer')
hum_2 = Human ('Misty Williams', 'female', 12, 'pokemon trainer')
Brock = Human ('Brock Harrison', 'male', 17, 'pokemon trainer')

# Создаём злодеев

ev_1 = Evil('Giavanni', 'male', None, 'crime lord', 'Team Rocket')
ev_2 = Evil('Jessie', 'female', None, 'member of Team Rocket', 'Team Rocket')
ev_3 = Evil('James', 'male', None, 'member of Team Rocket', 'Team Rocket')
ev_4 = Evil('Meowth', 'male', None, 'member of Team Rocket', 'Team Rocket')

# Полиморфизм

action = [pok_1,pok_2,pok_3,hum_1,hum_2]
for p in action:
    p.move()

pok_1.fight(pok_2)  # Информация о бое между двумя покемонами
pok_3.protection()


print(ev_1)
#print(hum_2)
#print(hum_3)