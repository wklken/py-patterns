#!/usr/bin/env python
# encoding: utf-8
"""
命令模式

讲一个请求封装为一个对象, 从而使你可用不同的请求对客户进行参数化
对请求排队或记录请求日志, 以及支持可撤销操作

- 比较容易设计一个命令队列
- 在需要情况下, 可以将命令计入日志
- 允许接受请求的一方决定是否要否决请求
- 可以容易的实现对请求的撤销和崇左
- 由于加紧新的具体命令类不影响其他类,  可以很容易新增
- 把请求一个操作的对象与指导怎么执行一个操作的对象分隔开
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """
    声明执行操作的接口
    """

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    将一个接受着对象绑定于一个动作, 调用接收者相应的操作
    """

    def execute(self):
        self.receiver.action()


class Invoker(object):
    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        self.__command = value

    def execute_command(self):
        self.__command.execute()


class Receiver(object):
    def action(self):
        print("execute command")


if __name__ == '__main__':
    r = Receiver()

    cmd = ConcreteCommand(r)

    invoker = Invoker()
    invoker.command = cmd
    invoker.execute_command()
