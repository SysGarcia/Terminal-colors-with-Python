import sys
import ctypes

def enable_windows_ansi_support():
    if sys.platform.startswith('win32'):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
enable_windows_ansi_support()

def colored(color, text):
    """
    Use it to color the terminal, recognizes between hexadecimal and RGB
    """
    if isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
    elif isinstance(color, str) and len(color) == 6:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
    else:
        raise ValueError("Invalid color format")

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

"""
You may encounter issues using this methods i have above,
to ensure it works on your system, you need to be sure ANSI
is supported. To enable it on Windows that is the code.

Another option is to use colorama, which is a library which makes ANSI
escape character sequences work under Windows as well

if you are interested in testing the code, try this snippets of code below.

# the functions colored, and enable_windows_ansi_support...

def random_rgb_value(): #random RGB generator.
    return tuple(random.randint(0, 255) for _ in range(3))
    
for i in range(0,30): #Loop to print 30 examples of colors
    print(colored(random_rgb_value(),"Example"))
"""
