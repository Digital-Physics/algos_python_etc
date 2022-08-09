print("Stacks are Last In First Out 'LIFO'")
print("think stacks of plates, where the top plate is the only one accessible")
print("the call stack is a stack of frames in a dependency order")
print("the back functionality in a browser is a 'pop' off the stack")
print("going to a new page in your browser is a 'push' onto the stack")
print("undo and redo on a file editor utilize stacks")
print("we could create a stack from scratch like below, but we'll use lists with built in methods in python")
print("it's almost like a linked list, but when pushing to stack new node points back to previous top node, not forward")
print("so the most recently added node isn't hanging with a None value on self.next")


class Node():
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack():
    def __init__(self):
        self.top = None

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise Exception("Stack is empty so can't peek")

    def pop(self):
        if self.top:
            temp = self.top.value
            self.top = self.top.next
            return temp
        else:
            raise Exception("Stack is empty so can't pop")

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node


list_for_stack = [i**2 for i in range(10)]
stack = Stack()
for val in list_for_stack:
    stack.push(val)

print(stack.peek())
popped = stack.pop()
print(popped)
print(stack.peek())
stack.push(42)
print(stack.peek())

print("let's do Stacks the Python way...")
print("pop() method for lists, index -1 to 'peek' at the end/top, and append() as 'push'")
list_for_stack = [i**2 for i in range(10)]
print("peek", list_for_stack[-1])
popped = list_for_stack.pop()
print(popped)
print("peek", list_for_stack[-1])
list_for_stack.append(42)
print("peek", list_for_stack[-1])

print()


print("Queue are First In First Out 'FIFO' or 'first-come, first-serve'")
print("think of line of people waiting for something, say queueing up to see 'Digital Physics' the movie")
print("they will 'enqueue' before they are let into the theater")
print("they will then be 'dequeue' one at a time as the usher takes the ticket stub")
print("let's create a queue from 'scratch' like we did for a stack")


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.rear = new_node
            self.front = new_node

    def dequeue(self):
        if self.front:
            temp = self.front.value
            self.front = self.front.next
            return temp
        else:
            raise Exception("Queue is empty")


list_for_queue = [i**2 for i in range(10)]
queue = Queue()
for val in list_for_queue:
    queue.enqueue(val)

dequeued = queue.dequeue()
print(dequeued)
dequeued = queue.dequeue()
print(dequeued)
queue.enqueue(42)

while queue.front:
    print("dequeued", queue.dequeue())

print("let's do Queues the Python way as well...")
print("so to 'dequeue' we'll use the pop(0) method for lists, and to 'enqueue' we'll use the append() method")
list_for_queue = [i**2 for i in range(10)]

dequeued = list_for_queue.pop(0)
print(dequeued)
dequeued = list_for_queue.pop(0)
print(dequeued)
list_for_queue.append(42)

while list_for_queue:
    print("dequeued", list_for_queue.pop(0))

print("Lists are actually not great for Queues in Python because when you dequeue or pop(0), it shifts all indexed items in list")
print("we could 'from collections import dequeue' if we wanted constant time popping at both ends")

