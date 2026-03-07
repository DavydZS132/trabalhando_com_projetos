import random

def jogo(jogo_digitado):
    jogo_on = ['pedra', 'papel', 'tesoura']

    maquina = random.choice(jogo_on)

    if jogo_digitado == maquina:
        return f"Empate! A máquina também escolheu {maquina}"

    elif (jogo_digitado == 'pedra' and maquina == 'tesoura') or \
         (jogo_digitado == 'tesoura' and maquina == 'papel') or \
         (jogo_digitado == 'papel' and maquina == 'pedra'):
        return f"Você ganhou! A máquina escolheu {maquina}"

    else:
        return f"Você perdeu! A máquina escolheu {maquina}"


jogador_digitado = input('Digite Pedra, Papel ou Tesoura: ').lower()

print(jogo(jogador_digitado))