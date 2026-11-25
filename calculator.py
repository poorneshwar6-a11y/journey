
while(True):
    print("="*40)
    print("WELCOME TO BASIC CALCULATOR")
    print("="*40)
    a=int(input("Enter a number1:"))
    b=int(input("Enter a number2:"))
    print("="*40)
    c=input("enter your choice:'+' '*' '-' '/' to exit enter 'QUIT' :") 
    match c:
        case '+':
            print("Addition of",a,"&",b,"is: ",a+b)
            
        case '-':
            print("Substraction of",a,"&",b,"is: ",a-b)
            
        case '*':
            print("Multiplication of",a,"&",b,"is: ",a*b)
            5
            
        case '/':
            if(b==0):
                print("cannot be divided by ZERO (0)")
                
            else:
                print("Division of",a,"&",b,"is: ",a/b)
                
        case 'QUIT':
            print("Good bye!")
            break
        case _:
            print("invalid")
        
        