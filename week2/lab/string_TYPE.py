course="Programming Language Paradigms"


# First char: P, last char: s

# print(course[3:-1])
# gramming Language Paradigm

# print(course[:-1])
# Programming Language Paradigm
# printon t gjitha nga index 0->der tek e parafundit


# print(course[course.index('Pa'):])
# Paradigms
# pas : merr t gjith element m posht


# immutabile means, we dont modify the content,it creates a new string obj, it points somewhere else

# escaped = 'O\'Reilly'
# r_str = r'O\'Reilly'
# print(escaped, r_str)


# sos
# def is_palindrome(name):
#     """
#     for 
    
#     """
    
#     for i in range (len(name)-1,0):
#         n_name="".join(name[i])
        
#     if(n_name==name):return True
#     return False
#     pass
# print(is_palindrome("sos"))


def is_exx(name):
    len_str = len(name) - 1
    string_builder = []
    for i in range(len_str, -1, -1):
        string_builder.append(name[i])
    reversed_str = ''.join(string_builder)
    if(reversed_str==name): return True
    return False


print(is_exx("ardisa"))



# def is_palindrome(s):
#     return s == s[::-1]





  