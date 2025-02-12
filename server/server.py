from flask import Flask, request, send_file
import time ,os, json, requests, atexit, shutil, random

def purge_shitty_images():
    shutil.rmtree('img/')

if not os.path.exists('img/'):
    os.makedirs('img/')

app = Flask(__name__)

def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

@app.route('/fatorial')
def calcula_fatorial():
    n = request.args.get('n', default=0, type=int)
    if n < 0:
        return 'N deve ser maior ou igual a zero.'
    return f'Fatorial de {n} = {fatorial(n)}'

@app.route('/anime')
def anime():
    tags = ['cringe', 'dance', 'happy', 'kill', 'slap', 'glomp', 'yeet', 'bonk', 'smug']
    response = requests.get('https://api.waifu.pics/sfw/' + random.choice(tags))
    json_data = json.loads(response.text)
    image_url = json_data['url']
    image_name = image_url.split('/')[-1]

    image_data = requests.get(image_url).content

    with open('img/' + image_name, 'wb') as handler:
        handler.write(image_data)
    
    return send_file('../img/' + image_name)

atexit.register(purge_shitty_images)

app.run(host='localhost', port=3001)