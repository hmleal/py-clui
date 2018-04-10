import unittest

from py_clui.colorize import Colorize


class TestColorize(unittest.TestCase):

    def setUp(self):
        self.c = Colorize()

    def test_grey(self):
        self.assertEqual(self.c.grey("Colorize"), "\x1b[30;1mColorize\x1b[0m")

    def test_red(self):
        self.assertEqual(self.c.red("Colorize"), "\x1b[31mColorize\x1b[0m")

    def test_green(self):
        self.assertEqual(self.c.green("Colorize"), "\x1b[32mColorize\x1b[0m")

    def test_yellow(self):
        self.assertEqual(self.c.yellow("Colorize"), "\x1b[33mColorize\x1b[0m")

    def test_blue(self):
        self.assertEqual(self.c.blue("Colorize"), "\x1b[34mColorize\x1b[0m")

    def test_pink(self):
        self.assertEqual(self.c.pink("Colorize"), "\x1b[35mColorize\x1b[0m")

    def test_light_blue(self):
        self.assertEqual(self.c.light_blue("Colorize"), "\x1b[36mColorize\x1b[0m")
