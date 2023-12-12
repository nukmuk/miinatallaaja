import sweeperlib as ui
import functions as f
import tallaaja

from tallaaja import game


def get_btn_pos():
    btn_x = f.XRES / 4
    btn_y = f.YRES / 2
    return btn_x, btn_y


TEXT_OFFSET = 48

state = {"focused_input": 0}

game["cursor_char"] = ""


def load():
    ui.set_draw_handler(draw_handler)
    ui.set_mouse_handler(mouse_handler)
    ui.set_keyboard_handler(keyboard_handler)
    state["focused_input"] = 0


def cursor_blink(_):
    if not game["cursor_char"]:
        game["cursor_char"] = "_"
    else:
        game["cursor_char"] = ""


settings = ("w", "h", "mines")


def try_load_tallaaja():
    try:
        if int(game["w"]) < 1 or int(game["h"]) < 1:
            return
        tallaaja.load()
    except ValueError:
        print("invalid settings")


def keyboard_handler(symbol, mod):
    UP = 65362
    DOWN = 65364
    ENTER = 65293
    BACK = 65288
    TAB = 65289

    # print(symbol)

    setting = settings[state["focused_input"]]

    if (symbol == UP) and (state["focused_input"] >= 1):
        state["focused_input"] = state["focused_input"] - 1
    elif symbol in (DOWN, ENTER, TAB):
        if state["focused_input"] < 2:
            state["focused_input"] += 1
        elif symbol == ENTER:
            try_load_tallaaja()
    elif symbol == BACK:
        game[setting] = str(game[setting])[:-1]

    if 48 <= symbol <= 57:
        if state["focused_input"] != 2 and len(str(game[setting])) >= 2:
            return

        if len(str(game[setting])) >= 3:
            return

        number_to_input = str(symbol - 48)
        game[setting] = str(game[setting]) + number_to_input


def cursor(n):
    return game["cursor_char"] if state["focused_input"] == n else ""


def draw_handler():
    ui.clear_window()
    ui.draw_background()

    btn_x, btn_y = get_btn_pos()

    f.draw_text_custom(
        "settings", f.XRES / 4, f.YRES - f.YRES / 4, size=48, anchor_x="left"
    )

    f.draw_text_custom(
        f"field width: {game['w']}{cursor(0)}", btn_x, btn_y, anchor_x="left", size=24
    )
    f.draw_text_custom(
        f"field height: {game['h']}{cursor(1)}",
        btn_x,
        btn_y - TEXT_OFFSET,
        anchor_x="left",
        size=24,
    )
    f.draw_text_custom(
        f"mines: {game['mines']}{cursor(2)}",
        btn_x,
        btn_y - TEXT_OFFSET * 2,
        anchor_x="left",
        size=24,
    )

    f.draw_text_custom(
        "go",
        f.XRES - btn_x,
        btn_y - TEXT_OFFSET * 3,
        anchor_x="right",
    )


def mouse_handler(x, y, btn, mod):
    # print(x, y, btn, mod)

    btn_x, btn_y = get_btn_pos()

    f0 = f.button_in_range(x, y, btn_x, btn_y, f.XRES / 2, TEXT_OFFSET / 2)
    f1 = f.button_in_range(
        x, y, btn_x, btn_y - TEXT_OFFSET, f.XRES / 2, TEXT_OFFSET / 2
    )
    f2 = f.button_in_range(
        x, y, btn_x, btn_y - TEXT_OFFSET * 2, f.XRES / 2, TEXT_OFFSET / 2
    )
    f3 = f.button_in_range(
        x, y, btn_x, btn_y - TEXT_OFFSET * 3, f.XRES / 2, TEXT_OFFSET / 2
    )

    # print(t0, t1, t2)

    if f0:
        state["focused_input"] = 0
    elif f1:
        state["focused_input"] = 1
    elif f2:
        state["focused_input"] = 2
    elif f3:
        try_load_tallaaja()
