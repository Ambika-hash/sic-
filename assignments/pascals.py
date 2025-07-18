def pascals_triangle(n):
    triangle = []
    for row_num in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)])
            row.append(1) 
        triangle.append(row)
    for row in triangle:
        print(" " * (n - len(row)), *row)
n = int(input("Enter the N value: "))
pascals_triangle(n)
