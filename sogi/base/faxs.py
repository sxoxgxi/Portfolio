import requests


def get_quote() -> tuple:
    response = requests.get('https://zenquotes.io/api/quotes')
    data = response.json()[0]
    quote = data['q']
    author = data['a']
    return quote, author
