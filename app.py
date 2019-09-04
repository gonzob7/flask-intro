from random import choice
from flask import Flask

app = Flask(__name__)

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']
days = ['amazing','great','fast','awesome']

@app.route('/compliment')
def get_compliment():
    compliment = choice(compliments)
    return(f'Hello there, user! You are so {compliment}!')

def get_horoscope():
    day = choice(days)
    return(f'Your day will go {day}!')


#-------------------------#
if __name__ == "__main__":
    app.run(debug=True)
#-------------------------#
