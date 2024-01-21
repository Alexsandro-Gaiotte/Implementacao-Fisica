def calcular_comprimento_do_trem(velocidade_km, comprimento_ponte, tempo_atravessar):
    
    # Converter velocidade para metros por segundo (m/s)
    velocidade = velocidade_km * (1000 / 3600)
    comprimento_trem = velocidade * tempo_atravessar - comprimento_ponte
    return comprimento_trem

velocidade_trem = 144
comprimento_ponte = 90 
tempo_atravessar = 4.5

comprimento_trem = calcular_comprimento_do_trem(velocidade_trem, comprimento_ponte, tempo_atravessar)
print("O comprimento do trem é", round(comprimento_trem, 2), "metros.")
