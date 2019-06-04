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

def work_on_exclamation(words):
    for i in range (0,len(words)):
        if words[i] == '!' and i > 0:
            words[i] = words[i-1]
    return words
i = 0
word_dict = {}
with open('dict_to_be_used.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        word_dict[row[0]] = row[1]
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

i = 0
with open('base_formatted.csv', encoding='utf-8') as csvfile:
    with open('base_sentimental.csv', 'w', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csv_result, delimiter = ',')
        for row in reader:
            new_row = []
            new_row.append(row[0])
            new_row.append(row[1])            
            if i == 0:
                new_row.append('sentimental_value')
            else:
                count = 0.0
                text = row[1]
                tokens = tokenize_and_lemmatize(text)
                tokens = work_on_exclamation(tokens)
                for token in tokens:
                    if token in word_dict:
                        count = count + float(word_dict[token])
                new_row.append(count)
            writer.writerow(new_row)
            i = i+1
            if i % 100 == 0:
                print('Already added: ' + str(i))               

