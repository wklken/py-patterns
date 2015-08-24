#!/usr/bin/env python
# encoding: utf-8
"""
适配器模式

将一个类的接口转换成客户希望的另一个接口.
使得原本由于接口不兼容而不能work的那些类可以work

- 适用: 系统的数据和行为都正确, 但是接口不符时. (已存在, 但是其接口和需要的不同)
- 主要用于, 希望复用一些现存的类, 但接口又与复用环境要求不一致的情况
- 客户代码可以统一调用同一接口, 简单直接紧凑
"""

from abc import ABCMeta, abstractmethod


class Target(object):
    """
    客户锁期待的接口, 目标可以使具体或抽象的类, 也可以是接口
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def request(self):
        pass


class Adaptee(object):
    """
    需要适配的类
    """

    def special_request(self):
        print "I am special"


class Adapter(Target):
    """
    适配器, 通过在内部包装一个adapter对象, 把源接口转换成目标接口
    """

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.special_request()


if __name__ == '__main__':
    a = Adapter()

    a.request()
