
import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.ab import calculate_multi_dilution

class TestAntibodyDilution(unittest.TestCase):

    def test_calculate_multi_dilution(self):
        # Test case 1: Basic scenario
        result1 = calculate_multi_dilution(10, 20, {"ab1": 500, "ab2": 1000}, 10)
        self.assertAlmostEqual(result1['adjusted_total_volume_uL'], 220.0)
        self.assertAlmostEqual(result1['stock_volumes_uL']['ab1'], 0.44)
        self.assertAlmostEqual(result1['stock_volumes_uL']['ab2'], 0.22)
        self.assertAlmostEqual(result1['diluent_volume_uL'], 219.34)

        # Test case 2: No overage
        result2 = calculate_multi_dilution(5, 50, {"ab1": 200}, 0)
        self.assertAlmostEqual(result2['adjusted_total_volume_uL'], 250.0)
        self.assertAlmostEqual(result2['stock_volumes_uL']['ab1'], 1.25)
        self.assertAlmostEqual(result2['diluent_volume_uL'], 248.75)

        # Test case 3: Empty antibody list
        result3 = calculate_multi_dilution(12, 25, {}, 5)
        self.assertAlmostEqual(result3['adjusted_total_volume_uL'], 315.0)
        self.assertEqual(result3['stock_volumes_uL'], {})
        self.assertAlmostEqual(result3['diluent_volume_uL'], 315.0)

if __name__ == '__main__':
    unittest.main()
