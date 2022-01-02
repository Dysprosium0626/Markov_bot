import re

text = ''

with open("Data.txt", "r", encoding='utf-8') as f:
    for line in f:
        if line == '\n' or line.startswith('Page '):
            continue
        
        text += line.rstrip() + ' '

# Filtered = filter(None, re.split("\“|\” |; |, |\? |! |\. |\.\n", text))
Filtered = filter(None, re.split("; |! |\. |\.\n", text))
sentences = list(Filtered)

dataset = {}

for sentence in sentences:
    sentence = '^ ' + sentence + ' $'
    words_list = sentence.split(' ')
    q = p = words_list[0]

    for word in words_list[1:]:
        p = q
        q = word
        # print(p, q)
        if p in dataset.keys():
            if q in dataset[p]:
                dataset[p][q] += 1
            else:
                dataset[p][q] = 1
        else:
            dataset[p] = {}
            dataset[p][q] = 1
    

print(dataset)