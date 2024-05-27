import math
import pytest

class TestTemp:

    # @pytest.mark.square
    def test_sqrt(self):
        num = 25
        assert math.sqrt(num) == 5

    # @pytest.mark.square
    def testsquare(self):
        num = 7
        assert 7*7 == 40

    # @pytest.mark.others
    def testequality(self):
        assert 10 == 10