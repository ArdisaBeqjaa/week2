# def function(str1,lenn):
#    for i in range(0,lenn-1):
#        for j in range(0,lenn):
#         if(str1[i]==str1[j]):str1[i]='$'
#         else:continue

# lenn=len('ardisa')-1
# function('ardisa',lenn)

 
def function(str2,str1):

    name =str1[0:2]+str2[-1]+" "+str2[0:2]+str1[-1]
    return name
print(function('abc','xyz'))