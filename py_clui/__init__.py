#!/usr/bin/env python
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# http://aurelio.net/shell/canivete/
# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color

import math
import sys

from .colorize import Colorize

__author__ = 'Henrique Leal'
__author_email__ = 'hm.leal@hotmail.com'
__version__ = '0.0.2'


c = Colorize()


def gauge(value, max_value, width, danger_zone, suffix=None):
    if max_value == 0:
        return '[]'

    length = math.ceil(value / max_value * width)

    if length > width:
        length = width

    bars = '|' * length
    if value > danger_zone:
        bars = c.red(bars)
    bars = c.green(bars)
    bars += '-' * (width + 1 - length)

    return '[{0}] {1}'.format(bars, suffix)


class Spinner:
    def __init__(self, message, style=None):
        self.message = message
        self._number = 0
        self.style = self._style(style)

    def run(self):
        self._draw()

    def update_msg(self, message):
        self.message = message

    def _draw(self):
        self._number += 1

        frames = [' {0} '.format(c.light_blue(f)) for f in self.style]

        print('{0}{1}'.format(frames[self._number % len(self.style)], c.grey(self.message)), end='\r', file=sys.stdout, flush=True)

    def _style(self, style):
        if style is not None:
            return style

        if sys.platform == 'win32':
            return ['|','/', '-', '\\']

        return ['◜', '◠', '◝', '◞', '◡', '◟']
        # return ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
