from trainer import Trainer


class Pokemon:
    def __init__(self, name, level, lifePoints):
        self.name = name
        self.__level = level
        self.__lifePoints = lifePoints

    def __str__(self):
        return f"Pokemon({self.name}, Level: {self.__level}, HP: {self.__lifePoints})"

    def get_level(self):
        return self.__level
    
    def set_level(self, level):
        self.__level = level
        self.update_pokemon()

    def get_lifePoints(self):
        return self.__lifePoints
    
    def set_lifePoints(self, lifePoints):
        self.__lifePoints = lifePoints
        self.update_pokemon()

    def update_pokemon(self):
        self.__lifePoints = self.__level * 10

    def attack(self, other_pokemon):
        damage = self.__level * 5
        other_pokemon.set_lifePoints(other_pokemon.get_lifePoints() - damage)
        print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")


if __name__ == "__main__":
    trainer_eins = Trainer('Ash Ketchup')
    trainer_zwei = Trainer('Misty')
    pikachu = Pokemon('Pikachu', 5, 120)
    evoli = Pokemon('Evoli', 3, 80)
    trainer_eins.add_pokemon(pikachu)
    trainer_zwei.add_pokemon(evoli)

    for pokemon in trainer_eins.get_pokemonsOwner():
        print(pokemon)

    for pokemon in trainer_zwei.get_pokemonsOwner():
        print(pokemon)

    print(pikachu.attack(evoli))

    print(f"{evoli.name} has {evoli.get_lifePoints()} HP left.")