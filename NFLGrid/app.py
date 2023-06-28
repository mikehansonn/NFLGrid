from flask import Flask, render_template, request
import re

app = Flask(__name__)

def recommend_names(user_input, names_list):
    matches = []
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching
    
    for name in names_list:
        if user_input in name.lower():
            matches.append(name)

    return matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_input = request.form['name']
        with open("players.txt", "r") as file:
            names_list = file.read().splitlines()
        recommendations = recommend_names(user_input, names_list)
        return render_template('index.html', recommendations=recommendations)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
