import string
def read_file(data):
    '''
    read in input data from txt file.
    '''
    # open file
    my_file = open(data, 'r')
    # reading the file
    data = my_file.read()

    # splitting the text when \n\n
    data_into_list = data.split("\n")
    my_file.close()
    return data_into_list

data = read_file('input.txt')

def char_position(letter):
    '''
    Get index of letter in the alphabet. Double index for upper case letters
    '''
    if letter.isupper():
        return ord(letter.lower()) - 70
    else:
        return ord(letter) - 96

rank_score = 0
for bp in data:
    comp_1 = set(bp[:len(bp)//2])
    comp_2 = set(bp[len(bp)//2:])
    comp_intersection = comp_1.intersection(comp_2)
    rank_score += char_position(list(comp_intersection)[0])

print(rank_score)