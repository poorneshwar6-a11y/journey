
while(True):
    print("="*40)
    print("WELCOME TO BASIC CALCULATOR")
    print("="*40)
    a=int(input("Enter a number1:"))
    b=int(input("Enter a number2:"))
    c=input("enter your choice:'+' '*' '-' '/' to exit enter 'QUIT' :").strip().lower()
    print("="*40)
    match c:
        case '+':
            print("Addition of",a,"&",b,"is: ",a+b)
            print("="*40)
            
        case '-':
            print("Substraction of",a,"&",b,"is: ",a-b)
            print("="*40)
            
        case '*':
            print("Multiplication of",a,"&",b,"is: ",a*b)
            print("="*40)
            
        case '/':
            if(b==0):
                print("cannot be divided by ZERO (0)")
                print("="*40)
                
            else:
                print("Division of",a,"&",b,"is: ",a/b)
                print("="*40)
                
        case 'quit':
            print("Good bye!")
            print("="*40)
            break
        case _:
            print("Please enter valid operation")
        
        