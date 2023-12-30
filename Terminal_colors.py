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