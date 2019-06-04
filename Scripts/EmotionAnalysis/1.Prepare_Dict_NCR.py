import csv
import re  

i = 0
count = 0
word_dict = {}
ncr_dict = {}
headers = ['token','anger','anticipation', 'disgust', 'fear', 'joy','sadness', 'surprise', 'trust']

with open('dict_ncr.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        text = row[0].strip()
        if count == 0:
            ncr_dict[text] = {}
        ncr_dict[text][row[1].strip()] = row[2].strip()
        i = i + 1
        count = count + 1
        if count == 10:
            count = 0
    print('Total of seeds added to dict: ' + str(i))

i = 0
with open('ncr_dict_formatted.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',')
    writer.writerow(headers)
    for key,val in ncr_dict.items():
        new_row = [key, val['anger'], val['anticipation'], val['disgust'], val['fear'], val['joy'], val['sadness'], val['surprise'], val['trust']]
        writer.writerow(new_row)
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))