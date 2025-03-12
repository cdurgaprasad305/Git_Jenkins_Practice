
import pytest
@pytest.mark.parametrize("a, b, exp ", [(1, 2,3), (3, 4,7), (5, 6,11)])
def test_add1(a, b, exp):
   assert exp == (a+b)
   pytest.mark.skip()
   pytest.skip()
