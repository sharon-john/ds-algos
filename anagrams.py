#anagram detection 

def basicIsAnagram(str1, str2):
	lst1 =  []
	for char in str1: 		#O(N)
		lst1.append(char)	

	lst2= []
	for char in str2:		#O(N)
		lst2.append(char)

	for i in lst1:
		if i not in lst2:	#O(N^2)
			return False 
		else:
			lst2.remove(i)

	return True 

'''
This approach has an O(N^2) time complexity because we search the entire second list 
If the characters were sorted, this could be brought down to O(N Log N)
'''

def betterIsAnagram(str1, str2):
	lst1 =  []
	for char in str1: 		#O(N)
		lst1.append(char)	

	lst2= []
	for char in str2:		#O(N)
		lst2.append(char)

	lst1.sort()   #O(N Log N)
	lst2.sort()  #O(N Log N)

	if lst1 == lst2:  #O(N)
		return True 
	else:
		return False 

'''
Time complexity of this approach is O(N Log N). This is the optimized approach 
'''

def bestIsAnagram(str1, str2):
	lst1 = [0] * 26 
	lst2 = [0] * 26 

	for i in range(0,len(str1)):
		pos = ord(str1[i]) - ord('a')
		lst1[pos]+=1 

	for j in range(0,len(str2)):
		pos = ord(str2[j]) - ord('a')
		lst2[pos]+=1 

	k= 0
	while k < 26:
		if str1[i] == str2[j]:
			k+=1 
		else:
			return False 

	return True 


first_string = "ab"
second_string = "ba"
print (basicIsAnagram(first_string, second_string))
print (betterIsAnagram(first_string, second_string))
print (bestIsAnagram(first_string, second_string))
