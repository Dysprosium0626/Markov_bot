#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-02 12:09
# @Author  : Dysprosium
# @File    : analysis.py

import re
import jieba


class Analysis:

    def __init__(self, string):
        self.string = string
        self.key_len = 2
        self.sentences = []

    def split_string_into_sentences(self):
        text = self.string
        Filtered = filter(None, re.split("\“|\” |; |! |\. |\n |。|；|：|: |\?|？|” ", text))
        sentences = list(Filtered)
        self.sentences = sentences
        return None

    def split_text_into_sentences(self):
        lines = []
        with open(self.string, "r", encoding='utf-8') as f:
            for line in f:
                if line == '\n' or line.startswith('Page '):
                    continue
                lines.append(line)

        text = ' '.join(lines).replace('\n', '')
        Filtered = filter(None, re.split("\“|\” |; |! |\. |\n |。|；|：|: |\? |？|” ", text))
        sentences = list(Filtered)
        self.sentences = sentences
        return None

    def prepare_dataset(self, sentences):
        dataset = {}
        sent_head = {}
        if sentences == None:
            sentences = self.sentences

        LANG = 'en'
        for _char in sentences[0]:
            if '\u4e00' <= _char <= '\u9fa5':
                LANG = 'ch'

        for sentence in sentences:
            sentence = '^ ' + sentence + ' $'
            if LANG == 'en':
                sentence.replace(',', '')
                sentence.replace('，', '')
                words_list = sentence.split(' ')
            else:
                words_list = list(jieba.cut(sentence))
                if words_list[-2] == ' ':
                    words_list.pop(-2)
                if words_list[1] == ' ':
                    words_list.pop(1)

            keys = words_list[:self.key_len]
            # print(words_list)
            # print('\n')

            if keys[1] == ' ':
                continue
            elif keys[1] in sent_head.keys():
                sent_head[keys[1]] += 1
            else:
                sent_head[keys[1]] = 1

            symbols = [',', ', ', '.', '. ', '，', '， ', '。 ', '。']
            for word in words_list[self.key_len:]:
                # print(p, q)
                if word in symbols:
                    continue

                if tuple(keys) in dataset.keys():
                    if word in dataset[tuple(keys)]:
                        dataset[tuple(keys)][word] += 1
                    else:
                        dataset[tuple(keys)][word] = 1
                else:
                    dataset[tuple(keys)] = {}
                    dataset[tuple(keys)][word] = 1
                keys.pop(0)
                keys.append(word)
        return dataset, sent_head, LANG


if __name__ == '__main__':
    # txt = input("Please enter the text file to be analyzed:")
    txt = './data/hp.txt'
    analysis = Analysis(txt)
    sentences = analysis.split_text_into_sentences()
    dataset, head, lang = analysis.prepare_dataset(sentences)

    for i in head.items():
        print(i)
        break