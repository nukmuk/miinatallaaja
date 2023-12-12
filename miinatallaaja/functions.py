"""functions and global variables"""

import pyglet

XRES_START = 800
YRES_START = 600
XRES = XRES_START
YRES = YRES_START
# xres = 1280
# yres = 720
text_color = (230, 230, 230, 255)


def button_in_range(mouse_x, mouse_y, btn_x, btn_y, size_x, size_y):
    """check if click in inside some distance of button center"""
    if btn_x - size_x <= mouse_x <= btn_x + size_x:
        if btn_y - size_y <= mouse_y <= btn_y + size_y:
            return True
    return False


# copied from sweeperlib.py
def draw_text_custom(
    text,
    x,
    y,
    color=text_color,
    font="comic sans ms",
    size=32,
    anchor_x="center",
    anchor_y="center",
):
    """
    Draws text on the screen. Can be used if you want to write something to
    the game window (e.g. counters or instructions). Default font is serif,
    size 32, color black. These can be altered by providing the function its
    optional arguments. The x and y coordinates define the bottom left corner
    of the text.

    Text, if any, should be drawn last.

    :param str text: string to display
    :param int x: bottom left x coordinate for the text
    :param int y: bottom left y coordinate for the text
    :param tuple color: color value, a tuple of four integers (RGBA)
    :param str font: name of the font family
    :param int size: fontin size as points
    :param str anchor_x: textin anchor_x
    :param str anchor_y: textin anchor_y
    """

    text_box = pyglet.text.Label(
        text,
        font_name=font,
        font_size=size,
        color=color,
        x=x,
        y=y,
        anchor_x=anchor_x,
        anchor_y=anchor_y,
    )
    text_box.draw()
