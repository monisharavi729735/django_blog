import requests

def quote_of_the_day(request):
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return {'quote_of_the_day': f'{data["content"]} — {data["author"]}'}
    return {'quote_of_the_day': 'Quote not available'}