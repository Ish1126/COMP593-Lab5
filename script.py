import sys
import poke_api
import pastebin_api

def get_pokemon_name():
    """
    Gets the Pokémon name from the command line parameters or prompts the user to input it.

    Returns:
        str: Pokémon name.
    """
    if len(sys.argv) < 2:
        return input("Please provide the Pokémon name: ").strip()
    else:
        return sys.argv[1]

def construct_paste_title_and_body(pokemon_info):
    """
    Constructs the title and body text for the new paste.

    Args:
        pokemon_info (dict): Dictionary containing the Pokémon information.

    Returns:
        tuple: Paste title and body text as strings in a tuple.
    """
    title = f"{pokemon_info['name'].capitalize()}'s Abilities"
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    body = '\n'.join(abilities)

    return title, body

def main():
    # Get the Pokémon name
    pokemon_name = get_pokemon_name()

    # Fetch Pokémon information from the PokéAPI
    pokemon_info = poke_api.fetch_pokemon_info(pokemon_name)

    if pokemon_info:
        # Determine the title and body text of the new PasteBin paste
        title, body = construct_paste_title_and_body(pokemon_info)

        # Create the new PasteBin paste
        expire_date = '1M'  # Expires after 1 month
        is_public = False   # Not publicly listed
        paste_url = pastebin_api.create_paste(title, body, expire_date, is_public)

        if paste_url:
            # Print the URL of the new PasteBin paste
            print(f"New PasteBin paste created: {paste_url}")
        else:
            print("Failed to create a new PasteBin paste.")
    else:
        print("Failed to fetch Pokémon information. Exiting...")

if __name__ == "__main__":
    main()
