def velocidade_media_ultimo_trecho(ultimo_trecho, tempo_total):
    velocidade_media_ultimo_trecho = ultimo_trecho/ tempo_total
    return velocidade_media_ultimo_trecho

distancia_primeiros_trechos = 70 
velocidade_primeiro_trecho = 90 
velocidade_segundo_trecho = 80 
distancia_ultimo_trecho = 30  

tempo_primeiro_trecho = 30 / velocidade_primeiro_trecho
tempo_segundo_trecho = 40 / velocidade_segundo_trecho
tempo_total_primeiros_trechos = tempo_primeiro_trecho + tempo_segundo_trecho

tempo_total_viagem = 1.5
velocidade_media_ultimo_trecho = velocidade_media_ultimo_trecho(distancia_ultimo_trecho, tempo_total_viagem)

print("A velocidade média no último trecho da viagem foi de", round(velocidade_media_ultimo_trecho, 2), "km/h.")
