import json 
import requests
from googletrans import Translator




def personagens():

    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    personagem = (requests.get(api_url)).json()

    

    translator = Translator()

    for p in personagem:
        afiliacao = p.get('affiliation', '')
        p['afiliacao_traduzida'] = translator.translate(afiliacao, dest='pt').text
        nome = p.get('name','')
        p['nome_traduzida'] = translator.translate(nome, dest='pt').text

        print(personagem)










personagens()   






