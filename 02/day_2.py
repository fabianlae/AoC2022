# import
from collections import Counter


def get_combination_and_count(data):
    '''
    Gets all possible combinations and their number of occurences.
    '''
    # open file
    my_file = open(data, 'r')
    # reading the file
    data = my_file.read()

    # splitting the text when \n\n
    data_into_list = data.split("\n")
    my_file.close()

    keys = Counter(data_into_list).keys()
    values = Counter(data_into_list).values()

    return list(keys), list(values)


keys, values = get_combination_and_count('input2.txt')

# A: Stein, B: Papier, C: Schere
# X: Stein, Y: Papier, Z: Schere

scores = {
    'A X': 4, 
    'B Z': 9, 
    'C Z': 6, 
    'A Y': 8, 
    'A Z': 3, 
    'B Y': 5, 
    'C X': 7, 
    'B X': 1, 
    'C Y': 2
}

final_score = 0
for idx, key in enumerate(keys):
    final_score += values[idx]*scores[key]

print(final_score)