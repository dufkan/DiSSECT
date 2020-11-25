import unittest, ast
from curve_analyzer.tests.a23.a23 import a23_curve_function
from curve_analyzer.tests.example_curves import curves, curve_names
results={'secp112r2': {"{'l': 2}": {'crater_degree': 0, 'depth': 1}}, 'bn158': {"{'l': 2}": {'crater_degree': 0, 'depth': 0}}, 'brainpoolP160r1': {"{'l': 2}": {'crater_degree': 0, 'depth': 0}}}

class Test_a23(unittest.TestCase):
 
    # This test has been auto-generated by gen_unittest
    def test_auto_generated_secp112r2(self):
        params = ast.literal_eval(list(results["secp112r2"].keys())[0]).values()
        computed_result = a23_curve_function(curve_names["secp112r2"],*params)
        self.assertEqual(computed_result,list(results["secp112r2"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_bn158(self):
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = a23_curve_function(curve_names["bn158"],*params)
        self.assertEqual(computed_result,list(results["bn158"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_brainpoolP160r1(self):
        params = ast.literal_eval(list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = a23_curve_function(curve_names["brainpoolP160r1"],*params)
        self.assertEqual(computed_result,list(results["brainpoolP160r1"].values())[0])


if __name__ == '__main__':
   unittest.main()
   print("Everything passed")
