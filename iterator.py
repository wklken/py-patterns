#!/usr/bin/env python
# encoding: utf-8
"""
迭代器模式

提供一种方法顺序地访问一个聚合对象中的各个元素, 而又不暴露改对象的内部表示

- 无差别遍历聚合对象
- 需要对聚集进行多种方式遍历时
- 分离了集合对象的遍历行为, 做到不暴露集合内部结构, 又可以让外部代码透明的访问集合内部的数据

用于在数据集合中按照顺序遍历集合, 让用户通过特定的接口巡访容器中的每一个元素而不用了解底层的实现
wiki: https://zh.wikipedia.org/wiki/%E8%BF%AD%E4%BB%A3%E5%99%A8%E6%A8%A1%E5%BC%8F
python:
    - http://nvie.com/posts/iterators-vs-generators/
    - https://docs.python.org/2/glossary.html#term-iterator
    - https://docs.python.org/2/library/collections.html#collections.Iterable
    - https://docs.python.org/2/library/collections.html#collections.Iterator
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
        """
        object
        """
        pass

    @abstractmethod
    def has_next(self):
        """
        bool
        """
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

    def has_next(self):
        return self.current >= len(self.__aggregate)

    def current_item(self):
        return self.__aggregate[self.current]


# python 定义一个迭代器
import collections # noqa


class YRange(collections.Iterator):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def has_next(self):
        return self.i < self.n

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


if __name__ == '__main__':
    aggregate = [0] * 3

    aggregate[0] = 'a'
    aggregate[1] = 'b'
    aggregate[2] = 'c'

    it = ConcreteIterator(aggregate)
    i = it.first()
    while not it.has_next():
        print "current:", it.current_item()
        it.next()

    y = YRange(3)
    print list(y)

    y1 = YRange(5)
    print iter(y1)
