from random import choice, sample
from flask import Flask, request

app = Flask(__name__)

compliments = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']

@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    compliment = choice(compliments)
    return(f'Hello there, {name}! You are so {compliment}!')

def get_horoscope():
    day = choice(days)
    return(f'Your day will go {day}!')

@app.route('/')
def index():
    return  """
    <form action = '/compliment'>
        What is your name??
        <input type = "text" name = "name"></input>
        <button type = "submit">Submit!</button>
        <input type="checkbox" name="show_compliments"/>
        <select name="num_compliments">
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
        </select>
    </form>
    """

#-------------------------#
if __name__ == "__main__":
    app.run(debug=True)
#-------------------------#
