MESSAGES = {
    "outside": "The tile is outside the field.",
    "corner": "The tile is in the corner of the field.",
    "edge": "The tile is on the edge of the field.",
    "middle": "The tile is in the middle of the field.",
}


def position_in_field(x, y, width, height):
    if x < 0 or x > width - 1 or y < 0 or y > height - 1:
        return "outside"

    if (x == 0 and (y == 0 or y == width - 1)) or (
        x == width - 1 and (y == 0 or y == height - 1)
    ):
        return "corner"

    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return "edge"

    if x >= 0 and x < width and y >= 0 and y < height:
        return "middle"


def print_position(key):
    print(MESSAGES[key])


try:
    w = int(input("Input field width: "))
    h = int(input("Input field height: "))
    xxx = int(input("Input x coordinate: "))
    yyy = int(input("Input y coordinate: "))
    if w < 1 or h < 1:
        print("You can't fit a single tile on a field that small!")
    else:
        result = position_in_field(w, h, xxx, yyy)
        print_position(result)
except:
    print("error")
