#!/usr/bin/env python
# encoding: utf-8
"""
工厂方法

定义一个用于创建对象的接口, 让子类决定实例化哪个类
工厂方法使一个类的实例化延迟到其子类

如果存在变更, 改creator即可
"""

from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    """
    定义工厂方法所创建的对象接口
    """

    @abstractmethod
    def echo(self):
        pass


class ConcreteProductA(Product):
    """
    具体的产品, 实现了product的接口
    """

    def echo(self):
        print(self.__class__.__name__)


class ConcreteProductB(Product):
    """
    具体的产品, 实现了product的接口
    """

    def echo(self):
        #print("product B")
        print(self.__class__.__name__)


class Creator(object):
    """
    声明了工厂方法, 该方法返回一个Product类型的对象
    """

    @abstractmethod
    def create(self):
        pass


class ConcreteCreatorA(Creator):
    """
    重定义, 返回一个ConcreteProduct实例
    """

    def create(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def create(self):
        return ConcreteProductB()


if __name__ == '__main__':
    factory_a = ConcreteCreatorA()
    product = factory_a.create()
    product.echo()

    factory_b = ConcreteCreatorB()
    product = factory_b.create()
    product.echo()

