from sage.all import GF, Integer

from curve_analyzer.traits.trait_interface import pretty_print_results, compute_results, timeout

# global time for one factorization
TIME = 10


def a01_curve_function(curve, deg):
    """returns the orders of the two generators of the curve over the deg-th relative extension"""
    E = curve.EC
    q = curve.q
    curve_results = {}

    E_ext = E.base_extend(GF(q ** deg))
    t = TIME
    curve_results['ord1'] = timeout(E_ext.abelian_group().gens()[0].order, [], timeout_duration=t)
    if not isinstance(curve_results['ord1'],Integer):
        curve_results['ord2'] = 1
        return curve_results
    try:
        curve_results['ord2'] = timeout(E_ext.abelian_group().gens()[1].order, [], timeout_duration=t)
    except IndexError:
        curve_results['ord2'] = 1
    return curve_results


def compute_a01_results(curve_list, desc='', verbose=False):
    compute_results(curve_list, 'a01', a01_curve_function, desc=desc, verbose=verbose)


def get_a01_captions(results):
    return ['ord1', 'ord2']


def select_a01_results(curve_results):
    keys = ['ord1', 'ord2']
    selected_results = []
    for key in keys:
        for x in curve_results:
            selected_results.append(x[key])
    return selected_results


def pretty_print_a01_results(curve_list, save_to_txt=True):
    pretty_print_results(curve_list, 'a01', get_a01_captions, select_a01_results, save_to_txt=save_to_txt)