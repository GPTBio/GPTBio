#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/6/22 11:00 上午
@Author  : george ant
@File    : environment.py
"""
import asyncio
import random
from deap import tools
from typing import Iterable

from pydantic import BaseModel, Field 

from abc import ABC, abstractmethod


class Lexobe:
    """
    词汇个体,包含基因
    """
    def __init__(self, gene, env, maxtokens):
        self.genes = gene
        self.env = env
        self.fitness = 0  # 适应度,初始值为0
        self.life = True  # 是否存活

    def mutate(self):
        """
        变异
        """
        pass

    def crossover(self, lexobe, target):
        """
        杂交
        """
        pass

    def answer_question(self, question):
        """
        回答问题
        """
        pass



class Environment(BaseModel):
    """
    环境，包含种群、问题集合，评估器，评估结果
    
    """

    generation: int = Field(default=0)
    population: list[str, Lexobe] = Field(default_factory=list)
    questions: list[str] = Field(default_factory=list)
    evaluator: str = Field(default_factory=str)  # 
    target: str = Field(default_factory=str)
    retain_rate: float = Field(default=0.2)  # 保留率
    mutate_rate: float = Field(default=0.1)  # 种群个体变异率
    pop_size: int = Field(default=100)  # 种群大小

    class Config:
        arbitrary_types_allowed = True


    def create_population(self, pop_size):
        """
        创建初始种群,包含多个词汇个体
        可以从文件中提取创世基因，也可以随机生成
        """
        pass
        
    def evolve(self, target, pop_size, max_generation):
        """
        进化过程
        """
        self.population = self.create_population(pop_size, target)
        while self.generation < max_generation:
            self.next_generation()
            self.generation += 1

    def eval_fitness(self, lexobe):
        """
        评估适应度,对lexobe来评估适应度。
        包含：评估数据集
        """
        for question in self.questions:
            answer = lexobe.answer_question(question['question'])
            lexobe.fitness += self.eval_answer(answer, question)

    async def eval_answer(self, answer, question):
        """
        评估回答, 采用LLM对回答进行评估，返回分数
        """
        pass

    async def evaluate(self):
        """
        评估种群中的个体
        """
        for lexobe in self.population:
            if lexobe.live:  # 存活的个体
                self.eval_fitness(lexobe)

    async def next_generation(self):
        """
        生成下一代
        """
        retain_lexobes = self.select(self.population, self.retain_rate) # 选择保留的个体
        num_child = self.pop_size - len(retain_lexobes) # 需要繁殖的个体数量
        new_lexobes = self.reproduce(num_child) # 繁殖
        self.population = retain_lexobes + new_lexobes # 新一代的种群
        self.mutate(self.population, self.mutate_rate) # 变异
        pass

    async def mutate(self, pop, mutate_rate):
        """
        变异
        """
        for lexobe in random.sample(pop, int(len(pop)*mutate_rate)):  # 随机选取变异的个体
            lexobe.mutate()


    def select(self, pop, retain_rate):
        """
        选择保留的个体，可以根据适应度来选择
        param:
            pop:种群 
            retain_rate:保留率
        """
        live_lexobes = [lexobe for lexobe in pop if lexobe.life] # 存活的个体
        live_lexobes.sort(key=lambda x: x.fitness, reverse=True) 
        selectsize = int(len(self.population) * retain_rate)
        if len(live_lexobes) > selectsize:
            return live_lexobes[:selectsize] # 保留适应度高的个体
        else:
            return live_lexobes

    async def reproduce(self, num_child):
        """
        繁殖, 从种群中选择两个个体进行杂交，生成新的个体
        """
        new_lexobes = []
        for i in range(num_child):
            c1, c2 = tools.selRoulette(self.population, 2, lambda p: p.fitness) 
            child = c1.crossover(c2, self.target)
            new_lexobes.append(child)
        return new_lexobes
