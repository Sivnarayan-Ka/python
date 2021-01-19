## 8.Write a program by designing a function named as INSERTIONSORT to sort a list containing
# integers in ascending order using insertion sort method.

def main():
    ori_list = []
    ori_list = take_input_list_from_user(ori_list)
    print(f"The sorted list ascending order is :  {insertion_sort(ori_list)}")

def insertion_sort(list): 

    # Traverse through 1 to len(list) 
    for i in range(1, len(list)): 

        key = list[i] 

        # Move elements of list[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < list[j] : 
                list[j+1] = list[j] 
                j -= 1
        list[j+1] = key 
    return list

def take_input_list_from_user(list):
    try:
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    return list    

main()