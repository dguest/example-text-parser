#!/usr/bin/env python3

import sys
from collections import Counter
from csv import reader

def run():
    input_name = sys.argv[1]
    csv = reader(open(input_name), skipinitialspace=True)

    # first read off the titles
    titles = next(csv)
    indices = {name:number for number, name in enumerate(titles)}

    # keep track of something (proj_by_company) in this case
    proj_by_company = Counter()

    # iterate through all the records
    for fields in csv:

        # build up a dictionary of fields
        named_fields = {titles[idx]:val for idx, val in enumerate(fields)}
        company = named_fields['Company Name']

        # The empty string us used in the CSV to represent zero.
        comp_projs_as_string = named_fields['# projects completed']
        # Unfortunately, this means that we have to manually enter
        # zero in the case of en empty string. Empty strings evaluate
        # to False.
        #
        # Note that this whole operation could be represented with some
        # more magic as:
        # > comp_projs = int(named_fields['# projects completed'] or 0)
        # but it's a bit confusing to understand why that works.
        if not comp_projs_as_string:
            comp_projs = 0
        else:
            comp_projs = int(comp_projs_as_string)

        # add to the counter
        proj_by_company[company] += comp_projs

    # Do some sorting. The sort function works on a container, which
    # we get by using `.items()` to return a list of (key, value)
    # pairs. In this case we're sorting by the second value, thus the
    # anonymous function created with `lambda`.
    sorted_companies = sorted(proj_by_company.items(),key=lambda x: x[1])
    for company, count in reversed(sorted_companies):
        if count > 0:
            print(company, count)



if __name__ == '__main__':
    run()
