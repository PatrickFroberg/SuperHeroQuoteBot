import requests
import json

class SuperHeroQuotesService:

    def get_random_quote():
        response = requests.get("https://superhero-quotes.herokuapp.com/random")
        jsonData = json.loads(response.text)
        quote = jsonData['Stuff']['data']['quote'] + " \n -" + jsonData['Stuff']['data']['author']
        return(quote)




