#!/usr/bin/env python
# encoding: utf-8
"""
简单工厂模式

增加操作:
    1. 增加对应子类
    2. 修改工厂类
"""


class Operation(object):

    @property
    def number_a(self):
        return self.__number_a

    @number_a.setter
    def number_a(self, value):
        self.__number_a = value

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, value):
        self.__number_b = value


class OperationAdd(Operation):
    def get_result(self):
        return self.number_a + self.number_b


class OperationSub(Operation):
    def get_result(self):
        return self.number_a - self.number_b


class OperationFactory(object):
    @staticmethod
    def create_operation(operate):
        if operate == "+":
            return OperationAdd()
        elif operate == "-":
            return OperationSub()


if __name__ == '__main__':
    op = OperationFactory.create_operation('-')
    op.number_a = 10
    op.number_b = 5

    print(op.get_result())
