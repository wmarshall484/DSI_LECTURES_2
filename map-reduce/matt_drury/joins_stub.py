from mrjob.job import MRJob
import json


def all_equal(lst):
    """Are all the entries in a list equal?""" 
    return lst.count(lst[0]) == len(lst)

def extend_into_dict_from_dict(into_dict, from_dicts, blacklist=None):
    """
      Add new key, value pairs to a dictionary that are contained in any
    dictionary from a list of dictionaries.  Additonally, do not add pairs
    whose keys are in a blacklist.
    """
    if blacklist == None:
        blacklist = []
    for d in from_dicts:
        into_dict.update({key: value for key, value in d.iteritems()
                                     if key not in blacklist})
    return into_dict


class InnerJoin(MRJob):
    """Implements an inner join on a collection of tables.

    Each table row should be represented as a json object.  For convenience,
    each table should have a "table" attribute identifying the table, and a
    "date" attribute, which will be used as the join key.
    """
    def mapper(self, _, line):
        pass

    def reducer(self, key, json_group):
        pass


if __name__ == '__main__':
    InnerJoin.run()
