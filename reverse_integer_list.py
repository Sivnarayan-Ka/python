## 7.Write a program by designing a function in python to reverse a
# list of integers.(Don’t use reverse function)

def main():
    ori_list = []
    ori_list = take_input_list_from_user(ori_list)
    print(f"The reversed list is :  {reverse(ori_list)}")

# Reversing a list using slicing technique 
def reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 

def take_input_list_from_user(list):
    try:
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    return list    

main()