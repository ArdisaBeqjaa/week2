# we can simulate a main function
# ?__name__ the main function in this fin __main__
# if __name__ == "__main__"

# in python we have s[0] in java s.charAt(0)
# escaped = 'O\'Reilly'
# r_str = r'O\'Reilly'
# # raw strign e printon bashk me \
# print(escaped, r_str)




def is_exx(name):
    # for(int =len-1;i=>0;i--)
    
    len_str = len(name) - 1
    string_builder = []
    for i in range(len_str, -1, -1):
        string_builder.append(name[i])
    
    reversed_str = ''.join(string_builder)
    if(reversed_str==name): return True
    return False

   

print(is_exx("ardisa"))
print(is_exx('sos'))

# def is_palandrome(string):
#     i,j=0,len(string)-1
    
# LSISTSS
# list() it is calling a class
# list[] language constract
# list is dynamminc

ls = ['Hello', 'World', 1, 2]
ls.append(3)
ls.insert(0, lambda b, ex: b ** ex)
print(ls)

# tek e para, do jet referenca

# one line funciton ->annoymus fucntion no nca fucntioin
# lambda a:2*a
# slicing kerkon 3 arg
# range step->(s,e,step)

# empty list,for loop,pastaj append
# list comprehensions,shorter
# even_nums = [2*x for x in range(1, 6)]

# nesed list comprehention
# i=1
# matrix = [[(i+j) for j in range(3)] for i in range(3)]
# print(matrix)

# def get_mat(n):
#     return [[n*i+j for j in range(1,n+1)]for i in range(n)]

# matrix=get_mat(3)
# print(matrix)

# tuples
# a=(1,2,3)
# nk i bjem dot append,remove,ose change 
# jan t nevojshme per stuctures 
# nk e deklaron vec me 1 elemnet
# len() in oop
# b=(1,)
# print(b)

# dictronaries
# they keep key-value paris,VALUES CAN BE ANYTHING,they can be even a dictionaries,but list are not,unhashable
# hashable,-> give me smth, it will truen smth unique
# immuatble are keys, if it meatuable then we chage the meaing of it,(the key will change)->it should be unique
# (p:v)
# we dont have to iterate,we go directly to the key
# in an array we have to travares an array

a={
    'id':1,
    
}
# or hashmap
# iterate through the dictroinareis
a['id']
# 1's way
if 'id' in a:
    a[id]
    # ture ose false
# a['daga']-> del error

# 2'nd way
a.get('id')
# nqs nk e gjen do japi None eshte NULL
a.keys()
# an array of keys
a.values()
# an array of values
a.items()
# it will return a key-value pairs,do e kthej si tuple
# (k,v)
# remove a key from the dictrionary a.pop('id')

for key in a.keys():
    print(key)

    
arr=[1,1,2,2,3]
cnt=0
for i in range(len(arr)):
    if(i==i+1):
        cnt=cnt+1
        print(i)