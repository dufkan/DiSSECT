import unittest, ast
from curve_analyzer.tests.a22.a22 import a22_curve_function
from curve_analyzer.tests.example_curves import curves, curve_names
results={'secp112r2': {"{'l': 2}": {'factorization': [['x + 841610090548475696082223908882494', 1], ['x^2 + 3610075134545239076002374364665933*x + 2797590916291665130774294894805068', 1]], 'degs_list': [1, 2], 'len': 2}}, 'bn158': {"{'l': 2}": {'factorization': [['x^3 + 17', 1]], 'degs_list': [3], 'len': 1}}, 'brainpoolP160r1': {"{'l': 2}": {'factorization': [['x^3 + 297190522446607939568481567949428902921613329152*x + 173245649450172891208247283053495198538671808088', 1]], 'degs_list': [3], 'len': 1}}}

class Test_a22(unittest.TestCase):
 
    # This test has been auto-generated by gen_unittest
    def test_auto_generated_secp112r2(self):
        params = ast.literal_eval(list(results["secp112r2"].keys())[0]).values()
        computed_result = a22_curve_function(curve_names["secp112r2"],*params)
        self.assertEqual(computed_result,list(results["secp112r2"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_bn158(self):
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = a22_curve_function(curve_names["bn158"],*params)
        self.assertEqual(computed_result,list(results["bn158"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_brainpoolP160r1(self):
        params = ast.literal_eval(list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = a22_curve_function(curve_names["brainpoolP160r1"],*params)
        self.assertEqual(computed_result,list(results["brainpoolP160r1"].values())[0])


if __name__ == '__main__':
   unittest.main()
   print("Everything passed")
