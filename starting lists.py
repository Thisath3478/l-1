a=[]
print(a)
b=[1,2,3,4,5]
print(b)
c=[1,2,88]*2
print(c)
d=[12,17,91]
d=d[::-1]
print(d)

def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
            print(lst)
            return ctr
        count=match_words(['abc','daf','for','2025'])
    print("Number of numbers and words having same first and last character are:",count)



l=[2,75,84,74]
print("Original list is:",l)
count=0
for i in l:
    count+=i
    print(count)
    print(len(l))