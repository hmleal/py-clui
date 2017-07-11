import unittest

from py_clui import gauge


class TestGauge(unittest.TestCase):
    def test_empty_max_value_gauge(self):
        self.assertEqual('[]', gauge(10, 0, 100, 80))
