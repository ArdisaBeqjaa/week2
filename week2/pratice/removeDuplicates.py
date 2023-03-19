def fucntion(arr):
    arr2=[]
    for i in range(len(arr)):
        if(arr[i] not in arr2):
            arr2.append(arr[i])
        else:
            continue
    return arr2

arr=[1,2,3,2,4,4]
arr3=list(arr)

# print(fucntion(arr))
print(arr3)
