"""
Requests is a simple HTTP library to execute requests such as GET and POST to manipulate data
Documentation here: https://pypi.org/project/requests/ 

JSON is a common data format used to store and transmit data
An example of a json would be: 
{
    "coding languages": {
        "python": "https://www.python.org/",
        "javascript": "https://www.javascript.com/"
    },
    "workshop name": "intro to API"
}
Common commands include:
- json.load or json.loads: (turns either a file or a string of json into a Python dictionary object)
- json.dump or json.dumps: (turns either a file or a Python dictionary to a json)
Documentation here: https://docs.python.org/3/library/json.html 
"""
import requests, json

base_url = "" # Look for the base url in https://swapi.dev/documentation 
example_response = requests.get(base_url).json() # This will execute a GET request and convert the response to json that we can manipulate with

"""
Given a JSON that looks like this: 
example_response = {
    "workshop": "intro to api",
    "languages": ["Python", "JavaScript"],
}
You can use the key to access the value of each piece of data in the JSON. 
For example, example_response["workshop"] will equate to "intro to api"
"""

#TODO: 1. Return the title of every film in the API
def every_film():
    pass

#TODO: 2. Create a method to allow a user to search a category by field
def search_by_name(category, field):
    pass

#TODO: 3. Given a character's name, return the planet that the character comes from, as well as the titles of the films the character appeared in
def character_and_their_films_paragraph(name):
    pass

#TODO(optional to implement): 4. Print json in an organized way
def pretty_print(response_json: json):
    print(response_json)

print_every_film()
pretty_print(search_by_name("planets", "Tatooine"))
print(character_and_their_films_paragraph("Luke Skywalker"))