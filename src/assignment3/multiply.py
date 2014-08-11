import MapReduce
import sys

"""
Matrix Multiplication Example in the Simple Python MapReduce Framework
By Yi Luo
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]
    if matrix == "a":
        for k in range(0, 5):
            mr.emit_intermediate((row, k), (matrix, col, value))
    else:
        for i in range(0, 5):
            mr.emit_intermediate((i, col), (matrix, row, value))

def reducer(key, list_of_values):
    result = 0;
    for A in list_of_values:
        if A[0] == "a":
            for B in list_of_values:
                if B[0] == "b" and B[1] == A[1]:
                    result += A[2] * B[2]
    mr.emit((key[0], key[1], result))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
