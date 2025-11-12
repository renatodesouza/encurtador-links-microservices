from flask import Flask, redirect, abort
import requests
import os


app = Flask(__name__)

# O nome 'servico-links' funciona por causa do Docker Compose
LINKS_API_URL = "http://servico-links:8000/api/internal-lookup/"

@app.route('/<string:short_code>')
def redirect_to_url(short_code):
    try:
        # Pergunta ao Serviço de Links qual e a URL longa
        # Esta é a comunicação microsserviço-para-microsserviço! 
        response = requests.get(f'{LINKS_API_URL}{short_code}')

        if response.status_code == 200:
            data = response.json()
            # Redireciona o usuário
            # (Aqui você redirecionaria o evento de analytics)
            return redirect(data['original_url'], code=302)
        else:
            abort(404)

    except requests.exceptions.ConnectionError:
        # Serviço de links está fora do ar
        abort(503) # Service Unavailable

@app.route('/')
def health_check():
    # Rota raiz (/) apenas para mostrar que o serviço está no ar
    # O Nginx vai capturar isso
    return "Serviço de Redirect está no ar. Use /<codigo> para redirecionar."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        