import requests
import json


def get_insult():
    response  = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    json_data = json.loads(response.text)
    insult = json_data.get('insult')
    return insult    
    

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -irgendein weiser Mensch'
    return quote


def get_compliment():
    response = requests.get('https://complimentr.com/api')
    json_data = json.loads(response.text)
    compliment = json_data.get('compliment')
    return compliment


def get_urban_awnser(input):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    try:
        querystring = {"term": input}
        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "63527eb38dmsh9c4da43b7c36852p19756cjsnb66ab270aa11"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(response.text)
        awnser = json_data.get('list')[0]
        return awnser.get('definition')
    except:
        return 'Keine Antwort gefunden (⌣̩̩́_⌣̩̩̀)'
    
    

