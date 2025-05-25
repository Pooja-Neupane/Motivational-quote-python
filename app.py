from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Success doesn't come from what you do occasionally, it comes from what you do consistently.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream big. Start small. Act now.",
    "Discipline is the bridge between goals and accomplishment.",
    "Every day is a new opportunity to grow and get better.",
    "Be brave enough to be bad at something new.",
    "Stay patient and trust your journey."
]

@app.route('/')
def index():
    return render_template('index.html', quote=random.choice(quotes))

@app.route('/quote')
def quote():
    return jsonify(quote=random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
