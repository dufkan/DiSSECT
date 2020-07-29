from sage.all import prime_range, Integers, ZZ
from curve_analyzer.tests.test_interface import pretty_print_results, compute_results

# Computes the order of l (small prime) modulo curve order and bit length of the index of <l>
# Returns a dictionary
def a12_curve_function(curve, l):
    mul_ord = (Integers(curve.order)(l)).multiplicative_order()
    curve_results = {'order': mul_ord}
    tmp = (curve.order - 1) / curve_results['order']
    curve_results['complement_bit_length'] = ZZ(tmp).nbits()
    return curve_results


def compute_a12_results(curve_list, desc=''):
    compute_results(curve_list, 'a12', a12_curve_function, desc=desc)


def get_a12_captions(results):
    captions = ['order', 'complement_bit_length']
    return captions


def select_a12_results(curve_results):
    keys = ['order', 'complement_bit_length']
    selected_results = []
    for key in keys:
        selected_key = []
        for x in curve_results:
            selected_key.append(x[key])
        selected_results.append(selected_key)
    return selected_results


def pretty_print_a12_results(curve_list, save_to_txt=True):
    pretty_print_results(curve_list, 'a12', get_a12_captions, select_a12_results, save_to_txt=save_to_txt)