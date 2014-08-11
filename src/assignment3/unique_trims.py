import MapReduce
import sys

"""
Unique Trims Example in the Simple Python MapReduce Framework
By Yi Luo
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    dna = record[1]
    mr.emit_intermediate(dna[:-10], 1)

def reducer(key, list_of_values):
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
