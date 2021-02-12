"""
    this is for creating a dictionary

    Returns:
        [type]: [description]
"""
words = set()

def main():
    # load("file_containing_words.txt")
    
    print(f"The total number of unique words in the file are : {size()}")
    print(f"All the unique words are ")
    print(f"{words}")

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def addUnqueWords(dictionary): 
    file = open(dictionary, 'r')
    for line in file:
        list = line.split(" ")
        print(f"line = {line}")
        print(f"{type(list)}")
        print(*list,sep="/")
        for element in list:
            print(f"element = {element}")
            words.add(element.rstrip())
    ##close(file)
    file.close()
    return True

def load(dictionary):
    file = open(dictionary,'r')
    for line in file:
        words.add(line.rstrip())
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True

main()



