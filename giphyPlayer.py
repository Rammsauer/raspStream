import webbrowser
import Constants
import requests
import urllib

from PIL import Image
from io import BytesIO


def randomGif():
    url = f'https://api.giphy.com/v1/gifs/random?api_key={Constants.giphyApiKey}'
    response = requests.get(url)
    id = response.json()['data']['id']
    gifUrl = f'https://i.giphy.com/media/{id}/giphy.gif'
    print(gifUrl)
    image = Image.open(BytesIO(urllib.request.urlopen(gifUrl).read()))
    webbrowser.open_new(gifUrl)