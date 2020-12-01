product=lambda x,y:x*y
print(product(2,3))

#fibonacci series

def fibonacci(count):
    fib_list=[0,1]
    any(map(lambda _:  fib_list.append(sum(fib_list[-2:])),range(2,count)))
    return fib_list[:count]
print(fibonacci(10))

#multiply each number of given list with a given number

nums=[2,4,6,9,11]
n=2
print("orginal list: ",nums)
print("given number: ",n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("result:")
print(' '.join(map(str,filtered_numbers)))

#divisible by 9

my_list=[9,18,27,99,999,23,50,45]
result=list(filter(lambda x: (x%9==0),my_list))
print("Number divisible by 9 are",result)

#count the even numbers in a given list

list1=[13,10,8,6,33,87,3,516,44]
even_count,odd_count=0,0
num = 0
while(num<len(list1)):

    if list1[num]%2==0:
        even_count +=1
    else:
        odd_count +=1
    num +=1
print("even number in the list: ",even_count)
