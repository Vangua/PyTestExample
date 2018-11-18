#!/usr/bin/env python3


class My_class:
    def __init__(self):
        self.var = 2

    def func1(self) -> bool:
        return False

    def func2(self, new_var : int) -> None:
        self.var = new_var


