## Write a program by designing a function named as bsearch( ) to search an element using 
# binary search from a list containing integers listanged in ascending order

def main():
    ori_list = []
    try:
        ori_list = [ int(item) for item in input(f"Enter the sorted list of integers with comma separated in Ascending order: ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        ori_list = [ int(item) for item in input(f"Enter the sorted list of integers with comma separated in Ascending order: ").split(',') ]
    
    x = int(input(f"Enter the integer to bserach : "))
    
    result = binary_search(ori_list, x) 
    if result != -1: 
        print(f"Element is present at index {result}") 
    else: 
        print("Element is not present in list") 

# Iterative Binary Search Function 
# It returns index of x in given list list if present, 
# else returns -1 
def binary_search(list, x): 
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high: 

        mid = (high + low) // 2

        # Check if x is present at mid 
        if list[mid] < x: 
            low = mid + 1

        # If x is greater, ignore left half 
        elif list[mid] > x: 
            high = mid - 1

        # If x is smaller, ignore right half 
        else: 
            return mid 

    # If we reach here, then the element was not present 
    return -1


main()