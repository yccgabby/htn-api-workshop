"""
Flask is a backend web app framework that can serve as an API through using routes.
Documentation here: https://flask.palletsprojects.com/en/1.1.x/ 
Documentation for render_template to display html files in routes: https://riptutorial.com/flask/example/5303/render-template-usage 
Documentation for routes to map URLs to specific functions in the API: https://www.javatpoint.com/flask-app-routing#:~:text=App%20routing%20is%20used%20to,Tutorial%20in%20the%20web%20application 
"""
from flask import Flask, render_template
import requests, json
app = Flask(__name__)

"""
This is the initial landing page. We will want to display landing.html. 
"""
@app.route("/")
def landing_page():
    return render_template('landing.html')

"""
This is a route to show a page with all the films in the Star Wars universe.
Use what you have written for #1 in playground.py to retrieve the list of films
You will have to create a new html template in the templates folder and send the films to the frontend
"""
@app.route("/all_films")
def all_films():
    pass

"""
Run 'python3 api.py' in the terminal to start the Flask API server
"""
if __name__ == '__main__':
   app.run(debug = True)