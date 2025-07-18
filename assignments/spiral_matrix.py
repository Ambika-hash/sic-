def print_spiral(m, n):
    matrix = [[(i * n + j + 1) for j in range(n)] for i in range(m)]
    print("Original Matrix:")
    for row in matrix:
        print(row)

    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    print("\nSpiral Order:")
    while top <= bottom and left <= right:
        for i in range(left, right + 1):  # Left to Right
            print(matrix[top][i], end=" ")
        top += 1

        for i in range(top, bottom + 1):  # Top to Bottom
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):  # Right to Left
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):  # Bottom to Top
                print(matrix[i][left], end=" ")
            left += 1

print_spiral(4, 4)
