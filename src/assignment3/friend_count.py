import MapReduce
import sys

"""
Friend Count Example in the Simple Python MapReduce Framework
By Yi Luo
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    name = record[0]
    mr.emit_intermediate(name, 1)

def reducer(key, list_of_values):
    result = 0
    for c in list_of_values:
        result += c
    mr.emit((key, result))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
