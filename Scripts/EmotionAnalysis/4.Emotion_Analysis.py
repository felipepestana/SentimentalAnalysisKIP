import csv
import nltk
from nltk.stem import WordNetLemmatizer 

def get_wordnet_pos(word):
    tag = word[1]
    if tag.startswith('J'):
        return 'a'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('R'):
        return 'r'
    else:
        return 'n'

def tokenize_and_lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.pos_tag(nltk.word_tokenize(text))
    lemmas = []
    for word in words:
        tag = get_wordnet_pos(word)
        lemma = lemmatizer.lemmatize(word[0], pos = tag)
        if word[1] != '.' and '_' not in word[0]:
            lemma = lemma + '#' + tag
        lemmas.append(lemma)
    return lemmas

ncr_dict = {}
i = 0
with open('emotion_dict_to_be_used.csv', encoding='utf-8') as csvfile:
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


headers = ['ID','body','anger','anticipation', 'disgust', 'fear', 'joy','sadness', 'surprise', 'trust']
i = 0
with open('base_formatted.csv', encoding='utf-8') as csvfile:
    with open('base_emotion.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csv_result, delimiter = ',')
        for row in reader:
            new_row = []
            if i == 0:
                new_row = headers 
            else:
                new_row.append(row[0])
                new_row.append(row[1])
                text = row[1]
                tokens = tokenize_and_lemmatize(text)
                values = [0,0,0,0,0,0,0,0]
                for token in tokens:
                    if token in ncr_dict:
                        for count in range(0,8):
                            values[count] = values[count] or ncr_dict[token][count]
                for count in range(0,len(values)):
                    new_row.append(int(values[count]))
            writer.writerow(new_row)
            i = i+1
            if i % 100 == 0:
                print('Already added: ' + str(i))               

