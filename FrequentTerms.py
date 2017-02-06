#Enter your code here
import sys

#Compare method for sorting
#reverse sort by Value which the term count here
#if count is same then sort by key which the term string
def dictCompare((aKey, aValue), (bKey, bValue)):
    if aValue > bValue:
	return -1
    elif aValue == bValue:
	return cmp(aKey, bKey)
    else:
	return 1

#parse the total count of the terms
numbers = []
count = int(sys.stdin.readline().strip())

#parse out the terms and add it to a dict(hash)
words  = {}
for i in range(count):
    word = sys.stdin.readline().strip()
    if word in words:
	words[word] += 1
    else:
	words[word] = 1
k = int(sys.stdin.readline().strip())

#get a list of (key, value) from the dict 
words_list = [x for x in words.iteritems()]

#sort the list
sorted_words_list = sorted(words_list, cmp=dictCompare) # sort by value

#create a list of frequent terms
frequent_terms = [x[0] for x in sorted_words_list[:k]]

#print the frequent terms
for x in frequent_terms:
    print("{}".format(x))
