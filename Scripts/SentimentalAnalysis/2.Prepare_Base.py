import csv
      

i = 0
word_dict = {}
headers = ['ID','message']
with open('dict_to_be_used.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        word_dict[row[0]] = row[1]
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))
    
i = 0
with open('translated.csv', encoding='utf-8') as csvfile:
    with open('base_formatted.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csv_result, delimiter = ',')
        for row in reader:
            if i == 0:
                writer.writerow(headers)
                i = i+1
                continue
            new_row = []
            text = row[1]
            for key in word_dict:
                if key.replace('_',' ') in text:
                    text = text.replace(key.replace('_',' '), key)
            new_row.append(row[0])
            new_row.append(text.lower())
            writer.writerow(new_row)
            i = i+1
            if i % 100 == 0:
                print('Already added: ' + str(i))               


