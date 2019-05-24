import csv
import re  

i = 0
word_dict = {}
headers = ['token','value']
with open('dict.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            text = row[0].strip()
            if ' ' in row[0]: #join expressions 
                text = text.replace(' ','_')                
            if '_' in text: #remove classification from expressions
                text = re.sub(r'#.{1}','',text)
            if text in word_dict: #combine if two expressions have different values
                mean = float(word_dict[text]) + float(row[3])   
                word_dict[text] = mean/2
            else:
                word_dict[text] = row[3]
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

i = 0
with open('dict_to_be_used.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',')
    writer.writerow(headers)
    for key,val in word_dict.items():
        new_row = []
        new_row.append(key)
        new_row.append(val)
        writer.writerow(new_row)
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))