# Py-clui
> This is a Python toolkit for quickly building nice looking command line interfaces.

[![Build Status](https://travis-ci.org/hmleal/py-clui.svg?branch=master)](https://travis-ci.org/hmleal/py-clui)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

It also includes the following easy to use components:

* Spinners
* Gauge
* Progress

### Spinner(message, style=None)

![Picture of a spinner](https://raw.githubusercontent.com/hmleal/py-clui/master/docs/spinner.gif)

__Parameters__

* `message` - The default status text to display while the spinner is spinning.
* `style` - Array of graphical characters used to draw the spinner. By default,
  on Windows: ['|', '/', '-', '\'], on other platforms: ['◜','◠','◝','◞','◡','◟']

__Methods__

* `run()` - Show the spinner on the screen.
* `update_msg(message)` - Update the status message that follows the spinner.

__Example__

```python
from py_clui import Spinner

spinner = Spinner('Processing documents...')
spinner.run()

for x in range(100):
    spinner.update_msg('{0} Processed documents'.format(x))
    spinner.run()
```

### Gauge(value, max_value, width, danger_zone, suffix=None)

![Picture of a gauge](https://raw.githubusercontent.com/hmleal/py-clui/master/docs/gauge.png)

Draw a basic horizontal gauge to the screen.

Parameters

* `value`
* `max_value`
* `width`
* `danger_zone`
* `suffix`

Example

```python
from py_clui import gauge

total = 100
free = 30

used = total - free

print(gauge(used, total, 20, total * 0.8, 'Used memory'))
```

### Progress(width=20)

![Picture of a progress](https://raw.githubusercontent.com/hmleal/py-clui/master/docs/progress.png)

__Parameters__

* `width` - The width in characters of progress_bar

__Methods__

* `update(percent)` - Return a progress bar width a this percente filled.

__Example__

```python
from py_clui import Progress

progress = Progress(20)

print(progress.update(.5))
```

## Motivation
  1. [clui](https://github.com/nathanpeck/clui) makes NodeJS even more sexy. Python needed something like it.
