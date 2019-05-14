import csv
import re
from bs4 import BeautifulSoup

def clearEmail(body):
    clearText = re.sub(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", '', body)
    return clearText

def clearUrl(body):
    clearText = re.sub(r'\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b', '', body)
    return clearText

def clearTel(body):
    clearText = re.sub(r'\(?\b([0-9]{2,3}|0((x|[0-9]){2,3}[0-9]{2}))\)?\s*[0-9]{4,5}[- ]*[0-9]{4}\b', '', body)
    return clearText

def strip_html(body):
    soup = BeautifulSoup(body, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(body):
    return re.sub(r'\[[^]]*\]', '', body)
    
def remove_between_tags(body):
    return re.sub(r'<[^]]*>', '', body)
    
def remove_special_char(body):
    return re.sub(r'[^.,!?-a-zA-Z0-9 \n\.]', '', body)

def remove_break_line(body):
    text = re.sub('\n',' ',body)
    return re.sub(' +', ' ', text)
    
csv.field_size_limit(2147483647)
i = 0
with open('Tcc_history.csv', encoding='utf-8') as csvfile:
    with open('Tcc_Clear.csv', 'a', newline='', encoding='utf-8') as csv_result:
        reader = csv.reader(csvfile, delimiter=',',quotechar='"',skipinitialspace=True)
        writer = csv.writer(csv_result, delimiter = ',',quotechar='"',skipinitialspace=True)
        for row in reader:
            new_row = []
            print(row[0])
            if i == 0:
                new_row = row
            else:
                result = clearEmail(row[1])
                result = clearUrl(result)
                result = clearTel(result)
                result = strip_html(result)
                result = remove_between_square_brackets(result)
                result = remove_between_tags(result)
                result = remove_break_line(result)
                new_row.append(row[0])
                new_row.append(result.strip())
            writer.writerow(new_row)   
            i = i + 1
            if i == 100:
                print('Already processed: ' + str(i))

