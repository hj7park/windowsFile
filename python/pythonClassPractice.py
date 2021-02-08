class Pokemon():

    def __init__(self,name,health):
        self.name = name
        self.health = health
        print(self.name + " created!")

    def attack(self,target_pokemon):
        target_pokemon.health -= 10

    def __str__(self):
        return f"{self.name} now has {self.health} health left!"
    





class EvolvedPokemon(Pokemon):
    def __init__(self,name,health):
        Pokemon.__init__(self,name,health)
    def attack(self,target_pokemon):
        target_pokemon.health -= 20





class PokemonBattle():
    def __init__(self, pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
    
    def start(self):
        print("Let's Battle!")
        print(f"Fighter#1 is {self.pokemon1.name}")
        print(f"Fighter#2 is {self.pokemon2.name}")
        turn = 1
        while self.pokemon1.health > 0 and self.pokemon2. health > 0:
            if turn >0 :
                print(f"{self.pokemon1.name} is attacking {self.pokemon2.name}")
                self.pokemon1.attack(self.pokemon2)
                print(self.pokemon2)
            else:
                print(f"{self.pokemon2.name} is attacking {self.pokemon1.name}")
                self.pokemon2.attack(self.pokemon1)
                print(self.pokemon1)
            turn *=-1
        print("Battle over!")
        print(self.pokemon1)
        print(self.pokemon2)


Pikachu = Pokemon("Pikachu",100)
Bulbasaur = Pokemon("Bulbasaur",120)
battle = PokemonBattle(Pikachu,Bulbasaur)
battle.start()


Charmender = Pokemon("Charmender",50)
Raichu = EvolvedPokemon("Raichu",50)
battle = PokemonBattle(Charmender,Raichu)
battle.start()