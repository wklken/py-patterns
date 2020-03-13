#!/usr/bin/env python
# encoding: utf-8
"""
享元模式

运用共享技术有效地支持大量细粒度的对象

- 可以避免大量非常相似类的开销
- 把区分的参数放在类实例外面, 在方法调用时传递进去

- 如果一个应用程序使用了大量对象, 而大量的这些对象造成了很大的存储开销时
"""

from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """
    所有具体享元类的超类或接口

    通过这个接口, flyweight可以接受并作用于外部状态
    """

    @abstractmethod
    def operation(self, extrinsicstate):
        pass


class ConcreteFlyweight(Flyweight):
    """
    继承flyweight超类或实现flyweight接口, 并未内部状态增加存储空间
    """

    def operation(self, extrinsicstate):
        print("specific flyweight:", extrinsicstate)


class UnsharedConcreteFlyweight(Flyweight):
    """
    不需要共享的flyweight子类
    """

    def operation(self, extrinsicstate):
        print("unshared flyweight:", extrinsicstate)


class FlyweightFactory(object):
    """
    一个享元工厂, 用来创建并管理flyweight对象, 主要是用阿里确保合理地共享 flyweight

    当用户请求一个flyweight是, flyweightfactory提供一个已经创建的实例, 或者创建一个
    """

    def __init__(self):
        self.__flyweights = dict()

        fx = ConcreteFlyweight()
        self.__flyweights["X"] = fx

        fy = ConcreteFlyweight()
        self.__flyweights["Y"] = fy

    def add_flyweight(self, key, flyweight):
        self.__flyweights[key] = flyweight

    def get_flyweight(self, key):
        flyweight = self.__flyweights.get(key)
        if not flyweight:
            flyweight = ConcreteFlyweight()
            self.__flyweights[key] = flyweight
        return flyweight


if __name__ == '__main__':
    f = FlyweightFactory()

    flyweight = f.get_flyweight("X")
    flyweight.operation(100)
