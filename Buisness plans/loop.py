

num=int(input("Enter your number"))
sum=0
temp=num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num==sum:
    print (num,"is Amstrong number")
else:
    print (num,"is not Amstrong number")