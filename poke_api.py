import requests

def fetch_pokemon_info(pokemon_name):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Args:
        pokemon_name (str): Name or PokéDex number of the Pokémon.

    Returns:
        dict: Dictionary containing the Pokémon information if retrieved successfully, otherwise None.
    """
    # Convert the parameter to lowercase and remove whitespace
    pokemon_name = pokemon_name.strip().lower()

    # Construct the URL for the PokéAPI request
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # Fetch Pokémon information from the PokéAPI
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        pokemon_info = response.json()
        print(f"Successfully fetched information for {pokemon_name}")
        return pokemon_info
    else:
        print(f"Failed to fetch information for {pokemon_name}")
        return None

# Test the function with a variety of Pokémon names
if __name__ == "__main__":
    pokemon_names = ["pikachu", "bulbasaur", "charizard", "eevee"]

    for name in pokemon_names:
        pokemon_info = fetch_pokemon_info(name)
        if pokemon_info:
            print(pokemon_info)
            print()  # Add a blank line between each Pokémon information
