import random
import pokedex

class Pokemon:
    def __init__(self, name, species, type, level, hp, moves):
        self.name = name
        self.species = species
        self.type = type
        self.level = level
        self.hp = hp
        self.moves = moves

    def choose_move(self):
        print(f"Choose a move for {self.name}:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move}")
        choice = int(input("Enter the number of your choice: ")) - 1
        return self.moves[choice]

def introduction():
    print("Welcome to the world of Pokémon!")
    print("In this journey, you'll embark on an adventure as a Pokémon Trainer.")
    print("Your mission is to become a Pokémon Champion by capturing and training powerful Pokémon.")
    print("But first, you must choose your starter Pokémon.")

def choose_starter_pokemon():
    starters = [Pokemon("Bulbasaur", "Bulbasaur", "Grass", 5, 20, ["Tackle", "Vine Whip"]),
                Pokemon("Charmander", "Charmander", "Fire", 5, 20, ["Scratch", "Ember"]),
                Pokemon("Squirtle", "Squirtle", "Water", 5, 20, ["Tackle", "Water Gun"])]

    introduction()  # Display the game introduction

    print("Choose your starter Pokémon:")
    for i, pokemon in enumerate(starters):
        print(f"{i + 1}. {pokemon.name}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return starters[choice]

def choose_wild_pokemon():
    wild_pokemon_list = [
        Pokemon("Pidgey", "Pidgey", "Flying", 3, 15, ["Tackle", "Gust"]),
        Pokemon("Rattata", "Rattata", "Normal", 4, 18, ["Tackle", "Quick Attack"]),
        Pokemon("Caterpie", "Caterpie", "Bug", 2, 10, ["Tackle", "String Shot"]),
        # Add more wild Pokémon to the list here
    ]
    return random.choice(wild_pokemon_list)

# Type chart for type advantages and disadvantages
type_chart = {
    "Grass": {"Water": 2.0, "Fire": 0.5, "Grass": 0.5, "Electric": 0.5},
    "Water": {"Fire": 2.0, "Grass": 0.5, "Electric": 0.5},
    "Fire": {"Water": 0.5, "Grass": 2.0, "Electric": 0.5},
    "Electric": {"Water": 2.0, "Grass": 2.0, "Fire": 2.0},
}

# Evolution data
evolution_data = {
    "Bulbasaur": ("Ivysaur", 16),  # Bulbasaur evolves into Ivysaur at level 16
    "Charmander": ("Charmeleon", 16),  # Charmander evolves into Charmeleon at level 16
    "Squirtle": ("Wartortle", 16)  # Squirtle evolves into Wartortle at level 16
}

# Simple Pokédex data structure
pokedex = {}

def add_to_pokedex(pokemon):
    if pokemon.species not in pokedex:
        pokedex[pokemon.species] = {
            "Type": pokemon.type,
            "Level": pokemon.level,
            "Moves": pokemon.moves
        }

def view_pokedex():
    print("Pokédex:")
    for species, info in pokedex.items():
        print(f"{species} - Type: {info['Type']}, Level: {info['Level']}, Moves: {', '.join(info['Moves'])}")

def calculate_type_effectiveness(move_type, target_type):
    if move_type in type_chart and target_type in type_chart[move_type]:
        return type_chart[move_type][target_type]
    return 1.0  # Default: No advantage or disadvantage

def level_up_pokemon(pokemon):
    print(f"Congratulations! {pokemon.name} leveled up!")
    pokemon.level += 1
    # You can add logic to update moves or stats as Pokémon level up.

def evolve_pokemon(pokemon):
    if pokemon.species in evolution_data and pokemon.level >= evolution_data[pokemon.species][1]:
        new_species, _ = evolution_data[pokemon.species]
        print(f"Congratulations! Your {pokemon.name} evolved into {new_species}!")
        return Pokemon(new_species, new_species, pokemon.type, 1, 20, ["Tackle", "New Move"])  # Modify evolution stats and moves
    return pokemon

def battle(player_pokemon, wild_pokemon):
    print(f"A wild {wild_pokemon.name} appeared!\n")

    while player_pokemon.hp > 0 and wild_pokemon.hp > 0:
        print(f"{player_pokemon.name} (Level {player_pokemon.level}) - HP: {player_pokemon.hp}")
        print(f"{wild_pokemon.name} (Level {wild_pokemon.level}) - HP: {wild_pokemon.hp}\n")

        # Player's turn
        player_move = player_pokemon.choose_move()
        wild_type = wild_pokemon.type

        # Calculate type effectiveness for player's move
        type_multiplier = calculate_type_effectiveness(player_move, wild_type)

        # Implement damage calculation based on type effectiveness
        player_damage = random.randint(5, 15) * type_multiplier
        wild_pokemon.hp -= player_damage

        print(f"{player_pokemon.name} used {player_move}!")

        if wild_pokemon.hp <= 0:
            print(f"{wild_pokemon.name} fainted. You won the battle!")
            add_to_pokedex(wild_pokemon)  # Add wild Pokémon to the Pokédex
            level_up_pokemon(player_pokemon)  # Level up the player's Pokémon
            player_pokemon = evolve_pokemon(player_pokemon)  # Check for evolution
            capture_choice = input("Do you want to try to catch the wild Pokémon? (Yes/No): ").strip().lower()
            if capture_choice == "yes":
                if random.random() < 0.5:  # You can adjust the catch rate (0.5 is just an example).
                    print(f"Congratulations! You caught the wild {wild_pokemon.name}!")
                    # Add the captured Pokémon to the player's collection.
                else:
                    print(f"{wild_pokemon.name} broke free and fled.")
            break  # Exit the battle loop

        print(f"{wild_pokemon.name} - HP: {wild_pokemon.hp}\n")

        # Wild Pokémon's turn
        wild_move = random.choice(wild_pokemon.moves)
        player_type = player_pokemon.type

