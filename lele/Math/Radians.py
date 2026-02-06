class Radians(float):
    def __new__(cls, value):
        return super().__new__(cls, value)
        
    @classmethod
    def from_degrees(cls, degrees):
        import math
        return cls(math.radians(degrees))

def default():
    return Radians(0.0)


def test_():
    import math
    assert Radians(math.pi) == Radians.from_degrees(180)
