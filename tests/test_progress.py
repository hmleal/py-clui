import unittest

from py_clui import Progress


class TestProgress(unittest.TestCase):
    def setUp(self):
        self.progress = Progress(width=100)

    def test_percent_progress_bar(self):
        self.progress.update(.8)

        self.assertEqual(self.progress.percent, 80)

    def test_bar_length(self):
        self.progress.update(.8)

        self.assertEqual(self.progress.bar_length, 80)

    def test_empty_progress_bar(self):
        self.assertEqual(self.progress.percent, 0)
        self.assertEqual(self.progress.bar_length, 0)
