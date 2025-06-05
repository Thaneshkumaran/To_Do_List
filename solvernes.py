n=4
k=2
def array(n):
    array = []
    for i in range(n):
        value=int(input("Enter value: "))
        array += [value]
    return array
def srot(a):
    for i in range (len(a)):
        for j in range (len(a)):
            if a[i]<a[j] and j!=i:
                a[i],a[j]=a[j],a[i]
    return a

def count(a,k):
    sum,count=0,0
    for i in a:
        if k==count:
            return sum
        else:
            sum +=i
            count +=1
Array=array(n)
Array=srot(Array)
print(Array)
count=count(Array,k)
print(count)