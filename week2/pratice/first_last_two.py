def function(str1):
  
   if(len(str1)<2):
    #    print('empyt string')
       name=" "
   else:
    #    me slicing 
        # name=str1[0]+str1[1]+str1[-2]+str1[-1]
          name=str1[0:2]+str1[-2:]
   return name


str2=input('enter a name:\n')
# print(len(str2))
print(function(str2))

