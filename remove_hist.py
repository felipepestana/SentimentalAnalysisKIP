import csv
import sys
import re

def removeHist(body):
    lines = body.splitlines()
    result = ""
    for line in lines:
        if not(line.startswith('>')):
            result = result + line.strip() + '\n'
        elif line.startswith('--'):
            print('1232')
            return result
    return result    
csv.field_size_limit(2147483647)
i = 0
with open('TCC_base.csv', encoding='utf-8') as csvfile:
    with open('Tcc_history.csv', 'a', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = row
            else:
                result = removeHist(row[1])
                new_row.append(row[0])
                new_row.append(result.strip())
            writer.writerow(new_row)   
            i = i + 1
            if i == 100:
                print('Already processed: ' + str(i))     
