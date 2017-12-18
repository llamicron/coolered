from sys import argv

from colored import fg, bg, attr
from color_list import color_list as colors

def color(color, string, **args):
    color_code = None
    bg_code = None
    end = None
    reset = attr(0)

    if color:
        color_code = fg(colors[color])

    if 'bg' in args.keys():
        bg_code = bg(colors[args['bg']])

    if 'end' in args.keys():
        end = ''

    if bg_code and color_code:
        print(color_code, bg_code, string, reset, end=end)
    if not bg_code and color_code:
        print(color_code, string, reset, end=end)

    if bg_code and not color_code:
        print(bg_code, string, reset, end=end)

def demo():
    """
    This is generally run from the command line
    Just a demo of the colors
    """
    print('\n')
    color('light_blue', "--- --- --- Coolered Quick reference --- --- ---")
    print('\n')

    print("from coolered import color")
    print('\n')
    print("color('red', 'A red string') # ", end='')
    color('red', "A red string")

    print("color('blue', 'A blue string') # ", end='')
    color('blue', "A blue string")

    print("color('green', 'Green string, blue background', bg='dark_blue') # ", end='')
    color('green', 'Green string, blue background', bg='dark_blue')

    print('\n')
    if '-l' in argv:
        print("Colors: ")
        half = int(len(colors) / 2)
        first = list(colors.keys())[:half]
        second = list(colors.keys())[half:]

        for i in range(len(first)):
            print('{0:30}  {1}'.format(first[i], second[i]))

    else:
        print("Add -l to see a (long) list of possible color names")

    if '-b' in argv:
        print("Basic colors:")

        for name in colors.keys():
            if "_" not in name:
                if name == 'black':
                    color(name, name, bg='white')
                else:
                    color(name, name)
    else:
        print("Add -b to see a (short) list of basic colors")

    print('\n')


if __name__ == '__main__':
    demo()
