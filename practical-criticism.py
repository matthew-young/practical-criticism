from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

def get_random_poem():
    # Read the CSV file
    df = pd.read_csv('kaggle_poem_dataset.csv')
    # Choose a random poem
    random_poem = df.sample(n=1).iloc[0]
    return {
        'title': random_poem['Title'],
        'author': random_poem['Author'],
        'content':random_poem['Content'].replace('&amp;', '&')
    }

@app.route('/')
def index():
    poem = get_random_poem()
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)