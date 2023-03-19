def function(str1):
   if len(str1)>2:
       if str1[-3:]=='ing':
           str1+='ly'
       else:
           str1+='ing'
   else:
       str1=str1
   return str1
print(function('abc'))
print(function('string'))