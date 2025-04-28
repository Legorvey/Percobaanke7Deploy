from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

def load_greetings():
    if os.path.exists('greetings.json'):
        with open('greetings.json', 'r') as f:
            return json.load(f)
    return []

def save_greeting(name, message):
    greetings = load_greetings()
    greetings.append({'name': name, 'message': message})
    with open('greetings.json', 'w') as f:
        json.dump(greetings, f, indent=4)

@app.route('/')
def home():
    greetings = load_greetings()
    return render_template('index.html', greetings=greetings)

@app.route('/submit_greeting', methods=['POST'])
def submit_greeting():
    name = request.form['name']
    message = request.form['message']
    save_greeting(name, message)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
