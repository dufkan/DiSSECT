import unittest, ast
from curve_analyzer.tests.i07.i07 import i07_curve_function
from curve_analyzer.tests.example_curves import curves, curve_names
results={'secp112r2': {'{}': {'distance': 740611633441112928659565470072532, 'ratio': 6, 'distance 32': 12, 'distance 64': 20}}, 'bn158': {'{}': {'distance': 23639966694374437715554742421545236103616790541, 'ratio': 8, 'distance 32': 13, 'distance 64': 13}}, 'brainpoolP160r1': {'{}': {'distance': 129204038890858043376599793886101655442989974519, 'ratio': 10, 'distance 32': 9, 'distance 64': 9}}}

class TestI07(unittest.TestCase):

    def test_auto_generated_secp112r2(self):
        '''This test has been auto-generated by gen_unittest'''
        params = ast.literal_eval(list(results["secp112r2"].keys())[0]).values()
        computed_result = i07_curve_function(curve_names["secp112r2"],*params)
        self.assertEqual(computed_result,list(results["secp112r2"].values())[0])

    def test_auto_generated_bn158(self):
        '''This test has been auto-generated by gen_unittest'''
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = i07_curve_function(curve_names["bn158"],*params)
        self.assertEqual(computed_result,list(results["bn158"].values())[0])

    def test_auto_generated_brainpoolP160r1(self):
        '''This test has been auto-generated by gen_unittest'''
        params = ast.literal_eval(list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = i07_curve_function(curve_names["brainpoolP160r1"],*params)
        self.assertEqual(computed_result,list(results["brainpoolP160r1"].values())[0])


if __name__ == '__main__':
   unittest.main()
   print("Everything passed")
