import MapReduce
import sys

"""
Relational Join Example in the Simple Python MapReduce Framework
By Yi Luo
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    identifier = record[0]
    order_id = record[1]
    records = record[2:len(record)]
    pair = [identifier, records]
    mr.emit_intermediate(order_id, pair)

def reducer(key, list_of_values):
    result = ""
    for head in list_of_values:
        if head[0] == "order":
            for tail in list_of_values:
                if tail[0] == "line_item":
                    result = [head[0], key]
                    for e in head[1]:
                        result.append(e)
                    result.append(tail[0])
                    result.append(key)
                    for e in tail[1]:
                        result.append(e)
                    mr.emit(result)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
