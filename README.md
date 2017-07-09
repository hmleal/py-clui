# Py-clui
> This is a Python toolkit for quickly building nice looking command line interfaces.

It also includes the following easy to use components:
* Spinners

### Spinner(message, style=None)

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

## Motivation
  1. clui makes NodeJS even more sexy. Python needed something like it.
