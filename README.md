# Coolered
## A better [dslackw/colored](https://github.com/dslackw/colored)
I read the readme of dslackw/colored for Python, and thought it was too complicated. This will be an interface so simple you memorize it immediately.

## Example
```python
# Colors
color('red', 'This is red')
color('blue', 'This is blue')
color('yellow', 'This is yellow')

# Backgrounds
color('red', "This is red with a blue background", bg='blue')
color('blue', "This is blue with a yellow background", bg='yellow')

# That's it
```

## Color reference
Run
```bash
$ coolered -b
```
to see a list of basic (`-b`) colors. Run
```bash
$ coolered -l
```
to see a complete list (`-l`) of colors

## Usage in python
```python
from coolered import color

# Do shit
color('red', "Oh fuck, something bad happened")
# Do more shit
color('green', "Something good happened")
# Do more shit
color('yellow', "Warning: something happened")
```

## Installation
```
pip install coolered
```
## Uninstallation
```
pip uninstall coolered
```
