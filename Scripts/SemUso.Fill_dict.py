import csv
import nltk
from nltk.corpus import wordnet as wn

def get_pos(pos_text):
    if pos_text == 'a':
        return wn.ADJ
    elif pos_text == 'r':
        return wn.ADV
    elif pos_text == 'n':
        return wn.NOUN
    elif pos_text == 'v':
        return wn.VERB
    

def word_find(term):
    term_pos = term.split('#')
    toReturn = []
    results = []
    if len(term_pos) >= 2:
        results = wn.synsets(term_pos[0], pos=get_pos(term_pos[1]))
    if len(results) == 0:
        toReturn.append(term)
    for synset in results:
        for lemma in synset.lemmas():
            toReturn.append(str(lemma.name()) + '#' + term_pos[1])
    toReturn = list(dict.fromkeys(toReturn))
    return toReturn

def extract_terms(rawText):
    words = rawText.split()
    words_returned = []
    for word in words:
        words_returned.append(word_find(word)) 
    print(words_returned)
    if len(words) == 1:
         return words_returned[0]
    elif len(words) == 2:
        combined = []
        for word1 in words_returned[0]:
            for word2 in words_returned[1]:
                 combined.append(word1 + ' ' + word2)
        return combined
    elif len(words) == 3:
        combined = []
        for word in words_returned[0]:
            for word2 in words_returned[1]:
                for word3 in words_returned[2]:
                 combined.append(word + ' ' + word2 + ' ' + word3)
        return combined

        
#nltk.download()
i = 0
with open('seeds.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    with open('seeds_expanded2.csv', 'a', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csv_result, delimiter = ',')
        for row in reader:
            print(row[0])
            if i == 0:
                new_row = []
                new_row = row              
                new_row.append('is_seed')
                writer.writerow(new_row) 
            else:
                results = extract_terms(row[0])
                for result in results:
                    new_row = []
                    new_row.append(result)
                    new_row.append(row[1])                    
                    if str(row[0]) == str(result):
                        new_row.append('0')
                    else:
                        new_row.append('1')
                    print(new_row)
                    writer.writerow(new_row)   
            i = i + 1
            if i == 2:
                print('Already processed: ' + str(i))  
