class Trainer:
    def __init__(self, owner):
        self.owner = owner
        self.__pokemons = []

    def add_pokemon(self, pokemon):
        self.__pokemons.append(pokemon)

    def remove_pokemon(self, pokemon):
        self.__pokemons.remove(pokemon)

    def get_pokemons(self):
        return self.__pokemons
    
    def get_pokemonsOwner(self):
        return self.__pokemons
    