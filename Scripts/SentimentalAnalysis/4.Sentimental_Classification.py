import csv
import sys
from datetime import datetime

def class_dif(points):
    classification = ''
    score = float(points)
    if score > 0:
        classification = 'positive'
    elif score < 0:
        classification = 'negative'
    else:
        classification = 'neutral'
    return classification

csv.field_size_limit(2147483647)
i = 0
with open('3.Base_Sentimental.csv', encoding='utf-8') as csvfile:
    with open('Tcc_senti_final.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID","Body", "Sentimental_Score","Classification"]
            else:
                new_row.append(row[0])
                new_row.append(row[1])
                new_row.append(row[2])
                result = class_dif(row[2])
                new_row.append(result)
                print(result)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))     
