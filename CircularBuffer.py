import sys

# Circular Buffer class
# takes in a size argument in constructor
# implements append, remove and list method
class CircularBuffer:
    def __init__(self, size):
	self.size = size
        self.data = []

    def append(self, x):
	if len(self.data) == self.size:
            self.data.pop(0)
            self.data.append(x)
	else:
	    self.data.append(x)

    def remove(self, count):
	for i in range(count):
	    self.data.pop(0)

    def get(self):
        return self.data

    def list(self):
	for item in self.data:
	    print("{}".format(item))

    def buf_size(self):
	return len(self.data)

#parse the buffer size
buffer_size = int(sys.stdin.readline().strip())
circular_buffer = CircularBuffer(buffer_size)

#parse the first command
full_command = sys.stdin.readline().strip().split()
command = full_command[0]
command_arg = 0
if len(full_command) > 1:
    command_arg = int(full_command[1])

#loop until quit command
while command != "Q":
    #process commands A, R and L
    if command == "A":
	#parse items
	for i in range(command_arg):
	    item = sys.stdin.readline().strip()
	    circular_buffer.append(item)
    elif command == "R":
	#remove items
	if command_arg <= circular_buffer.buf_size():
	    circular_buffer.remove(command_arg)
    elif command == "L":
	#list items
	circular_buffer.list()

    full_command = sys.stdin.readline().strip().split()
    command = full_command[0]
    command_arg = 0
    if len(full_command) > 1:
	command_arg = int(full_command[1])

