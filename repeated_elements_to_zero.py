## 10.Write a program by designing a function in python to store zero
# for every repeated elements in the list.
	# For example if the list contains 			10	7	15	7	10
	# Finally the list will contain		        10	7	15	0	0

def main():
    ori_list = []
    ori_list = take_input_list_from_user(ori_list)

    print(f"The repeated elemnts replaced list is :  {replace_duplicates_with_zero(ori_list)}")

def replace_duplicates_with_zero(list):
    unique_list = set([])
    for indx,ele in enumerate(list):
        if ele in unique_list:
            list[indx] = 0
        unique_list.add(ele)
    return list

def take_input_list_from_user(list):
    try:
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    except:
        print(f"!!ERROR!! Please enter only integer and no empty ones between commas")
        list = [ int(item) for item in input(f"Enter the list of integers with comma separated : ").split(',') ]
    return list  

main()