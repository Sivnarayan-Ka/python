## Write a program by designing a function named as BUBBLESORT to sort a list 
# containing integers in descending order using Bubble sort method.

def main():
    ori_list = []
    try:
        ori_list = [ int(item) for item in input(f"Enter the unsorted list of integers with comma separated : ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        ori_list = [ int(item) for item in input(f"Enter the unsorted list of integers with comma separated : ").split(',') ]
    print(f"The bubble sorted list in descending order is : ")
    print(f"{bubblesort(ori_list)}")

def bubblesort(our_list):
    has_swapped = True
    num_of_iterations = 0
    
    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations -1):
            if our_list[i] < our_list[i+1]: # since we need descending order
                #swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1
    return our_list

main()