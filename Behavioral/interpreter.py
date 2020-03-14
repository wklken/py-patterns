#!/usr/bin/env python
# encoding: utf-8
"""
解释器模式

给定一个语言, 定义他的文法的一种表示, 并定义一个解释器, 这个解释器使用该表示来解释语言中的句子

- 解决: 如果一种特定类型问题发生的频率足够高, 那么可能就值得将该问题的各个实例表述为一个简单语言中的句子,
        这样就可以构建一个解释器, 该解释其通过解释这些句子来解决该问题

- 适用: 当有一个语言需要解释执行, 并且你可以将该语言中的句子表示为一个抽象语法树时
- 好处: 容易改变和扩展文法
- 不足: 需要为文法中的每一条规则至少定义一个类, 可能难以维护和管理
"""

from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):
    """
    抽象表达式, 声明一个抽象的解释操作

    这个接口被抽象语法书中的所有节点所共享
    """

    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):
    """
    终结符表达式

    实现与文法中的终结符相关联的解释操作
    """

    def interpret(self, context):
        print("terminal")


class NoterminalExpression(AbstractExpression):
    """
    非终结符表达式

    为文法中的非终结符实现解释操作, 对文法中每一条规则R1/R2...Rn都需要一个具体的非终结符表达式
    """

    def interpret(self, context):
        print("no terminal")


class Context(object):
    """
    包含解释器之外的一些全局信息
    """

    def __init__(self, input, output):
        self.__input = input
        self.__output = output

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        self.__input = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value


if __name__ == '__main__':
    context = Context("in", "out")

    l = []
    l.append(TerminalExpression())
    l.append(TerminalExpression())
    l.append(NoterminalExpression())

    for i in l:
        i.interpret(context)
