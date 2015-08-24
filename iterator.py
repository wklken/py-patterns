#!/usr/bin/env python
# encoding: utf-8
"""
迭代器模式

提供一种方法顺序地访问一个聚合对象中的各个元素, 而又不暴露改对象的内部表示

- 无差别遍历聚合对象
- 需要对聚集进行多种方式遍历时
- 分离了集合对象的遍历行为, 做到不暴露集合内部结构, 又可以让外部代码透明的访问集合内部的数据
"""

# 不考虑默认的迭代器

from abc import ABCMeta, abstractmethod


class Iterator(object):
    """
    迭代抽象类

    定义迭代器抽象方法
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current_item(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.__aggregate = aggregate
        self.current = 0

    def first(self):
        return self.__aggregate[0]

    def next(self):
        result = None
        self.current += 1
        if self.current < len(self.__aggregate):
            result = self.__aggregate[self.current]
        return result

    def is_done(self):
        return self.current >= len(self.__aggregate)

    def current_item(self):
        return self.__aggregate[self.current]


if __name__ == '__main__':
    aggregate = [0] * 3

    aggregate[0] = 'a'
    aggregate[1] = 'b'
    aggregate[2] = 'c'

    it = ConcreteIterator(aggregate)
    i = it.first()
    while not it.is_done():
        print "current:", it.current_item()
        it.next()




