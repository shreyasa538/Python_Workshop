def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    print("\nThe matrix is:")
    for row in matrix:
        print(row)

def transpose_matrix(matrix):
    print("\nTranspose matrix is given as:\n")
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=' ')
        print()

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][n - i - 1]
        total += matrix[i][i]
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    return total

def main():
    x = int(input("Enter number of rows: "))
    y = int(input("Enter number of columns: "))

    if x != y:
        print("Diagonal sum is only defined for square matrices.")
        return

    matrix = input_matrix(x, y)
    print_matrix(matrix)
    transpose_matrix(matrix)
    print("\nSum of diagonal elements is given as:\n")
    print(diagonal_sum(matrix))

if __name__ == "__main__":
    main()
