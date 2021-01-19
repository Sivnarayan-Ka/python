## 14.Write a program, to create an new my_file “TEST.TXT” and write some lines 
# to it and the same program will read one line at a time from the text my_file 
# and displays it to a monitor and also count the number of lines present. 
# Your program has to read all the contents of the my_file. Assume the length of 
# the line not to exceed 80 characters.

def main():
    my_file = open("file_read.txt","w+")
    
    dummy_text=["Hello","\nHi","\nPython"]
    # dummy_text=["Hello","Hi","Python"]
    my_file.writelines(dummy_text)
    
    #printing the my_file's contents all at once
    my_file.seek(0)
    for line in my_file:
        print(line)
    
    #reading and printing line by line
    print(f"\n-----------Reading line by line -------------")
    my_file.seek(0) ## bringing file cursor to start of file
    buf = my_file.readline()
    if len(buf) > 0:
        lines = 1
    else:
        lines = 0
        print(f"File is empty")
        my_file.close()
        return
        
    print(buf)
    while True:
        buf = my_file.readline()
        if len(buf) > 0:
            lines += 1
            print(buf)
        else:
            break
        
    
    print(f"End of file reached and no of lines in file is : {lines}")
    my_file.close()
    

main()