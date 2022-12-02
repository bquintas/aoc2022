file1 = open('day2/input', 'r')
total_score_pt1 = 0
total_score_pt2 = 0
table_score = {('A', 'Y'): 8, ('A', 'X'): 4, ('A', 'Z'): 3, ('B', 'Y'): 5,
               ('B', 'X'): 1, ('B', 'Z'): 9, ('C', 'Y'): 2, ('C', 'X'): 7, ('C', 'Z'): 6}
behavior_map = {('A', 'X'): 'Z', ('A', 'Y'): 'X', ('A', 'Z'): 'Y', ('B', 'X'): 'X',
                ('B', 'Y'): 'Y', ('B', 'Z'): 'Z', ('C', 'X'): 'Y', ('C', 'Y'): 'Z', ('C', 'Z'): 'X'}


while True:
    line = file1.readline().strip()
    if not line:
        break
    combination = tuple(line.split(' '))
    total_score_pt1 += table_score[combination]
    choice = behavior_map[combination]
    keys = (combination[0], choice)
    total_score_pt2 += table_score[keys]
print("Part1:", total_score_pt1)
print("Part2:", total_score_pt2)
