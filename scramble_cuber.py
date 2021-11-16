# Scramble para o Cubo Mágico
import random
from random import choice, randint

movimentos = [["R", "R'", "R2"],
              ["U", "U'", "U2"],
              ["B", "B'", "B2"],
              ["F", "F'", "F2"],
              ["L", "L'", "L2"],
              ["D", "D'", "D2"]]


def reducao(list):
    m1 = []
    for i in list:
        m1.append(choice(i))
    return m1


t_mov = [19, 20, 21]
quant = choice(t_mov)
scramble_num = []
mov1 = randint(1, 6)

contador = 0

while contador < quant:
    mov2 = randint(1, 6)
    while mov2 != mov1:
        scramble_num.append(mov2)
        mov1 = mov2
        contador += 1

scramble = []

for i in scramble_num:
    s = reducao(movimentos)
    if i == 1:
        scramble.append(s[0])
    elif i == 2:
        scramble.append(s[1])
    elif i == 3:
        scramble.append(s[2])
    elif i == 4:
        scramble.append(s[3])
    elif i == 5:
        scramble.append(s[4])
    elif i == 6:
        scramble.append(s[5])

alg = " ".join(scramble)
print(len(scramble))
print(alg)
