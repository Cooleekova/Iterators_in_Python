from Wiki import Wiki
from generator import hashlines

countries = Wiki('countries.json')
countries.func('wikipedia.json')

hashlines('wikipedia.json')


