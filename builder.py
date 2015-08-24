#!/usr/bin/env python
# encoding: utf-8
"""
建造者模式

将一个复杂对象的构建与它的表示分离, 使得同样的构建过程可以创建不同的表示

- 用户只需指定需要建造的类型, 不需要知道具体地建造过程和细节
- 建造者模式是在当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时适用的模式
"""

from abc import ABCMeta, abstractmethod


class Product(object):
    """
    具体产品
    """

    def __init__(self):
        self.__parts = []

    def add(self, part):
        self.__parts.append(part)

    def show(self):
        print '-'.join(self.__parts)


class Builder(object):
    """
    为创建一个product对象的各个部件指定的抽象接口
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def build_part_1(self):
        pass

    @abstractmethod
    def build_part_2(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class BuilderA(Builder):
    def __init__(self):
        self.__product = Product()

    def build_part_1(self):
        self.__product.add("partA1")

    def build_part_2(self):
        self.__product.add("partA2")

    def get_result(self):
        return self.__product


class BuilderB(Builder):
    def __init__(self):
        self.__product = Product()

    def build_part_1(self):
        self.__product.add("partB1")

    def build_part_2(self):
        self.__product.add("partB2")

    def get_result(self):
        return self.__product


class Director(object):
    @staticmethod
    def construct(builder):
        builder.build_part_1()
        builder.build_part_2()


if __name__ == '__main__':
    ba = BuilderA()
    bb = BuilderB()

    Director.construct(ba)
    product = ba.get_result()
    product.show()

    Director.construct(bb)
    product = bb.get_result()
    product.show()


