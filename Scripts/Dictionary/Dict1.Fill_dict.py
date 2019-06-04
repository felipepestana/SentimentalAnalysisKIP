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
        
nltk.download('wordnet')
i = 0
dict = {}
headers = []
seedsList = []
with open('Dict3.Seeds.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            dict[row[0]] = [row[1],0]
            seedsList.append(row)
        else:
            headers = row
            headers.append('is_seed')
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

for seed in seedsList:
	print(seed[0])
	results = extract_terms(seed[0])
	for result in results:
		if result not in dict:
			dict[result] = [seed[1],1]
	i = i + 1
	if i % 100 == 0:
		print('Already processed: ' + str(i))
		
with open('seeds_expanded.csv', 'w', newline='', encoding='utf-8') as csv_result:
	writer = csv.writer(csv_result, delimiter = ',')
	writer.writerow(headers)
	for key,val in dict.items():
		new_row = []
		new_row.append(key)
		new_row.append(val[0])
		new_row.append(val[1])
		writer.writerow(new_row)
 
