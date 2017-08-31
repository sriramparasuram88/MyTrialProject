print("hello")

#tempVariable = input("enter your input string variable")

#print(tempVariable)

#i=0

def recursive(n):

    if(n==0):
        return 1

    else:

        i = n*recursive(n-1)
        print("i is ", i)


    return i

#var = int(input("enter an input integer variable whose factorial you want"))


#print("the factorial of ",var,"is",recursive(var))


def fibonacciSeries(n):

    a = 0
    b = 1
    c = a + b
    print(a)
    print(b)
    print(c)
    while(c<=n):
        a=b
        b=c
        c=a+b
        print(c)
        continue


#print(fibonacciSeries(20))




string = "abcdef"


length = len(string)
while(length>=0):
    print(string[length-1])
    length = length-1



prefixes = "JKLMNOPQ"

suffix = "ack"

for char in prefixes:

    if(char == 'Q'):
        print(char+"uack")

    else:
        print(char+suffix)

