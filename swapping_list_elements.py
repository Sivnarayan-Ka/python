## 9.Write a program by designing a function in python to swap / interchange 
# each adjacent element in a list of integers. Or swap / interchange even location 
# elements of list with odd location elements.
		# For example if the list consists of 		10	17	8	5	18	15
		# After interchanging or swapping		    17	10	5	8	15	18


def main():
    ori_list = []
    ori_list = take_input_list_from_user(ori_list)
    for i in range(0, len(ori_list),2):
        swapPositions(ori_list,i,i+1)
    print(f"The swapped list is :  {ori_list}")


def swapPositions(list, pos1, pos2): 
    list[pos1],list[pos2] = list[pos2],list[pos1] 
    return list

def take_input_list_from_user(list):
    try:
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    return list  

main()