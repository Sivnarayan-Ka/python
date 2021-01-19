## 4.Write a program that accepts the information of 5 students as follows and 
# store it in a dictionary.  The information are: roll number, name of the student, marks 
# of 5 subject stored in list.  Design a function named as calculate( ) to calculate 
# the average mark of each student and display the information.

def main():
    students_info = {} 
    student_data = ['Roll no : ', 'Math marks : ', 'Physics marks : ', 'Chemistry marks : ', 'Biology marks : ', 'History marks : ']
    num_students = int(input("Enter the number of students : "))
    
    for i in range(1,num_students+1):
        student_name = input(f"Enter the name of the {i} th student : ")
        students_info[student_name] = {} #create a new empty dictionary for each input name by the user , to sore the marks for various subjects . 
        for entry in student_data:
            students_info[student_name][entry] = int(input(entry)) #storing the marks entered as integers to perform arithmetic operations later on.

    # print the students information
    print("-------------------Students Average Info----------------------------")
    for student_name, data in students_info.items(): # since we are using nested dict
        print(f"Student name : {student_name} and average marks is : {calculate_average_marks(data)}")   


def calculate_average_marks(student_marks):
    sum = 0
    for key in student_marks:
        if "marks" in key.lower(): # to pick only marks data and ignoring any other data stored like roll
            sum += student_marks.get(key)
    return sum/5.0 #Average of 5 subject's marks

main()