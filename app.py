from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# Load greetings
def load_greetings():
    if os.path.exists('greetings.json'):
        with open('greetings.json', 'r') as file:
            return json.load(file)
    return []

# Save greetings
def save_greeting(greetings):
    with open('greetings.json', 'w') as file:
        json.dump(greetings, file)

@app.route('/')
def index():
    greetings = load_greetings()
    return render_template('index.html', greetings=greetings)

@app.route('/submit_greeting', methods=['POST'])
def submit_greeting():
    name = request.form['name']
    message = request.form['message']
    greetings = load_greetings()
    greetings.append({'name': name, 'message': message})
    save_greeting(greetings)
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
