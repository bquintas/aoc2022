file1 = open('day8/input', 'r')
matrix = []


def create_array(file):
    while True:
        row = []
        line = file.readline().strip()
        if not line:
            break
        row = [int(s) for s in line]
        matrix.append(row)


create_array(file1)

visible_counter = {}
# using the first list to determine length of array
max_x = len(matrix[0])
# number of lists = max y
max_y = len(matrix)

for list in range(max_y):
    for value in range(max_x):
        #print(list, value)
        # check if values are in outer edge
        if value == 0 or value == max_x-1 or list == 0 or list == max_y-1:
            visible_counter[value, list] = True
        # check to the right
        if len([matrix[list][x] for x in range(value+1, max_x) if matrix[list][x] >= matrix[list][value]]) == 0:
            visible_counter[value, list] = True
        # # check to the left
        if len([matrix[list][x] for x in range(value) if matrix[list][x] >= matrix[list][value]]) == 0:
            visible_counter[value, list] = True
        # # check up
        if len([matrix[y][value] for y in range(list) if matrix[y][value] >= matrix[list][value]]) == 0:
            visible_counter[value, list] = True
        # # check down
        if len([matrix[y][value] for y in range(list+1, max_y) if matrix[y][value] >= matrix[list][value]]) == 0:
            visible_counter[value, list] = True


print(len(visible_counter))
# print(visible_counter)
