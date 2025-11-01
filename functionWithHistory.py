def add(a,b):
    return(a+b)
def multiply(a,b):
    return(a*b)
def minus(a,b):
    return(a-b)
def divide(a,b):
    return(a/b)

history=[]
while True:
    print("press 1 for addition")
    print("press 2 multiply")
    print("press 3 subtraction")
    print("press 4 for division")
    print("press 5 for history")  
    print("press 6 for EXIT")

    choice = input("Select number 1-6.....> ")
    if choice=="6":
        print("Thank you for using calculator")
        break
    elif choice=="5":
        if len(history)==0:
            print("Record is zero")
        else:
            print("\n calculation history")
            for record in history:
             print(record)
            continue #skip taking new inputs

    elif choice in ["1","2","3","4"]:   
        num1= int(input("Enter first number "))
        num2= int(input("Enter second number "))   
        if choice=="1":
            result=add(num1, num2)
            operation='+'
        elif choice=="2":
            result=multiply(num1,num2)
            operation='*'
        elif choice=="3":
            result=minus(num1,num2)
            operation='-'
        elif choice=="4":
             result=divide(num1,num2)
             operation='/'
        print(f"Result: {result}")
        history.append(f"{num1} {operation} {num2} = {result}")
    else:
        print("You enter wrong number")