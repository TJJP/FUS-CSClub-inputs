f = open("numericalsort-input.txt", "r")
Lines = f.readlines()

numberlist = []

for line in Lines:
    numberlist.append(int(line.strip()))

pop = numberlist.pop(0)

numberlist.sort()

print(pop)

for line in numberlist:
    print(line)