file1 = open('input', 'r')
count = 1
results = {}
max = 0
current = 0
while True:
    line = file1.readline()
    # if line.strip can be done it's not empty
    if line.strip():
        current += int(line)
    else:
        # line was empty mean separator between elfs, write current sum to elf number and reinitialize variable
        results[count] = current
        current = 0
        count += 1
    # end of file is reached
    if not line:
        break
    # ordered view of dict and sum highest 3 values
print(sorted(results.values())[-1:])
print(sum(sorted(results.values())[-3:]))
