from Wiki import Wiki
from generator import hashlines

countries = Wiki('countries.json', 'wikipedia.json')
for item in countries:
    print(item)


for item in hashlines('wikipedia.json'):
    print(item)


