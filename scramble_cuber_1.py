# Esse código gera um embaralhamento para uma posição inicial
# para a resoluçaõ do Cubo Mágico

from random import choice, randint

# Uma lista contendo todos os movimentos básicos para gerar o embaralhamento.
# Para todos os movimentos existe o sentido horário, anti-horário e duplo.

movimentos = [["R", "R'", "R2"],  # Movimento right (lado direito do cubo)
              ["U", "U'", "U2"],  # Movimento Up (lado de cima do cubo)
              ["B", "B'", "B2"],  # Movimento Back (lado de atrás do cubo)
              ["F", "F'", "F2"],  # Movimento Front (lado da frente do cubo)
              ["L", "L'", "L2"],  # Movimento left (lado esquerdo do cubo)
              ["D", "D'", "D2"]]  # Movimento down (lado de baixo do cubo)

t_mov = [19, 20, 21] # São as quantidades padrões de movimentos no embaralhamento do cubo.
cont = 0
quant = choice(t_mov)
scramble_num = []
mov1 = randint(1, 6)

# Esse loop gera uma lista de elementos inteiros de 1 a 6 sem repetição seguida, pois
# lá na frente do código para cada número vai se relacionar a um índice de cada elemento
# da lista movimentos para que não ocorra a repetição de movimento seguido..

while cont < quant:
    mov2 = randint(1, 6)
    while mov2 != mov1:
        scramble_num.append(mov2)
        mov1 = mov2
        cont += 1

scramble = []

# Como foi dito antes, esse loop não vai impedir que ocorra movimentos seguidamente repetido.
# Exemplo de um embaralhamento gerado = F' L2 U2 D2 L' U' D2 L2 R U2 B2 U2 F L F2 U' L R' B
for i in scramble_num:
    if i == 1:
        scramble.append(choice(movimentos[0]))
    elif i == 2:
        scramble.append(choice(movimentos[1]))
    elif i == 3:
        scramble.append(choice(movimentos[2]))
    elif i == 4:
        scramble.append(choice(movimentos[3]))
    elif i == 5:
        scramble.append(choice(movimentos[4]))
    elif i == 6:
        scramble.append(choice(movimentos[5]))

alg = ' '.join(scramble)
print(alg)
