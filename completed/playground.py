import requests, json

base_url = 'https://swapi.dev/api/'

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
    "films": "http://swapi.dev/api/films/",
    "people": "http://swapi.dev/api/people/",
    "planets": "http://swapi.dev/api/planets/",
    "species": "http://swapi.dev/api/species/",
    "starships": "http://swapi.dev/api/starships/",
    "vehicles": "http://swapi.dev/api/vehicles/"
}
"""

#TODO: 1. Return the title of every film in the API
def every_film():
    all_films = requests.get(base_url + "films").json()
    return ", ".join([film["title"] for film in all_films["results"]])

#TODO: 2. Create a method to allow a user to search a category by field
def search_by_name(category, field):
    return requests.get(base_url + category + "/?search=" + field).json()

#TODO: 3. Given a character's name, return the planet that the character comes from, as well as the titles of the films the character appeared in
def character_and_their_films_paragraph(name):
    character = requests.get(base_url + "people/?search=" + name).json()["results"][0]
    planet = requests.get(character["homeworld"]).json()["name"]
    films = [requests.get(url).json()["title"] for url in character["films"]]
    return(name + " is from " + planet + ". They have appeared in the following films: " + ", ".join(films) + ".")

#TODO: 4. Print json in an organized way
def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

print(every_film())
pretty_print(search_by_name("planets", "Tatooine"))
print(character_and_their_films_paragraph("Luke Skywalker"))