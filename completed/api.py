from flask import Flask, render_template
import requests, json
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing.html')

@app.route("/all_films")
def all_films():
    all_films = requests.get("https://swapi.dev/api/films").json()
    return render_template('films.html', films = [film["title"] for film in all_films["results"]])

if __name__ == '__main__':
    app.run(debug = True)