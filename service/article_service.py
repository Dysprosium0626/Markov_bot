#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-05 20:35
# @Author  : Dysprosium
# @File    : article_service.py

from dao.generator import Generator
from dao.analysis import Analysis


class ArticleService:

    def __init__(self, theme, number):
        self.theme = theme
        self.number = number

    def generate_text(self):
        """
        根据构造的TextSerive对象生成文本
        :return: 生成的文本
        """
        theme = self.theme
        number = self.number
        analysis = None
        if theme == '1':
            analysis = Analysis("./data/huozhe.txt")
        elif theme == '2':
            analysis = Analysis("./data/yueliang.txt")
        elif theme == '3':
            analysis = Analysis("./data/hp.txt")
        elif theme == '4':
            analysis = Analysis("./data/hhgttg.txt")
        elif theme == '5':
            analysis = Analysis("./data/aiwl.txt")
        elif theme == '6':
            analysis = Analysis("./data/omas.txt")
        elif theme == '7':
            analysis = Analysis("./data/sh.txt")
        sentences = analysis.split_text_into_sentences()
        dataset, head, LANG = analysis.prepare_dataset(sentences)
        # create a generator
        g = Generator(dataset, head)
        result = ""
        if theme == '1':
            starter = ['^']
            Newsent = False
            i = 0
            while i < number:
                try:
                    next, starter = g.generate('', starter = starter)
                except:
                    starter = ['^']
                    Newsent = True
                    next, starter = g.generate('', starter = starter)
                if next != '':
                    result += next + ('，' if i != number-1 else '。')
                    i += 1
                else:
                    continue
                Newsent = False

        elif theme == '2':
            starter = ['^']
            Newsent = False
            i = 0
            while i < number:
                try:
                    next, starter = g.generate('', starter = starter)
                except:
                    starter = ['^']
                    Newsent = True
                    next, starter = g.generate('', starter = starter)
                if next != '':
                    result += next + ('，' if i != number-1 else '。')
                    i += 1
                else:
                    continue
                Newsent = False

        else:
            starter = ['^']
            Newsent = False
            i = 0
            while i < number:
                try:
                    next, starter = g.generate(' ', starter = starter)
                except:
                    starter = ['^']
                    Newsent = True
                    next, starter = g.generate(' ', starter = starter)
                if next != '':
                    result += next + (', ' if i != number-1 else '. ')
                    i += 1
                else:
                    continue
                Newsent = False

        return result
