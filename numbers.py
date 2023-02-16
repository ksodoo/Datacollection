import csv
import os
import json
# import matplotlib.pyplot as plt
from collections import Counter

# Example usage
statements = []
counters = []
directory = '/home/zodi/PycharmProjects/sec/sec/'
def extract_numbers(directory):
    for filename in os.listdir(directory):
        with open(directory + filename) as f:
            xrbl_json = json.load(f)
            get_income_statement(xrbl_json)
    counter = Counter(statements)
    counters.append(counter)
    # with open( '/home/zodi/PycharmProjects/sec/5c/counter_test.csv', 'w') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for key, value in counter:
    #         writer.writerow([key] + [value])

def get_income_statement(xrbl_json):

    if 'facts' in xrbl_json:
        if 'us-gaap' in xrbl_json['facts']:
#    CIK0001943320 - doesn't have us-gaap
#    CIK0001221482.json - doesn't have facts

            for usGaapItem in xrbl_json['facts']['us-gaap']:

                statements.append(usGaapItem)

extract_numbers(directory)

