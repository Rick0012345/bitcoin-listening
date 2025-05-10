import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações do Twilio
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE')
SEU_PHONE = os.getenv('SEU_PHONE')

def enviar_mensagem_whatsapp(mensagem):
    try:
        print("Tentando enviar mensagem via WhatsApp...")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            from_=TWILIO_PHONE,
            body=mensagem,
            to=SEU_PHONE
        )
        print(f"Mensagem enviada com sucesso! SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")
        return None

def obter_preco_bitcoin():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    parametros = {
        'ids': 'bitcoin',
        'vs_currencies': 'brl'
    }
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        dados = resposta.json()
        preco_brl = dados['bitcoin']['brl']
        print(f'Preço atual do Bitcoin: R$ {preco_brl:,.2f}')
        return preco_brl  # Retorna o valor numérico
    else:
        mensagem = 'Erro ao obter o preço do Bitcoin.'
        print(mensagem)
        return 0  # Retorna 0 em caso de erro