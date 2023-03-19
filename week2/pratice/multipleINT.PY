# def funciton(arr):
#     name=''
#     for i in range(0,len(arr)):
#         name=''.join(arr[i])
#     return name
# arr=[1,2,3]
# print(funciton(arr))

def function(arr):
    name = ''.join(str(i) for i in arr)
    return name

arr = [1, 2, 3]
print(function(arr))
