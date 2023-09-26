import math
from finance import future_value, present_value

def test_future_value():
    assert(future_value(1000, .05, 3) == 1157.6250000000002)

def test_present_value():
    fv = future_value(1000, .05, 3)
    pv = present_value(fv, .05, 3)
    assert(math.isclose(pv, 1000))
