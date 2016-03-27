import nose
import unittest
from day1 import whichLevel
from day1 import firstCharacterResultingInBasement


class day1_test_part_1(unittest.TestCase):
    def setUp(self):

        self.goingUpEquals0 = '(())'
        self.goingUpEquals0_secondEx = '()()'
        self.goingUpEquals3 = '((('
        self.goingUpEquals3_secondEx = '(()(()('
        self.goingUpEquals3_thirdEx = '))((((('
        self.goingDownEqualsBasementMinus1 = '())'
        self.goingDownEqualsBasementMinus1_secondEx = '))('
        self.goingDownEqualsBasementMinus3 = ')))'
        self.goingDownEqualsBasementMinus3_secondEx = ')())())'
        self.answer = 138

    def test_results_in_floor_0_first(self):
        result = whichLevel(self.goingUpEquals0)
        self.assertEquals(result, 0)

    def test_results_in_floor_0_second(self):
        result = whichLevel(self.goingUpEquals0_secondEx)
        self.assertEquals(result, 0)

    def test_results_in_floor_3_first(self):
        result = whichLevel(self.goingUpEquals3)
        self.assertEquals(result, 3)

    def test_results_in_floor_3_second(self):
        result = whichLevel(self.goingUpEquals3_secondEx)
        self.assertEquals(result, 3)

    def test_results_in_floor_3_third(self):
        result = whichLevel(self.goingUpEquals3_thirdEx)
        self.assertEquals(result, 3)

    def test_results_in_basement_minus1_first(self):
        result = whichLevel(self.goingDownEqualsBasementMinus1)
        self.assertEquals(result, -1)

    def test_results_in_basement_minus1_second(self):
        result = whichLevel(self.goingDownEqualsBasementMinus1_secondEx)
        self.assertEquals(result, -1)

    def test_results_in_basement_minus3_first(self):
        result = whichLevel(self.goingDownEqualsBasementMinus3)
        self.assertEquals(result, -3)

    def test_results_in_basement_minus3_second(self):
        result = whichLevel(self.goingDownEqualsBasementMinus3_secondEx)
        self.assertEquals(result, -3)


class day1_test_part_2(unittest.TestCase):
    def setUp(self):

        self.positionIs1 = ')'
        self.positionIs5 = '()())'

    def test_function_returns_position_1(self):
        result = firstCharacterResultingInBasement(self.positionIs1)
        self.assertEquals(result, 1)

    def test_function_returns_position_5(self):
        result = firstCharacterResultingInBasement(self.positionIs5)
        self.assertEquals(result, 5)

if __name__ == '__main__':
    nose.main()
