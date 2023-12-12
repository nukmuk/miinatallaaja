import copy
import math
import random
from datetime import datetime

import functions as f
import menu
import stats
import sweeperlib as ui

game = {
    "w": 9,
    "h": 9,
    "mines": 10,
    "state": 0,  # 0 starting, 1 playing, 2 lose, 3 win
    "time": 0,
    "arena_mines": [],
    "arena_player": [],
    "turns": 0,
    "mines_remaining": 0,
}

CORNER_OFFSET = 30


def load():
    game["w"] = int(game["w"])
    game["h"] = int(game["h"])
    game["mines"] = int(game["mines"])
    ui.set_draw_handler(draw_handler)
    ui.set_mouse_handler(mouse_handler)
    start_game()


def generate_arena(w, h):
    arena = []
    for y in range(h):
        arena.append([])
        for _ in range(w):
            arena[y].extend(" ")
    return arena


def get_arena_size(arena):
    h = len(arena)
    w = len(arena[0])
    return h, w


def count_mines_around(arena, x, y, radius=1):
    h, w = get_arena_size(arena)

    x1 = max(0, x - radius)
    x2 = min(w, x + radius + 1)
    y1 = max(0, y - radius)
    y2 = min(h, y + radius + 1)

    mines = 0

    for y in range(y1, y2):
        for x in range(x1, x2):
            if arena[y][x] == "x":
                mines += 1

    return mines


def generate_mines(arena, amount):
    arena_new = copy.deepcopy(arena)
    h, w = get_arena_size(arena)

    # print(w, h)
    mines = 0

    if amount > w * h:
        amount = w * h
        game["mines"] = amount

    while mines < amount:
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)

        if arena_new[y][x] != "x":
            arena_new[y][x] = "x"
            mines += 1

    return arena_new


def get_mines_remaining_from_flags(arena_player):
    h, w = get_arena_size(arena_player)

    flags = 0

    for y in range(h):
        for x in range(w):
            if arena_player[y][x] == "f":
                flags += 1

    mines = game["mines"] - flags
    return mines


def get_mines_remaining_actual(arena_player, arena_mines):
    h, w = get_arena_size(arena_player)

    remaining = game["mines"]

    for y in range(h):
        for x in range(w):
            if arena_mines[y][x] == "x":
                if arena_player[y][x] == "f":
                    remaining -= 1

    return remaining


def check_victory(arena_player, arena_mines):
    h, w = get_arena_size(arena_player)
    for y in range(h):
        for x in range(w):
            if arena_player[y][x] == " " and arena_mines[y][x] == " ":
                return False
    return True


def generate_stats():
    now = datetime.now()
    game_stats = {}

    game_stats["w"] = game["w"]
    game_stats["h"] = game["h"]
    game_stats["finished_at"] = now.strftime("%d.%m.%Y %H:%M:%S")
    game_stats["mines_remaining"] = get_mines_remaining_actual(
        game["arena_player"], game["arena_mines"]
    )
    game_stats["time_taken"] = game["time"]
    game_stats["turns_taken"] = game["turns"]
    game_stats["outcome"] = "Win" if game["state"] == 3 else "Lose"

    return game_stats


def open_tile(arena_mines, arena_player, x, y):
    game["turns"] += 1
    if arena_mines[y][x] == "x":
        # print("lose game")
        game["state"] = 2
        game["mines_remaining"] = get_mines_remaining_actual(arena_player, arena_mines)
        stats.save_score(generate_stats())
        copy_tiles(game["arena_mines"], game["arena_player"], "x")
    else:
        check_tiles(arena_mines, arena_player, x, y)


def check_tiles(arena_mines, arena_player, x, y):
    h, w = get_arena_size(arena_mines)

    radius = 1

    x1 = max(0, x - radius)
    x2 = min(w, x + radius + 1)
    y1 = max(0, y - radius)
    y2 = min(h, y + radius + 1)

    tile_old_value = arena_player[y][x]
    tile_new_value = count_mines_around(arena_mines, x, y)

    if tile_old_value not in (" ", "f"):
        return

    arena_player[y][x] = tile_new_value

    if tile_new_value == 0:
        for y_next in range(y1, y2):
            for x_next in range(x1, x2):
                arena_player[y_next][x_next] = arena_player[y_next][x_next]
                if (
                    arena_player[y_next][x_next] == " "
                    or arena_player[y_next][x_next] == "f"
                ):
                    check_tiles(arena_mines, arena_player, x_next, y_next)


def copy_tiles(source, to, tile):
    h, w = get_arena_size(source)
    for y in range(h):
        for x in range(w):
            if source[y][x] == tile:
                to[y][x] = source[y][x]


