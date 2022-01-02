#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-02 12:09
# @Author  : Dysprosium
# @File    : analysis.py

import re


class Analysis:

    def __init__(self, txt):
        self.txt = txt

    def split_text_into_sentences(self):
        text = ''
        with open(self.txt, "r", encoding='utf-8') as f:
            for line in f:
                if line == '\n' or line.startswith('Page '):
                    continue

                text += line.rstrip() + ' '

        # Filtered = filter(None, re.split("\“|\” |; |, |\? |! |\. |\.\n", text))
        Filtered = filter(None, re.split("; |! |\. |\.\n", text))
        sentences = list(Filtered)
        return sentences

    def prepare_dataset(self, sentences):
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
        return dataset
