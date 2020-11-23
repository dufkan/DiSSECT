import unittest, ast
from curve_analyzer.tests.a01.a01 import a01_curve_function
from curve_analyzer.tests.testing_curves import curves, curve_names
results={'secp112r2': {"{'deg': 1}": {'ord1': 4451685225093714699870930859147564, 'ord2': 1}}, 'bn158': {"{'deg': 1}": {'ord1': 206327671360737302491015346511080613560608358413, 'ord2': 1}}, 'brainpoolP160r1': {"{'deg': 1}": {'ord1': 1332297598440044874827085038830181364212942568457, 'ord2': 1}}}

class Test_a01(unittest.TestCase):
 
    # This test has been auto-generated by gen_unittest
    def test_auto_generated_secp112r2(self):
        params = ast.literal_eval(list(results["secp112r2"].keys())[0]).values()
        computed_result = a01_curve_function(curve_names["secp112r2"],*params)
        self.assertEqual(computed_result,list(results["secp112r2"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_bn158(self):
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = a01_curve_function(curve_names["bn158"],*params)
        self.assertEqual(computed_result,list(results["bn158"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_brainpoolP160r1(self):
        params = ast.literal_eval(list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = a01_curve_function(curve_names["brainpoolP160r1"],*params)
        self.assertEqual(computed_result,list(results["brainpoolP160r1"].values())[0])


if __name__ == '__main__':
   unittest.main()
   print("Everything passed")
