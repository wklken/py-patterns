#!/usr/bin/env python
# encoding: utf-8
"""
装饰模式

动态地给一个对象添加一些额外的职责,
就增加功能来说, 装饰模式比生成子类更为灵活

- 装饰模式, 是为已有功能动态地添加更多功能的一种方式
- 有效地将核心职责和装饰功能区分开

"""

from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """
    定义一个对象接口
    可以给这些对象动态地增加职责
    """

    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    定义了一个具体对象, 也可以给这个对象增加职责
    """

    def operation(self):
        print("Hello world")


class Decorator(Component):
    """
    装饰抽象类, 继承了component, 从外类来扩展component类的功能, 但对于component来说, 是无须知道decorator类的存在的
    """
    def __init__(self, component):
        self.__component = component

    def operation(self):
        if self.__component:
            self.__component.operation()


class DecoratorA(Decorator):
    """
    具体装饰对象, 给component添加职责
    """
    def operation(self):
        print("<h1>")
        super(DecoratorA, self).operation()
        print("</h1>")


class DecoratorB(Decorator):
    def operation(self):
        print("<strong>")
        super(DecoratorB, self).operation()
        print("</strong>")

if __name__ == '__main__':
    c = ConcreteComponent()

    d1 = DecoratorA(c)

    d1.operation()

    d2 = DecoratorB(d1)
    d2.operation()
