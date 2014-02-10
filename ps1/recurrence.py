l = map(int, raw_input().split())
K = l[0]
N = l[1]

a_s = map(int, raw_input().split())
c_s = map(int, raw_input().split())

def identity(size):
    matrix = [[0]*size for i in xrange(size)] 
    for i in xrange(size):
        matrix[i][i] = 1
    return matrix

# first n-1 rows of size n identity matrix
def bottomRows(size):
    return identity(size)[:-1]

matrix = [c_s] + bottomRows(len(c_s))

def matrix_multiply_mod1000(x, y):
    def num_rows(m): return len(m)
    def num_cols(m): return len(m[0])
    # calculate what the value for a_th row and b_th column should be,
    # given the two matrices x and y
    def calculate_point(a, b, x, y):
        acc = 0
        for i in xrange(num_cols(x)):
            acc = (acc + x[a][i] * y[i][b]) % 1000
        return acc
    # calculates the product of matrices x and y, row by row
    def build_matrix(x,y):
        output = []
        for i in xrange(num_rows(x)):
            row = []
            for j in xrange(num_cols(y)):
                row.append(calculate_point(i,j,x,y))
            output.append(row)
        return output
    return build_matrix(x,y)

def square_mod1000(matrix):
	return matrix_multiply_mod1000(matrix, matrix)

def exponentiation(matrix, exponent):
	if exponent == 0:
		size = len(matrix)
		return identity(size)
	if exponent == 1:
		return matrix
	elif exponent % 2 == 0:
		return exponentiation(square_mod1000(matrix), exponent / 2)
	else:
		return matrix_multiply_mod1000(matrix, exponentiation(matrix, exponent-1))

# e.g. [1,2,3] to [[3], [2], [1]]
def flip(lst):
	return [[i] for i in list(reversed(lst))]

final_matrix = exponentiation(matrix, N)
final_vector = matrix_multiply_mod1000(final_matrix, flip(a_s))
print final_vector[-1][0]