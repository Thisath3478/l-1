a = input("Enter a word - ")
for i in a:
    if (i=="a"):
        print("A is found")
        break
    else:
        print("A is not found") 



e = 10
while e > 0: 
    e = e - 1
    if e == 7:
            continue
    print (e)


for i in range(100):
    if i % 20 == 0:
        print ("twist")
    elif i % 15 == 0:
        pass
    elif i % 5:
        print ("fizz")
    elif i % 3:
        print ("buzz")
    else:
        print (i)