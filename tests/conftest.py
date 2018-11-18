import pytest
from some_app import My_class

@pytest.fixture(scope='class', autouse='True')
def raw_obj():
    print("\nCreating obj")
    obj = My_class()
    yield obj
    print("\nFinished")
