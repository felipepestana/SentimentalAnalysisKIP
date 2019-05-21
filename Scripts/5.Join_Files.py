import csv

csv.field_size_limit(2147483647)

def remove_special_char(body):
    return re.sub(r'[^.,!?-a-zA-Z0-9 \n\.]', '', body)

with open('Tcc_Translate.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
    headers = ['ID','body_translated']
    writer.writerow(headers)
    for i in range(1,9):
        csv_source = open('Tcc_Split' + str(i) + '.csv', encoding='utf-8')
        reader = csv.reader(csv_source, delimiter=',',quotechar='"',skipinitialspace=True)
        count = 1
        for row in reader:
			text = remove_special_char(row[2])
            new_row = [row[0], text]            
            if count % 100 :
                print('Already processed: ' + str(count) + ' files')
            writer.writerow(new_row)


