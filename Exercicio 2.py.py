def velocidade_caminhao(gotejamento, distancia_entre_gotas):
    velocidade_caminhao = gotejamento * distancia_entre_gotas
    return velocidade_caminhao

gotejamento = 2
distancia_entre_gotas = 2.5
velocidade_caminhao = velocidade_caminhao(gotejamento, distancia_entre_gotas)

print("A velocidade do caminhão é", velocidade_caminhao, "metros por segundo.")