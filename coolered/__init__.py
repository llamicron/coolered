from colored import fg, bg, attr


def red(string):
    print (fg(1), string, attr(0))


def demo():
    """
    This is generally run from the command line
    Just a demo of the colors
    """
    red("Red!")
