from dissect.traits import Trait

class I13(Trait):
    NAME = "i13"
    DESCRIPTION = "Computation of $a^3/b^2$."
    INPUT = {}
    OUTPUT = {
        "r": (int, "Integer r")
    }
    DEFAULT_PARAMS = {}

    def compute(curve, params):
        """
        Computation of r=a^3/b^2 which is used during the generation in x962, secg, fips and others
        """
        from sage.all import ZZ

        a, b = curve.a(), curve.b()
        return {"r": ZZ(curve.field()((a ** 3) / (b ** 2)))}


def test_i13():
    assert True