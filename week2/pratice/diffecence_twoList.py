def funciton(arr,arr1):
    arr3=[]
    for i in range(len(arr)):
        x=arr[i]-arr1[i]
        arr3.append(x)
    return arr3

arr=[12,3,2]
arr1=[1,1,1]
print(funciton(arr,arr1))
