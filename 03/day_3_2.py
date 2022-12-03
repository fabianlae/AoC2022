from day_3 import read_file, char_position

# read data
data = read_file('input.txt')

# build groups and sum up
prev_idx = 0
rank_score = 0
for idx in range(3, len(data)+1, 3):
    group = data[prev_idx:idx]
    prev_idx = idx
    # find common letter between three backpacks
    for elve in group:
        backpack_1 = set(group[0])
        backpack_2 = set(group[1])
        backpack_3 = set(group[2])
        item_type = backpack_1 & backpack_2 & backpack_3
    rank_score += char_position(list(item_type)[0])

print(rank_score)