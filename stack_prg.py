## Write a program by using appropriate functions to push, pop and display the contents 
# of a stack containing book details (book no, book name, price).


from queue import LifoQueue ## using python queue.LifoQueue module


def main():
    # Initializing a stack
    stack = LifoQueue(maxsize = 3)
    # qsize() show the number of elements
    # in the stack
    print(f"stack sizee : {stack.qsize()}")
    
    books_info = {} 
    book_data = ['book name  ', 'price  ']
    num_books = int(input("Enter the number of books : "))
    
    for i in range(1,num_books+1):
        book_no = input(f"Enter the no of the {i} th book : ")
        books_info[book_no] = {} #create a new empty dictionary for each input book no by the user , to sore the book details . 
        for entry in book_data:
            books_info[book_no][entry] = input(entry)
            # books_info[book_no][entry] = input(entry) #storing the marks entered as integers to perform arithmetic operations later on.
        
        # put() function to push
        # element in the stack
        stack.put(books_info[book_no])
        
    print(f"Stack Full: {stack.full()}") 
    print(f"Stack Size: {stack.qsize()}")  
    
    # get() fucntion to pop
    # element from stack in 
    # LIFO order
    print('\nElements poped from the stack')
    print(stack.get())
    print(stack.get())
    
    
    print(f"\n Is Empty: {stack.empty()}")

main()




