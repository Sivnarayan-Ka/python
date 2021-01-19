## Pallindrome
def main():
    print(f"The return value of the pallin function is {pallin()}")

def pallin():
    string = input("Enter a number or string : ")
    if string == string[::-1]:
        # this is a pallindrome
        return 1
    else:
        #this is not a pallindrome
        return 0

main()


