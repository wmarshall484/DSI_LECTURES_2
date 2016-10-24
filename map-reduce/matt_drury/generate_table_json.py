"""
Functions for generating fake json that represent rows in a relational
database.
"""
import sys
import json
import argparse
import random
import string

dtypes = ['int', 'decimal', 'char']

def random_data(dtype):
    if dtype == 'int':
        return random.randint(0, 9)
    elif dtype == 'decimal':
        return random.random()
    elif dtype == 'char':
        return random.choice(string.letters)

def random_row(table_name, key, date, fields=None):
    if fields == None:
        fields = {}
    row = {'table': table_name, 'key': key, 'date': date}
    for field_name, field_type in fields.iteritems():
        row[field_name] = random_data(field_type)
    return row

def random_rows(table_name, key, dates, fields=None):
    for date in dates:
        yield random_row(table_name, key, date, fields)

def run(table_name, key, dates, fields):
    dates = [date for date in dates.split(',')]
    for row in random_rows(table_name, key, dates, fields):
        json.dump(row, sys.stdout)
        sys.stdout.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tablename")
    parser.add_argument("key")
    parser.add_argument("dates")
    parser.add_argument("dataspec")
    args = parser.parse_args()
    run(args.tablename, args.key, args.dates, json.loads(args.dataspec))
