from sage.all import kronecker, ZZ

from dissect.utils.custom_curve import CustomCurve
from dissect.traits import Trait

class A23(Trait):
    NAME = "a23"
    DESCRIPTION = "Volcano depth and crater degree of the $l$-isogeny graph."
    INPUT = {
        "l": (int, "Prime")
    }
    OUTPUT = {
        "crater_degree": (int, "Crater degree"),
        "depth": (int, "Depth")
    }
    DEFAULT_PARAMS = {
        "l": [2, 3, 5, 7, 11, 13, 17, 19]
    }


    def compute(curve: CustomCurve, params):
        """
        Computes the depth of volcano and the degree of the crater subgraph containing E
        Returns a dictionary (keys: 'crater_degree', 'depth')
        """
        D = curve.extended_frobenius_disc()
        curve_results = {}
        if params["l"] != 2:
            curve_results["crater_degree"] = kronecker(D, params["l"]) + 1
            curve_results["depth"] = ZZ.valuation(params["l"])(D) // 2
        else:
            e = ZZ.valuation(2)(D)
            if e % 2 == 0:
                d = D // (2 ** e)
                if d % 4 != 1:
                    curve_results["crater_degree"] = 1
                    curve_results["depth"] = e // 2 - 1
                else:
                    curve_results["crater_degree"] = kronecker(d, params["l"]) + 1
                    curve_results["depth"] = e // 2
            else:
                curve_results["crater_degree"] = 1
                curve_results["depth"] = e // 2 - 1
        return curve_results
