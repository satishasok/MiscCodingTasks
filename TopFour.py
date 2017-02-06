import sys

numbers = []
count = int(sys.stdin.readline().strip())

for i in range(count):
    number = int(sys.stdin.readline().strip())
    numbers.append(number)

numbers.sort(reverse=True)
for i in range(4):
    print("{}".format(numbers[i]))
    
