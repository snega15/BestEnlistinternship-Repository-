test_list=[1,5,6,7,9]
res_list=[]
for i in range(0,len(test_list)):    
   res_list.append(test_list[i] +2)            
print("resultant list is :" + str(res_list))
#next program	
n=int(input('enter number :'))
for i in range(n):
    print(' '.join(map(str,range(n-i,0,-1))))

    #fibonacci sequence

nterms=int(input("how many terms? "))
n1,n2=0,1
count=0
if nterms <=0:
    print("please enter a positive integer")
elif nterms==0:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

       #armstrong number is called if it is equal to the sum of cube of its own digits
num=int(input("enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

    #multiplication table of 9
num=9
for i in range(1,11):
    print(num, 'x',i, '=',num*i)

           #negative or ;positive

num=float(input("enter a number: "))
if num>0:
    print("positive number")
else:
    print("negative number")

            #days to ages
days=5555
ages=days/365
print("number of ages is: ")
print(ages)

     #trigonometry problem using math function
import math
print(math.sin(math.pi/3))
print(math.tan(math.pi/3))
print(math.cos(math.pi/3))

         #calculator creating
print("calculator")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
ch=int(input("enter choice(1-4): "))
if ch==1:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    print("sum =",c)
elif ch==2:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a-b
    print("difference =",c)
elif ch==3:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a*b
    print("product =",c)
elif ch==4:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a/b
    print("quotient =",c)
else:
    print("invalid choice")
