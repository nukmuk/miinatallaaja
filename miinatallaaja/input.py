import sweeperlib as ui
import functions as f
import tallaaja

from tallaaja import game


def get_btn_pos():
    btn_x = f.xres / 4
    btn_y = f.yres / 2
    return btn_x, btn_y


text_offset = 48

state = {
    "focused_input": 0
}

game["cursor_char"] = ''


def load():
    ui.set_draw_handler(draw_handler)
    ui.set_mouse_handler(mouse_handler)
    ui.set_keyboard_handler(keyboard_handler)
    state["focused_input"] = 0


def cursor_blink(_):
    if not game["cursor_char"]:
        game["cursor_char"] = '_'
    else:
        game["cursor_char"] = ''


settings = ("w", "h", "mines")


def try_load_tallaaja():
    try:
        tallaaja.load()
    except:
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
    elif symbol == DOWN or symbol == ENTER or symbol == TAB:
        if state["focused_input"] < 2:
            state["focused_input"] += 1
        elif symbol == ENTER:
            try_load_tallaaja()
    elif symbol == BACK:
        game[setting] = str(game[setting])[:-1]

    if 48 <= symbol <= 57:

        if state["focused_input"] != 2 and len(str(game[setting])) >= 2:
            return

        elif len(str(game[setting])) >= 3:
            return

        number_to_input = str(symbol - 48)
        game[setting] = str(game[setting]) + number_to_input


def cursor(n):
    return game["cursor_char"] if state["focused_input"] == n else ''


def draw_handler():
    ui.clear_window()
    ui.draw_background()

    btn_x, btn_y = get_btn_pos()

    f.draw_text_custom("settings", f.xres / 4, f.yres -
                       f.yres / 4, size=48, anchor_x="left")

    f.draw_text_custom(f"field width: {game['w']}{cursor(0)}", btn_x, btn_y, anchor_x="left",
                       size=24)
    f.draw_text_custom(f"field height: {game['h']}{cursor(1)}",
                       btn_x, btn_y - text_offset, anchor_x="left", size=24)
    f.draw_text_custom(f"mines: {game['mines']}{cursor(2)}",
                       btn_x, btn_y - text_offset * 2, anchor_x="left", size=24)

    f.draw_text_custom("go", f.xres - btn_x, btn_y -
                       text_offset * 3, anchor_x="right", )


def mouse_handler(x, y, btn, mod):
    # print(x, y, btn, mod)

    btn_x, btn_y = get_btn_pos()

    t0 = f.button_in_range(x, y, btn_x, btn_y, f.xres / 2, text_offset / 2)
    t1 = f.button_in_range(x, y, btn_x, btn_y -
                           text_offset, f.xres / 2, text_offset / 2)
    t2 = f.button_in_range(x, y, btn_x, btn_y -
                           text_offset * 2, f.xres / 2, text_offset / 2)
    t3 = f.button_in_range(x, y, btn_x, btn_y -
                           text_offset * 3, f.xres / 2, text_offset / 2)

    # print(t0, t1, t2)

    if t0:
        state["focused_input"] = 0
    elif t1:
        state["focused_input"] = 1
    elif t2:
        state["focused_input"] = 2
    elif t3:
        try_load_tallaaja()
