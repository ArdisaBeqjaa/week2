# def funciton(str1):
#     alphabet='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     name=""
#     for i in range(0,len(str1)):
#         if str1[i] not in alphabet[i]:
#             name+=str1[i]
#         else:continue
#     return name
# print(funciton('AR02DIS'))

def function(str1):
    alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    name = ''
    for i in range(len(str1)):
        if str1[i] in alphabet:
            name += str1[i]
    return name

print(function('AR02DIS')) # Output: 02
