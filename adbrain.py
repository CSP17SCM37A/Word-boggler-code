
# coding: utf-8

# In[4]:

input_dict = {}
data_input = open("Input_Matrix2.txt","r") 
row = 0
col = 0
rows = 0
cols = 0
flag = True
next_row = data_input.readline()
while next_row != "":
    rows = rows + 1
    for each in next_row.split(' '):
        if flag:
            cols = cols + 1
        input_dict[(row,col)] = each.strip()
        col = col + 1
    row = row + 1
    col = 0
    flag = False;
    next_row = data_input.readline()
#print(rows,cols)

def find_word_from_path(path):
    return ''.join([input_dict[p] for p in path])

def read_dictionary_words():
    stems, dictionary = set(), set()
    with open('Dictinoary2.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)
            for i in range(len(word)):
                stems.add(word[:i + 1])
    return dictionary, stems

def find_adjacent_Character_with_loop():
    adjacent = {}
    for each in input_dict:
        x, y = each
        positions = [(x, y),(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        adjacent[each] = [p for p in positions if 0 <= p[0] < rows and 0 <= p[1] < cols]
    return adjacent


def find_word_path(path):
    word = find_word_from_path(path)
    if word not in stems:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in adjacent[path[-1]]:
        if next_pos not in path:
            find_word_path(path + [next_pos])
        elif next_pos in path:
            find_word_path(path + [next_pos])
        

def get_words():
    for each in input_dict.keys():
        find_word_path([each])     
    return [find_word_from_path(p) for p in paths]



paths = []

adjacent = find_adjacent_Character_with_loop()
dictionary, stems = read_dictionary_words()
words = get_words()
print(words)


# In[ ]:




# In[ ]:




# In[ ]:



