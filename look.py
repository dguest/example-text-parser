#!/usr/bin/env python3

import sys
from collections import Counter
from csv import reader

def run():
    input_name = sys.argv[1]
    csv = reader(open(input_name), skipinitialspace=True)
    titles = next(csv)
    indices = {name:number for number, name in enumerate(titles)}

    # iterate through
    proj_by_company = Counter()
    for fields in csv:
        named_fields = {titles[idx]:val for idx, val in enumerate(fields)}
        company = named_fields['Company Name']
        comp_projs = int(named_fields.get('# projects completed') or 0)
        proj_by_company[company] += comp_projs

    sorted_companies = sorted(proj_by_company.items(),key=lambda x: x[1])
    for company, count in reversed(sorted_companies):
        if count > 0:
            print(company, count)



if __name__ == '__main__':
    run()
