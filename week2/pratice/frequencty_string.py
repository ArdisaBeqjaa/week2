# def function():
#     name='ardisa'
#     for i in range(len(name)-1):
#         cnt=0
#         for j in range(i,len(name)):
#            if(name[i]==name[j]):cnt=cnt+1
#            print({name[i],cnt})
           
# function()

def funciton(str1):
    dictt={}
    for i in str1:
        if i in dictt:dictt[i]+=1
        else:dictt[i]=1
     
    for j in dictt:
        print(f'{j},{dictt[j]}')
        
funciton('ardisa')