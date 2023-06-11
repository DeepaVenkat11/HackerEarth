Test_cases=int(input())
for i in range (Test_cases):
    m,n=map(int,input().split())
    lst=[]
    for row in range(m):
        cell=input()
        count=0
        for i in cell:
            if i =='#':
                count+=1
        lst.append(count)
        num=max(lst)
    print(num)
