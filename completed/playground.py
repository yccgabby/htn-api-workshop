import requests, json

base_url = 'https://swapi.py4e.com/api/'

"""
The response object a client receives after making a HTTP request can be parsed in a number of ways 
- response.text: retrieves the text response
- response.json(): built-in JSON decoder, similar to json.loads
- response.content: retrieves the bytes response  
Documentation here: https://requests.readthedocs.io/en/master/user/quickstart/#response-content 
"""
example_response = requests.get(base_url)
"""
This is the JSON response when you make a GET request to the base_url 
It displays every sub-route to different categories of data in the Star Wars API
{
    "films": "https://swapi.py4e.com/api/films/",
    "people": "https://swapi.py4e.com/api/people/",
    "planets": "https://swapi.py4e.com/api/planets/",
    "species": "https://swapi.py4e.com/api/species/",
    "starships": "https://swapi.py4e.com/api/starships/",
    "vehicles": "https://swapi.py4e.com/api/vehicles/"
}
"""

#TODO: 1. Return the title of every film in the API
def every_film():
    all_films = requests.get(base_url + "films").json()
    return ", ".join([film["title"] for film in all_films["results"]])

#TODO: 2. Create a method to allow a user to search a category by field
def search_by_category(category: str, field: str):
    return requests.get(base_url + category + "/?search=" + field).json()

#TODO: 3. Given a character's name, return the planet that the character comes from, as well as the titles of the films the character appeared in
def character_and_their_films_paragraph(name: str):
    character = requests.get(base_url + "people/?search=" + name).json()["results"][0]
    planet = requests.get(character["homeworld"]).json()["name"]
    films = [requests.get(url).json()["title"] for url in character["films"]]
    return(name + " is from " + planet + ". They have appeared in the following films: " + ", ".join(films) + ".")

def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

print(every_film())
pretty_print(search_by_category("planets", "Tatooine"))
print(character_and_their_films_paragraph("Luke Skywalker"))