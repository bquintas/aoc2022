from collections import defaultdict
file1 = open('day7/input', 'r')
commands = file1.read().strip().split('\n')
filesystem = defaultdict(int)
cwd = []


def store_directories(list):
    for command in list:
        if command == '$ cd ..':
            cwd.pop()
        elif command.startswith('$ cd'):
            cwd.append((''.join(cwd)+'/'+command.split(' ')
                        [2]).replace('//', '/'))
        elif command[0].isdigit():
            for d in cwd:
                filesystem[d] += int(command.split(' ')[0])


def part1(dict):
    total = 0
    for i in dict:
        if (dict[i]) <= 100000:
            total += dict[i]
    return(total)


def part2(dict):
    temp_list = []
    space_needed = 30000000 - (70000000 - dict['/'])
    for i in dict:
        if dict[i] >= space_needed:
            temp_list.append(dict[i])
    return(min(temp_list))


store_directories(commands)
print(f"Part1:{part1(filesystem)}")
print(f"Part2:{part2(filesystem)}")
