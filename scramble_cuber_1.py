from random import choice, randint

movimentos = [["R", "R'", "R2"],
              ["U", "U'", "U2"],
              ["B", "B'", "B2"],
              ["F", "F'", "F2"],
              ["L", "L'", "L2"],
              ["D", "D'", "D2"]]

t_mov = [19, 20, 21]
cont = 0
quant = choice(t_mov)
scramble_num = []
mov1 = randint(1, 6)

while cont < quant:
    mov2 = randint(1, 6)
    while mov2 != mov1:
        scramble_num.append(mov2)
        mov1 = mov2
        cont += 1

scramble = []

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
