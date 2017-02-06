import sys

numbers = []
multiplication = 1
count = int(sys.stdin.readline().strip())

isZero = False
isMultipleZero = False
for i in range(count):
    number = int(sys.stdin.readline().strip())
    if number:
    	multiplication = multiplication * number
    else:
        if not isZero:
	    isZero = True
        else:
            isMultipleZero = True
    numbers.append(number)

for i in range(count):
    if numbers[i]:
        if isZero:
            print("{}".format(0))
        else:
            print("{}".format(multiplication/numbers[i]))
    else:
        if isMultipleZero:
            print("{}".format(0))
        else:    
            print("{}".format(multiplication))

