"""
API Request using Python

requests is used to send HTTP requests to an API.

In this example, we use the PokeAPI to get information
about a Pokemon.
"""


import requests


# Base URL of the PokeAPI.
base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):

    # Create the complete URL using the Pokemon name.
    url = f"{base_url}pokemon/{name}"

    # Send a GET request to the API.
    response = requests.get(url)

    # Status code 200 means the request was successful.
    if response.status_code == 200:

        # Convert the JSON response into a Python dictionary.
        pokemon_data = response.json()

        # print(pokemon_data)  # Uncomment to see all the data.

        return pokemon_data

    else:
        print("Failed to retrieve data!")


pokemon_name = "pikachu"

pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:

    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")


"""
HOW IT WORKS
------------

1. We create the API URL:

    https://pokeapi.co/api/v2/pokemon/pikachu


2. requests.get() sends a GET request to the API:

    response = requests.get(url)


3. We check the status code:

    response.status_code == 200

    200 → Request was successful
    Other → Something went wrong


4. response.json() converts the JSON response
   into a Python dictionary:

    pokemon_data = response.json()


5. We can then access the data using dictionary keys:

    pokemon_info["name"]
    pokemon_info["id"]
    pokemon_info["height"]
    pokemon_info["weight"]


Simple flow:

    Python
       ↓
    requests.get()
       ↓
    API
       ↓
    JSON response
       ↓
    response.json()
       ↓
    Python dictionary
       ↓
    Access the required data
"""