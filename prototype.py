#!/usr/bin/env python
# encoding: utf-8
"""
原型模式

用原型实例指定创建对象的种类, 并且通过拷贝这些原型创建新的对象

- 原型模型其实是从一个对象再创建另外一个可定制的对象, 而且不需要知道任何创建细节
- 一般在初始化信息不发生变化的情况下, 克隆是最好的办法, 既隐藏了对象创建的细节, 有提高了性能
"""
import copy
from abc import ABCMeta, abstractmethod


class Prototype(object):
    """
    原型类, 声明一个克隆自身的接口
    """
    __metaclass__ = ABCMeta

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @abstractmethod
    def clone(self):
        pass


class ConcretePrototypeA(Prototype):
    """
    具体原型类, 实现一个克隆自身的操作
    """
    def clone(self):
        # 浅拷贝
        return copy.copy(self)


class ConcretePrototypeB(Prototype):
    """
    具体原型类, 实现一个克隆自身的操作
    """
    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    ca = ConcretePrototypeA(1)
    c2 = ca.clone()
    print c2.id


