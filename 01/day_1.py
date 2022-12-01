import numpy as np

# open file
my_file = open('input.txt', 'r')
# reading the file
data = my_file.read()

# splitting the text when \n\n
data_into_list = data.split("\n\n")
my_file.close()
# split and transform
data_into_list = [[int(j) for j in i.split('\n')] for i in data_into_list]

calory_sums = []
for elf in data_into_list:
  calory_sums.append(sum(elf))


# printing the data
# print(data_into_list)
calory_sums.sort(reverse=True)
# solution task 1
print(f'top 1 elf: {calory_sums[0]}')
# solution task 2
print(f'top 3 elfs sum: {sum(calory_sums[:3])}')#.sort(reverse=True))
