n = int(input("Enter the number whome you want to find:-"))
sum=0
for i in range (1,n+1):
    sum=sum+1
    print ("\nSum=",sum)


string=input("Please enter your own string:-")
string2=('')
for i in string:
    string2=i+string2
    print ("\n Original string",string)
    print ("\n Reversed string",string2)

c=int(input("Enter your number:-"))
for i in range(c,0,-1):
    print(i)