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
Documentation here: https://docs.python.org/3/library/json.html 

A Python dictionary is a data structure, or a way of storing data, that is similar to a JSON
It is an unordered collection used to store data in key:value pairs
Documentation here: https://www.w3schools.com/python/python_dictionaries.asp
"""
import requests, json

base_url = "" # Look for the base url in http://swapi.py4e.com/documentation 
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

#TODO: 1. Return the title of every film in the API as a string or a list
def every_film():
    pass

#TODO: 2. Create a method to allow a user to search a category by field, and return the json response of the search
def search_by_category(category: str, field: str):
    pass

#TODO: 3. Given a character's name, return the planet that the character comes from, as well as the titles of the films the character appeared in
def character_and_their_films_paragraph(name: str):
    pass

def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

# print(every_film())
# pretty_print(search_by_category("planets", "Tatooine"))
# print(character_and_their_films_paragraph("Luke Skywalker"))