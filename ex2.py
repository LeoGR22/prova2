import random

dado = [1,2,3,4,5,6]
jogador1 = []
jogador2 = []
opcao = 0
while True:
    opcao = (int(input("digite 1 p jogar e 2 p sair")))
    if opcao == 1:
        jogador1.append(random.choice(dado))
        jogador2.append(random.choice(dado))
    elif opcao ==2:
        break

print("Jogadas do jogador1 "+ str(jogador1))
print("Jogadas do jogador2 "+ str(jogador2))
print("somas do valor do jogador1 " + str(sum(jogador1)))
print("somas do valor do jogador2 " + str(sum(jogador2)))
if jogador1 > jogador2:
    print("Jogador 1 venceu")
elif jogador2 > jogador1:
    print("Jogador 2 venceu")


