#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-30 21:24
# @Author  : Dysprosium
# @File    : main.py
import analysis
import generator

if __name__ == '__main__':
    txt = input("Please enter the text file to be analyzed:")
    analysis = analysis.Analysis(txt)
    sentences = analysis.split_text_into_sentences()
    dataset = analysis.prepare_dataset(sentences)
    # create a generator
    g = generator.Generator(dataset)
    # the first letter of the text must be '^'
    times = int(input("How many sentences do you want to generate?"))
    for i in range(0, times):
        result = g.generate(' ')
        print(result)


