N = int(input())
data = [int(x) for x in input().split()]
string=''
for x in data:
    dig=str(x%10)
    string+=dig

if(string[-1]=='0'):
    print("Yes")
else:
    print("No")