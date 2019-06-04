import csv
import sys
   
csv.field_size_limit(2147483647)

map_time = {}
i = 0
with open('3.Tcc_Time_Final.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            map_time[row[0]] = [row[1],row[2],row[3]]
        i = i + 1

map_senti = {}
i = 0
with open('4.Base_Sentimental_Class.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            map_senti[row[0]] = [row[2],row[3]]
        i = i + 1

map_emotion = {}
i = 0
with open('5.Base_Emotion.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            map_emotion[row[0]] = [row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
        i = i + 1


'''i = 0
with open('6.Tcc_Database_Final.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Final.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID", "Body", "Ticket_Id", "Duration", "Time_Classification", "Sentimental_Score","Sentimental_Classification","Anger","Antecipation","Disgust","Fear","Joy","Sadness","Surprise","Trust"]
            else:
                new_row.append(row[0])
                new_row.append(row[1])
                new_row.append(map_time[row[0]][0])
                new_row.append(map_time[row[0]][1])
                new_row.append(map_time[row[0]][2])
                new_row.append(map_senti[row[0]][0])
                new_row.append(map_senti[row[0]][1])
                new_row.append(map_emotion[row[0]][0])
                new_row.append(map_emotion[row[0]][1])
                new_row.append(map_emotion[row[0]][2])
                new_row.append(map_emotion[row[0]][3])
                new_row.append(map_emotion[row[0]][4])
                new_row.append(map_emotion[row[0]][5])
                new_row.append(map_emotion[row[0]][6])
                new_row.append(map_emotion[row[0]][7])
                print(new_row)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))    ''' 

i = 0
with open('6.Tcc_Database_Final.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Final_Small.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = ["ID", "Ticket_Id", "Time_Classification", "Sentimental_Classification","Anger","Antecipation","Disgust","Fear","Joy","Sadness","Surprise","Trust"]
            else:
                new_row.append(row[0])
                new_row.append(map_time[row[0]][0])
                new_row.append(map_time[row[0]][2])
                new_row.append(map_senti[row[0]][1])
                new_row.append(map_emotion[row[0]][0])
                new_row.append(map_emotion[row[0]][1])
                new_row.append(map_emotion[row[0]][2])
                new_row.append(map_emotion[row[0]][3])
                new_row.append(map_emotion[row[0]][4])
                new_row.append(map_emotion[row[0]][5])
                new_row.append(map_emotion[row[0]][6])
                new_row.append(map_emotion[row[0]][7])
                print(new_row)
            writer.writerow(new_row)   
            i = i + 1
            if i % 100 == 0:
                print('Already processed: ' + str(i))     
