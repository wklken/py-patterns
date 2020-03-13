#!/usr/bin/env python
# encoding: utf-8
"""
访问者模式

标识一个作用于某对象结构中的各元素的操作

可以使你在不改变各元素类的前提下定义作用于这些元素的新操作

- 适用于数据结构相对稳定的系统, 把数据结构和作用于结构上的操作之间的耦合解脱开, 是的操作集合可以相对自由地演化
- 目的是: 把处理从数据结构分离出来, 有比较稳定的数据结构, 又有易于变化的算法
- 优点: 增加新的操作很容易, 等同于增加一个新的访问者
"""

from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    """
    为该对象结构中concreteelement的每一个类声明一个visit操作
    """

    @abstractmethod
    def visitor_concrete_element_a(self, concrete_element_a):
        pass

    @abstractmethod
    def visitor_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor1(Visitor):
    """
    具体访问者, 实现每个声明的操作

    每个操作实现算法的一部分, 而该算法片段乃是对应于结构中对象的类
    """

    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_a.__class__.__name__))

    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_b.__class__.__name__))


class ConcreteVisitor2(Visitor):
    """
    具体访问者, 实现每个声明的操作

    每个操作实现算法的一部分, 而该算法片段乃是对应于结构中对象的类
    """

    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_a.__class__.__name__))

    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_b.__class__.__name__))


class Element(metaclass=ABCMeta):
    """
    定义一个accept操作, 以一个访问者为参数
    """

    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    """
    具体元素, 实现accept操作
    """

    def accept(self, visitor):
        visitor.visitor_concrete_element_a(self)


class ConcreteElementB(Element):
    """
    具体元素, 实现accept操作
    """

    def accept(self, visitor):
        visitor.visitor_concrete_element_b(self)


class ObjectStructure(object):
    """
    能枚举它的元素, 可以提供一个高层的接口以允许访问者访问它的元素
    """
    def __init__(self):
        self.__elements = []

    def attach(self, element):
        self.__elements.append(element)

    def detach(self, element):
        self.__elements.remove(element)

    def accept(self, visitor):
        for e in self.__elements:
            e.accept(visitor)


if __name__ == '__main__':
    os = ObjectStructure()

    os.attach(ConcreteElementA())
    os.attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    os.accept(v1)

    v2 = ConcreteVisitor2()
    os.accept(v2)
