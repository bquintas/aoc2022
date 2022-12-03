import string
file1 = open('day3/input', 'r')
counter = 0
priority_dict = {v: k+1 for k, v in enumerate(string.ascii_letters)}
total_score_pt2 = 0
lines = []


def get_value(letter):
    return(priority_dict[letter])


def find_common(l):
    common = set.intersection(*map(set, l))
    return(common)


while True:
    line = file1.readline().strip()
    if not line:
        break
    counter += 1
    lines.append(line)
    if counter == 3:
        total_score_pt2 += get_value(''.join(find_common(lines)))
        lines = []
        counter = 0
print("Part2:", total_score_pt2)
