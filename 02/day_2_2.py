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
    data_into_list = [i.split(' ') for i in data_into_list]
    my_file.close()
    index_list = {
        'A': 0,
        'B': 1,
        'C': 2
    }
    data_list_extended = ['A', 'B', 'C', 'A', 'B']

    # generate own shape as third item in list
    for idx, game in enumerate(data_into_list):
        # draw
        if game[1] == 'Y':
            data_into_list[idx].append(game[0])
        elif game[1] == 'X':
            opp_idx = index_list[game[0]]
            data_into_list[idx].append(data_list_extended[opp_idx+2])
        else:
            opp_idx = index_list[game[0]]
            data_into_list[idx].append(data_list_extended[opp_idx+1])

    # A: Stein, B: Papier, C: Schere
    print(data_into_list)
    # count points
    final_score = 0
    shape_score = {'A': 1, 'B': 2, 'C': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    for game in data_into_list:
        final_score += outcome_score[game[1]]
        final_score += shape_score[game[2]]
    
    return final_score

final_score = get_combination_and_count('input2.txt')
print(final_score)