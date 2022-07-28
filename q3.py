def yaksoogasoo(a):
    count=0
    for x in range(1,a+1):
        if a%x==0:
            count+=1
    return count

def lefthook(a,b):
    sumn=0
    for x in range(a,b+1):
        if yaksoogasoo(x)%2==0:
            sumn+=x
        else:
            sumn-=x
    return sumn

left=int(input("입력1"))
right=int(input("입력2"))
print(lefthook(left,right))