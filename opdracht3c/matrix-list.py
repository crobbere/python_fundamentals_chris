matrix = [[i for i in range(10)] for x in range(10)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
