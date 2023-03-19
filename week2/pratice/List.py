# for i in range(1,5,2):
#     print(i)

# even_nr=[2*x for x in range(1,6)]
# print(even_nr)

# Build the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]] using list comprehension 
# k=0
# arr=[[]]
# for i in range(3):
    
#     for j in range(1,4):
#         k+=1
#         arr.append(j + 1 + i * 3)
# print(arr)
        

# matrix = [[j + 1 + i * 3 for j in range(3)] for i in range(3)]
# print(matrix)

# mat=[[]]
# for i in range(3):
#     for j in range (3):
#       mat.append(j+1+i*3)
# print(mat)

# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(j + 1 + i * 3)
#     matrix.append(row)
# print(matrix)
k=0
matrix=[[j+1+i*3 for j in range(3)] for i in range(3)]
print(matrix)
