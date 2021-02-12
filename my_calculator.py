#create a caliculator

def  main():
    while True:
        user_choice_of_operation = take_operation_todo_input()
        num_calculate(user_choice_of_operation)
        should_countinue = input("Do you wish to continue (Y/N) : ")
        print() # for a blank newline
        if should_countinue.lower() != "y":
            print("Thanks for using our calculator.Bye")
            break

def take_operation_todo_input():
    print("===================My Calaculator===============")
    print(f'Please press the below for your calculation : ')
    print("+ - for addition")
    print("- - for substraction")
    print("* - for multipication")
    print("/ - for division")
    print("'%' - for modulo")
    print("** for to the power")
    print("// for floor operation") #gives quotent rounding up
    user_choice = input("Please enter your choice : ")
    return user_choice

def num_calculate(user_choice_of_operation):    
    while True:
        try:
            num1 = int(input("Enter num1 = "))
            num2 = int(input("Enter num2 = "))
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter a valid number")
            continue
        
        # improper_input = False
        result = calcuate_num(user_choice_of_operation,num1,num2)
        print(f"The result of the operation num1 {user_choice_of_operation} num2 is :\n {num1} {user_choice_of_operation} {num2} = {result}")
        return result
        
        
        

def calcuate_num(user_choice,num1,num2):
    result = 0
    if user_choice == "+":
        result = num1 + num2
    elif user_choice == "-":
        result = num1 - num2
    elif user_choice == "*":
        result = num1*num2
    elif user_choice == "/":
        result = num1/num2 
    elif user_choice == "%":
        result = num1 % num2
    elif user_choice == "**":
        result = num1 ** num2
    elif user_choice == "//":
        result = num1 // num2

    return result
    

print(f"And the name of this program is {__name__}")
if __name__ == "__main__":
    main()


