from flask import Flask, render_template
import pandas as pd 
import requests

s08 = pd.read_csv('NFL_2008_Schedule.csv')

app = Flask(__name__)
s = s08.shape
print(s)
@app.route('/')
def hello():
    return render_template('home.html', s=s)
color = 'red'
URL = f'https://pokeapi.co/api/v2/pokemon-color/{color}'
response = requests.get(URL)
#print(response.text)
pokeList = []
for i in response.json()['pokemon_species']:
    pokeList.append(i['name'])

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html', response=pokeList,count=len(pokeList))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

