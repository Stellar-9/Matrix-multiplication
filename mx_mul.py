class Matrix:

    def __init__(self):
        matrix = []

    @staticmethod
    def create_matrix():
        matrix = []
        # loop for exception in case of wrong user input
        while True:
            try:
                height = int(input("Height: "))
                width = int(input("Width: "))
                break
            except ValueError:
                print("Please insert a number")

        # loop for input values from user for matrix
        for i in range(height):
            height = []
            for j in range(width):
                while True:
                    try:
                        height.append(int(input("Insert value: ")))
                        break
                    except ValueError:
                        print("Please insert a number")
            matrix.append(height)  # creating matrix with values from user input
        return matrix

    def multiplication(self, *args):

        result_matrix = []
        # matrix multiplication
        for i in range(len(matrix_a)):
            temp_result = []
            for j in range(len(matrix_b[0])):
                sum_matrices = 0
                for k in range(len(matrix_b)):
                    sum_matrices += (matrix_a[i][k] * matrix_b[k][j])

                temp_result.append(sum_matrices)
            result_matrix.append(temp_result)
        return result_matrix


print("Matrix A")
matrix_a = Matrix()
matrix_a = matrix_a.create_matrix()

print("Matrix B")
matrix_b = Matrix()
matrix_b = matrix_b.create_matrix()
# print created matrix_b to output
print("Matrix A values")
for a in matrix_a:
    print(a)

# print created matrix_a to output
print("Matrix B values")
for b in matrix_b:
    print(b)

# printing result
if len(matrix_a[0]) == len(matrix_b):
    result = Matrix.multiplication(matrix_a, matrix_b)
    print("Result")
    for r in result:
        print(r)
else:
    print("Cannot execute multiplication.\nWidth of first matrix have to be same as height of second matrix")
