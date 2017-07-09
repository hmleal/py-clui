#!/usr/bin/env python
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# http://aurelio.net/shell/canivete/
# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color

import sys
import time

#def colored(text, color):
#    return COLORS[color] + text + COLORS['white']


#def Gauge(value, max_value, width, danger_zone, suffix=None):
#    if max_value == 0:
#        return '[]'
#
#    length = math.ceil(value / max_value * width)
#
#    if length > width:
#        length = width
#
#    bar_color = 'green'
#    if value > danger_zone:
#        bar_color = 'red'
#
#    return '[' + colored('|' * length, bar_color) + '-' * (width + 1 - length) + '] ' + colored(suffix, 'grey')


#COLORS = {
#    'white': '\033[0m',   # White (normal)
#    'red': '\033[31m',    # Red
#    'green': '\033[32m',  # Green
#    'orange': '\033[33m', # Orange
#    'blue': '\033[34m',   # Blue
#    'purple': '\033[35m', # Purple
#    'grey': '\033[30;1m', # Grey
#}


class Spinner:
    def __init__(self, message, style=None):
        self.message = message
        self.style = ['|','/', '-', '\\']
        self._number = 0
        #self.style = ['◜', '◠', '◝', '◞', '◡', '◟']
        self.style = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']

    def run(self):
        self._draw()

    def update_msg(self, message):
        self.message = message

    def _draw(self):
        frames = ['  \u001b[96m{0} '.format(el) for el in self.style]
        msg = '\u001b[0G{0}\u001b[90m{1}\u001b[0m'

        self._number += 1

        print(msg.format(frames[self._number % len(self.style)], self.message), end='\r', file=sys.stdout, flush=True)
