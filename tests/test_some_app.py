from some_app import My_class
import pytest


class Test_some_app:
    
    def test_func1_result(self, raw_obj : My_class):
        assert raw_obj.func1() is True

