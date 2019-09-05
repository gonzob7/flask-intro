from random import choice, sample
from flask import Flask, request, render_template


app = Flask(__name__)

compliments = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']

@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, 3)

    return render_template(
        'compliments.html',
        name=name,
        show_compliments=show_compliments,
        compliments=compliments_to_show)


def get_horoscope():
    day = choice(days)
    return(f'Your day will go {day}!')

@app.route('/')
def index():
    return render_template('index.html')


#-------------------------#
if __name__ == "__main__":
    app.run(debug=True)
#-------------------------#
