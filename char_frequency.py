#!/usr/bin/env python 

'''

Return most common characters appearing with a character given a list of words. 

'''

def solve(list_of_strs):
    # return Dict[char, List[char]]
    
    chars_DB = dict()

    #'database' data structure to represent the words with frequencies 
    
    for word in list_of_strs:               
        for char in word:
            if char not in chars_DB:
                chars_DB[char] = { }

            for char2 in word:
                if char != char2:
                    if char2 not in chars_DB[char]:
                        chars_DB[char][char2] = 1
                    else: 
                        chars_DB[char][char2] +=1 

    return chars_DB

    '''
    chars_DB output: 

    {'a': {'b': 1, 'c': 1}, 'b': {'a': 1, 'c': 2, 'd': 1}, 'c': {'a': 1, 'b': 2, 'd': 2, 'e': 1},
     'd': {'b': 1, 'c': 2, 'e': 1}, 'e': {'c': 1, 'd': 1}}

     Last portion: Need to further query this to return largest by key. Not completed. 

    '''

my_lst = ['abc', 'bcd', 'cde']
print(solve(my_lst))

