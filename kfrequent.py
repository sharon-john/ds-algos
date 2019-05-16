def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    needed = k[v.index(max(v))]		#O(n) operation, O(n) 
    d.pop(k[v.index(max(v))])       #O(1) 
    return needed

def topKFrequent(nums, k):
    frequency_HashMap = dict()
    for elem in nums:								#O(n)
        if frequency_HashMap.get(elem, 0) == 0:
            frequency_HashMap[elem] = 1 
        else:
            frequency_HashMap[elem] +=1 
        
    vals = [] 
    print (frequency_HashMap)
    for i in range(0,k):								#O(k)
        new_entry = keywithmaxval(frequency_HashMap)    
        vals.append(new_entry)      #O(1)
        
    return vals 

lst = [1,1,1,2,2,3]
print (topKFrequent(lst,2))

