file = open("data.txt", "r")

for line in file.read().splitlines():
    print(line.strip())

file.close()