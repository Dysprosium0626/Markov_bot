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
        # with open(self.txt, "r", encoding='utf-8') as f:
        #     for line in f:
        #         if line == '\n' or line.startswith('Page '):
        #             continue
        #
        #         text += line.rstrip() + ' '

        # Filtered = filter(None, re.split("\“|\” |; |, |\? |! |\. |\.\n", text))
        Filtered = filter(None, re.split("\“|\” |; |! |\. |\n |，|。|；|, |：|: |\?|” ", text))
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
        # Filtered = filter(None, re.split("\“|\” |; |, |\? |! |\. |\.\n", text))
        # Filtered = filter(None, re.split("\“|\” |; |! |\. |，|。|；", text))
        Filtered = filter(None, re.split("\“|\” |; |! |\. |\n |，|。|；|, |：|: |\?|” ", text))
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
                words_list = sentence.split(' ')
            else:
                words_list = list(jieba.cut(sentence))

            keys = words_list[:self.key_len]

            if keys[1] in sent_head.keys():
                sent_head[keys[1]] += 1
            else:
                sent_head[keys[1]] = 1

            for word in words_list[self.key_len:]:
                # print(p, q)
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
    txt = input("Please enter the text file to be analyzed:")
    analysis = Analysis(txt)
    sentences = analysis.split_text_into_sentences()
    print(sentences)