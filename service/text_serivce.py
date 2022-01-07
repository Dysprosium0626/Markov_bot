#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-05 20:41
# @Author  : Dysprosium
# @File    : text_serivce.py


from dao.generator import Generator
from dao.analysis import Analysis


class TextService:
    def __init__(self, number):
        self.number = number

    def generate_text(self, text):
        """
        根据上传的文件解析后生成文本
        :param text: 上传的文本
        :return: 生成的文本
        """
        number = self.number
        analysis = Analysis(text)
        sentences = analysis.split_string_into_sentences()
        dataset, head, LANG = analysis.prepare_dataset(sentences)
        # create a generator
        g = Generator(dataset, head)
        result = ""
        if LANG == 'ch':
            starter = ['^']
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
        else:
            starter = ['^']
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
        return result
