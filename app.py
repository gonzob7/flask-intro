import pyaztro
from random import choice, sample
from flask import Flask, request, render_template


app = Flask(__name__)

compliments = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    horoscope_sign = request.args.get('horoscope_type')
    horoscope = pyaztro.Aztro(sign=horoscope_sign)
    horoscope_desc = horoscope.description

    return render_template(
        'compliments.html',
        name=name,
        horoscope_name = horoscope_sign,
        horoscope_desc = horoscope_desc)


def get_horoscope():
    day = choice(days)
    return(f'Your day will go {day}!')



#-------------------------#
if __name__ == "__main__":
    app.run(debug=True)
#-------------------------#
