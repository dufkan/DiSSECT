from sage.all import PolynomialRing
from dissect.utils.kohel.modular_polynomials import modular_polynomials
from dissect.utils.custom_curve import CustomCurve
from dissect.traits import Trait


class A28(Trait):
    NAME = "a28"
    DESCRIPTION = "Number of $j$-invariants adjacent to the curve by $l$-isogeny. This is the degree of the point in the $l$-isogeny graph."
    INPUT = {
        "l": (int, "Small prime")
    }
    OUTPUT = {
        "len": (int, "Number of adjacent curves")
    }
    DEFAULT_PARAMS = {
        "l": [2, 3, 5]
    }


    def compute(curve: CustomCurve, params):
        """
        Computes number of j-invariants j2 such that Phi_l(j,j2) where Phi_l is the l-modular polynomial.
        """
        Phi = modular_polynomials(params["l"])
        x = PolynomialRing(curve.field(), "x").gen()
        j = curve.j_invariant()
        f = Phi(j, x)
        return {"len": sum([i[1] for i in f.roots()])}
