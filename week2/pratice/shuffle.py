import random
def function(arr):
    arr2=[]
    lenn=len(arr)-1
    for i in range (len(arr)):
        x=random.randint(0,lenn)

        arr2.append(arr[x])
    return arr2
    
arr=[1,2,3,41,2]
print(function(arr))