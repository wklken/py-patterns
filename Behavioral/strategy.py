#!/usr/bin/env python
# encoding: utf-8
"""
策略模式

它定义了算法家族, 分别封装起来, 让他们之间可以互相替换, 此模式让算法的变化, 不会影响到使用算法的客户

- 策略模式是一种定义一系列算法的方法, 从概念上来讲, 所有算法完成的都是相同的工作, 只是实现不同,
  它可以以相同的方式调用所有的算法, 减少各种算法与算法类之间的耦合
- 策略模式的Strategy类层次位Context定义了一系列的可供重用的算法或行为, 继承有助于析取出这些算法中的公用功能
- 优点: 简化了单元测试, 每个算法有自己的类, 可以通过自己的接口单独测试
- 解决: 不同行为堆砌在同一个类中, 很难避免使用条件语句, 通过Strategy消除之
- 作用: 封装算法/业务规则等
"""

from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    """
    策略类, 定义所有支持的算法的公共接口
    """

    @abstractmethod
    def calculate(self):
        pass


class StrategyA(Strategy):
    """
    具体策略类, 封装了具体的算法和行为
    """

    def calculate(self):
        print("calculate A")


class StrategyB(Strategy):
    """
    具体策略类, 封装了具体的算法和行为
    """

    def calculate(self):
        print("calculate B")


class Context(object):
    """
    上下文, 维护一个对strategy对象的引用
    """

    def __init__(self, strategy):
        self.__strategy = strategy

    def do_calculate(self):
        self.__strategy.calculate()


if __name__ == '__main__':
    c1 = Context(StrategyA())
    c1.do_calculate()


    c2 = Context(StrategyB())
    c2.do_calculate()
