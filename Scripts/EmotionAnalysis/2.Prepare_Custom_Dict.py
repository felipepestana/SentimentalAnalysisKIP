import csv
import re

ncr_dict = {}
i = 0
with open('ncr_dict_formatted.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i == 0:
            i = i + 1            
            continue
        text = row[0].strip()
        ncr_dict[text] = []
        for count in range(1,len(row)):
            ncr_dict[text].append(int(row[count]))
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

i = 0
word_dict = {}
headers = ['token','anger','anticipation', 'disgust', 'fear', 'joy','sadness', 'surprise', 'trust']
with open('dict.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            text = row[0].strip()
            if ' ' in row[0]: #join expressions 
                text = text.replace(' ','_')
            if '_' in text: #remove classification from expressions
                text = re.sub(r'#.{1}','',text)      
            if text in word_dict:
                continue
            values = [0,0,0,0,0,0,0,0]
            keys = re.sub(r'#.{1}','',text).split('_')
            for key in keys:
                if key in ncr_dict:
                    for count in range(0,8):
                        values[count] = values[count] or ncr_dict[key][count]
            word_dict[text] = values
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

i = 0
with open('emotion_dict_to_be_used.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',')
    writer.writerow(headers)
    for key,val in word_dict.items():
        new_row = []
        new_row.append(key)
        for count in range(0,len(val)):
            new_row.append(int(val[count]))
        i = i + 1
        writer.writerow(new_row)
    print('Total of seeds added to dict: ' + str(i))


