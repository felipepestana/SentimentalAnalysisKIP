import csv
import sys
   
csv.field_size_limit(2147483647)

map_ar_ti = {}
i = 0
with open('Tcc_Time_Class.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
    for row in reader:
        if i != 0:
            map_ar_ti[row[0]] = [row[1],row[2]]
        i = i + 1
i = 0
with open('Tcc_map_article_body.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Time_Final.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID", "Ticket_id", "Duration", "Classification"]
            else:
                new_row.append(row[0])
                new_row.append(row[1])
                if row[1] in map_ar_ti:
                    time = map_ar_ti[row[1]]
                else:
                    time = [129600.0, 'regular']
                new_row.append(time[0])
                new_row.append(time[1])
                print(new_row)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))     
