### Takes a list of words and returns the length of the longest word in the list

def main():
    words = []
    n = int(input("Enter the number of words in the list you want to enter : "))
    for strings in range(n):
        string = input(f"Enter the {strings} th number : ")
        words += string, # add strings to the list
    
    print(f"The length of the longest word in the list is {longest_word_length(words)}" )

def longest_word_length(words):
    print(words)
    longest_word =max(words,key=len)
    return len(longest_word)

main()