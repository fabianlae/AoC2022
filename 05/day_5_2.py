data = open("..\\inputs\\5.txt").read().split("\n\n")
table_data = data [0]
instructions = data[1].split('\n')

table_data = table_data.split('\n')
data_prep = []
# read out data
for idx, line in enumerate(table_data):
    n = 4
    row = [line[i:i+n].replace(" ", "") for i in range(0, len(line), n)]
    row = [item.replace('[', '') for item in row]
    row = [item.replace(']', '') for item in row]
    data_prep.append(row)

# rearrange data
data_prep = list(map(list, zip(*data_prep)))
data_final = []
for stack in data_prep:
    data_final.append(list(filter(None, stack)))

for instruction in instructions:
    # extract instructions
    instruction_split = instruction.split(' ')
    move = int(instruction_split[1])
    von = int(instruction_split[3])
    to = int(instruction_split[5])
    
    # apply instruction
    take = data_final[von-1][:move]
    for crate in reversed(take):
        data_final[to-1].insert(0, crate)
    del data_final[von-1][:move]

# extract top items
solution = ''
for stack in data_final:
    solution += stack[0]

print(solution)