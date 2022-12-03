import string
file1 = open('day3/input', 'r')

# 1 split line in half
# 2 find common letter
# 3 check letter for priority value
# 4 sum and iterate

priority_dict = {v: k+1 for k, v in enumerate(string.ascii_letters)}
total_score_pt1 = 0
comp1 = []
comp2 = []


def get_value(letter):
    return(priority_dict[letter])


def find_common(s):
    comp1 = s[:len(s)//2]
    comp2 = s[len(s)//2:len(s)+1]
    for i in comp1:
        if i in comp2:
            return(i)


while True:
    line = file1.readline().strip()
    if not line:
        break
    total_score_pt1 += (get_value(find_common(line)))

print(total_score_pt1)
# print("Part2:", total_score_pt2)
