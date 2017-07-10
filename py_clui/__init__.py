#!/usr/bin/env python
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# http://aurelio.net/shell/canivete/
# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color

import math
import sys
import time

__author__ = 'Henrique Leal'
__author_email__ = 'hm.leal@hotmail.com'
__version__ = '0.0.2'


class Colored:
    COLORS = {
        'white':  '\033[0m',    # White (normal)
        'red':    '\033[31m',   # Red
        'green':  '\033[32m',   # Green
        'orange': '\033[33m',   # Orange
        'blue':   '\033[34m',   # Blue
        'purple': '\033[35m',   # Purple
        'grey':   '\033[30;1m', # Grey
    }

    def red(self, text):
        return self._format(text, 'red')

    def green(self, text):
        return self._format(text, 'green')

    def orange(self, text):
        return self._format(text, 'orange')

    def blue(self, text):
        return self._format(text, 'blue')

    def purple(self, text):
        return self._format(text, 'purple')

    def grey(self, text):
        return self._format(text, 'grey')

    def _format(self, text, color):
        return '{0}{1}{2}'.format(
            self.COLORS[color], text, self.COLORS['white'])


def gauge(value, max_value, width, danger_zone, suffix):
    color = Colored()

    if max_value == 0:
        return '[]'

    length = math.ceil(value / max_value * width)

    if length > width:
        length = width

    bars = '|' * length
    if value > danger_zone:
        bars = color.red(bars)
    bars = color.green(bars)
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
        frames = ['  \u001b[96m{0} '.format(el) for el in self.style]
        msg = '\u001b[0G{0}\u001b[90m{1}\u001b[0m'

        self._number += 1

        print(msg.format(frames[self._number % len(self.style)], self.message), end='\r', file=sys.stdout, flush=True)

    def _style(self, style):
        if style is not None:
            return style

        if sys.platform == 'win32':
            return ['|','/', '-', '\\']

        return ['◜', '◠', '◝', '◞', '◡', '◟']
        # return ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']


if __name__ == '__main__':
    for x in range(20):
        print(gauge(x, 20, 20, 12, 'Henrique'), end='\r', file=sys.stdout, flush=True)
        time.sleep(0.2)
