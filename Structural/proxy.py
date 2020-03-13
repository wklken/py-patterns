#!/usr/bin/env python
# encoding: utf-8
"""
代理模式

为其他对象提供一种代理以控制这个对象的访问

远程代理/虚拟代理/安全代理/智能指引
"""

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """
    定义了RealSubject和Proxy的共用接口
    这样就在任何使用realsubject的地方都可以使用proxy
    """

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    """
    定义了真正的实体
    """
    def request(self):
        print("hello")


class Proxy(Subject):
    """
    保存一个引用使得代理可以访问尸体并提供一个与subject的接口相同的接口, 这样代理就可以用来替代实体
    """
    def __init__(self):
        self.__realsubject = RealSubject()

    def request(self):
        self.__realsubject.request()


if __name__ == '__main__':
    proxy = Proxy()

    proxy.request()
