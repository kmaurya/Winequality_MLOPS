import pytest

class not_in_range(Exception):
    def __init__(self, message="Value is not in the range of minimum and maximum value"):
        self.message = message
        super().__init__(self.message)


def test_generic():
     a=2
     with pytest.raises(not_in_range):
         if a not in range(3,10):
            raise not_in_range