def timer(delta):
    if game["state"] == 1:
        game["time"] += delta


def start_game():
    game["arena_mines"] = generate_arena(game["w"], game["h"])
    game["arena_player"] = generate_arena(game["w"], game["h"])
    game["arena_mines"] = generate_mines(game["arena_mines"], game["mines"])
    game["state"] = 0
    game["time"] = 0
    game["turns"] = 0
    game["mines_remaining"] = game["mines"]

    padding = 200
    w = max(min(1920, game["w"] * 40 + CORNER_OFFSET + padding), 320)
    h = max(min(1080, game["h"] * 40 + CORNER_OFFSET + padding), 240)
    ui.resize_window(w, h)
    f.XRES = w
    f.YRES = h


def mouse_handler(x, y, btn, mod):
    # ui and buttons clicks handling
    if btn == ui.MOUSE_LEFT:
        # retry btn
        if (
            f.button_in_range(x, y, f.XRES / 2, f.YRES - 48, 32, 48)
            and game["state"] != 1
        ):
            # print("retried")
            start_game()

        # back btn
        if f.button_in_range(x, y, 0, f.YRES - 80, 140, 22) and game["state"] != 1:
            # print("back")
            menu.load()

    # game arena clicks handling
    x = math.floor((x - f.XRES / 2 + game["w"] * 40 / 2) / 40)
    y = math.floor((y - f.YRES / 2 + game["h"] * 40 / 2) / 40)
    # print("click:", x, y, btn, mod)
    if x >= game["w"] or y >= game["h"]:
        # print("click outside")
        return

    if x < 0 or y < 0:
        # print("click outside 2")
        return

    # print(x, y)

    clicked_tile = game["arena_player"][y][x]

    # return if game ended
    if game["state"] > 1:
        return

    if btn == ui.MOUSE_LEFT:
        if game["state"] == 2:
            return

        if clicked_tile == " ":
            open_tile(game["arena_mines"], game["arena_player"], x, y)

            if game["state"] == 0:
                game["state"] = 1

            victory = check_victory(game["arena_player"], game["arena_mines"])
            if victory and game["state"] != 2:
                game["state"] = 3
                stats.save_score(generate_stats())
    elif btn == ui.MOUSE_RIGHT:
        if clicked_tile == " ":
            game["arena_player"][y][x] = "f"
        elif clicked_tile == "f":
            game["arena_player"][y][x] = " "
        game["mines_remaining"] = get_mines_remaining_from_flags(game["arena_player"])


def draw_game_text(offset=0, text_color=f.text_color):
    s = game["state"]
    state_text = ""
    if s == 0:
        state_text = ":)"
    elif s == 1:
        state_text = ":)"
    elif s == 2:
        state_text = ":("
    elif s == 3:
        state_text = "8)"

    time = str(math.floor(game["time"]))

    f.draw_text_custom(
        state_text,
        f.XRES / 2 + offset,
        f.YRES - offset,
        anchor_y="top",
        color=text_color,
    )
    f.draw_text_custom(
        str(game["mines_remaining"]),
        CORNER_OFFSET + offset,
        f.YRES - offset,
        anchor_y="top",
        anchor_x="left",
        color=text_color,
    )
    f.draw_text_custom(
        time,
        f.XRES - CORNER_OFFSET + offset,
        f.YRES - offset,
        anchor_y="top",
        anchor_x="right",
        color=text_color,
    )

    if game["state"] != 1:
        f.draw_text_custom(
            "< menu",
            CORNER_OFFSET + offset,
            f.YRES - 80 - offset,
            anchor_x="left",
            anchor_y="center",
            size=22,
            color=text_color,
        )

    if game["state"] > 1:
        f.draw_text_custom(
            "retry",
            f.XRES / 2 + offset,
            f.YRES - 64 - offset,
            size=16,
            anchor_y="top",
            color=text_color,
        )


def draw_handler():
    ui.clear_window()
    ui.draw_background()

    ui.begin_sprite_draw()

    for y in range(game["h"]):
        for x in range(game["w"]):
            # sprite = game["arena_mines"][y][x]
            sprite = " "
            if game["arena_player"][y][x] != " ":
                sprite = game["arena_player"][y][x]
            ui.prepare_sprite(
                sprite,
                f.XRES / 2 - game["w"] * 40 / 2 + 40 * x,
                f.YRES / 2 - game["h"] * 40 / 2 + 40 * y,
            )

    ui.draw_sprites()

    draw_game_text(2, (0, 0, 0, 255))
    draw_game_text()
