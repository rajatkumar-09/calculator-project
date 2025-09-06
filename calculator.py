def add(num1,num2):
    return num1+num2 

def subtract(num1,num2):
    return num1-num2 

def divide(num1,num2):
    return num1/num2 

def multi(num1,num2):
    return num1*num2 

def avg(num1,num2):
    return (num1+num2)/2 
print("please select your operation \n1.ADD \n2.SUBTRACT\n3.DIVIDE\n4.MULTI\n5.AVG")
number1 = int(input("enter your first number : "))
number2 = int(input("enter your second number : "))
select = int(input("enter your option : "))
 

if select == 1:
    print("sum of two number = ",add(number1,number2))

elif select == 2:
    print("subtract of two number = ",subtract(number1,number2))

elif select == 3:
    print("multiply of two number = ",divide(number1,number2))    

elif select == 4:
    print("division of two number = ",multi(number1,number2))
      
else:
    print("avrage of two number = ",avg(number1,number2))