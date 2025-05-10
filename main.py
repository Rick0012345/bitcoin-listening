from get_price import obter_preco_bitcoin, enviar_mensagem_whatsapp
import time

while True:
    preco = obter_preco_bitcoin()
    if preco > 50000:
        mensagem = f"Preço atual do Bitcoin: nada a fazer R$ {preco:,.2f}"
        enviar_mensagem_whatsapp(mensagem)
    else:
        mensagem = f"Preço atual do Bitcoin: VENDER R$ {preco:,.2f}"
        enviar_mensagem_whatsapp(mensagem)
    time.sleep(10)