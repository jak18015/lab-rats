
import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.ifa import c1v1, formaldehyde, triton, bsa

class TestIFACalculations(unittest.TestCase):

    def test_c1v1(self):
        self.assertAlmostEqual(c1v1(10, 5, 2, None), 25)
        self.assertAlmostEqual(c1v1(10, None, 2, 25), 5)
        self.assertAlmostEqual(c1v1(None, 5, 2, 25), 10)
        self.assertAlmostEqual(c1v1(10, 5, None, 25), 2)

    def test_formaldehyde(self):
        result = formaldehyde(10, 4, 10, 1, 12)
        self.assertAlmostEqual(result['volume_stock_formaldehyde'], 4.8)
        self.assertAlmostEqual(result['volume_stock_pbs'], 1.2)
        self.assertAlmostEqual(result['volume_water'], 6.0)

    def test_triton(self):
        result = triton(10, 0.1, 10, 1, 12)
        self.assertAlmostEqual(result['volume_stock_triton'], 0.12)
        self.assertAlmostEqual(result['volume_stock_pbs'], 1.2)
        self.assertAlmostEqual(result['volume_water'], 10.68)

    def test_bsa(self):
        result = bsa(1, 12)
        self.assertAlmostEqual(result['mass_bsa'], 0.12)
        self.assertAlmostEqual(result['dissolve_volume'], 6.0)
        self.assertAlmostEqual(result['final_volume'], 12.0)

if __name__ == '__main__':
    unittest.main()
