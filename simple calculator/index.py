#wap for simple calculator

def add(number1,number2):
    print("result: ",number1+number2)
def subtract(number1,number2):
    print("result: ",number1-number2)
def multiply(number1,number2):
    print("result: ",number1*number2)
def divide(number1,number2):
    print("result: ",number1/number2)


while(True):
    print("1.add number :")
    print("2.subtract number :")
    print("3.Multiply number :")
    print("4.Division number :")
    ch= int(input("Enter choice: "))
    number1 = int(input("Enter the first number: "))
    number2=int(input("Enter the second number: "))
    if ch == 1:
        add(number1,number2)
    elif ch==2:
        subtract(number1,number2)

    elif ch == 3:
        multiply(number1, number2)
    elif ch == 4:
        divide(number1, number2)
