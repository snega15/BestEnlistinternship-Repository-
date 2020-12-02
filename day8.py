print("Types of errors")

print("1.Index error")
arr=[11,25,35]
try:
    print(arr[35])
except IndexError:
    print("index not found in array")

print("2.key error")
dicti={"1" : 1,"2" : 2,"3" : 3}
try:
    print(dicti["4"])
except KeyError:
    print("key not found in dictionary")
    
print("3.Module Not Found Error")
try:
    import numpy
except ModuleNotFoundError:
    print("Module not found")


print("4.ZeroDivisionError")
try:
    print(1/0)
except ZeroDivisionError:
    print("unable to divide by zero")
    
     #TRY BLOCK RAISES A NAME ERROR

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

#WHEN TRY EXCEPT NOT REQUIRED
   # it is used to catch and handle exceptions.when we speed down python it not required
   
#CALCULATOR USING TRY AND EXCEPT

loop = 1
choice = 0
while loop==1:
    print("welcome to calculator.py")
    print( "your options are:")
    print( "")
    print( "1)Addition")
    print( "2)Subtraction")
    print( "3)Multiplication")
    print( "4)Division")
    print( "5)Quit calculator.py")
    choice=input("choose your option: ")
    try:
        if choice==1:
            add1=input("add this: ")
            add2=input("to this: ")
            print( add1,"+",add2,"=",add1+add2)
        elif choice==2:
            sub1=input("subtract this: ")
            sub2=input("from this: ")
            print( sub1, "-",sub2,"=",sub1-sub2)
        elif choice==3:
            mul1=input("multiply this: ")
            mul2=input("with this: ")
            print( mul1,"x",mul2,"=",mul1*mul2)
        elif choice==4:
            div1=input("divide this: ")
            div2=input("by this: ")
            if div2==0:
                print( "Error! Cannot divide by zero! youwill destroy the universe! ;)")
            else:
                print( div1,"/",div2,"=",div1/div2)
        elif chice==5:
            loop=0
        else:
            print( "%d is not valid input. please enter 1,2,3,4 or 5."% choice)
    except ValueError:
        print( "%r is not valid input. Please enter 1,2,3,4 or 5."% choice)
    print( "Thamk you for using calculator.py!" )

    #TRY GETTING INPUT INSIDE CATCH BLOCK

Scanner in = new Scanner(System.in);
int userIn= -1;
try {
    useIn=in.nextInt();
}
catch (InputMismatchException a) {
    system.out.print("problem");
}
switch(userIn){
case -1:
   break;
    

    








    
                       
    
