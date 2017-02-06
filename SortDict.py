import sys

def dictCompare((aKey, aValue), (bKey, bValue)):
    if aValue > bValue:
        return -1
    elif aValue == bValue:
        return cmp(aKey, bKey)
    else:
        return 1

numbers = []
count = int(sys.stdin.readline().strip())

words  = {}
for i in range(count):
    word = sys.stdin.readline().strip()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
k = int(sys.stdin.readline().strip())
print ("Dict words = {}".format(words))

words_list = [x for x in words.iteritems()]
sorted_words_list = sorted(words_list, cmp=dictCompare) # sort by value

print ("Sorted Dict of words = {}".format(sorted_words_list))

print ("Sorted Dict of top {} words  = {}".format(k, sorted_words_list[:k]))

#numbers.sort(reverse=True)
#for i in range(4):
#    print("{}".format(numbers[i]))
    
