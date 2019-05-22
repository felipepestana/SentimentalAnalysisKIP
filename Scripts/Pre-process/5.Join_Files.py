import csv
import re

csv.field_size_limit(2147483647)

def remove_special_char(body):
    return re.sub(r'[^.,!?a-zA-Z0-9 \\n\.]', '', body)

def remove_double_spaces(body):
    return re.sub(' +', ' ', text).strip()

with open('Tcc_Database_Final.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
    headers = ['ID','body_translated']
    writer.writerow(headers)
    for i in range(1,10):
        csv_source = open('Tcc_Split' + str(i) + '_Translate.csv', encoding='utf-8')
        reader = csv.reader(csv_source, delimiter=',',quotechar='"',skipinitialspace=True)
        count = 0
        for row in reader:
            count = count + 1
            if count == 1:
                continue
            text = remove_special_char(row[2])
            new_row = [row[0], text]            
            if count % 100 == 0:
                print('Already processed: ' + str(count) + ' files')
            writer.writerow(new_row)
        print('Already finished file: ' + str(i))


