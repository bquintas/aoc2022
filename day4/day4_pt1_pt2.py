file1 = open('day4/input', 'r')
elf1 = []
elf2 = []
elf1n = []
elf2 = []
counter_contained = 0
counter_overlap = 0


def preprocess(line):
    list_of_strings = line.split(',')
    elf1 = list_of_strings[0].split('-')
    elf1n = [x for x in range((int(elf1[0])), int(elf1[1])+1)]
    elf2 = list_of_strings[1].split('-')
    elf2n = [x for x in range((int(elf2[0])), int(elf2[1])+1)]
    return (elf1n, elf2n)


def iscontained(t):
    list1, list2 = t
    return((set(list1).issubset(set(list2))) or (set(list2).issubset(set(list1))))


def isoverlap(t):
    list1, list2 = t
    return(bool(set(list1) & set(list2)))


while True:
    line = file1.readline().strip()
    if not line:
        break
    if (iscontained(preprocess(line))):
        counter_contained += 1
    if (isoverlap(preprocess(line))):
        counter_overlap += 1

print(f"Is contained: {counter_contained}, Is overlapped:{counter_overlap}")
