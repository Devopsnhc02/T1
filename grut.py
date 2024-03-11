import unittest

from graobj import Grade

class TestcalculatorMethods(unittest.TestCase):

    obj=Grade()

    def testAddition(self):

        self.assertEqual(self.obj.c(90),"Grade A")

    def testAddition(self):
        self.assertEqual(self.obj.c(80), "Grade B")

    def testAddition(self):
        self.assertEqual(self.obj.c(70), "Grade C")

    def testAddition(self):
        self.assertEqual(self.obj.c(60), "Fail")


if __name__=='__main__':
    unittest.main()