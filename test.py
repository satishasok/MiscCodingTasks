#Enter your code here
import sys

numbers = []
multiplication = 1
line = sys.stdin.readline()
line.strip()
if not line:
        print ("Invalid Input, enter a line break followed by intergers one per line with an empty line in the end")
else:
        while True:
                try:
                        line = sys.stdin.readline()
                        line = line.strip()
                        if line:
                                num = 1
                                try:
                                        num = int(line)
                                except:
                                        num = 1
                        else:
                                break
                        numbers.append(num)
                        multiplication = multiplication * num
                except KeyboardInterrupt:
                        break

        length = len(numbers)
        if length >= 2:
                for i in range(length):
                        if numbers[i]:
                                print ("{}".format(multiplication/numbers[i]))
                        else:
                                print ("{}".format(numbers[i]))

        else:
                print ("Invalid Input: need to enter minimum 2 numbers")
