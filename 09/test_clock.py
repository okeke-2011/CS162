import unittest
from clock import ClockIterator


class TestClock(unittest.TestCase):
    def test_clock(self):
        clock = ClockIterator()
        for ind, time in enumerate(clock):
            if ind == 0:
                self.assertEqual(time, "00:00")
            if ind == 59:
                self.assertEqual(time, "00:59")
            if ind == 60:
                self.assertEqual(time, "01:00")
            if ind == 1439:
                self.assertEqual(time, "23:59")
            if ind == 1440:
                self.assertEqual(time, "00:00")
                break
