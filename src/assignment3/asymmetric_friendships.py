import MapReduce
import sys

"""
Asymmetric Friend Example in the Simple Python MapReduce Framework
By Yi Luo
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate((personA, personB), 1)
    mr.emit_intermediate((personB, personA), -1)

def reducer(key, list_of_values):
    summ = 0
    for v in list_of_values:
        summ += v
    if summ != 0:
        mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
