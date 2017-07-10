#!/usr/bin/env python

class Colorize:
    def _colorize(self, color_code, text):
        return '\033[{0}m{1}\33[0m'.format(color_code, text)

    def grey(self, text):
        return self._colorize('30;1', text)

    def red(self, text):
        return self._colorize('31', text)

    def green(self, text):
        return self._colorize('32', text)

    def yellow(self, text):
        return self._colorize('33', text)

    def blue(self, text):
        return self._colorize('34', text)

    def pink(self, text):
        return self._colorize('35', text)

    def light_blue(self, text):
        return self._colorize('36', text)


if __name__ == '__main__':
    c = Colorize()

    samples = [
        c.grey('Henrique'),
        c.red('Henrique'),
        c.green('Henrique'),
        c.yellow('Henrique'),
        c.blue('Henrique'),
        c.pink('Henrique'),
        c.light_blue('Henrique')
    ]

    for x in samples:
        print(x)
