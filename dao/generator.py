#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-30 21:28
# @Author  : Dysprosium
# @File    : generator.py
from random import randint
import re


# from analysis import Analysis

class Generator:
    def __init__(self, dataset, head):
        self.dataset = dataset
        self.key_len = 2
        self.sent_head = head

    def get_next_word(self, word):
        sum_of_candidates = 0
        # number of frequencies
        # for keys in self.dataset[tuple(word)].keys():
        #     sum_of_candidates += self.dataset[tuple(word)][keys]
        sum_of_candidates = sum(self.dataset[tuple(word)].values())
        random = randint(1, sum_of_candidates)
        t = 0
        # select a number from candidates randomly
        for w in self.dataset[tuple(word)].keys():
            t += self.dataset[tuple(word)][w]
            if random <= t:
                return w

    def generate(self, word_separator, starter=['^']):
        prefix = len(starter)

        sentences = starter[:]
        while len(sentences) < self.key_len:
            r = randint(1, sum(self.sent_head.values()))
            for item in self.sent_head.items():
                if r >= item[1]:
                    r -= item[1]
                else:
                    sentences.append(item[0])
                    print(item[0])
                    break

        while True:
            end = sentences[-self.key_len:]
            next_word = self.get_next_word(end)
            if next_word == '$':
                break
            else:
                sentences.append(next_word)

        print("======")

        while prefix > 0:
            prefix -= 1
            sentences.pop(0)

        print(sentences)

        return word_separator.join(sentences), sentences[-self.key_len:]


if __name__ == '__main__':
    txt = input("Please enter the text file to be analyzed:")
    analysis = Analysis(txt)
    sentences = analysis.split_text_into_sentences()
    dataset, head = analysis.prepare_dataset(sentences)
    g = Generator(dataset, head)
    number = 1
    result = ''
    starter = ['^']
    for i in range(0, number):
        next, starter = g.generate(' ', starter)
        result += next + ', ' if i != number else '. '

    print(result)

