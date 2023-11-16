#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
这个程序本身是一个基因，它的功能是实现基因的交叉、变异的功能
之所称为线粒体，以因为它不进行交差，并保持相对稳定的状态
@Time    : 2023/8/22 11:00 上午
@Author  : george ant
@File    : mitochondrial.py
"""

def crossover(self, talk, lexobe1, lexobe2, target):
    """
    杂交
    """
    a = """
    以\"{target}\"为目的，从以下给出的两个prompts中提取有用的信息，结合生成一段新的提示:
    1.{lexobe1.genes}
    2.{lexobe2.genes}
    """
    answer = talk(a)

def mutate(self, talk, lexobe):
    """
    变异
    目标: 提高文本的感染力。
OGP（旧基因Prompt）: "请你用富有激情的语言描述下面的内容。"
MCP（突变命令Prompt）: “请将以下内容视为原始基因，从你认为合适的角度进行突变，你可以添加新的元素，或者减少不必要的信息：”
生成NGP（新基因Prompt）:
输入给LLM：MCP + OGP = "请将以下内容视为原始基因，从你认为合适的角度进行突变，你可以添加新的元素，或者减少不必要的信息：请你用富有激情的语言描述下面的内容。"
LLM生成NGP："请使用生动、富有感染力的文字，将下述内容呈现出来，并尽量激起读者的共鸣。"
    """
    MCPMCP = """
    以\"{target}\"为目的，从以下给出的prompts中提取有用的信息，结合生成一段新的提示:
    1.{lexobe.genes}
    """
    answer = talk(a)