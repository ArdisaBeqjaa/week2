arr=[1,1,2,2,3]
cnt=0
arr2=[]
for i in range(0,len(arr)):
    j=i
    
    if(arr[i]==arr[i+1]):
        cnt=cnt+1
        arr2[i]=cnt
        print({j},{arr[i]})
    else:
        continue
    

    
    
    
 