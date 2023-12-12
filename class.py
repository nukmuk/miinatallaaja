def count_ninjas(xxx, yyy, listi):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well."""

    xxx = int(xxx)
    yyy = int(yyy)
    y_len = len(listi)
    x_len = len(listi[0])

    radius = 1
    x_min = max(0, xxx - radius)
    x_max = min(x_len - 1, xxx + radius)
    y_min = max(0, yyy - radius)
    y_max = min(y_len - 1, yyy + radius)

    ninjas = 0

    for yyy in range(y_min, y_max + 1):
        for xxx in range(x_min, x_max + 1):
            tile = listi[yyy][xxx]
            if tile == "N":
                ninjas += 1

    return ninjas


room = [
    ["N", " ", " ", " ", " "],
    ["N", "N", "N", "N", " "],
    ["N", " ", "N", " ", " "],
    ["N", "N", "N", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]
print(" ", "- " * 5)
for row in room:
    print("|", " ".join(row), "|")
print(" ", "- " * 5)
x = input("x")
y = input("y")
COUNT = count_ninjas(x, y, room)
print(COUNT)
