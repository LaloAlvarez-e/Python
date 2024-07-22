#!E:\GIT\Python\100_Days_of_Code\Day16/venv/Scripts/python.exe
from prettytable import PrettyTable

def main():
    # Create an example table
    table = PrettyTable()
    table.field_names = ["Pokemon Name", "Type"]
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Charmander", "Fire"])
    table.add_row(["Squirtle", "Water"])
    table.add_row(["Bulbasaur", "Grass"])
    table.add_row(["Jigglypuff", "Fairy"])
    table.add_row(["Meowth", "Normal"])
    table.add_row(["Psyduck", "Water"])
    table.add_row(["Snorlax", "Normal"])
    table.add_row(["Magikarp", "Water"])
    table.add_row(["Eevee", "Normal"])
    table.add_row(["Mewtwo", "Psychic"])
    table.add_row(["Dragonite", "Dragon"])
    table.add_row(["Mew", "Psychic"])
    table.add_row(["Moltres", "Fire"])
    table.add_row(["Zapdos", "Electric"])
    table.add_row(["Articuno", "Ice"])
    table.add_row(["Ditto", "Normal"])
    table.align = "l"
    
    print(table)

if __name__ == "__main__":
    main()