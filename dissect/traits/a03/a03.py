#!/usr/bin/env python3
import dissect.traits.trait_utils as tu
from dissect.traits.trait_interface import compute_results
from dissect.utils.custom_curve import CustomCurve

TRAIT_TIMEOUT = 30


def a03_curve_function(curve: CustomCurve, deg):
    """Returns the factorization of the cardinality of the quadratic twist of the curve"""
    tr = tu.ext_trace(curve, deg)
    card = tu.ext_card(curve, deg)
    twist_card = card + 2 * tr
    f = tu.factorization(twist_card, timeout_duration=TRAIT_TIMEOUT)

    curve_results = {"twist_cardinality": twist_card, "factorization": f}
    return curve_results


def compute_a03_results(curve_list, desc='', verbose=False):
    compute_results(curve_list, 'a03', a03_curve_function, desc=desc, verbose=verbose)