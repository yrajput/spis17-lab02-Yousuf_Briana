import unittest
from tempFuncs import ftoc

class Test_tempFuncs(unittest.TestCase):

    def test_ftoc_1(self):
        self.assertAlmostEqual(ftoc(212.0),100.0)

    def test_ftoc_2(self):
        self.assertAlmostEqual(ftoc(32.0),0.0)

    def test_ftoc_3(self):
        self.assertAlmostEqual(ftoc(-40.0),-40.0)

    def test_ftoc_4(self):
        self.assertAlmostEqual(ftoc(67.0),19.4444,places=3)

if __name__=='__main__':
    unittest.main()
