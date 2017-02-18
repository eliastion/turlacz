import unittest
import rolling

# stubs
class RandomizerMock(object):

    def __init__(self):
        self.hardcodedRand = 0

    def rand(self):
        return self.hardcodedRand

# tests
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.randomizer = RandomizerMock()
        self.sut = rolling.Die(self.randomizer)

    def test_roll_range(self):
        # given
        expectedRollMin = 1
        expectedRollMax = 6
        self.randomizer.hardcodedRand = 6

        # when
        rollResult = self.sut.roll()

        # then
        self.assertTrue(rollResult<=expectedRollMax)
        self.assertTrue(rollResult>=expectedRollMin)


if __name__ == '__main__':
    unittest.main()
