from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

def get_random_poem():
    # Read the CSV file
    df = pd.read_csv('PoetryFoundationData.csv')
    # Choose a random poem
    random_poem = df.sample(n=1).iloc[0]
    return {
        'title': random_poem['Title'],
        'author': random_poem['Poet'],
        'content': random_poem['Poem']
    }

@app.route('/')
def index():
    poem = get_random_poem()
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)