
def main():
    """ call the function ==> main() ==> and do not enter any value in main function between bracets and run :)
     
      My module by anas essam """
    
    while True:
        print("_________________________________________________")
        print("Welcome to my program  :) ' Simple_Calc_Dev ' ")

        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        oper = input("Enter operation: ")

        if oper == "+":
            print("= ", num1 + num2)
        elif oper == "-":
            print("= ", num1 - num2)
        elif oper == "*":
            print("= ", num1 * num2)
        elif oper == "/":
            print("= ", num1 / num2)
        else:
            print(" !! ERROR !! Enter valid value and try again")
            break