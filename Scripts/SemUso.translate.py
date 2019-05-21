import csv
from googletrans import Translator
translator = Translator()

i = 0
with open('Tcc_clear.csv', encoding='utf-8') as csvfile:
    with open('Tcc_translate.csv', 'a', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',escapechar='\\',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',')
        for row in reader:
            new_row = []
            print(row[0])
            new_row.append(row[0])
            if i == 0:
                new_row.append('article_traduzido')
            else:
                text = translator.translate(row[1], src='pt', dest='en').text
                for j in range(0,5):
                    try:
                        
                        new_row.append(text)
                        break
                    except:
                        if j == 4:
                            print('Deu erro nesse aqui' + row[0])                    
            writer.writerow(new_row)            
            i = i + 1
            if i == 100:
                print('Already processed: ' + str(i))     
