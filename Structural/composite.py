#!/usr/bin/env python
# encoding: utf-8
"""
组合模式

将对象组合成树状结构以表示`部分-整体`的层次结构
使得用户对单个对象和组合对象的使用具有一致性

- 适用: 需求中体现部分与整体层次的结构, 希望用户可以忽略组合对象与单个对象的不同, 统一地使用组合结构中的所有对象时, 就应该考虑使用组合模式
- 优点: 让用户可以一致性的使用组合结构和单个对象
"""


class Component(object):
    """
    组合中的对象声明接口

    在适当情况下, 实现所有类共有接口的默认行为

    声明接口用于访问和管理Component的子部件
    """

    def __init__(self, name):
        self.name = name

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, depth):
        pass


class Leaf(Component):
    """
    组合中表示叶节点对象, 叶节点没有子节点
    """

    def add(self, component):
        print("can not add to a leaf")

    def remove(self, component):
        print("can not remove from a leaf")

    def display(self, depth):
        print('-' * depth + self.name)


class Composite(Component):
    """
    定义有枝节点行为, 用于存储子部件

    实现相关操作
    """

    def __init__(self, name):
        super(Composite, self).__init__(name)
        self.__children = []

    def add(self, component):
        self.__children.append(component)

    def remove(self, component):
        self.__children.remove(component)

    def display(self, depth):
        print('-' * depth + self.name)
        for c in self.__children:
            c.display(depth + 2)


if __name__ == '__main__':
    root = Composite("root")

    root.add(Leaf("A"))
    root.add(Leaf("B"))

    comp = Composite("X")
    comp.add(Leaf("XA"))
    comp.add(Leaf("XB"))

    root.add(comp)

    root.display(1)

