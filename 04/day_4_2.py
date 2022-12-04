data = open("..\\inputs\\4.txt").read().strip().split("\n")

contain_count = 0
for i in data:
    # separate pairs and transform numbers to int
    pair = [[int(k.split('-')[0]), int(k.split('-')[1])] for j in i.split(',') for k in j.split(',')]
    # check if one overlaps the other
    elve_one = set(range(pair[0][0], pair[0][1]+1))
    elve_two = set(range(pair[1][0], pair[1][1]+1))
    if elve_one.intersection(elve_two):
        contain_count += 1

print(contain_count)