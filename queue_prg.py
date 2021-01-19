## Write a program by using appropriate functions to 
# add, delete and display the contents of a queue represent as a list of integers.

# Initializing a queue
queue = []

# in case of list implementation of queue pop and append is used instead of dequeue and enqueue
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty