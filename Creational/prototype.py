#!/usr/bin/env python
# encoding: utf-8
"""
原型模式

用原型实例指定创建对象的种类, 并且通过拷贝这些原型创建新的对象

- 原型模型其实是从一个对象再创建另外一个可定制的对象, 而且不需要知道任何创建细节
- 一般在初始化信息不发生变化的情况下, 克隆是最好的办法, 既隐藏了对象创建的细节, 有提高了性能

在不指定类名的前提下生成实例
- 对象种类繁多, 无法将它们整合到一个类中
- 难以根据类生成实例时
- 解耦框架与生成实例: 让框架不依赖于具体的类, 不能指定类名来生成实例, 要实现注册一个原型
  然后, 通过复制该实例来生成新的实例

why: 一旦在代码中出现要使用的类的名字, 就无法与该类分离开来, 也就无法实现复用

示例:

"""
import copy
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    """
    原型类, 声明一个克隆自身的接口
    """

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
        # 浅拷贝, 注意
        return copy.copy(self)


class ConcretePrototypeB(Prototype):
    """
    具体原型类, 实现一个克隆自身的操作
    """
    def clone(self):
        return copy.copy(self)


class Manager(object):
    def __init__(self):
        self._dict = {}

    def register(self, name, prototype):
        self._dict[name] = prototype

    def create(self, proto_name):
        p = self._dict.get(proto_name)
        return p.clone()


if __name__ == '__main__':
    ca = ConcretePrototypeA(1)
    c2 = ca.clone()
    print(c2.id)

    # with manager
    cb = ConcretePrototypeB(2)

    m = Manager()
    m.register("ca", ca)
    m.register("cb", cb)

    x = m.create("cb")
    print(x.id)

