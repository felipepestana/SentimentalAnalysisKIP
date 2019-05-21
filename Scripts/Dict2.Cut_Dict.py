import csv
import nltk
from nltk.corpus import sentiwordnet as swn
import statistics

def get_single_score(term):
    term_pos = term.split('#')
    toReturn = []
    if len(term_pos) >= 2:
        synsets = list(swn.senti_synsets(term_pos[0], term_pos[1]))
    else:
        synsets = list(swn.senti_synsets(term_pos[0]))
    if len(synsets) <= 0:
        return 0
    results = synsets[0]
    print(results)
    toReturn = results.pos_score() - results.neg_score()
    return toReturn

def extract_score(rawText):
    words = rawText.split()
    total_score = 0.0
    for word in words:
        total_score += get_single_score(word)
    print(total_score)
    return total_score

def get_polarity(score):
    if score > 0.1:
        return 'positive'
    elif score < -0.1:
        return 'negative'
    else:
        return 'neutral'
        
#nltk.download()
i = 0
seed_dict = {}
final_dict = {}
headers = []
with open('seeds_expanded.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if i != 0:
            seed_dict[row[0]] = [row[1],row[2]]
        else:
            headers.append(row[0])
            headers.append(row[1])
        i = i + 1
    print('Total of seeds added to dict: ' + str(i))

list_pos = []
list_neg = []
i = 0

for seed in seed_dict:
    print(seed)
    score_result = extract_score(seed)
    polarity = get_polarity(score_result)
    print(seed_dict[seed][0])
    if polarity == seed_dict[seed][0].strip():
        final_dict[seed] = [seed_dict[seed][0], seed_dict[seed][1], score_result]
        if polarity == 'positive':
            list_pos.append(score_result)
        elif polarity == 'negative':
            list_neg.append(score_result)
    elif seed_dict[seed][1] == '0':
        seed_dict[seed].append(0)
        final_dict[seed] = [seed_dict[seed][0], seed_dict[seed][1], 0.0]
    i = i + 1
    if i % 100 == 0:
        print('Already processed: ' + str(i))

med_pos = statistics.median(list_pos)
med_neg = statistics.median(list_neg)
print(med_pos)
print(med_neg)

for seed in final_dict:
    if final_dict[seed][2] == 0:
        if final_dict[seed][1] == 'positive':
            final_dict[seed][2] = med_pos
        else:
            final_dict[seed][2] = med_neg
		
with open('seeds_cut2.csv', 'w', newline='', encoding='utf-8') as csv_result:
    writer = csv.writer(csv_result, delimiter = ',')
    writer.writerow(headers)
    for key,val in final_dict.items():
        new_row = []
        new_row.append(key)
        new_row.append(val[0])
        new_row.append(val[1])
        new_row.append(val[2])
        writer.writerow(new_row)
     