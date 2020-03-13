#!/usr/bin/env python
# encoding: utf-8
"""
模板方法模式

定义一个操作中的算法的构架, 而将一些步骤的实现延迟到子类中
这样, 可以使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤(相当于, 只需要覆写某些方法)

- 在父类中定义处理流程的框架, 在子类中实现具体处理的模式
- 在抽象类阶段确定处理的流程
- 使用继承改变程序的行为
- 把不变行为放到超类, 去除子类中的重复代码
- 提供了一个很好地代码复用平台

注意: 在子类中实现父类中声明的抽象方法时, 必须要理解这些抽象方法被调用的时机

"""

from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    """
    实现了一个模板方法, 定义了算法的挂架
    """

    def say_hello(self):
        print("begin...")
        self.hello()
        self.world()
        print("end...")

    @abstractmethod
    def hello(self):
        pass

    @abstractmethod
    def world(self):
        pass


class ConcreteClass(AbstractClass):
    """
    实现了特定的步骤
    """
    def hello(self):
        print("hello")

    def world(self):
        print("world")


if __name__ == '__main__':
    c = ConcreteClass()
    c.say_hello()
