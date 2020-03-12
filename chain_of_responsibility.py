#!/usr/bin/env python
# encoding: utf-8
"""
责任链模式

使多个对象都以机会处理请求, 从而避免请求的发送者和接受者之间的耦合关系
将这个对象连成一条链, 沿着这条链传递请求, 直到有一个对象处理它为止

- 可以随意增加或修改处理一个请求的链式结构
"""

from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    """
    定义一个处理请求的接口
    """

    def __init__(self):
        self.__successor = None

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        self.__successor = value

    @abstractmethod
    def handle_request(self, request):
        pass


class ConcreteHandlerA(Handler):
    """
    具体处理类, 处理它所负责的请求

    如果可以处理该请求, 处理之, 否则转给后继者
    """

    def handle_request(self, request):
        if 0 <= request < 10:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)


class ConcreteHandlerB(Handler):
    """
    具体处理类, 处理它所负责的请求

    如果可以处理该请求, 处理之, 否则转给后继者
    """

    def handle_request(self, request):
        if 10 <= request < 20:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)


class ConcreteHandlerC(Handler):
    """
    具体处理类, 处理它所负责的请求

    如果可以处理该请求, 处理之, 否则转给后继者
    """

    def handle_request(self, request):
        if 20 <= request < 30:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)


if __name__ == '__main__':
    h1 = ConcreteHandlerA()
    h2 = ConcreteHandlerB()
    h3 = ConcreteHandlerC()

    h1.successor = h2
    h2.successor = h3

    for req in [2, 14, 22]:
        print(req)
        h1.handle_request(req)
