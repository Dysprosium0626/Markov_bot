#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-30 21:28
# @Author  : Dysprosium
# @File    : generator.py
from random import randint
import re

class Generator:
    def __init__(self, dataset):
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
            next_word = self.get_next_word(self.dataset, end)
            sentences.append(next_word)
        return word_separator.join(sentences[1:-1])

