string=input()
word=''
for i in string:
    if i>='a' and i<='z':
        i=i.upper()
        word+=i
    elif i>='A' and i<='Z':
        i=i.lower()
        word+=i
print(word)