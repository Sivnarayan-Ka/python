## 16.Write a program to increase the salary by 2000/- of the employee whose 
# employee number is taken input in the program at run time. Assuming “employee.dat” 
# contains records of the employee according to the following dictionary definition.
# Emp={“enum”:_______, “ename”:_________, “salary”:_______} 

def main():
    emp_info = {} 
    # emp_data = ['enum','ename', 'salary']
    num_emp = int(input("Enter the number of employees : "))
    
    for i in range(1,num_emp+1):
        emp_info[i] = {} #create a new empty dictionary for each input emp no by the user , to store the emp details . 
        emp_info[i]["enum"] = input(f"Enter the emp_no of the {i} th employee : ")
        emp_info[i]["ename"] = input("Emp name : ")
        emp_info[i]["salary"] = float(input("Emp salary : "))
        
    print(emp_info)
    
    sal_modify_emp_no = input(f"Enter the emp no whose salary needs to be incremented : ")
    emp_found = False
    for index,emp in emp_info.items(): ## iterating through the emp info nested dictionary
        print(f"index is at : {index}")
        if emp["enum"] == sal_modify_emp_no:
            emp["salary"] += 2000
            emp_found = True
            print("emp salary sucessfully incremented.")
            break
    
    if emp_found == False:
        print("No emp found")
    
    print("-----New updated emp records ----------")
    print(emp_info)

main()