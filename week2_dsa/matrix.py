rows = int(input("No. of rows: "))
column = int(input("No. of columns: "))
input_matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
i = rows - 1
j = column - 1
while i >= 0:
    print(input_matrix[i][j])
    i -= 1