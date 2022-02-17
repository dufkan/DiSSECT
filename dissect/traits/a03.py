#!/usr/bin/env python3
from typing import List

from dissect.utils.utils import Factorization
from dissect.utils.custom_curve import CustomCurve
from dissect.traits import Trait

TRAIT_TIMEOUT = 30


class A03(Trait):
    NAME = "a03"
    DESCRIPTION = "Factorization of the quadratic twist cardinality in an extension, i.e. $\\#E(\\mathbb{F}_{p^d})$."
    MOTIVATION = "Smooth cardinality of a quadratic twist might allow attacks on some implementations."
    INPUT = {
        "deg": (int, "Degree of extension")
    }
    OUTPUT = {
        "twist_cardinality": (int, "Twist cardinality"),
        "factorization": (List[int], "Factorization of the cardinality")
    }
    DEFAULT_PARAMS = {
        "deg": [1, 2]
    }


    def compute(curve: CustomCurve, params):
        """Returns the factorization of the cardinality of the quadratic twist of the curve"""
        tr = curve.extended_trace(params["deg"])
        card = curve.extended_cardinality(params["deg"])
        twist_card = card + 2 * tr
        f = Factorization(twist_card, timeout_duration=TRAIT_TIMEOUT)

        curve_results = {"twist_cardinality": twist_card, "factorization": f.factorization()}
        return curve_results
