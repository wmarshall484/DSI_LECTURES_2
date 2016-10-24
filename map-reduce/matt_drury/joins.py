from mrjob.job import MRJob
from collections import defaultdict
from itertools import product
import json


def all_equal(t):
    return t.count(t[0]) == len(t)

def extend_into_from(into_dict, from_dicts, blacklist=None):
    for d in from_dicts:
        into_dict.update({key: value for key, value in d.iteritems()
                                     if key not in blacklist})
    return into_dict

class InnerJoin(MRJob):

    def mapper(self, _, line):
        jsn = json.loads(line)
        key = jsn['key']
        yield key, line

    def reducer(self, key, json_group):
        # Collect all the data together in a fixed data structure
        tables = defaultdict(list)
        table_names = set([])
        for jsn in json_group:
            jsn = json.loads(jsn)
            tables[jsn['table']].append(jsn)
            table_names.add(jsn['table'])
        # Now join the data structures in a totally inefficient way : )
        joined = []
        for rows in product(*tables.values()):
            if all_equal([row['date'] for row in rows]):
                new_row = {}
                extend_into_from(new_row, rows, blacklist=['table'])
                joined.append(new_row)
        # Now yield all the new data.
        for row in joined:
            yield (row, None) 


if __name__ == '__main__':
    InnerJoin.run()
