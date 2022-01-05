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
        dataset = analysis.prepare_dataset(sentences)
        # create a generator
        g = Generator(dataset)
        result = ""
        if theme == '1':
            for i in range(0, number):
                result += g.generate(' ') + '。'
        elif theme == '2':
            for i in range(0, number):
                result += g.generate(' ') + '。'
        else:
            for i in range(0, number):
                result += g.generate(' ') + '. '
        return result
