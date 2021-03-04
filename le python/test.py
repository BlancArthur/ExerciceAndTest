# -- coding: utf8 --
import random
import json

# quotes = [
#     "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
#     "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
# ]

# characters = [
#     "alvin et les Chipmunks",
#     "Babar",
#     "betty boop",
#     "calimero",
#     "casper",
#     "le chat potté",
#     "Kirikou"
# ]

def values_json_quotes():
    values_quotes = []
    with open('quotes.json') as g:
        dataa = json.load(g)
        for entry in dataa:
            values_quotes.append(entry['quotes'])
        return values_quotes

def random_quotes():
    all_valuess = values_json_quotes()
    return get_random_item_in(all_valuess)          


def values_json():
    values = []
    with open('character.json') as s:
        data = json.load(s)
        for entry in data:
            values.append(entry['character'])
        return values

def random_character():
    all_values = values_json()
    return get_random_item_in(all_values)

  

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)


def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item

# Programm
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(random_quotes(), random_character()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


 