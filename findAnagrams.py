'''
Find all anagrams of a given string in another given string. 
'''

def findAnagrams(master,anagram):
	M = len(master)
	N = len(anagram)

	if N > M:
		return -1 

	char_set = set()
	for letter in anagram:
		char_set.add(letter)

	for index in range(0,M):
		if master[index] in char_set:
			



	
s = “cbaebabacd” 
p = “abc”