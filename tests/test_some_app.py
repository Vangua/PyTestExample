from some_app import My_class
import pytest


class Test_some_app:
    
    def test_func1_result(self, raw_obj : My_class):
        assert raw_obj.func1() is False
    
    def test_func2(self, raw_obj : My_class):
        assert raw_obj.var is 2
        raw_obj.func2(20)
        assert raw_obj.var is 20
