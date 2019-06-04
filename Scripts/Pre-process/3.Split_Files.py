import csv

csv.field_size_limit(2147483647)
i = 0
count = 1
with open('3.Tcc_Clear.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',quotechar='"',skipinitialspace=True)
    csv_result = open('Tcc_Split' + str(count) + '.csv', 'w', newline='', encoding='utf-8')   
    writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
    headers = []
    for row in reader:
        if i == 100000:
            print('Already processed: ' + str(count) + ' files')
            count = count + 1
            csv_result = open('Tcc_Split' + str(count) + '.csv', 'w', newline='', encoding='utf-8')   
            writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
            writer.writerow(headers)
            i = 0
        if i == 0 and count == 1:
            headers = row[:]
        writer.writerow(row)
        i = i + 1

