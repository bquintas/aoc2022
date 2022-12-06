file1 = open('day6/input', 'r')
stream = []


def store_stream(file):
    while True:
        line = file.readline().strip()
        if not line:
            break
        for c in line:
            stream.append(c)


def block_reading():
    for i in range(3, len(stream)):
        if (len(set(stream[i-3:i+1]))) == 4:
            print(i+1)
            break


store_stream(file1)
block_reading()
