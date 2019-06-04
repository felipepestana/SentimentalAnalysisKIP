import csv
import sys
from datetime import datetime

def class_dif(duration):
    hours = float(duration) // (60 * 60)
    classification = ''
    if hours < 1.5:
        classification = 'very short'
    elif hours < 16:
        classification = 'short'
    elif hours < 72:
        classification = 'regular'
    else :
        classification = 'long'
    return classification
    
csv.field_size_limit(2147483647)

i = 0
with open('Tcc_Time_Dur.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Time_Class.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID","Duration", "Classification"]
            else:
                new_row.append(row[0])
                new_row.append(row[3])
                result = class_dif(row[3])
                new_row.append(result)
                print(result)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))     
