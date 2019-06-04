import csv
import sys
from datetime import datetime

def calculate_dif(date_create, date_end):
    datetime_create = datetime.strptime(date_create, '%Y-%m-%d %H:%M:%S')
    datetime_end = datetime.strptime(date_end, '%Y-%m-%d %H:%M:%S')
    result = datetime_end - datetime_create
    return result.total_seconds()
   
csv.field_size_limit(2147483647)

i = 0
with open('TCC_Time.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Time_Class.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID","Time_Create","Time_End","Duration"]
            else:
                new_row.append(row[0])
                new_row.append(row[1])
                new_row.append(row[2])
                result = calculate_dif(row[1], row[2])
                new_row.append(result)
                print(result)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))     
