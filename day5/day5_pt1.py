import re
file1 = open('day5/input', 'r')
stacks = [['D', 'L', 'J', 'R', 'V', 'G', 'F'], ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S'], ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C'], ['M', 'D', 'P', 'N', 'G',
          'Q'], ['J', 'L', 'H', 'N', 'F'], ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z'], ['F', 'D', 'B', 'L'], ['M', 'J', 'B', 'S', 'V', 'D', 'N'], ['G', 'L', 'D']]

moves = []


def list_moves(file1):
    while True:
        line = file1.readline().strip()
        if not line:
            break
        match = re.match(
            r"^move\s(\d*)\sfrom\s(\d)\sto\s(\d)", line)
        if match:
            # storing amount , from , to
            moves.append(match.groups())


list_moves(file1)
for sublist in moves:
    for i in range(-1, -int(sublist[0])-1, -1):
        stacks[(int(sublist[2])-1)].append(stacks[(int(sublist[1])-1)].pop())

for l in range(0, len(stacks)):
    print(stacks[l][-1])
