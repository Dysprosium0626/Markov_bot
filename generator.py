#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-30 21:28
# @Author  : Dysprosium
# @File    : generator.py
from random import randint
import re

class Generator:
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset

    def get_next_word(self, dataset, word):
        sum_of_candidates = 0
        # number of frequencies
        for keys in dataset[word[-1]].keys():
            sum_of_candidates += dataset[word[-1]][keys]
        random = randint(1, sum_of_candidates)
        t = 0
        # select a number from candidates randomly
        for w in dataset[word[-1]].keys():
            t += dataset[word[-1]][w]
            if random <= t:
                return w

    def generate(self, word_separator):
        sentences = ['^']
        end_sign = ['$']
        while True:
            end = sentences[-1:]
            if end == end_sign:
                break
            next_word = self.get_next_word(dataset, end)
            sentences.append(next_word)
        return word_separator.join(sentences[1:][:-1])


if __name__ == '__main__':

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

    # create a generator
    name = input('plz enter the name:')
    g = Generator(name, dataset)
    # the first letter of the text must be '^'
    result = g.generate(' ')
    print(result)