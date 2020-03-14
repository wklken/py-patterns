#!/usr/bin/env python
# encoding: utf-8
"""
抽象工厂模式

提供一个创建一系列相关或相互依赖对象的接口, 而无需指定他们具体的类

- 优点: 易于交换产品, 具体工厂配置不同的产品
- 优点: 让具体的创建实例过程与客户端分离, 客户端是通过它们的抽象接口操纵实例, 产品的具体类名也被具体工厂的实现分离, 不会出现在客户端的代码中
"""

from abc import ABCMeta, abstractmethod


class AbstractProductA(object):
    """
    抽象产品, 可能拥有多种实现
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "ProductA: %s" % self.name


class ConcreteProductA1(AbstractProductA):
    pass


class ConcreteProductA2(AbstractProductA):
    pass


class AbstractProductB(object):
    """
    抽象产品, 可能拥有多种实现
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "ProductB: %s" % self.name


class ConcreteProductB1(AbstractProductB):
    pass


class ConcreteProductB2(AbstractProductB):
    pass


class AbstractFactory(metaclass=ABCMeta):
    """
    抽象工厂接口, 包含所有产品创建的抽象方法
    """

    
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    具体工厂, 创建具有特定实现的产品对象
    """

    def create_product_a(self):
        return ConcreteProductA1("PA1")

    def create_product_b(self):
        return ConcreteProductB1("PB1")


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2("PA2")

    def create_product_b(self):
        return ConcreteProductB2("PB2")


if __name__ == '__main__':
    factory = ConcreteFactory2()

    product_a = factory.create_product_a()
    print(product_a)
